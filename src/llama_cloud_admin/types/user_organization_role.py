# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from .role import Role

from typing import Optional, List

from datetime import datetime

__all__ = ["UserOrganizationRole"]

class UserOrganizationRole(BaseModel):
    """Schema for a user's role in an organization."""
    id: str
    """Unique identifier"""

    organization_id: str
    """The organization's ID."""

    role: Role
    """The role."""

    user_id: str
    """The user's ID."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    project_ids: Optional[List[str]] = None
    """The project ID scope."""

    updated_at: Optional[datetime] = None
    """Update datetime"""