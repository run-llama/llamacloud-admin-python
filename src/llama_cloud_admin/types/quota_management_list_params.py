# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["QuotaManagementListParams"]


class QuotaManagementListParams(TypedDict, total=False):
    source_id: Required[str]

    source_type: Required[Literal["GLOBAL", "organization", "plan_tier", "project"]]

    configuration_type: Optional[
        Literal[
            "allow_pay_as_you_go",
            "limit_agent_coder_daily_usage_usd",
            "limit_agent_deployments",
            "limit_batch_files",
            "limit_classify_input_tokens",
            "limit_daily_usage_credits",
            "limit_directories",
            "limit_directory_files_per_directory",
            "limit_directory_ingest_download_size_bytes",
            "limit_directory_ingest_files",
            "limit_directory_sync_plan_actions",
            "limit_embedding_character",
            "limit_files_per_index",
            "limit_max_monthly_invoice_total_usd_cents",
            "limit_monthly_usage_credits",
            "limit_projects",
            "limit_split_categories",
            "limit_total_file_count",
            "limit_total_file_storage_bytes",
            "limit_users",
            "rate_limit_batch_api_creation",
            "rate_limit_chat_api_message",
            "rate_limit_classify_api_creation",
            "rate_limit_classify_api_list",
            "rate_limit_classify_api_query",
            "rate_limit_concurrent_jobs_in_execution_default",
            "rate_limit_concurrent_jobs_in_execution_doc_ingest",
            "rate_limit_concurrent_jobs_in_execution_metadata_update",
            "rate_limit_default_api_read",
            "rate_limit_default_api_write",
            "rate_limit_directory_file_api_read",
            "rate_limit_directory_file_api_write",
            "rate_limit_directory_ingest_project_job_creation",
            "rate_limit_extract_agent_creation",
            "rate_limit_extract_api_creation",
            "rate_limit_extract_api_list",
            "rate_limit_extract_api_query",
            "rate_limit_extract_concurrent_default",
            "rate_limit_file_api_read",
            "rate_limit_file_api_write",
            "rate_limit_index_v1_pipeline_concurrent_jobs",
            "rate_limit_parse_api_creation",
            "rate_limit_parse_api_list",
            "rate_limit_parse_api_query",
            "rate_limit_parse_concurrent_default",
            "rate_limit_parse_concurrent_pages_agentic",
            "rate_limit_parse_concurrent_pages_agentic_plus",
            "rate_limit_parse_concurrent_pages_cost_effective",
            "rate_limit_parse_concurrent_premium",
            "rate_limit_parse_token_bucket_agentic",
            "rate_limit_parse_token_bucket_agentic_plus",
            "rate_limit_parse_token_bucket_cost_effective",
            "rate_limit_parse_token_bucket_unknown_tier",
            "rate_limit_project_concurrent_jobs",
            "rate_limit_project_concurrent_turbo_jobs",
            "rate_limit_split_api_creation",
            "rate_limit_split_api_query",
            "rate_limit_spreadsheet_api_list",
            "rate_limit_spreadsheet_api_query",
            "rate_limit_spreadsheet_creation",
            "rate_limit_usage_api_query",
            "rate_limit_verify_api_creation",
            "rate_limit_verify_api_list",
            "rate_limit_verify_api_query",
        ]
    ]

    exclude_self_service: bool

    expand: bool

    page: int

    page_size: int
