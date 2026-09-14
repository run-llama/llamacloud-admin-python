# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

__all__ = ["ProjectCreateParams"]

class ProjectCreateParams(TypedDict, total=False):
    organization_id: Required[str]

    name: Required[str]
    """The project's display name."""