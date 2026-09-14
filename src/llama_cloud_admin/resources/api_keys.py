# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._resource import SyncAPIResource, AsyncAPIResource

from .._compat import cached_property

from ..types.api_key import APIKey

from .._utils import maybe_transform, path_template, async_maybe_transform

from .._base_client import make_request_options, AsyncPaginator

from typing import Union, Optional

from datetime import datetime

from .._types import Omit, omit, NotGiven, SequenceNotStr

from typing_extensions import Literal

from ..pagination import SyncPaginatedCursor, AsyncPaginatedCursor

from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from .._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ..types import api_key_create_params
from ..types import api_key_list_params

__all__ = ["APIKeysResource", "AsyncAPIKeysResource"]

class APIKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llamacloud-admin-python#accessing-raw-response-data-eg-headers
        """
        return APIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llamacloud-admin-python#with_streaming_response
        """
        return APIKeysResourceWithStreamingResponse(self)

    def create(self,
    *,
    expires_at: Union[str, datetime, None] | Omit = omit,
    key_type: Literal["agent", "user"] | Omit = omit,
    name: Optional[str] | Omit = omit,
    project_id: Optional[str] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> APIKey:
        """
        Create a new API key.

        If project_id is specified, validates the user can read that project.

        Args: api_key_create: API key creation data user: Current user db: Database
        session

        Returns: The created API key with the secret key visible in redacted_api_key
        field

        Args:
          expires_at: When the API key should expire. If not set, the key never expires.

          project_id: The project ID to associate with the API key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/api-keys",
            body=maybe_transform({
                "expires_at": expires_at,
                "key_type": key_type,
                "name": name,
                "project_id": project_id,
            }, api_key_create_params.APIKeyCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=APIKey,
        )

    def list(self,
    *,
    expand: SequenceNotStr[str] | Omit = omit,
    key_type: Optional[Literal["agent", "user"]] | Omit = omit,
    name: Optional[str] | Omit = omit,
    page_size: Optional[int] | Omit = omit,
    page_token: Optional[str] | Omit = omit,
    project_id: Optional[str] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> SyncPaginatedCursor[APIKey]:
        """
        List API keys.

        If project_id is provided, validates user has access to that project. If
        project_id is not provided, scopes results to the current user.

        Args: user: Current user page_size: Number of items per page page_token: Token
        for pagination name: Filter by API key name project_id: Filter by project ID
        key_type: Filter by key type

        Returns: Paginated response with API keys

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/api-keys",
            page = SyncPaginatedCursor[APIKey],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "expand": expand,
                "key_type": key_type,
                "name": name,
                "page_size": page_size,
                "page_token": page_token,
                "project_id": project_id,
            }, api_key_list_params.APIKeyListParams)),
            model=APIKey,
        )

    def delete(self,
    api_key_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Delete an API key.

        If the API key belongs to a project, validates user has admin permissions for
        that project. If the API key has no project, validates it belongs to the current
        user.

        Args: api_key_id: The ID of the API key to delete user: Current user

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_id:
          raise ValueError(
            f'Expected a non-empty value for `api_key_id` but received {api_key_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/beta/api-keys/{api_key_id}", api_key_id=api_key_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

class AsyncAPIKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llamacloud-admin-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llamacloud-admin-python#with_streaming_response
        """
        return AsyncAPIKeysResourceWithStreamingResponse(self)

    async def create(self,
    *,
    expires_at: Union[str, datetime, None] | Omit = omit,
    key_type: Literal["agent", "user"] | Omit = omit,
    name: Optional[str] | Omit = omit,
    project_id: Optional[str] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> APIKey:
        """
        Create a new API key.

        If project_id is specified, validates the user can read that project.

        Args: api_key_create: API key creation data user: Current user db: Database
        session

        Returns: The created API key with the secret key visible in redacted_api_key
        field

        Args:
          expires_at: When the API key should expire. If not set, the key never expires.

          project_id: The project ID to associate with the API key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/api-keys",
            body=await async_maybe_transform({
                "expires_at": expires_at,
                "key_type": key_type,
                "name": name,
                "project_id": project_id,
            }, api_key_create_params.APIKeyCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=APIKey,
        )

    def list(self,
    *,
    expand: SequenceNotStr[str] | Omit = omit,
    key_type: Optional[Literal["agent", "user"]] | Omit = omit,
    name: Optional[str] | Omit = omit,
    page_size: Optional[int] | Omit = omit,
    page_token: Optional[str] | Omit = omit,
    project_id: Optional[str] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> AsyncPaginator[APIKey, AsyncPaginatedCursor[APIKey]]:
        """
        List API keys.

        If project_id is provided, validates user has access to that project. If
        project_id is not provided, scopes results to the current user.

        Args: user: Current user page_size: Number of items per page page_token: Token
        for pagination name: Filter by API key name project_id: Filter by project ID
        key_type: Filter by key type

        Returns: Paginated response with API keys

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/api-keys",
            page = AsyncPaginatedCursor[APIKey],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "expand": expand,
                "key_type": key_type,
                "name": name,
                "page_size": page_size,
                "page_token": page_token,
                "project_id": project_id,
            }, api_key_list_params.APIKeyListParams)),
            model=APIKey,
        )

    async def delete(self,
    api_key_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Delete an API key.

        If the API key belongs to a project, validates user has admin permissions for
        that project. If the API key has no project, validates it belongs to the current
        user.

        Args: api_key_id: The ID of the API key to delete user: Current user

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_id:
          raise ValueError(
            f'Expected a non-empty value for `api_key_id` but received {api_key_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/beta/api-keys/{api_key_id}", api_key_id=api_key_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

class APIKeysResourceWithRawResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = to_raw_response_wrapper(
            api_keys.create,
        )
        self.list = to_raw_response_wrapper(
            api_keys.list,
        )
        self.delete = to_raw_response_wrapper(
            api_keys.delete,
        )

class AsyncAPIKeysResourceWithRawResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = async_to_raw_response_wrapper(
            api_keys.create,
        )
        self.list = async_to_raw_response_wrapper(
            api_keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            api_keys.delete,
        )

class APIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = to_streamed_response_wrapper(
            api_keys.create,
        )
        self.list = to_streamed_response_wrapper(
            api_keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            api_keys.delete,
        )

class AsyncAPIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = async_to_streamed_response_wrapper(
            api_keys.create,
        )
        self.list = async_to_streamed_response_wrapper(
            api_keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            api_keys.delete,
        )