# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .custom_claims import CustomClaims

__all__ = ["UserClaims"]


class UserClaims(BaseModel):
    """A user's fully resolved custom claims after applying system defaults."""

    claims: CustomClaims
    """The user's resolved custom claims."""

    user_id: str
    """The user ID the claims belong to."""
