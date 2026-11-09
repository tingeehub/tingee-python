"""
Signature tests.

1. Reference vectors (tests/vectors.json, produced by Node ``JSON.stringify`` + crypto): body serialization
   and signatures must be byte-identical to what the Tingee server computes.
2. Fake server (tests/signature_server.mjs, needs Node): real HTTP requests from TingeeClient are verified
   with the same logic as open-api ``validateSignature`` (JSON.parse -> JSON.stringify -> HMAC-SHA512).

Run: python -m unittest discover -s tests   (from repo root)
"""

import json
import os
import shutil
import subprocess
import sys
import unittest
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from tingee_sdk import (  # noqa: E402
    BankNameEnum,
    TingeeClient,
    create_url_validation_response,
    format_timestamp,
    generate_signature,
    verify_webhook_signature,
)
from tingee_sdk.signature import to_json  # noqa: E402

VECTORS = json.loads((Path(__file__).parent / "vectors.json").read_text(encoding="utf-8"))

# Python equivalents of the cases in gen_vectors.mjs
CASES = {
    "simple": {"accountNumber": "0123456789", "amount": 100000, "content": "Thanh toan don hang"},
    "unicode": {"name": "Nguyễn Văn A", "note": "Cảm ơn 🙏"},
    "escapes": {"s": "quote \" backslash \\ slash / tab\t nl\n cr\r bs\b ff\f ctl\u0001 del\u007f <a>&'"},
    "line_separators": {"s": "  "},
    "lone_surrogate": {"s": "a\ud800b"},
    "floats": {
        "a": 1.0, "b": 0.1, "c": 123.456, "d": -2.5, "e": 1e21, "f": 1e-7, "g": 1.5e-6, "h": 100.0, "i": 1e20,
        "j": -0.0, "k": 0.000001, "l": 123456789.123, "m": 5e-324, "n": 1.7976931348623157e308, "o": 0.1 + 0.2,
    },
    "nested": {"items": [{"id": 1, "ok": True, "v": None}, [], {}], "meta": {"x": [1, 2.0, "3"]}},
    "empty": {},
    "decimal": {"amount": Decimal("1000.50")},
    "enum_value": {"bankName": BankNameEnum.ACB},
    "max_safe_int": {"n": 9007199254740991},
}


class ReferenceVectorTest(unittest.TestCase):
    def test_cases_match_vectors(self):
        self.assertEqual(set(CASES), set(VECTORS["requests"]))

    def test_to_json_matches_json_stringify(self):
        for name, value in CASES.items():
            with self.subTest(name):
                self.assertEqual(to_json(value), VECTORS["requests"][name]["json"])

    def test_generate_signature_matches_server(self):
        for name, value in CASES.items():
            with self.subTest(name):
                signature = generate_signature(VECTORS["secret"], VECTORS["timestamp"], value)
                self.assertEqual(signature, VECTORS["requests"][name]["signature"])

    def test_format_timestamp_is_vietnam_time(self):
        self.assertEqual(format_timestamp(datetime(2026, 11, 6, 8, 30, 45, 123456, tzinfo=timezone.utc)), "20261106153045123")
        self.assertRegex(format_timestamp(), r"^\d{17}$")


class WebhookTest(unittest.TestCase):
    def setUp(self):
        self.secret = VECTORS["webhookSecret"]
        self.timestamp = VECTORS["timestamp"]
        self.raw = VECTORS["webhook"]["json"]
        self.signature = VECTORS["webhook"]["signature"]

    def test_valid_signature_raw_and_parsed(self):
        for body in (self.raw, self.raw.encode("utf-8"), json.loads(self.raw)):
            with self.subTest(type(body).__name__):
                self.assertEqual(verify_webhook_signature(self.secret, self.signature, self.timestamp, body)["code"], "00")

    def test_uppercase_signature_accepted(self):
        result = verify_webhook_signature(self.secret, self.signature.upper(), self.timestamp, self.raw)
        self.assertEqual(result["code"], "00")

    def test_rejects_tampered_requests(self):
        tampered = json.loads(self.raw)
        tampered["amount"] = 50001
        self.assertEqual(verify_webhook_signature(self.secret, self.signature, self.timestamp, tampered)["code"], "INVALID_SIGNATURE")
        self.assertEqual(verify_webhook_signature("other-secret", self.signature, self.timestamp, self.raw)["code"], "INVALID_SIGNATURE")
        self.assertEqual(verify_webhook_signature(self.secret, self.signature, "20261106153045124", self.raw)["code"], "INVALID_SIGNATURE")

    def test_input_errors(self):
        self.assertEqual(verify_webhook_signature(self.secret, "", self.timestamp, self.raw)["code"], "MISSING_SIGNATURE")
        self.assertEqual(verify_webhook_signature(self.secret, self.signature, None, self.raw)["code"], "MISSING_TIMESTAMP")
        self.assertEqual(verify_webhook_signature(self.secret, self.signature, "2026", self.raw)["code"], "INVALID_TIMESTAMP")
        self.assertEqual(verify_webhook_signature(self.secret, self.signature, self.timestamp, "{bad")["code"], "INVALID_BODY")
        self.assertEqual(verify_webhook_signature(self.secret, self.signature, self.timestamp, {})["code"], "MISSING_BODY")
        missing = json.loads(self.raw)
        del missing["transactionCode"]
        self.assertEqual(verify_webhook_signature(self.secret, self.signature, self.timestamp, missing)["code"], "MISSING_BODY_FIELD")


