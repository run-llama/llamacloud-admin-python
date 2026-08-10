# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["InviteAcceptResponse"]


class InviteAcceptResponse(BaseModel):
    """Response for accepting an invitation."""

    organization_id: str
    """The organization the user just joined."""
