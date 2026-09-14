# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_cloud_admin import LlamaCloudAdmin, AsyncLlamaCloudAdmin
from llama_cloud_admin.types import (
    QuotaConfiguration,
)
from llama_cloud_admin.pagination import SyncPaginatedPageNumber, AsyncPaginatedPageNumber

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuotaManagement:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloudAdmin) -> None:
        quota_management = client.quota_management.create(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            setting="allow_pay_as_you_go",
            value=0,
        )
        assert_matches_type(QuotaConfiguration, quota_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloudAdmin) -> None:
        quota_management = client.quota_management.create(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            setting="allow_pay_as_you_go",
            value=0,
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(QuotaConfiguration, quota_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloudAdmin) -> None:
        response = client.quota_management.with_raw_response.create(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            setting="allow_pay_as_you_go",
            value=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quota_management = response.parse()
        assert_matches_type(QuotaConfiguration, quota_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloudAdmin) -> None:
        with client.quota_management.with_streaming_response.create(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            setting="allow_pay_as_you_go",
            value=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quota_management = response.parse()
            assert_matches_type(QuotaConfiguration, quota_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloudAdmin) -> None:
        quota_management = client.quota_management.list(
            source_id="source_id",
            source_type="GLOBAL",
        )
        assert_matches_type(SyncPaginatedPageNumber[QuotaConfiguration], quota_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloudAdmin) -> None:
        quota_management = client.quota_management.list(
            source_id="source_id",
            source_type="GLOBAL",
            configuration_type="allow_pay_as_you_go",
            exclude_self_service=True,
            expand=True,
            page=0,
            page_size=1,
        )
        assert_matches_type(SyncPaginatedPageNumber[QuotaConfiguration], quota_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloudAdmin) -> None:
        response = client.quota_management.with_raw_response.list(
            source_id="source_id",
            source_type="GLOBAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quota_management = response.parse()
        assert_matches_type(SyncPaginatedPageNumber[QuotaConfiguration], quota_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloudAdmin) -> None:
        with client.quota_management.with_streaming_response.list(
            source_id="source_id",
            source_type="GLOBAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quota_management = response.parse()
            assert_matches_type(SyncPaginatedPageNumber[QuotaConfiguration], quota_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamaCloudAdmin) -> None:
        quota_management = client.quota_management.delete(
            quota_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert quota_management is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamaCloudAdmin) -> None:
        response = client.quota_management.with_raw_response.delete(
            quota_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quota_management = response.parse()
        assert quota_management is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamaCloudAdmin) -> None:
        with client.quota_management.with_streaming_response.delete(
            quota_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quota_management = response.parse()
            assert quota_management is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `quota_id` but received ''"):
            client.quota_management.with_raw_response.delete(
                quota_id="",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncQuotaManagement:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloudAdmin) -> None:
        quota_management = await async_client.quota_management.create(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            setting="allow_pay_as_you_go",
            value=0,
        )
        assert_matches_type(QuotaConfiguration, quota_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloudAdmin) -> None:
        quota_management = await async_client.quota_management.create(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            setting="allow_pay_as_you_go",
            value=0,
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(QuotaConfiguration, quota_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.quota_management.with_raw_response.create(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            setting="allow_pay_as_you_go",
            value=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quota_management = await response.parse()
        assert_matches_type(QuotaConfiguration, quota_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.quota_management.with_streaming_response.create(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            setting="allow_pay_as_you_go",
            value=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quota_management = await response.parse()
            assert_matches_type(QuotaConfiguration, quota_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloudAdmin) -> None:
        quota_management = await async_client.quota_management.list(
            source_id="source_id",
            source_type="GLOBAL",
        )
        assert_matches_type(AsyncPaginatedPageNumber[QuotaConfiguration], quota_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloudAdmin) -> None:
        quota_management = await async_client.quota_management.list(
            source_id="source_id",
            source_type="GLOBAL",
            configuration_type="allow_pay_as_you_go",
            exclude_self_service=True,
            expand=True,
            page=0,
            page_size=1,
        )
        assert_matches_type(AsyncPaginatedPageNumber[QuotaConfiguration], quota_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.quota_management.with_raw_response.list(
            source_id="source_id",
            source_type="GLOBAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quota_management = await response.parse()
        assert_matches_type(AsyncPaginatedPageNumber[QuotaConfiguration], quota_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.quota_management.with_streaming_response.list(
            source_id="source_id",
            source_type="GLOBAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quota_management = await response.parse()
            assert_matches_type(AsyncPaginatedPageNumber[QuotaConfiguration], quota_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaCloudAdmin) -> None:
        quota_management = await async_client.quota_management.delete(
            quota_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert quota_management is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.quota_management.with_raw_response.delete(
            quota_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quota_management = await response.parse()
        assert quota_management is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.quota_management.with_streaming_response.delete(
            quota_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quota_management = await response.parse()
            assert quota_management is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaCloudAdmin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `quota_id` but received ''"):
            await async_client.quota_management.with_raw_response.delete(
                quota_id="",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
