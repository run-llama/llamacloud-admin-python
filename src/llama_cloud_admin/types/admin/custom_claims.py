# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CustomClaims"]


class CustomClaims(BaseModel):
    """
    Custom claims that dictate various limits or allowed behaviors.
    Currently these claims reside at a per user level. Claims may expand to a per organization level or project in the future.
    """

    allow_org_deletion: Optional[bool] = None
    """Whether the user is allowed to delete organizations."""

    allowed_org_creation: Optional[bool] = None
    """Whether the user is allowed to create organizations."""

    api_datasource_access: Optional[bool] = None
    """Whether the user is allowed to access API data sources."""

    maximum_org_creation: Optional[int] = None
    """Cap on how many organizations this user may create.

    None means unlimited. Only enforced when allowed_org_creation is True.
    """
