# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Optional

__all__ = ["UserAddToProjectParams"]

class UserAddToProjectParams(TypedDict, total=False):
    organization_id: Required[str]

    project_id: Optional[str]