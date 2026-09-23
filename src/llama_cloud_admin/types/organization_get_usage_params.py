# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["OrganizationGetUsageParams"]


class OrganizationGetUsageParams(TypedDict, total=False):
    get_current_invoice_total: bool

    include: List[Literal["offers"]]
