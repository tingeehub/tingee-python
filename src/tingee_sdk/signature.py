"""Tingee request signing, webhook verification and URL validation helpers."""

import hashlib
import hmac
import json
import math
import re
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from typing import Any, Dict, Optional, Union

__all__ = [
    "URL_VALIDATION_EVENT",
    "to_json",
    "generate_signature",
    "format_timestamp",
    "verify_webhook_signature",
    "create_url_validation_response",
]

VN_TZ = timezone(timedelta(hours=7))

#: Value of the ``event`` field (and ``webhook-type`` header) of a URL validation request
URL_VALIDATION_EVENT = "url-validation"

_TIMESTAMP_REGEX = re.compile(r"^\d{17}$")

# Required fields of a Tingee webhook body
_REQUIRED_BODY_FIELDS = ("clientId", "transactionCode", "amount", "bank", "accountNumber", "transactionDate")

# Same escaping as JSON.stringify: short escapes + \u00XX for other control chars, nothing else
_ESCAPE_MAP = {'"': '\\"', "\\": "\\\\", "\b": "\\b", "\f": "\\f", "\n": "\\n", "\r": "\\r", "\t": "\\t"}
_ESCAPE_REGEX = re.compile(r'["\\\x00-\x1f]|[\ud800-\udfff]')


def _js_string(value: str) -> str:
    def _replace(match: "re.Match[str]") -> str:
        ch = match.group(0)
        return _ESCAPE_MAP.get(ch) or "\\u{0:04x}".format(ord(ch))

    return '"' + _ESCAPE_REGEX.sub(_replace, value) + '"'


def _js_number(value: Union[int, float, Decimal]) -> str:
    """Format a number exactly like JavaScript's Number#toString."""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)

    number = float(value)
    if math.isnan(number) or math.isinf(number):
        return "null"
    if number == 0:
        return "0"

    sign = "-" if number < 0 else ""
    # repr() gives the shortest round-trip digits, same as JS; only the layout differs
    digits_tuple = Decimal(repr(abs(number))).normalize().as_tuple()
    digits = "".join(str(d) for d in digits_tuple.digits)
    k = len(digits)
    n = digits_tuple.exponent + k  # value = 0.<digits> * 10^n

    if k <= n <= 21:
        text = digits + "0" * (n - k)
    elif 0 < n <= 21:
        text = digits[:n] + "." + digits[n:]
    elif -6 < n <= 0:
        text = "0." + "0" * (-n) + digits
    else:
        exponent = n - 1
        mantissa = digits if k == 1 else digits[0] + "." + digits[1:]
        text = mantissa + "e" + ("+" if exponent >= 0 else "-") + str(abs(exponent))
    return sign + text


def to_json(value: Any) -> str:
    """
    Serialize ``value`` to the exact string ``JSON.stringify`` produces.

    Tingee signs ``JSON.stringify(body)``, so the SDK signs and sends this string.
    Plain ``json.dumps`` differs (spaces, ``1.0`` vs ``1``, unicode escaping) and breaks the signature.
    """
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float, Decimal)):
        return _js_number(value)
    if isinstance(value, str):
        return _js_string(value)
    if isinstance(value, dict):
        return "{" + ",".join(_js_string(str(k)) + ":" + to_json(v) for k, v in value.items()) + "}"
    if isinstance(value, (list, tuple)):
        return "[" + ",".join(to_json(v) for v in value) + "]"
    if isinstance(value, datetime):
        return _js_string(value.isoformat())
    if hasattr(value, "value") and isinstance(getattr(value, "value"), (str, int, float)):
        # Enum members
        return to_json(value.value)
    raise TypeError("Object of type {0} is not JSON serializable".format(type(value).__name__))


def generate_signature(secret_key: str, timestamp: str, body: Any) -> str:
    """
    Generate signature for a Tingee API request.

    Signature format: ``HMAC-SHA512(secretKey, "{timestamp}:{JSON.stringify(body)}")``, hex.
    ``body`` may be a dict/list or an already serialized JSON string.
    """
    body_json = body if isinstance(body, str) else to_json(body)
    message = "{0}:{1}".format(timestamp, body_json)
    return hmac.new(secret_key.encode("utf-8"), message.encode("utf-8"), hashlib.sha512).hexdigest()


