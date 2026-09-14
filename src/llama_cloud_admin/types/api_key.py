# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["APIKey"]


class APIKey(BaseModel):
    """Schema for an API Key."""

    id: str
    """Unique identifier"""

    redacted_api_key: str

    user_id: str

    created_at: Optional[datetime] = None
    """Creation datetime"""

    expires_at: Optional[datetime] = None
    """When the API key expires. Null if the key never expires."""

    key_type: Optional[Literal["agent", "user"]] = None

    metadata: Optional[Dict[str, object]] = None

    name: Optional[str] = None

    project_id: Optional[str] = None

    updated_at: Optional[datetime] = None
    """Update datetime"""
