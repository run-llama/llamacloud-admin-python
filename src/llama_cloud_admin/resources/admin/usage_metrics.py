# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.admin import usage_metric_export_params, usage_metric_aggregate_params
from ..._base_client import make_request_options
from ...types.admin.usage_metric_aggregate_response import UsageMetricAggregateResponse

__all__ = ["UsageMetricsResource", "AsyncUsageMetricsResource"]


class UsageMetricsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llamacloud-admin-python#accessing-raw-response-data-eg-headers
        """
        return UsageMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llamacloud-admin-python#with_streaming_response
        """
        return UsageMetricsResourceWithStreamingResponse(self)

    def aggregate(
        self,
        *,
        day_on_or_after: str,
        day_on_or_before: str,
        group_by: SequenceNotStr[str],
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
        | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageMetricAggregateResponse:
        """
        Aggregate usage metrics by one or more dimensions, reporting total credits used.
        Global admin only.

        A date range is required, which bounds the scan via the `day`-leading index.
        Supplying `organization_id` narrows it further via the `(organization_id, day)`
        index.

        Supported `group_by` dimensions: `day`, `organization_id`, `project_id`,
        `event_type`, `user_id`. Buckets are ordered by total credits descending.

        Args:
          day_on_or_after: Inclusive lower bound on the day (YYYY-MM-DD, UTC)

          day_on_or_before: Inclusive upper bound on the day (YYYY-MM-DD, UTC)

          group_by: Dimensions to group by: day, organization_id, project_id, event_type, user_id

          event_types: Filter by event types

          organization_id: Filter by organization ID

          project_id: Filter by project ID

          user_id: Filter by user ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/admin/usage-metrics/aggregate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "day_on_or_after": day_on_or_after,
                        "day_on_or_before": day_on_or_before,
                        "group_by": group_by,
                        "event_types": event_types,
                        "organization_id": organization_id,
                        "project_id": project_id,
                        "user_id": user_id,
                    },
                    usage_metric_aggregate_params.UsageMetricAggregateParams,
                ),
            ),
            cast_to=UsageMetricAggregateResponse,
        )

    def export(
        self,
        *,
        day_on_or_after: str,
        day_on_or_before: str,
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
        | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Export usage metrics line by line as CSV over a date range.

        Global admin only.

        Each row is a single usage metric. Use the optional filters to scope the export
        to an organization, project, user, or set of event types.

        Args:
          day_on_or_after: Inclusive lower bound on the day (YYYY-MM-DD, UTC)

          day_on_or_before: Inclusive upper bound on the day (YYYY-MM-DD, UTC)

          event_types: Filter by event types

          organization_id: Filter by organization ID

          project_id: Filter by project ID

          user_id: Filter by user ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/v1/admin/usage-metrics/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "day_on_or_after": day_on_or_after,
                        "day_on_or_before": day_on_or_before,
                        "event_types": event_types,
                        "organization_id": organization_id,
                        "project_id": project_id,
                        "user_id": user_id,
                    },
                    usage_metric_export_params.UsageMetricExportParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncUsageMetricsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llamacloud-admin-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llamacloud-admin-python#with_streaming_response
        """
        return AsyncUsageMetricsResourceWithStreamingResponse(self)

    async def aggregate(
        self,
        *,
        day_on_or_after: str,
        day_on_or_before: str,
        group_by: SequenceNotStr[str],
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
        | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageMetricAggregateResponse:
        """
        Aggregate usage metrics by one or more dimensions, reporting total credits used.
        Global admin only.

        A date range is required, which bounds the scan via the `day`-leading index.
        Supplying `organization_id` narrows it further via the `(organization_id, day)`
        index.

        Supported `group_by` dimensions: `day`, `organization_id`, `project_id`,
        `event_type`, `user_id`. Buckets are ordered by total credits descending.

        Args:
          day_on_or_after: Inclusive lower bound on the day (YYYY-MM-DD, UTC)

          day_on_or_before: Inclusive upper bound on the day (YYYY-MM-DD, UTC)

          group_by: Dimensions to group by: day, organization_id, project_id, event_type, user_id

          event_types: Filter by event types

          organization_id: Filter by organization ID

          project_id: Filter by project ID

          user_id: Filter by user ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/admin/usage-metrics/aggregate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "day_on_or_after": day_on_or_after,
                        "day_on_or_before": day_on_or_before,
                        "group_by": group_by,
                        "event_types": event_types,
                        "organization_id": organization_id,
                        "project_id": project_id,
                        "user_id": user_id,
                    },
                    usage_metric_aggregate_params.UsageMetricAggregateParams,
                ),
            ),
            cast_to=UsageMetricAggregateResponse,
        )

    async def export(
        self,
        *,
        day_on_or_after: str,
        day_on_or_before: str,
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
        | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Export usage metrics line by line as CSV over a date range.

        Global admin only.

        Each row is a single usage metric. Use the optional filters to scope the export
        to an organization, project, user, or set of event types.

        Args:
          day_on_or_after: Inclusive lower bound on the day (YYYY-MM-DD, UTC)

          day_on_or_before: Inclusive upper bound on the day (YYYY-MM-DD, UTC)

          event_types: Filter by event types

          organization_id: Filter by organization ID

          project_id: Filter by project ID

          user_id: Filter by user ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/api/v1/admin/usage-metrics/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "day_on_or_after": day_on_or_after,
                        "day_on_or_before": day_on_or_before,
                        "event_types": event_types,
                        "organization_id": organization_id,
                        "project_id": project_id,
                        "user_id": user_id,
                    },
                    usage_metric_export_params.UsageMetricExportParams,
                ),
            ),
            cast_to=NoneType,
        )


class UsageMetricsResourceWithRawResponse:
    def __init__(self, usage_metrics: UsageMetricsResource) -> None:
        self._usage_metrics = usage_metrics

        self.aggregate = to_raw_response_wrapper(
            usage_metrics.aggregate,
        )
        self.export = to_raw_response_wrapper(
            usage_metrics.export,
        )


class AsyncUsageMetricsResourceWithRawResponse:
    def __init__(self, usage_metrics: AsyncUsageMetricsResource) -> None:
        self._usage_metrics = usage_metrics

        self.aggregate = async_to_raw_response_wrapper(
            usage_metrics.aggregate,
        )
        self.export = async_to_raw_response_wrapper(
            usage_metrics.export,
        )


class UsageMetricsResourceWithStreamingResponse:
    def __init__(self, usage_metrics: UsageMetricsResource) -> None:
        self._usage_metrics = usage_metrics

        self.aggregate = to_streamed_response_wrapper(
            usage_metrics.aggregate,
        )
        self.export = to_streamed_response_wrapper(
            usage_metrics.export,
        )


class AsyncUsageMetricsResourceWithStreamingResponse:
    def __init__(self, usage_metrics: AsyncUsageMetricsResource) -> None:
        self._usage_metrics = usage_metrics

        self.aggregate = async_to_streamed_response_wrapper(
            usage_metrics.aggregate,
        )
        self.export = async_to_streamed_response_wrapper(
            usage_metrics.export,
        )
