# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Optional

__all__ = ["ProjectUpdateParams"]

class ProjectUpdateParams(TypedDict, total=False):
    name: Required[str]
    """The project's new display name."""

    organization_id: Optional[str]