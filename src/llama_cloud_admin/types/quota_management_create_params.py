# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["QuotaManagementCreateParams"]


class QuotaManagementCreateParams(TypedDict, total=False):
    organization_id: Required[str]

    setting: Required[Literal["allow_pay_as_you_go", "limit_daily_usage_credits", "limit_monthly_usage_credits"]]
    """The quota setting to update"""

    value: Required[int]
    """The value for the setting.

    For boolean settings, use 1 (enabled) or 0 (disabled). For credit limits, the
    number of credits allowed in the window; delete the setting to remove the limit.
    For limits denominated in USD cents, a whole number of dollars (a multiple of
    100).
    """

    project_id: Optional[str]
    """Limit this project on its own.

    Omit to limit the organization as a whole. A project limit does not inherit from
    the organization limit: both apply, and whichever is reached first stops the
    work. Credit limits only.
    """
