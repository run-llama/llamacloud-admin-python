# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_cloud_admin import LlamaCloudAdmin, AsyncLlamaCloudAdmin
from llama_cloud_admin.types.admin import UsageMetricAggregateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsageMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_aggregate(self, client: LlamaCloudAdmin) -> None:
        usage_metric = client.admin.usage_metrics.aggregate(
            day_on_or_after="day_on_or_after",
            day_on_or_before="day_on_or_before",
            group_by=["string"],
        )
        assert_matches_type(UsageMetricAggregateResponse, usage_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_aggregate_with_all_params(self, client: LlamaCloudAdmin) -> None:
        usage_metric = client.admin.usage_metrics.aggregate(
            day_on_or_after="day_on_or_after",
            day_on_or_before="day_on_or_before",
            group_by=["string"],
            event_types=["audio_seconds_parsed", "chart_parsing_agentic"],
            organization_id="organization_id",
            project_id="project_id",
            user_id="user_id",
        )
        assert_matches_type(UsageMetricAggregateResponse, usage_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_aggregate(self, client: LlamaCloudAdmin) -> None:
        response = client.admin.usage_metrics.with_raw_response.aggregate(
            day_on_or_after="day_on_or_after",
            day_on_or_before="day_on_or_before",
            group_by=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_metric = response.parse()
        assert_matches_type(UsageMetricAggregateResponse, usage_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_aggregate(self, client: LlamaCloudAdmin) -> None:
        with client.admin.usage_metrics.with_streaming_response.aggregate(
            day_on_or_after="day_on_or_after",
            day_on_or_before="day_on_or_before",
            group_by=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_metric = response.parse()
            assert_matches_type(UsageMetricAggregateResponse, usage_metric, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsageMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_aggregate(self, async_client: AsyncLlamaCloudAdmin) -> None:
        usage_metric = await async_client.admin.usage_metrics.aggregate(
            day_on_or_after="day_on_or_after",
            day_on_or_before="day_on_or_before",
            group_by=["string"],
        )
        assert_matches_type(UsageMetricAggregateResponse, usage_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_aggregate_with_all_params(self, async_client: AsyncLlamaCloudAdmin) -> None:
        usage_metric = await async_client.admin.usage_metrics.aggregate(
            day_on_or_after="day_on_or_after",
            day_on_or_before="day_on_or_before",
            group_by=["string"],
            event_types=["audio_seconds_parsed", "chart_parsing_agentic"],
            organization_id="organization_id",
            project_id="project_id",
            user_id="user_id",
        )
        assert_matches_type(UsageMetricAggregateResponse, usage_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_aggregate(self, async_client: AsyncLlamaCloudAdmin) -> None:
        response = await async_client.admin.usage_metrics.with_raw_response.aggregate(
            day_on_or_after="day_on_or_after",
            day_on_or_before="day_on_or_before",
            group_by=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_metric = await response.parse()
        assert_matches_type(UsageMetricAggregateResponse, usage_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_aggregate(self, async_client: AsyncLlamaCloudAdmin) -> None:
        async with async_client.admin.usage_metrics.with_streaming_response.aggregate(
            day_on_or_after="day_on_or_after",
            day_on_or_before="day_on_or_before",
            group_by=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_metric = await response.parse()
            assert_matches_type(UsageMetricAggregateResponse, usage_metric, path=["response"])

        assert cast(Any, response.is_closed) is True
