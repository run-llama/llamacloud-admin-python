# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_cloud_admin import LlamaCloudAdmin, AsyncLlamaCloudAdmin
from llama_cloud_admin.types import Invite, InviteAcceptResponse
from llama_cloud_admin.pagination import SyncPaginatedCursor, AsyncPaginatedCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvites:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloudAdmin) -> None:
        invite = client.invites.list()
        assert_matches_type(SyncPaginatedCursor[Invite], invite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloudAdmin) -> None:
        invite = client.invites.list(
            page_size=0,
            page_token="page_token",
        )
        assert_matches_type(SyncPaginatedCursor[Invite], invite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloudAdmin) -> None:
        response = client.invites.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = response.parse()
        assert_matches_type(SyncPaginatedCursor[Invite], invite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloudAdmin) -> None:
        with client.invites.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = response.parse()
            assert_matches_type(SyncPaginatedCursor[Invite], invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamaCloudAdmin) -> None:
        invite = client.invites.delete(
            "invite_id",
        )
        assert invite is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamaCloudAdmin) -> None:
        response = client.invites.with_raw_response.delete(
            "invite_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = response.parse()
        assert invite is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamaCloudAdmin) -> None:
        with client.invites.with_streaming_response.delete(
            "invite_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = response.parse()
            assert invite is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            client.invites.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_accept(self, client: LlamaCloudAdmin) -> None:
        invite = client.invites.accept(
            "invite_id",
        )
        assert_matches_type(InviteAcceptResponse, invite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_accept(self, client: LlamaCloudAdmin) -> None:
        response = client.invites.with_raw_response.accept(
            "invite_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = response.parse()
        assert_matches_type(InviteAcceptResponse, invite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_accept(self, client: LlamaCloudAdmin) -> None:
        with client.invites.with_streaming_response.accept(
            "invite_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = response.parse()
            assert_matches_type(InviteAcceptResponse, invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_accept(self, client: LlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            client.invites.with_raw_response.accept(
                "",
            )


class TestAsyncInvites:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloudAdmin) -> None:
        invite = await async_client.invites.list()
        assert_matches_type(AsyncPaginatedCursor[Invite], invite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloudAdmin) -> None:
        invite = await async_client.invites.list(
            page_size=0,
            page_token="page_token",
        )
        assert_matches_type(AsyncPaginatedCursor[Invite], invite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.invites.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = await response.parse()
        assert_matches_type(AsyncPaginatedCursor[Invite], invite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.invites.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = await response.parse()
            assert_matches_type(AsyncPaginatedCursor[Invite], invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaCloudAdmin) -> None:
        invite = await async_client.invites.delete(
            "invite_id",
        )
        assert invite is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.invites.with_raw_response.delete(
            "invite_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = await response.parse()
        assert invite is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.invites.with_streaming_response.delete(
            "invite_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = await response.parse()
            assert invite is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            await async_client.invites.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_accept(self, async_client: AsyncLlamaCloudAdmin) -> None:
        invite = await async_client.invites.accept(
            "invite_id",
        )
        assert_matches_type(InviteAcceptResponse, invite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_accept(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.invites.with_raw_response.accept(
            "invite_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = await response.parse()
        assert_matches_type(InviteAcceptResponse, invite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_accept(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.invites.with_streaming_response.accept(
            "invite_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = await response.parse()
            assert_matches_type(InviteAcceptResponse, invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_accept(self, async_client: AsyncLlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            await async_client.invites.with_raw_response.accept(
                "",
            )
