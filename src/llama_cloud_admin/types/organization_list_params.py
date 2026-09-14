# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Optional

__all__ = ["OrganizationListParams"]

class OrganizationListParams(TypedDict, total=False):
    name: Optional[str]

    page_size: Optional[int]

    page_token: Optional[str]