class UrlValidationTest(unittest.TestCase):
    def test_challenge_response(self):
        body = {"event": "url-validation", "plainToken": VECTORS["urlValidation"]["plainToken"], "timestamp": 1}
        expected = {"plainToken": VECTORS["urlValidation"]["plainToken"], "encryptedToken": VECTORS["urlValidation"]["encryptedToken"]}
        for value in (body, json.dumps(body), json.dumps(body).encode("utf-8")):
            with self.subTest(type(value).__name__):
                self.assertEqual(create_url_validation_response(VECTORS["webhookSecret"], value), expected)

    def test_not_a_challenge(self):
        secret = VECTORS["webhookSecret"]
        self.assertIsNone(create_url_validation_response(secret, json.loads(VECTORS["webhook"]["json"])))
        self.assertIsNone(create_url_validation_response(secret, {"event": "url-validation"}))
        self.assertIsNone(create_url_validation_response(secret, "{bad"))
        self.assertIsNone(create_url_validation_response(secret, None))

    def test_client_uses_override_secret(self):
        client = TingeeClient(secret_key="api-secret", client_id="cid", environment="uat")
        body = {"event": "url-validation", "plainToken": VECTORS["urlValidation"]["plainToken"]}
        self.assertEqual(
            client.create_url_validation_response(body, VECTORS["webhookSecret"])["encryptedToken"],
            VECTORS["urlValidation"]["encryptedToken"],
        )


@unittest.skipUnless(shutil.which("node"), "node is required for the fake server test")
class FakeServerTest(unittest.TestCase):
    """Real HTTP requests verified by a Node server that mirrors open-api validateSignature."""

    SECRET = "fake-server-secret"

    @classmethod
    def setUpClass(cls):
        env = dict(os.environ, TZ="Asia/Ho_Chi_Minh")
        cls.server = subprocess.Popen(
            ["node", str(Path(__file__).parent / "signature_server.mjs"), cls.SECRET],
            stdout=subprocess.PIPE,
            env=env,
            text=True,
        )
        port = cls.server.stdout.readline().strip()
        cls.client = TingeeClient(secret_key=cls.SECRET, client_id="cid", base_url="http://127.0.0.1:{0}".format(port))

    @classmethod
    def tearDownClass(cls):
        cls.server.terminate()
        cls.server.wait(timeout=5)

    def assertAccepted(self, result):
        self.assertEqual(result["code"], "00", result)

    def test_post_bodies(self):
        for name, value in CASES.items():
            with self.subTest(name):
                self.assertAccepted(self.client._http.request("post", "/v1/test", body=value))

    def test_generated_methods(self):
        # GET without body -> server sees {} and the SDK signs "{}"
        result = self.client.bank.get_banks()
        self.assertAccepted(result)
        self.assertRegex(result["data"]["userAgent"], r"^tingee-sdk-python/\d+\.\d+\.\d+ \(python/")
        result = self.client.bank.create_va({"bankName": "OCB", "accountNumber": "0123456789", "accountName": "Nguyễn Văn A"})
        self.assertAccepted(result)
        self.assertEqual(result["data"]["body"]["accountName"], "Nguyễn Văn A")

    def test_query_params(self):
        result = self.client.bank.delete_va({"vaAccountNumber": "VA 001", "bankName": "OCB"})
        self.assertAccepted(result)
        self.assertIn("vaAccountNumber=VA+001", result["data"]["url"])

    def test_wrong_secret_rejected(self):
        bad = TingeeClient(secret_key="wrong", client_id="cid", base_url=self.client.get_base_url())
        self.assertEqual(bad.bank.get_banks()["code"], "97")


if __name__ == "__main__":
    unittest.main()
