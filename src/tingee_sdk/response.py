from typing import Any, Mapping, TypedDict

__all__ = ["TingeeApiResponse", "is_success_response", "is_error_response"]


class TingeeApiResponse(TypedDict, total=False):
    code: str
    message: str
    data: Any


def is_success_response(response: Mapping[str, Any]) -> bool:
    return response.get("code") == "00"


def is_error_response(response: Mapping[str, Any]) -> bool:
    return response.get("code") != "00"
