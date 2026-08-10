# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from llama_cloud_admin import LlamaCloudAdmin, AsyncLlamaCloudAdmin
from llama_cloud_admin.types import UserOrganizationRole
from llama_cloud_admin.types.organizations import (
    UserAddResponse,
    UserListResponse,
    UserListProjectsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloudAdmin) -> None:
        user = client.organizations.users.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloudAdmin) -> None:
        response = client.organizations.users.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloudAdmin) -> None:
        with client.organizations.users.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: LlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.users.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamaCloudAdmin) -> None:
        user = client.organizations.users.delete(
            member_user_id="member_user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: LlamaCloudAdmin) -> None:
        user = client.organizations.users.delete(
            member_user_id="member_user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamaCloudAdmin) -> None:
        response = client.organizations.users.with_raw_response.delete(
            member_user_id="member_user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamaCloudAdmin) -> None:
        with client.organizations.users.with_streaming_response.delete(
            member_user_id="member_user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.users.with_raw_response.delete(
                member_user_id="member_user_id",
                organization_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_user_id` but received ''"):
            client.organizations.users.with_raw_response.delete(
                member_user_id="",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: LlamaCloudAdmin) -> None:
        user = client.organizations.users.add(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}],
        )
        assert_matches_type(UserAddResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: LlamaCloudAdmin) -> None:
        response = client.organizations.users.with_raw_response.add(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserAddResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: LlamaCloudAdmin) -> None:
        with client.organizations.users.with_streaming_response.add(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserAddResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: LlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.users.with_raw_response.add(
                organization_id="",
                body=[{"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_to_project(self, client: LlamaCloudAdmin) -> None:
        user = client.organizations.users.add_to_project(
            user_id="user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_to_project_with_all_params(self, client: LlamaCloudAdmin) -> None:
        user = client.organizations.users.add_to_project(
            user_id="user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_to_project(self, client: LlamaCloudAdmin) -> None:
        response = client.organizations.users.with_raw_response.add_to_project(
            user_id="user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_to_project(self, client: LlamaCloudAdmin) -> None:
        with client.organizations.users.with_streaming_response.add_to_project(
            user_id="user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_to_project(self, client: LlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.users.with_raw_response.add_to_project(
                user_id="user_id",
                organization_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.organizations.users.with_raw_response.add_to_project(
                user_id="",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_assign_role(self, client: LlamaCloudAdmin) -> None:
        user = client.organizations.users.assign_role(
            path_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        )
        assert_matches_type(UserOrganizationRole, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_assign_role(self, client: LlamaCloudAdmin) -> None:
        response = client.organizations.users.with_raw_response.assign_role(
            path_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserOrganizationRole, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_assign_role(self, client: LlamaCloudAdmin) -> None:
        with client.organizations.users.with_streaming_response.assign_role(
            path_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserOrganizationRole, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_assign_role(self, client: LlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_organization_id` but received ''"):
            client.organizations.users.with_raw_response.assign_role(
                path_organization_id="",
                body_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="user_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_projects(self, client: LlamaCloudAdmin) -> None:
        user = client.organizations.users.list_projects(
            user_id="user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserListProjectsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_projects(self, client: LlamaCloudAdmin) -> None:
        response = client.organizations.users.with_raw_response.list_projects(
            user_id="user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListProjectsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_projects(self, client: LlamaCloudAdmin) -> None:
        with client.organizations.users.with_streaming_response.list_projects(
            user_id="user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListProjectsResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_projects(self, client: LlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.users.with_raw_response.list_projects(
                user_id="user_id",
                organization_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.organizations.users.with_raw_response.list_projects(
                user_id="",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_roles(self, client: LlamaCloudAdmin) -> None:
        user = client.organizations.users.list_roles(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[UserOrganizationRole], user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_roles_with_all_params(self, client: LlamaCloudAdmin) -> None:
        user = client.organizations.users.list_roles(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[UserOrganizationRole], user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_roles(self, client: LlamaCloudAdmin) -> None:
        response = client.organizations.users.with_raw_response.list_roles(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(Optional[UserOrganizationRole], user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_roles(self, client: LlamaCloudAdmin) -> None:
        with client.organizations.users.with_streaming_response.list_roles(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(Optional[UserOrganizationRole], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_roles(self, client: LlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.users.with_raw_response.list_roles(
                organization_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_from_project(self, client: LlamaCloudAdmin) -> None:
        user = client.organizations.users.remove_from_project(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        )
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove_from_project(self, client: LlamaCloudAdmin) -> None:
        response = client.organizations.users.with_raw_response.remove_from_project(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove_from_project(self, client: LlamaCloudAdmin) -> None:
        with client.organizations.users.with_streaming_response.remove_from_project(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove_from_project(self, client: LlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.users.with_raw_response.remove_from_project(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organization_id="",
                user_id="user_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.organizations.users.with_raw_response.remove_from_project(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.organizations.users.with_raw_response.remove_from_project(
                project_id="",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="user_id",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloudAdmin) -> None:
        user = await async_client.organizations.users.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.organizations.users.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.organizations.users.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.users.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaCloudAdmin) -> None:
        user = await async_client.organizations.users.delete(
            member_user_id="member_user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLlamaCloudAdmin) -> None:
        user = await async_client.organizations.users.delete(
            member_user_id="member_user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.organizations.users.with_raw_response.delete(
            member_user_id="member_user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.organizations.users.with_streaming_response.delete(
            member_user_id="member_user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.users.with_raw_response.delete(
                member_user_id="member_user_id",
                organization_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_user_id` but received ''"):
            await async_client.organizations.users.with_raw_response.delete(
                member_user_id="",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncLlamaCloudAdmin) -> None:
        user = await async_client.organizations.users.add(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}],
        )
        assert_matches_type(UserAddResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.organizations.users.with_raw_response.add(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserAddResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.organizations.users.with_streaming_response.add(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserAddResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncLlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.users.with_raw_response.add(
                organization_id="",
                body=[{"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_to_project(self, async_client: AsyncLlamaCloudAdmin) -> None:
        user = await async_client.organizations.users.add_to_project(
            user_id="user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_to_project_with_all_params(self, async_client: AsyncLlamaCloudAdmin) -> None:
        user = await async_client.organizations.users.add_to_project(
            user_id="user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_to_project(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.organizations.users.with_raw_response.add_to_project(
            user_id="user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_to_project(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.organizations.users.with_streaming_response.add_to_project(
            user_id="user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_to_project(self, async_client: AsyncLlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.users.with_raw_response.add_to_project(
                user_id="user_id",
                organization_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.organizations.users.with_raw_response.add_to_project(
                user_id="",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_assign_role(self, async_client: AsyncLlamaCloudAdmin) -> None:
        user = await async_client.organizations.users.assign_role(
            path_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        )
        assert_matches_type(UserOrganizationRole, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_assign_role(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.organizations.users.with_raw_response.assign_role(
            path_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserOrganizationRole, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_assign_role(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.organizations.users.with_streaming_response.assign_role(
            path_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserOrganizationRole, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_assign_role(self, async_client: AsyncLlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_organization_id` but received ''"):
            await async_client.organizations.users.with_raw_response.assign_role(
                path_organization_id="",
                body_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="user_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_projects(self, async_client: AsyncLlamaCloudAdmin) -> None:
        user = await async_client.organizations.users.list_projects(
            user_id="user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserListProjectsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_projects(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.organizations.users.with_raw_response.list_projects(
            user_id="user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListProjectsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_projects(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.organizations.users.with_streaming_response.list_projects(
            user_id="user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListProjectsResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_projects(self, async_client: AsyncLlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.users.with_raw_response.list_projects(
                user_id="user_id",
                organization_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.organizations.users.with_raw_response.list_projects(
                user_id="",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_roles(self, async_client: AsyncLlamaCloudAdmin) -> None:
        user = await async_client.organizations.users.list_roles(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[UserOrganizationRole], user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_roles_with_all_params(self, async_client: AsyncLlamaCloudAdmin) -> None:
        user = await async_client.organizations.users.list_roles(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[UserOrganizationRole], user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_roles(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.organizations.users.with_raw_response.list_roles(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(Optional[UserOrganizationRole], user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_roles(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.organizations.users.with_streaming_response.list_roles(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(Optional[UserOrganizationRole], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_roles(self, async_client: AsyncLlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.users.with_raw_response.list_roles(
                organization_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_from_project(self, async_client: AsyncLlamaCloudAdmin) -> None:
        user = await async_client.organizations.users.remove_from_project(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        )
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove_from_project(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.organizations.users.with_raw_response.remove_from_project(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove_from_project(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.organizations.users.with_streaming_response.remove_from_project(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove_from_project(self, async_client: AsyncLlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.users.with_raw_response.remove_from_project(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organization_id="",
                user_id="user_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.organizations.users.with_raw_response.remove_from_project(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.organizations.users.with_raw_response.remove_from_project(
                project_id="",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="user_id",
            )
