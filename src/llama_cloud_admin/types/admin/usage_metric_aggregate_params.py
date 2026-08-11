# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["UsageMetricAggregateParams"]


class UsageMetricAggregateParams(TypedDict, total=False):
    day_on_or_after: Required[str]
    """Inclusive lower bound on the day (YYYY-MM-DD, UTC)"""

    day_on_or_before: Required[str]
    """Inclusive upper bound on the day (YYYY-MM-DD, UTC)"""

    group_by: Required[SequenceNotStr[str]]
    """Dimensions to group by: day, organization_id, project_id, event_type, user_id"""

    event_types: Optional[
        List[
            Literal[
                "audio_seconds_parsed",
                "chart_parsing_agentic",
                "chart_parsing_efficient",
                "chart_parsing_plus",
                "chat_message_sent",
                "confidence_score_high",
                "directory_count_snapshot",
                "directory_file_count_snapshot",
                "directory_files_exported",
                "directory_files_ingested",
                "directory_pages_exported",
                "extraction_num_pages",
                "form_parsing_pages",
                "image_classified",
                "index_retrieve_query",
                "layout_aware_chart_extraction",
                "layout_aware_parsing",
                "layout_extracted",
                "pages_classified",
                "pages_embedded",
                "pages_indexed",
                "pages_parsed",
                "pages_split",
                "pages_verified",
                "precise_bbox_extraction",
                "set_total_indexes",
                "set_total_pages_indexed",
                "spreadsheet_regions_extracted",
                "stored_file_count",
                "stored_file_mb",
            ]
        ]
    ]
    """Filter by event types"""

    organization_id: Optional[str]
    """Filter by organization ID"""

    project_id: Optional[str]
    """Filter by project ID"""

    user_id: Optional[str]
    """Filter by user ID"""
