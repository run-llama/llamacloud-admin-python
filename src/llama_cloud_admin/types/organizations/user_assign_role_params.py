# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["UserAssignRoleParams"]


class UserAssignRoleParams(TypedDict, total=False):
    body_organization_id: Required[Annotated[str, PropertyInfo(alias="organization_id")]]
    """The organization's ID."""

    role_id: Required[str]
    """The role's ID."""

    user_id: Required[str]
    """The user's ID."""

    project_ids: Optional[SequenceNotStr[str]]
    """Projects to limit the role to.

    Empty: organization-wide, per-project roles removed. Omitted: organization-wide,
    per-project roles kept.
    """
