# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["UsageMetricAggregateResponse", "Bucket"]


class Bucket(BaseModel):
    """A single aggregation bucket grouped by the requested dimensions."""

    dimensions: Dict[str, str]
    """The dimension values that define this bucket"""

    metric_count: int
    """Number of metric rows in this bucket"""

    total_credits: Union[float, str]
    """Total credits consumed by metrics in this bucket"""

    total_value: int
    """Total of the metric `value` field in this bucket"""


class UsageMetricAggregateResponse(BaseModel):
    """Response containing usage metrics aggregated by one or more dimensions."""

    buckets: List[Bucket]
    """The aggregation buckets, ordered by total credits descending"""

    group_by: List[Literal["day", "event_type", "organization_id", "project_id", "user_id"]]
    """The dimensions the metrics were grouped by"""
