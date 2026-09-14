# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import quota_management_list_params, quota_management_create_params, quota_management_delete_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.quota_configuration import QuotaConfiguration
from ..types.quota_management_list_response import QuotaManagementListResponse

__all__ = ["QuotaManagementResource", "AsyncQuotaManagementResource"]


class QuotaManagementResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QuotaManagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llamacloud-admin-python#accessing-raw-response-data-eg-headers
        """
        return QuotaManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuotaManagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llamacloud-admin-python#with_streaming_response
        """
        return QuotaManagementResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        organization_id: str,
        setting: Literal["allow_pay_as_you_go", "limit_daily_usage_credits", "limit_monthly_usage_credits"],
        value: int,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuotaConfiguration:
        """
        Create a quota configuration for your organization, or for a single project
        within it.

        Args:
          setting: The quota setting to update

          value: The value for the setting. For boolean settings, use 1 (enabled) or 0
              (disabled). For credit limits, the number of credits allowed in the window;
              delete the setting to remove the limit. For limits denominated in USD cents, a
              whole number of dollars (a multiple of 100).

          project_id: Limit this project on its own. Omit to limit the organization as a whole. A
              project limit does not inherit from the organization limit: both apply, and
              whichever is reached first stops the work. Credit limits only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/quota-management",
            body=maybe_transform(
                {
                    "setting": setting,
                    "value": value,
                    "project_id": project_id,
                },
                quota_management_create_params.QuotaManagementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id}, quota_management_create_params.QuotaManagementCreateParams
                ),
            ),
            cast_to=QuotaConfiguration,
        )

    def list(
        self,
        *,
        source_id: str,
        source_type: Literal["GLOBAL", "organization", "plan_tier", "project"],
        configuration_type: Optional[
            Literal[
                "allow_pay_as_you_go",
                "limit_agent_coder_daily_usage_usd",
                "limit_agent_deployments",
                "limit_batch_files",
                "limit_classify_input_tokens",
                "limit_daily_usage_credits",
                "limit_directories",
                "limit_directory_files_per_directory",
                "limit_directory_ingest_download_size_bytes",
                "limit_directory_ingest_files",
                "limit_directory_sync_plan_actions",
                "limit_embedding_character",
                "limit_files_per_index",
                "limit_max_monthly_invoice_total_usd_cents",
                "limit_monthly_usage_credits",
                "limit_projects",
                "limit_split_categories",
                "limit_total_file_count",
                "limit_total_file_storage_bytes",
                "limit_users",
                "rate_limit_batch_api_creation",
                "rate_limit_chat_api_message",
                "rate_limit_classify_api_creation",
                "rate_limit_classify_api_list",
                "rate_limit_classify_api_query",
                "rate_limit_concurrent_jobs_in_execution_default",
                "rate_limit_concurrent_jobs_in_execution_doc_ingest",
                "rate_limit_concurrent_jobs_in_execution_metadata_update",
                "rate_limit_default_api_read",
                "rate_limit_default_api_write",
                "rate_limit_directory_file_api_read",
                "rate_limit_directory_file_api_write",
                "rate_limit_directory_ingest_project_job_creation",
                "rate_limit_extract_agent_creation",
                "rate_limit_extract_api_creation",
                "rate_limit_extract_api_list",
                "rate_limit_extract_api_query",
                "rate_limit_extract_concurrent_default",
                "rate_limit_file_api_read",
                "rate_limit_file_api_write",
                "rate_limit_index_v1_pipeline_concurrent_jobs",
                "rate_limit_parse_api_creation",
                "rate_limit_parse_api_list",
                "rate_limit_parse_api_query",
                "rate_limit_parse_concurrent_default",
                "rate_limit_parse_concurrent_pages_agentic",
                "rate_limit_parse_concurrent_pages_agentic_plus",
                "rate_limit_parse_concurrent_pages_cost_effective",
                "rate_limit_parse_concurrent_premium",
                "rate_limit_parse_token_bucket_agentic",
                "rate_limit_parse_token_bucket_agentic_plus",
                "rate_limit_parse_token_bucket_cost_effective",
                "rate_limit_parse_token_bucket_unknown_tier",
                "rate_limit_project_concurrent_jobs",
                "rate_limit_project_concurrent_turbo_jobs",
                "rate_limit_split_api_creation",
                "rate_limit_split_api_query",
                "rate_limit_spreadsheet_api_list",
                "rate_limit_spreadsheet_api_query",
                "rate_limit_spreadsheet_creation",
                "rate_limit_usage_api_query",
                "rate_limit_verify_api_creation",
                "rate_limit_verify_api_list",
                "rate_limit_verify_api_query",
            ]
        ]
        | Omit = omit,
        exclude_self_service: bool | Omit = omit,
        expand: bool | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuotaManagementListResponse:
        """Retrieve a paginated list of quota configurations with optional filtering.

        When
        expand=true, returns resolved quotas (effective values after fallback chain) and
        pagination parameters are ignored.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/beta/quota-management",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "source_id": source_id,
                        "source_type": source_type,
                        "configuration_type": configuration_type,
                        "exclude_self_service": exclude_self_service,
                        "expand": expand,
                        "page": page,
                        "page_size": page_size,
                    },
                    quota_management_list_params.QuotaManagementListParams,
                ),
            ),
            cast_to=QuotaManagementListResponse,
        )

    def delete(
        self,
        quota_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a quota configuration by removing the override.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not quota_id:
            raise ValueError(f"Expected a non-empty value for `quota_id` but received {quota_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/beta/quota-management/{quota_id}", quota_id=quota_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id}, quota_management_delete_params.QuotaManagementDeleteParams
                ),
            ),
            cast_to=NoneType,
        )


class AsyncQuotaManagementResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQuotaManagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llamacloud-admin-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQuotaManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuotaManagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llamacloud-admin-python#with_streaming_response
        """
        return AsyncQuotaManagementResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        organization_id: str,
        setting: Literal["allow_pay_as_you_go", "limit_daily_usage_credits", "limit_monthly_usage_credits"],
        value: int,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuotaConfiguration:
        """
        Create a quota configuration for your organization, or for a single project
        within it.

        Args:
          setting: The quota setting to update

          value: The value for the setting. For boolean settings, use 1 (enabled) or 0
              (disabled). For credit limits, the number of credits allowed in the window;
              delete the setting to remove the limit. For limits denominated in USD cents, a
              whole number of dollars (a multiple of 100).

          project_id: Limit this project on its own. Omit to limit the organization as a whole. A
              project limit does not inherit from the organization limit: both apply, and
              whichever is reached first stops the work. Credit limits only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/quota-management",
            body=await async_maybe_transform(
                {
                    "setting": setting,
                    "value": value,
                    "project_id": project_id,
                },
                quota_management_create_params.QuotaManagementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, quota_management_create_params.QuotaManagementCreateParams
                ),
            ),
            cast_to=QuotaConfiguration,
        )

    async def list(
        self,
        *,
        source_id: str,
        source_type: Literal["GLOBAL", "organization", "plan_tier", "project"],
        configuration_type: Optional[
            Literal[
                "allow_pay_as_you_go",
                "limit_agent_coder_daily_usage_usd",
                "limit_agent_deployments",
                "limit_batch_files",
                "limit_classify_input_tokens",
                "limit_daily_usage_credits",
                "limit_directories",
                "limit_directory_files_per_directory",
                "limit_directory_ingest_download_size_bytes",
                "limit_directory_ingest_files",
                "limit_directory_sync_plan_actions",
                "limit_embedding_character",
                "limit_files_per_index",
                "limit_max_monthly_invoice_total_usd_cents",
                "limit_monthly_usage_credits",
                "limit_projects",
                "limit_split_categories",
                "limit_total_file_count",
                "limit_total_file_storage_bytes",
                "limit_users",
                "rate_limit_batch_api_creation",
                "rate_limit_chat_api_message",
                "rate_limit_classify_api_creation",
                "rate_limit_classify_api_list",
                "rate_limit_classify_api_query",
                "rate_limit_concurrent_jobs_in_execution_default",
                "rate_limit_concurrent_jobs_in_execution_doc_ingest",
                "rate_limit_concurrent_jobs_in_execution_metadata_update",
                "rate_limit_default_api_read",
                "rate_limit_default_api_write",
                "rate_limit_directory_file_api_read",
                "rate_limit_directory_file_api_write",
                "rate_limit_directory_ingest_project_job_creation",
                "rate_limit_extract_agent_creation",
                "rate_limit_extract_api_creation",
                "rate_limit_extract_api_list",
                "rate_limit_extract_api_query",
                "rate_limit_extract_concurrent_default",
                "rate_limit_file_api_read",
                "rate_limit_file_api_write",
                "rate_limit_index_v1_pipeline_concurrent_jobs",
                "rate_limit_parse_api_creation",
                "rate_limit_parse_api_list",
                "rate_limit_parse_api_query",
                "rate_limit_parse_concurrent_default",
                "rate_limit_parse_concurrent_pages_agentic",
                "rate_limit_parse_concurrent_pages_agentic_plus",
                "rate_limit_parse_concurrent_pages_cost_effective",
                "rate_limit_parse_concurrent_premium",
                "rate_limit_parse_token_bucket_agentic",
                "rate_limit_parse_token_bucket_agentic_plus",
                "rate_limit_parse_token_bucket_cost_effective",
                "rate_limit_parse_token_bucket_unknown_tier",
                "rate_limit_project_concurrent_jobs",
                "rate_limit_project_concurrent_turbo_jobs",
                "rate_limit_split_api_creation",
                "rate_limit_split_api_query",
                "rate_limit_spreadsheet_api_list",
                "rate_limit_spreadsheet_api_query",
                "rate_limit_spreadsheet_creation",
                "rate_limit_usage_api_query",
                "rate_limit_verify_api_creation",
                "rate_limit_verify_api_list",
                "rate_limit_verify_api_query",
            ]
        ]
        | Omit = omit,
        exclude_self_service: bool | Omit = omit,
        expand: bool | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuotaManagementListResponse:
        """Retrieve a paginated list of quota configurations with optional filtering.

        When
        expand=true, returns resolved quotas (effective values after fallback chain) and
        pagination parameters are ignored.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/beta/quota-management",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "source_id": source_id,
                        "source_type": source_type,
                        "configuration_type": configuration_type,
                        "exclude_self_service": exclude_self_service,
                        "expand": expand,
                        "page": page,
                        "page_size": page_size,
                    },
                    quota_management_list_params.QuotaManagementListParams,
                ),
            ),
            cast_to=QuotaManagementListResponse,
        )

    async def delete(
        self,
        quota_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a quota configuration by removing the override.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not quota_id:
            raise ValueError(f"Expected a non-empty value for `quota_id` but received {quota_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/beta/quota-management/{quota_id}", quota_id=quota_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, quota_management_delete_params.QuotaManagementDeleteParams
                ),
            ),
            cast_to=NoneType,
        )


class QuotaManagementResourceWithRawResponse:
    def __init__(self, quota_management: QuotaManagementResource) -> None:
        self._quota_management = quota_management

        self.create = to_raw_response_wrapper(
            quota_management.create,
        )
        self.list = to_raw_response_wrapper(
            quota_management.list,
        )
        self.delete = to_raw_response_wrapper(
            quota_management.delete,
        )


class AsyncQuotaManagementResourceWithRawResponse:
    def __init__(self, quota_management: AsyncQuotaManagementResource) -> None:
        self._quota_management = quota_management

        self.create = async_to_raw_response_wrapper(
            quota_management.create,
        )
        self.list = async_to_raw_response_wrapper(
            quota_management.list,
        )
        self.delete = async_to_raw_response_wrapper(
            quota_management.delete,
        )


class QuotaManagementResourceWithStreamingResponse:
    def __init__(self, quota_management: QuotaManagementResource) -> None:
        self._quota_management = quota_management

        self.create = to_streamed_response_wrapper(
            quota_management.create,
        )
        self.list = to_streamed_response_wrapper(
            quota_management.list,
        )
        self.delete = to_streamed_response_wrapper(
            quota_management.delete,
        )


class AsyncQuotaManagementResourceWithStreamingResponse:
    def __init__(self, quota_management: AsyncQuotaManagementResource) -> None:
        self._quota_management = quota_management

        self.create = async_to_streamed_response_wrapper(
            quota_management.create,
        )
        self.list = async_to_streamed_response_wrapper(
            quota_management.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            quota_management.delete,
        )
