# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Invite"]


class Invite(BaseModel):
    """A pending invitation visible to the invitee."""

    id: str
    """The invite's unique identifier."""

    organization_id: str
    """The organization the user is invited to."""

    organization_name: str
    """The organization's display name."""

    role: str
    """The role being granted (e.g. admin, viewer)."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    updated_at: Optional[datetime] = None
    """Update datetime"""
