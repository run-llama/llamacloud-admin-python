# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Role"]


class Role(BaseModel):
    """Schema for a role."""

    id: str
    """Unique identifier"""

    name: str
    """A name for the role."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    updated_at: Optional[datetime] = None
    """Update datetime"""
