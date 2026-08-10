# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Organization"]


class Organization(BaseModel):
    """API response schema for an organization."""

    id: str
    """The organization's unique identifier."""

    name: str
    """The organization's display name."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    metadata: Optional[Dict[str, object]] = None
    """Additional organization metadata."""

    updated_at: Optional[datetime] = None
    """Update datetime"""
