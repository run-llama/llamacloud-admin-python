# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

__all__ = ["OrganizationCreateParams"]

class OrganizationCreateParams(TypedDict, total=False):
    name: Required[str]
    """The organization's display name."""