def format_timestamp(date: Optional[datetime] = None) -> str:
    """Format date to Tingee timestamp format ``yyyyMMddHHmmssSSS``, always in Vietnam time (UTC+7)."""
    date = date or datetime.now(timezone.utc)
    if date.tzinfo is None:
        date = date.astimezone()
    vn_date = date.astimezone(VN_TZ)
    return vn_date.strftime("%Y%m%d%H%M%S") + "{0:03d}".format(vn_date.microsecond // 1000)


def _parse_body(body: Union[Dict[str, Any], str, bytes, None]) -> Optional[Dict[str, Any]]:
    if isinstance(body, (str, bytes)):
        try:
            parsed = json.loads(body)
        except ValueError:
            return None
        return parsed if isinstance(parsed, dict) else None
    return body if isinstance(body, dict) else None


def verify_webhook_signature(
    secret_token: str,
    signature: Optional[str],
    timestamp: Optional[str],
    body: Union[Dict[str, Any], str, bytes, None],
) -> Dict[str, str]:
    """
    Verify the HMAC-SHA512 signature of an incoming Tingee webhook callback.

    Returns ``{"code": "00", "message": "OK"}`` when valid, otherwise an error code and message.

    Example (Flask)::

        result = verify_webhook_signature(
            os.environ["TINGEE_SECRET_TOKEN"],
            request.headers.get("x-signature"),
            request.headers.get("x-request-timestamp"),
            request.get_data(),
        )
        if result["code"] != "00":
            return result, 401
    """
    if not signature:
        return {"code": "MISSING_SIGNATURE", "message": "x-signature header is required"}
    if not timestamp:
        return {"code": "MISSING_TIMESTAMP", "message": "x-request-timestamp header is required"}
    if not _TIMESTAMP_REGEX.match(timestamp):
        return {"code": "INVALID_TIMESTAMP", "message": "x-request-timestamp must be in yyyyMMddHHmmssSSS format (17 digits)"}

    if isinstance(body, (str, bytes)):
        parsed_body = _parse_body(body)
        if parsed_body is None:
            return {"code": "INVALID_BODY", "message": "body string is not valid JSON"}
    else:
        parsed_body = body

    if not parsed_body or not isinstance(parsed_body, dict):
        return {"code": "MISSING_BODY", "message": "body is required and must be an object"}

    for field in _REQUIRED_BODY_FIELDS:
        value = parsed_body.get(field)
        if value is None or value == "":
            return {"code": "MISSING_BODY_FIELD", "message": "body.{0} is required".format(field)}

    expected = generate_signature(secret_token, timestamp, parsed_body)
    if not hmac.compare_digest(expected, signature.strip().lower()):
        return {"code": "INVALID_SIGNATURE", "message": "Signature does not match"}

    return {"code": "00", "message": "OK"}


def create_url_validation_response(
    secret_token: str,
    body: Union[Dict[str, Any], str, bytes, None],
) -> Optional[Dict[str, str]]:
    """
    Build the response for Tingee's webhook URL validation request.

    When you save a webhook URL, Tingee sends ``{"event": "url-validation", "plainToken": "...", "timestamp": ...}``
    and expects ``{"plainToken": "...", "encryptedToken": "..."}`` back with HTTP 200,
    where ``encryptedToken = HMAC-SHA256(secretToken, plainToken)`` in hex.
    Returns ``None`` when the body is not a URL validation request -> handle it as a normal webhook.

    :param secret_token: Secret token of your active "Webhook verification" API credential
    """
    parsed_body = _parse_body(body)
    if not parsed_body or parsed_body.get("event") != URL_VALIDATION_EVENT:
        return None

    plain_token = parsed_body.get("plainToken")
    if not isinstance(plain_token, str) or not plain_token:
        return None

    encrypted_token = hmac.new(secret_token.encode("utf-8"), plain_token.encode("utf-8"), hashlib.sha256).hexdigest()
    return {"plainToken": plain_token, "encryptedToken": encrypted_token}
