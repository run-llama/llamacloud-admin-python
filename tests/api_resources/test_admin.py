# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_cloud_admin import LlamaCloudAdmin, AsyncLlamaCloudAdmin
from llama_cloud_admin.types import (
    AdminGetLlmsInfoResponse,
    AdminGetS3ConfigResponse,
    AdminGetOcrStatusResponse,
    AdminGetLicenseInfoResponse,
    AdminGetFilestoresInfoResponse,
    AdminGetLlamaextractFeaturesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdmin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_filestores_info(self, client: LlamaCloudAdmin) -> None:
        admin = client.admin.get_filestores_info()
        assert_matches_type(AdminGetFilestoresInfoResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_filestores_info(self, client: LlamaCloudAdmin) -> None:
        response = client.admin.with_raw_response.get_filestores_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminGetFilestoresInfoResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_filestores_info(self, client: LlamaCloudAdmin) -> None:
        with client.admin.with_streaming_response.get_filestores_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(AdminGetFilestoresInfoResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_license_info(self, client: LlamaCloudAdmin) -> None:
        admin = client.admin.get_license_info()
        assert_matches_type(AdminGetLicenseInfoResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_license_info_with_all_params(self, client: LlamaCloudAdmin) -> None:
        admin = client.admin.get_license_info(
            include_scopes=True,
        )
        assert_matches_type(AdminGetLicenseInfoResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_license_info(self, client: LlamaCloudAdmin) -> None:
        response = client.admin.with_raw_response.get_license_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminGetLicenseInfoResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_license_info(self, client: LlamaCloudAdmin) -> None:
        with client.admin.with_streaming_response.get_license_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(AdminGetLicenseInfoResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_llamaextract_features(self, client: LlamaCloudAdmin) -> None:
        admin = client.admin.get_llamaextract_features()
        assert_matches_type(AdminGetLlamaextractFeaturesResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_llamaextract_features(self, client: LlamaCloudAdmin) -> None:
        response = client.admin.with_raw_response.get_llamaextract_features()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminGetLlamaextractFeaturesResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_llamaextract_features(self, client: LlamaCloudAdmin) -> None:
        with client.admin.with_streaming_response.get_llamaextract_features() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(AdminGetLlamaextractFeaturesResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_llms_info(self, client: LlamaCloudAdmin) -> None:
        admin = client.admin.get_llms_info()
        assert_matches_type(AdminGetLlmsInfoResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_llms_info(self, client: LlamaCloudAdmin) -> None:
        response = client.admin.with_raw_response.get_llms_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminGetLlmsInfoResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_llms_info(self, client: LlamaCloudAdmin) -> None:
        with client.admin.with_streaming_response.get_llms_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(AdminGetLlmsInfoResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_ocr_status(self, client: LlamaCloudAdmin) -> None:
        admin = client.admin.get_ocr_status()
        assert_matches_type(AdminGetOcrStatusResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_ocr_status(self, client: LlamaCloudAdmin) -> None:
        response = client.admin.with_raw_response.get_ocr_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminGetOcrStatusResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_ocr_status(self, client: LlamaCloudAdmin) -> None:
        with client.admin.with_streaming_response.get_ocr_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(AdminGetOcrStatusResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_s3_config(self, client: LlamaCloudAdmin) -> None:
        admin = client.admin.get_s3_config()
        assert_matches_type(AdminGetS3ConfigResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_s3_config(self, client: LlamaCloudAdmin) -> None:
        response = client.admin.with_raw_response.get_s3_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminGetS3ConfigResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_s3_config(self, client: LlamaCloudAdmin) -> None:
        with client.admin.with_streaming_response.get_s3_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(AdminGetS3ConfigResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdmin:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_filestores_info(self, async_client: AsyncLlamaCloudAdmin) -> None:
        admin = await async_client.admin.get_filestores_info()
        assert_matches_type(AdminGetFilestoresInfoResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_filestores_info(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.admin.with_raw_response.get_filestores_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(AdminGetFilestoresInfoResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_filestores_info(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.admin.with_streaming_response.get_filestores_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(AdminGetFilestoresInfoResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_license_info(self, async_client: AsyncLlamaCloudAdmin) -> None:
        admin = await async_client.admin.get_license_info()
        assert_matches_type(AdminGetLicenseInfoResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_license_info_with_all_params(self, async_client: AsyncLlamaCloudAdmin) -> None:
        admin = await async_client.admin.get_license_info(
            include_scopes=True,
        )
        assert_matches_type(AdminGetLicenseInfoResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_license_info(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.admin.with_raw_response.get_license_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(AdminGetLicenseInfoResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_license_info(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.admin.with_streaming_response.get_license_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(AdminGetLicenseInfoResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_llamaextract_features(self, async_client: AsyncLlamaCloudAdmin) -> None:
        admin = await async_client.admin.get_llamaextract_features()
        assert_matches_type(AdminGetLlamaextractFeaturesResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_llamaextract_features(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.admin.with_raw_response.get_llamaextract_features()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(AdminGetLlamaextractFeaturesResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_llamaextract_features(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.admin.with_streaming_response.get_llamaextract_features() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(AdminGetLlamaextractFeaturesResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_llms_info(self, async_client: AsyncLlamaCloudAdmin) -> None:
        admin = await async_client.admin.get_llms_info()
        assert_matches_type(AdminGetLlmsInfoResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_llms_info(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.admin.with_raw_response.get_llms_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(AdminGetLlmsInfoResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_llms_info(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.admin.with_streaming_response.get_llms_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(AdminGetLlmsInfoResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_ocr_status(self, async_client: AsyncLlamaCloudAdmin) -> None:
        admin = await async_client.admin.get_ocr_status()
        assert_matches_type(AdminGetOcrStatusResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_ocr_status(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.admin.with_raw_response.get_ocr_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(AdminGetOcrStatusResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_ocr_status(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.admin.with_streaming_response.get_ocr_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(AdminGetOcrStatusResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_s3_config(self, async_client: AsyncLlamaCloudAdmin) -> None:
        admin = await async_client.admin.get_s3_config()
        assert_matches_type(AdminGetS3ConfigResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_s3_config(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.admin.with_raw_response.get_s3_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(AdminGetS3ConfigResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_s3_config(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.admin.with_streaming_response.get_s3_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(AdminGetS3ConfigResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True
