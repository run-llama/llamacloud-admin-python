# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.admin import user_update_claims_params
from ..._base_client import make_request_options
from ...types.admin.user_claims import UserClaims

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-admin-py#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-admin-py#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def get_claims(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserClaims:
        """
        Get a user's resolved custom claims.

        Claims that have not been explicitly set fall back to their system default.
        Returns 404 if the user does not exist.

        Global admin only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/api/v1/admin/users/{user_id}/claims", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserClaims,
        )

    def update_claims(
        self,
        user_id: str,
        *,
        remove_claims: Optional[
            List[Literal["allow_org_deletion", "allowed_org_creation", "api_datasource_access", "maximum_org_creation"]]
        ]
        | Omit = omit,
        set_claims: Optional[user_update_claims_params.SetClaims] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserClaims:
        """
        Additively update a user's custom claims.

        Claims in `set_claims` are added or overwritten; claims named in `remove_claims`
        are reset to their system default. Claims not referenced by either field are
        left unchanged, so a single claim can be changed without resending the full set.
        Returns the user's resolved claims after the update.

        Returns 404 if the user does not exist.

        Global admin only.

        Args:
          remove_claims: Names of claims to reset to their system default.

          set_claims: A partial set of custom claims for additive updates.

              Every field is optional. Only the claims explicitly provided in a request are
              added or overwritten; claims left unset are not touched, so callers can change a
              single claim without resending the full claim set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            path_template("/api/v1/admin/users/{user_id}/claims", user_id=user_id),
            body=maybe_transform(
                {
                    "remove_claims": remove_claims,
                    "set_claims": set_claims,
                },
                user_update_claims_params.UserUpdateClaimsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserClaims,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-admin-py#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-admin-py#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def get_claims(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserClaims:
        """
        Get a user's resolved custom claims.

        Claims that have not been explicitly set fall back to their system default.
        Returns 404 if the user does not exist.

        Global admin only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/api/v1/admin/users/{user_id}/claims", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserClaims,
        )

    async def update_claims(
        self,
        user_id: str,
        *,
        remove_claims: Optional[
            List[Literal["allow_org_deletion", "allowed_org_creation", "api_datasource_access", "maximum_org_creation"]]
        ]
        | Omit = omit,
        set_claims: Optional[user_update_claims_params.SetClaims] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserClaims:
        """
        Additively update a user's custom claims.

        Claims in `set_claims` are added or overwritten; claims named in `remove_claims`
        are reset to their system default. Claims not referenced by either field are
        left unchanged, so a single claim can be changed without resending the full set.
        Returns the user's resolved claims after the update.

        Returns 404 if the user does not exist.

        Global admin only.

        Args:
          remove_claims: Names of claims to reset to their system default.

          set_claims: A partial set of custom claims for additive updates.

              Every field is optional. Only the claims explicitly provided in a request are
              added or overwritten; claims left unset are not touched, so callers can change a
              single claim without resending the full claim set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            path_template("/api/v1/admin/users/{user_id}/claims", user_id=user_id),
            body=await async_maybe_transform(
                {
                    "remove_claims": remove_claims,
                    "set_claims": set_claims,
                },
                user_update_claims_params.UserUpdateClaimsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserClaims,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.get_claims = to_raw_response_wrapper(
            users.get_claims,
        )
        self.update_claims = to_raw_response_wrapper(
            users.update_claims,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.get_claims = async_to_raw_response_wrapper(
            users.get_claims,
        )
        self.update_claims = async_to_raw_response_wrapper(
            users.update_claims,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.get_claims = to_streamed_response_wrapper(
            users.get_claims,
        )
        self.update_claims = to_streamed_response_wrapper(
            users.update_claims,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.get_claims = async_to_streamed_response_wrapper(
            users.get_claims,
        )
        self.update_claims = async_to_streamed_response_wrapper(
            users.update_claims,
        )
