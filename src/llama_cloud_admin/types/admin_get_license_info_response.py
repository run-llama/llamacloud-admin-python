# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AdminGetLicenseInfoResponse"]


class AdminGetLicenseInfoResponse(BaseModel):
    expires_at: datetime
    """License expiration date"""

    status: str
    """License validation status"""

    message: Optional[str] = None
    """License message"""

    scopes: Optional[List[str]] = None
    """License scopes"""
