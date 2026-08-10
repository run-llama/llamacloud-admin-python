# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["UserUpdateClaimsParams", "SetClaims"]


class UserUpdateClaimsParams(TypedDict, total=False):
    remove_claims: Optional[
        List[Literal["allow_org_deletion", "allowed_org_creation", "api_datasource_access", "maximum_org_creation"]]
    ]
    """Names of claims to reset to their system default."""

    set_claims: Optional[SetClaims]
    """A partial set of custom claims for additive updates.

    Every field is optional. Only the claims explicitly provided in a request are
    added or overwritten; claims left unset are not touched, so callers can change a
    single claim without resending the full claim set.
    """


class SetClaims(TypedDict, total=False):
    """A partial set of custom claims for additive updates.

    Every field is optional. Only the claims explicitly provided in a request
    are added or overwritten; claims left unset are not touched, so callers can
    change a single claim without resending the full claim set.
    """

    allow_org_deletion: Optional[bool]
    """Whether the user is allowed to delete organizations."""

    allowed_org_creation: Optional[bool]
    """Whether the user is allowed to create organizations."""

    api_datasource_access: Optional[bool]
    """Whether the user is allowed to access API data sources."""

    maximum_org_creation: Optional[int]
    """Cap on how many organizations this user may create.

    None means unlimited. Only enforced when allowed_org_creation is True.
    """
