# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_cloud_admin import LlamaCloudAdmin, AsyncLlamaCloudAdmin
from llama_cloud_admin.types import APIKey, APIKeyDeleteResponse
from llama_cloud_admin._utils import parse_datetime
from llama_cloud_admin.pagination import SyncPaginatedCursor, AsyncPaginatedCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloudAdmin) -> None:
        api_key = client.api_keys.create()
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloudAdmin) -> None:
        api_key = client.api_keys.create(
            expires_at=parse_datetime("2026-12-31T23:59:59Z"),
            key_type="agent",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloudAdmin) -> None:
        response = client.api_keys.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloudAdmin) -> None:
        with client.api_keys.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloudAdmin) -> None:
        api_key = client.api_keys.list()
        assert_matches_type(SyncPaginatedCursor[APIKey], api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloudAdmin) -> None:
        api_key = client.api_keys.list(
            expand=["string"],
            key_type="agent",
            name="name",
            page_size=1,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncPaginatedCursor[APIKey], api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloudAdmin) -> None:
        response = client.api_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(SyncPaginatedCursor[APIKey], api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloudAdmin) -> None:
        with client.api_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(SyncPaginatedCursor[APIKey], api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamaCloudAdmin) -> None:
        api_key = client.api_keys.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamaCloudAdmin) -> None:
        response = client.api_keys.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamaCloudAdmin) -> None:
        with client.api_keys.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_id` but received ''"):
            client.api_keys.with_raw_response.delete(
                "",
            )


class TestAsyncAPIKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloudAdmin) -> None:
        api_key = await async_client.api_keys.create()
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloudAdmin) -> None:
        api_key = await async_client.api_keys.create(
            expires_at=parse_datetime("2026-12-31T23:59:59Z"),
            key_type="agent",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.api_keys.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.api_keys.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloudAdmin) -> None:
        api_key = await async_client.api_keys.list()
        assert_matches_type(AsyncPaginatedCursor[APIKey], api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloudAdmin) -> None:
        api_key = await async_client.api_keys.list(
            expand=["string"],
            key_type="agent",
            name="name",
            page_size=1,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncPaginatedCursor[APIKey], api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.api_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(AsyncPaginatedCursor[APIKey], api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.api_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(AsyncPaginatedCursor[APIKey], api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaCloudAdmin) -> None:
        api_key = await async_client.api_keys.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.api_keys.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.api_keys.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_id` but received ''"):
            await async_client.api_keys.with_raw_response.delete(
                "",
            )
