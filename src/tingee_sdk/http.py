"""HTTP client for Tingee API: signs and executes requests (stdlib only)."""

import json
import platform
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, Mapping, Optional

from .signature import format_timestamp, generate_signature, to_json
from .version import SDK_VERSION

__all__ = ["TingeeHttpClient", "TingeeHttpError"]

USER_AGENT = "tingee-sdk-python/{0} (python/{1}; {2})".format(SDK_VERSION, platform.python_version(), sys.platform)


class TingeeHttpError(Exception):
    """Raised on non-2xx responses (``status`` > 0) and network errors / timeouts (``status`` == 0)."""

    def __init__(self, message: str, status: int, data: Any = None, headers: Optional[Dict[str, str]] = None):
        super().__init__(message)
        self.status = status
        self.data = data
        self.headers = headers or {}


class TingeeHttpClient:
    def __init__(self, base_url: str, secret_key: str, client_id: str, timeout: float = 90):
        self._base_url = base_url.rstrip("/")
        self._secret_key = secret_key
        self._client_id = client_id
        self._timeout = timeout

    def request(
        self,
        method: str,
        path: str,
        body: Any = None,
        query: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        # Sign and send the exact same string -> server's JSON.stringify(body) matches
        body_json = to_json(body) if body is not None else None
        timestamp = format_timestamp()
        signature = generate_signature(self._secret_key, timestamp, body_json if body_json is not None else "{}")

        base_path = path if path.startswith("/") else "/" + path
        url = self._base_url + base_path
        if query:
            params = {k: _query_value(v) for k, v in query.items() if v is not None and v != ""}
            if params:
                url += "?" + urllib.parse.urlencode(params)

        request_headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "x-signature": signature,
            "x-request-timestamp": timestamp,
            "x-client-id": self._client_id,
            "x-sdk-version": "tingee-sdk/python/{0}".format(SDK_VERSION),
            "user-agent": USER_AGENT,
        }
        if headers:
            request_headers.update(headers)

        request = urllib.request.Request(
            url,
            data=body_json.encode("utf-8") if body_json is not None else None,
            headers=request_headers,
            method=method.upper(),
        )
        effective_timeout = timeout or self._timeout

        try:
            with urllib.request.urlopen(request, timeout=effective_timeout) as response:
                return _read_body(response.headers, response.read())
        except urllib.error.HTTPError as error:
            data = _read_body(error.headers, error.read())
            raise TingeeHttpError(
                "Request failed with status {0}".format(error.code), error.code, data, dict(error.headers.items())
            ) from None
        except (socket.timeout, TimeoutError):
            raise TingeeHttpError("Request timeout after {0}s".format(effective_timeout), 0) from None
        except urllib.error.URLError as error:
            if isinstance(error.reason, (socket.timeout, TimeoutError)):
                raise TingeeHttpError("Request timeout after {0}s".format(effective_timeout), 0) from None
            raise TingeeHttpError(str(error.reason) or "Network error", 0) from None


def _query_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _read_body(headers: Any, raw: bytes) -> Any:
    content_type = (headers.get("content-type") or "") if headers else ""
    if "application/json" in content_type:
        try:
            return json.loads(raw.decode("utf-8"))
        except ValueError:
            return raw.decode("utf-8", errors="replace")
    if content_type.startswith("text/"):
        return raw.decode("utf-8", errors="replace")
    return raw
