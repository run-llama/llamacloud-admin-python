# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing_extensions import Literal

from typing import Optional, Dict

__all__ = ["AdminGetFilestoresInfoResponse"]

class AdminGetFilestoresInfoResponse(BaseModel):
    status: Literal["missing_buckets", "missing_credentials", "ok"]

    available_buckets: Optional[Dict[str, str]] = None

    unavailable_buckets: Optional[Dict[str, str]] = None