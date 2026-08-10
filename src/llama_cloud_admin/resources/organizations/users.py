# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.organizations import (
    user_add_params,
    user_list_roles_params,
    user_assign_role_params,
    user_add_to_project_params,
)
from ...types.user_organization_role import UserOrganizationRole
from ...types.organizations.user_add_response import UserAddResponse
from ...types.organizations.user_list_members_response import UserListMembersResponse
from ...types.organizations.user_list_projects_response import UserListProjectsResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llamacloud-admin-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llamacloud-admin-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def delete(
        self,
        member_user_id: str,
        *,
        organization_id: str,
        body: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove users from an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not member_user_id:
            raise ValueError(f"Expected a non-empty value for `member_user_id` but received {member_user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/api/v1/organizations/{organization_id}/users/{member_user_id}",
                organization_id=organization_id,
                member_user_id=member_user_id,
            ),
            body=maybe_transform(body, Optional[SequenceNotStr[str]]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def add(
        self,
        organization_id: str,
        *,
        body: Iterable[user_add_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserAddResponse:
        """
        Add a user to an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._put(
            path_template("/api/v1/organizations/{organization_id}/users", organization_id=organization_id),
            body=maybe_transform(body, Iterable[user_add_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAddResponse,
        )

    def add_to_project(
        self,
        user_id: str,
        *,
        organization_id: str,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Add a user to a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._put(
            path_template(
                "/api/v1/organizations/{organization_id}/users/{user_id}/projects",
                organization_id=organization_id,
                user_id=user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, user_add_to_project_params.UserAddToProjectParams),
            ),
            cast_to=object,
        )

    def assign_role(
        self,
        path_organization_id: str,
        *,
        body_organization_id: str,
        role_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserOrganizationRole:
        """
        Assign a role to a user in an organization.

        Args:
          body_organization_id: The organization's ID.

          role_id: The role's ID.

          user_id: The user's ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_organization_id:
            raise ValueError(
                f"Expected a non-empty value for `path_organization_id` but received {path_organization_id!r}"
            )
        return self._put(
            path_template(
                "/api/v1/organizations/{path_organization_id}/users/roles", path_organization_id=path_organization_id
            ),
            body=maybe_transform(
                {
                    "body_organization_id": body_organization_id,
                    "role_id": role_id,
                    "user_id": user_id,
                },
                user_assign_role_params.UserAssignRoleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserOrganizationRole,
        )

    def list_members(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListMembersResponse:
        """
        Get all users in an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            path_template("/api/v1/organizations/{organization_id}/users", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListMembersResponse,
        )

    def list_projects(
        self,
        user_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListProjectsResponse:
        """
        List all projects for a user in an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template(
                "/api/v1/organizations/{organization_id}/users/{user_id}/projects",
                organization_id=organization_id,
                user_id=user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListProjectsResponse,
        )

    def list_roles(
        self,
        organization_id: str,
        *,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserOrganizationRole]:
        """
        Get the role of a user in an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            path_template("/api/v1/organizations/{organization_id}/users/roles", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, user_list_roles_params.UserListRolesParams),
            ),
            cast_to=UserOrganizationRole,
        )

    def remove_from_project(
        self,
        project_id: str,
        *,
        organization_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Remove a user from a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._delete(
            path_template(
                "/api/v1/organizations/{organization_id}/users/{user_id}/projects/{project_id}",
                organization_id=organization_id,
                user_id=user_id,
                project_id=project_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llamacloud-admin-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llamacloud-admin-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def delete(
        self,
        member_user_id: str,
        *,
        organization_id: str,
        body: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove users from an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not member_user_id:
            raise ValueError(f"Expected a non-empty value for `member_user_id` but received {member_user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/api/v1/organizations/{organization_id}/users/{member_user_id}",
                organization_id=organization_id,
                member_user_id=member_user_id,
            ),
            body=await async_maybe_transform(body, Optional[SequenceNotStr[str]]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def add(
        self,
        organization_id: str,
        *,
        body: Iterable[user_add_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserAddResponse:
        """
        Add a user to an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._put(
            path_template("/api/v1/organizations/{organization_id}/users", organization_id=organization_id),
            body=await async_maybe_transform(body, Iterable[user_add_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAddResponse,
        )

    async def add_to_project(
        self,
        user_id: str,
        *,
        organization_id: str,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Add a user to a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._put(
            path_template(
                "/api/v1/organizations/{organization_id}/users/{user_id}/projects",
                organization_id=organization_id,
                user_id=user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, user_add_to_project_params.UserAddToProjectParams
                ),
            ),
            cast_to=object,
        )

    async def assign_role(
        self,
        path_organization_id: str,
        *,
        body_organization_id: str,
        role_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserOrganizationRole:
        """
        Assign a role to a user in an organization.

        Args:
          body_organization_id: The organization's ID.

          role_id: The role's ID.

          user_id: The user's ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_organization_id:
            raise ValueError(
                f"Expected a non-empty value for `path_organization_id` but received {path_organization_id!r}"
            )
        return await self._put(
            path_template(
                "/api/v1/organizations/{path_organization_id}/users/roles", path_organization_id=path_organization_id
            ),
            body=await async_maybe_transform(
                {
                    "body_organization_id": body_organization_id,
                    "role_id": role_id,
                    "user_id": user_id,
                },
                user_assign_role_params.UserAssignRoleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserOrganizationRole,
        )

    async def list_members(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListMembersResponse:
        """
        Get all users in an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            path_template("/api/v1/organizations/{organization_id}/users", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListMembersResponse,
        )

    async def list_projects(
        self,
        user_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListProjectsResponse:
        """
        List all projects for a user in an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template(
                "/api/v1/organizations/{organization_id}/users/{user_id}/projects",
                organization_id=organization_id,
                user_id=user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListProjectsResponse,
        )

    async def list_roles(
        self,
        organization_id: str,
        *,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserOrganizationRole]:
        """
        Get the role of a user in an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            path_template("/api/v1/organizations/{organization_id}/users/roles", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, user_list_roles_params.UserListRolesParams
                ),
            ),
            cast_to=UserOrganizationRole,
        )

    async def remove_from_project(
        self,
        project_id: str,
        *,
        organization_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Remove a user from a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._delete(
            path_template(
                "/api/v1/organizations/{organization_id}/users/{user_id}/projects/{project_id}",
                organization_id=organization_id,
                user_id=user_id,
                project_id=project_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.delete = to_raw_response_wrapper(
            users.delete,
        )
        self.add = to_raw_response_wrapper(
            users.add,
        )
        self.add_to_project = to_raw_response_wrapper(
            users.add_to_project,
        )
        self.assign_role = to_raw_response_wrapper(
            users.assign_role,
        )
        self.list_members = to_raw_response_wrapper(
            users.list_members,
        )
        self.list_projects = to_raw_response_wrapper(
            users.list_projects,
        )
        self.list_roles = to_raw_response_wrapper(
            users.list_roles,
        )
        self.remove_from_project = to_raw_response_wrapper(
            users.remove_from_project,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )
        self.add = async_to_raw_response_wrapper(
            users.add,
        )
        self.add_to_project = async_to_raw_response_wrapper(
            users.add_to_project,
        )
        self.assign_role = async_to_raw_response_wrapper(
            users.assign_role,
        )
        self.list_members = async_to_raw_response_wrapper(
            users.list_members,
        )
        self.list_projects = async_to_raw_response_wrapper(
            users.list_projects,
        )
        self.list_roles = async_to_raw_response_wrapper(
            users.list_roles,
        )
        self.remove_from_project = async_to_raw_response_wrapper(
            users.remove_from_project,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.delete = to_streamed_response_wrapper(
            users.delete,
        )
        self.add = to_streamed_response_wrapper(
            users.add,
        )
        self.add_to_project = to_streamed_response_wrapper(
            users.add_to_project,
        )
        self.assign_role = to_streamed_response_wrapper(
            users.assign_role,
        )
        self.list_members = to_streamed_response_wrapper(
            users.list_members,
        )
        self.list_projects = to_streamed_response_wrapper(
            users.list_projects,
        )
        self.list_roles = to_streamed_response_wrapper(
            users.list_roles,
        )
        self.remove_from_project = to_streamed_response_wrapper(
            users.remove_from_project,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            users.add,
        )
        self.add_to_project = async_to_streamed_response_wrapper(
            users.add_to_project,
        )
        self.assign_role = async_to_streamed_response_wrapper(
            users.assign_role,
        )
        self.list_members = async_to_streamed_response_wrapper(
            users.list_members,
        )
        self.list_projects = async_to_streamed_response_wrapper(
            users.list_projects,
        )
        self.list_roles = async_to_streamed_response_wrapper(
            users.list_roles,
        )
        self.remove_from_project = async_to_streamed_response_wrapper(
            users.remove_from_project,
        )
