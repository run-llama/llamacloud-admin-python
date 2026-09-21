# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["APIKeyCreateParams"]


class APIKeyCreateParams(TypedDict, total=False):
    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """When the API key should expire. If not set, the key never expires."""

    key_type: Literal["agent", "user"]

    name: Optional[str]

    project_id: Optional[str]
    """The project ID to associate with the API key."""

    role: Optional[Literal["admin", "agent_viewer", "viewer", "viewer_v2"]]
    """Role capping what this key may do.

    A key can only ever be narrower than the user who created it, never broader. If
    not set, the key authorizes as its owner.
    """
