# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_cloud_admin import LlamaCloudAdmin, AsyncLlamaCloudAdmin
from llama_cloud_admin.types.admin import UserClaims

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_claims(self, client: LlamaCloudAdmin) -> None:
        user = client.admin.users.get_claims(
            "user_id",
        )
        assert_matches_type(UserClaims, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_claims(self, client: LlamaCloudAdmin) -> None:
        response = client.admin.users.with_raw_response.get_claims(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserClaims, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_claims(self, client: LlamaCloudAdmin) -> None:
        with client.admin.users.with_streaming_response.get_claims(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserClaims, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_claims(self, client: LlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.admin.users.with_raw_response.get_claims(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_claims(self, client: LlamaCloudAdmin) -> None:
        user = client.admin.users.update_claims(
            user_id="user_id",
        )
        assert_matches_type(UserClaims, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_claims_with_all_params(self, client: LlamaCloudAdmin) -> None:
        user = client.admin.users.update_claims(
            user_id="user_id",
            remove_claims=["allowed_org_creation"],
            set_claims={
                "allow_org_deletion": True,
                "allowed_org_creation": True,
                "api_datasource_access": True,
                "maximum_org_creation": 0,
            },
        )
        assert_matches_type(UserClaims, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_claims(self, client: LlamaCloudAdmin) -> None:
        response = client.admin.users.with_raw_response.update_claims(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserClaims, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_claims(self, client: LlamaCloudAdmin) -> None:
        with client.admin.users.with_streaming_response.update_claims(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserClaims, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_claims(self, client: LlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.admin.users.with_raw_response.update_claims(
                user_id="",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_claims(self, async_client: AsyncLlamaCloudAdmin) -> None:
        user = await async_client.admin.users.get_claims(
            "user_id",
        )
        assert_matches_type(UserClaims, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_claims(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.admin.users.with_raw_response.get_claims(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserClaims, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_claims(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.admin.users.with_streaming_response.get_claims(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserClaims, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_claims(self, async_client: AsyncLlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.admin.users.with_raw_response.get_claims(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_claims(self, async_client: AsyncLlamaCloudAdmin) -> None:
        user = await async_client.admin.users.update_claims(
            user_id="user_id",
        )
        assert_matches_type(UserClaims, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_claims_with_all_params(self, async_client: AsyncLlamaCloudAdmin) -> None:
        user = await async_client.admin.users.update_claims(
            user_id="user_id",
            remove_claims=["allowed_org_creation"],
            set_claims={
                "allow_org_deletion": True,
                "allowed_org_creation": True,
                "api_datasource_access": True,
                "maximum_org_creation": 0,
            },
        )
        assert_matches_type(UserClaims, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_claims(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.admin.users.with_raw_response.update_claims(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserClaims, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_claims(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.admin.users.with_streaming_response.update_claims(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserClaims, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_claims(self, async_client: AsyncLlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.admin.users.with_raw_response.update_claims(
                user_id="",
            )
