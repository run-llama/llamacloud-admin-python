# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, Dict

from typing_extensions import Literal

from datetime import datetime

__all__ = ["QuotaConfiguration", "ConfigurationValue"]

class ConfigurationValue(BaseModel):
    """The quota configuration value"""
    numerator: int
    """The rate numerator"""

    denominator: Optional[int] = None
    """The rate limit denominator"""

    denominator_units: Optional[Literal["day", "hour", "minute", "second"]] = None
    """The default rate limit denominator units"""

class QuotaConfiguration(BaseModel):
    """Full quota configuration model."""
    configuration_metadata: Optional[Dict[str, object]] = None
    """The configuration metadata"""

    configuration_type: Literal["allow_pay_as_you_go", "limit_agent_coder_daily_usage_usd", "limit_agent_deployments", "limit_batch_files", "limit_classify_input_tokens", "limit_daily_usage_credits", "limit_directories", "limit_directory_files_per_directory", "limit_directory_ingest_download_size_bytes", "limit_directory_ingest_files", "limit_directory_sync_plan_actions", "limit_embedding_character", "limit_files_per_index", "limit_max_monthly_invoice_total_usd_cents", "limit_monthly_usage_credits", "limit_projects", "limit_split_categories", "limit_total_file_count", "limit_total_file_storage_bytes", "limit_users", "rate_limit_batch_api_creation", "rate_limit_chat_api_message", "rate_limit_classify_api_creation", "rate_limit_classify_api_list", "rate_limit_classify_api_query", "rate_limit_concurrent_jobs_in_execution_default", "rate_limit_concurrent_jobs_in_execution_doc_ingest", "rate_limit_concurrent_jobs_in_execution_metadata_update", "rate_limit_default_api_read", "rate_limit_default_api_write", "rate_limit_directory_file_api_read", "rate_limit_directory_file_api_write", "rate_limit_directory_ingest_project_job_creation", "rate_limit_extract_agent_creation", "rate_limit_extract_api_creation", "rate_limit_extract_api_list", "rate_limit_extract_api_query", "rate_limit_extract_concurrent_default", "rate_limit_file_api_read", "rate_limit_file_api_write", "rate_limit_index_v1_pipeline_concurrent_jobs", "rate_limit_parse_api_creation", "rate_limit_parse_api_list", "rate_limit_parse_api_query", "rate_limit_parse_concurrent_default", "rate_limit_parse_concurrent_pages_agentic", "rate_limit_parse_concurrent_pages_agentic_plus", "rate_limit_parse_concurrent_pages_cost_effective", "rate_limit_parse_concurrent_premium", "rate_limit_parse_token_bucket_agentic", "rate_limit_parse_token_bucket_agentic_plus", "rate_limit_parse_token_bucket_cost_effective", "rate_limit_parse_token_bucket_unknown_tier", "rate_limit_project_concurrent_jobs", "rate_limit_project_concurrent_turbo_jobs", "rate_limit_split_api_creation", "rate_limit_split_api_query", "rate_limit_spreadsheet_api_list", "rate_limit_spreadsheet_api_query", "rate_limit_spreadsheet_creation", "rate_limit_usage_api_query", "rate_limit_verify_api_creation", "rate_limit_verify_api_list", "rate_limit_verify_api_query"]
    """The quota configuration type"""

    configuration_value: ConfigurationValue
    """The quota configuration value"""

    source_id: str
    """The source ID, e.g. the organization ID"""

    source_type: Literal["GLOBAL", "organization", "plan_tier", "project"]
    """The source type, e.g. 'organization'"""

    status: Literal["ACTIVE", "INACTIVE"]
    """The status of the quota, i.e. 'ACTIVE' or 'INACTIVE'"""

    id: Optional[str] = None
    """The system-generated UUID for the quota"""

    created_at: Optional[datetime] = None
    """The creation date of the quota configuration in the database"""

    ended_at: Optional[datetime] = None
    """The end date of the quota"""

    idempotency_key: Optional[str] = None
    """The idempotency key"""

    started_at: Optional[datetime] = None
    """The start date of the quota"""

    updated_at: Optional[datetime] = None
    """The last updated date of the quota configuration in the database"""