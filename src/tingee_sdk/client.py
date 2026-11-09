from typing import Any, Dict, Literal, Optional, Union

from .generated_methods import GeneratedMethods
from .http import TingeeHttpClient
from .signature import create_url_validation_response, verify_webhook_signature

__all__ = ["TingeeClient", "TingeeEnvironment", "ENVIRONMENT_URLS"]

TingeeEnvironment = Literal["production", "uat"]

ENVIRONMENT_URLS: Dict[str, str] = {
    "production": "https://open-api.tingee.vn",
    "uat": "https://uat-open-api.tingee.vn",
}


class TingeeClient(GeneratedMethods):
    """
    Tingee Open API client.

    Example::

        client = TingeeClient(secret_key="...", client_id="...", environment="uat")
        result = client.bank.get_banks()
        if result["code"] == "00":
            print(result["data"])
    """

    def __init__(
        self,
        secret_key: str,
        client_id: str,
        environment: TingeeEnvironment = "production",
        timeout: float = 90,
        base_url: Optional[str] = None,
    ) -> None:
        """
        :param secret_key: Secret key for generating request signature
        :param client_id: Client ID for API authentication
        :param environment: ``production`` (default) or ``uat``
        :param timeout: Request timeout in seconds (default 90)
        :param base_url: Custom base URL (overrides environment)
        """
        if not secret_key:
            raise ValueError("secret_key is required")
        if not client_id:
            raise ValueError("client_id is required")
        if environment not in ENVIRONMENT_URLS and not base_url:
            raise ValueError("environment must be one of: {0}".format(", ".join(ENVIRONMENT_URLS)))

        self._secret_key = secret_key
        self._base_url = base_url or ENVIRONMENT_URLS[environment]
        super().__init__(TingeeHttpClient(self._base_url, secret_key, client_id, timeout))

    def get_base_url(self) -> str:
        return self._base_url

    def verify_webhook_signature(
        self,
        signature: Optional[str],
        timestamp: Optional[str],
        body: Union[Dict[str, Any], str, bytes, None],
    ) -> Dict[str, str]:
        """Verify an incoming Tingee webhook signature using this client's secret_key."""
        return verify_webhook_signature(self._secret_key, signature, timestamp, body)

    def create_url_validation_response(
        self,
        body: Union[Dict[str, Any], str, bytes, None],
        secret_token: Optional[str] = None,
    ) -> Optional[Dict[str, str]]:
        """
        Build the response for a webhook URL validation request, ``None`` if body is not one.
        Pass ``secret_token`` when your "Webhook verification" credential differs from this client's.
        """
        return create_url_validation_response(secret_token or self._secret_key, body)
