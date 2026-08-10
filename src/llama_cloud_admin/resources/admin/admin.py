# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ...types import admin_get_license_info_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .usage_metrics import (
    UsageMetricsResource,
    AsyncUsageMetricsResource,
    UsageMetricsResourceWithRawResponse,
    AsyncUsageMetricsResourceWithRawResponse,
    UsageMetricsResourceWithStreamingResponse,
    AsyncUsageMetricsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.admin_get_llms_info_response import AdminGetLlmsInfoResponse
from ...types.admin_get_s3_config_response import AdminGetS3ConfigResponse
from ...types.admin_get_ocr_status_response import AdminGetOcrStatusResponse
from ...types.admin_get_license_info_response import AdminGetLicenseInfoResponse
from ...types.admin_get_filestores_info_response import AdminGetFilestoresInfoResponse
from ...types.admin_get_llamaextract_features_response import AdminGetLlamaextractFeaturesResponse

__all__ = ["AdminResource", "AsyncAdminResource"]


class AdminResource(SyncAPIResource):
    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def usage_metrics(self) -> UsageMetricsResource:
        return UsageMetricsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-admin-py#accessing-raw-response-data-eg-headers
        """
        return AdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-admin-py#with_streaming_response
        """
        return AdminResourceWithStreamingResponse(self)

    def get_filestores_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminGetFilestoresInfoResponse:
        """Get File Store Info"""
        return self._get(
            "/api/v1/admin/filestores/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminGetFilestoresInfoResponse,
        )

    def get_license_info(
        self,
        *,
        include_scopes: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminGetLicenseInfoResponse:
        """
        Get License Info

        Args:
          include_scopes: Whether to include scopes in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/admin/license/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_scopes": include_scopes}, admin_get_license_info_params.AdminGetLicenseInfoParams
                ),
            ),
            cast_to=AdminGetLicenseInfoResponse,
        )

    def get_llamaextract_features(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminGetLlamaextractFeaturesResponse:
        """Get LlamaExtract feature availability based on available models."""
        return self._get(
            "/api/v1/admin/llamaextract/features",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminGetLlamaextractFeaturesResponse,
        )

    def get_llms_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminGetLlmsInfoResponse:
        """Get Llm Info"""
        return self._get(
            "/api/v1/admin/llms/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminGetLlmsInfoResponse,
        )

    def get_ocr_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminGetOcrStatusResponse:
        """Get OCR service health status including GPU availability."""
        return self._get(
            "/api/v1/admin/ocr/statusz",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminGetOcrStatusResponse,
        )

    def get_s3_config(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminGetS3ConfigResponse:
        """Return resolved S3 configuration and presigned URL signing details."""
        return self._get(
            "/api/v1/admin/s3/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminGetS3ConfigResponse,
        )


class AsyncAdminResource(AsyncAPIResource):
    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def usage_metrics(self) -> AsyncUsageMetricsResource:
        return AsyncUsageMetricsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-admin-py#accessing-raw-response-data-eg-headers
        """
        return AsyncAdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-admin-py#with_streaming_response
        """
        return AsyncAdminResourceWithStreamingResponse(self)

    async def get_filestores_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminGetFilestoresInfoResponse:
        """Get File Store Info"""
        return await self._get(
            "/api/v1/admin/filestores/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminGetFilestoresInfoResponse,
        )

    async def get_license_info(
        self,
        *,
        include_scopes: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminGetLicenseInfoResponse:
        """
        Get License Info

        Args:
          include_scopes: Whether to include scopes in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/admin/license/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_scopes": include_scopes}, admin_get_license_info_params.AdminGetLicenseInfoParams
                ),
            ),
            cast_to=AdminGetLicenseInfoResponse,
        )

    async def get_llamaextract_features(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminGetLlamaextractFeaturesResponse:
        """Get LlamaExtract feature availability based on available models."""
        return await self._get(
            "/api/v1/admin/llamaextract/features",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminGetLlamaextractFeaturesResponse,
        )

    async def get_llms_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminGetLlmsInfoResponse:
        """Get Llm Info"""
        return await self._get(
            "/api/v1/admin/llms/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminGetLlmsInfoResponse,
        )

    async def get_ocr_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminGetOcrStatusResponse:
        """Get OCR service health status including GPU availability."""
        return await self._get(
            "/api/v1/admin/ocr/statusz",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminGetOcrStatusResponse,
        )

    async def get_s3_config(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminGetS3ConfigResponse:
        """Return resolved S3 configuration and presigned URL signing details."""
        return await self._get(
            "/api/v1/admin/s3/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminGetS3ConfigResponse,
        )


class AdminResourceWithRawResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

        self.get_filestores_info = to_raw_response_wrapper(
            admin.get_filestores_info,
        )
        self.get_license_info = to_raw_response_wrapper(
            admin.get_license_info,
        )
        self.get_llamaextract_features = to_raw_response_wrapper(
            admin.get_llamaextract_features,
        )
        self.get_llms_info = to_raw_response_wrapper(
            admin.get_llms_info,
        )
        self.get_ocr_status = to_raw_response_wrapper(
            admin.get_ocr_status,
        )
        self.get_s3_config = to_raw_response_wrapper(
            admin.get_s3_config,
        )

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._admin.users)

    @cached_property
    def usage_metrics(self) -> UsageMetricsResourceWithRawResponse:
        return UsageMetricsResourceWithRawResponse(self._admin.usage_metrics)


class AsyncAdminResourceWithRawResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

        self.get_filestores_info = async_to_raw_response_wrapper(
            admin.get_filestores_info,
        )
        self.get_license_info = async_to_raw_response_wrapper(
            admin.get_license_info,
        )
        self.get_llamaextract_features = async_to_raw_response_wrapper(
            admin.get_llamaextract_features,
        )
        self.get_llms_info = async_to_raw_response_wrapper(
            admin.get_llms_info,
        )
        self.get_ocr_status = async_to_raw_response_wrapper(
            admin.get_ocr_status,
        )
        self.get_s3_config = async_to_raw_response_wrapper(
            admin.get_s3_config,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._admin.users)

    @cached_property
    def usage_metrics(self) -> AsyncUsageMetricsResourceWithRawResponse:
        return AsyncUsageMetricsResourceWithRawResponse(self._admin.usage_metrics)


class AdminResourceWithStreamingResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

        self.get_filestores_info = to_streamed_response_wrapper(
            admin.get_filestores_info,
        )
        self.get_license_info = to_streamed_response_wrapper(
            admin.get_license_info,
        )
        self.get_llamaextract_features = to_streamed_response_wrapper(
            admin.get_llamaextract_features,
        )
        self.get_llms_info = to_streamed_response_wrapper(
            admin.get_llms_info,
        )
        self.get_ocr_status = to_streamed_response_wrapper(
            admin.get_ocr_status,
        )
        self.get_s3_config = to_streamed_response_wrapper(
            admin.get_s3_config,
        )

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._admin.users)

    @cached_property
    def usage_metrics(self) -> UsageMetricsResourceWithStreamingResponse:
        return UsageMetricsResourceWithStreamingResponse(self._admin.usage_metrics)


class AsyncAdminResourceWithStreamingResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

        self.get_filestores_info = async_to_streamed_response_wrapper(
            admin.get_filestores_info,
        )
        self.get_license_info = async_to_streamed_response_wrapper(
            admin.get_license_info,
        )
        self.get_llamaextract_features = async_to_streamed_response_wrapper(
            admin.get_llamaextract_features,
        )
        self.get_llms_info = async_to_streamed_response_wrapper(
            admin.get_llms_info,
        )
        self.get_ocr_status = async_to_streamed_response_wrapper(
            admin.get_ocr_status,
        )
        self.get_s3_config = async_to_streamed_response_wrapper(
            admin.get_s3_config,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._admin.users)

    @cached_property
    def usage_metrics(self) -> AsyncUsageMetricsResourceWithStreamingResponse:
        return AsyncUsageMetricsResourceWithStreamingResponse(self._admin.usage_metrics)
