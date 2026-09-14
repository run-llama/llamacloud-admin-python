# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .quota_configuration import QuotaConfiguration

__all__ = ["QuotaManagementListResponse"]


class QuotaManagementListResponse(BaseModel):
    """Paginated list of quota configurations."""

    items: List[QuotaConfiguration]

    page: int

    pages: int

    size: int

    total: int
