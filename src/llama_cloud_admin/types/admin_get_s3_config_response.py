# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AdminGetS3ConfigResponse", "Buckets"]


class Buckets(BaseModel):
    document_bucket: str

    etl_bucket: str

    external_components_bucket: str

    file_parsing_bucket: str

    file_screenshot_bucket: str

    llama_cloud_parse_output_bucket: str

    llama_extract_output_bucket: str

    raw_file_bucket: str


class AdminGetS3ConfigResponse(BaseModel):
    buckets: Buckets

    byoc_mode_enabled: bool
    """Whether BYOC mode is enabled"""

    endpoint_url: Optional[str] = None
    """Custom S3 endpoint URL (None = standard AWS)"""

    kms_key_configured: bool
    """Whether a KMS key ID is configured for server-side encryption"""

    presigned_url_signature_version: Literal["default", "s3v4", "unsigned"]
    """Signature version used when generating presigned URLs.

    'unsigned' = s3proxy path (proxy handles auth), 's3v4' = explicit SigV4,
    'default' = no override set (botocore default, may produce SigV2 without a
    region)
    """

    s3_proxy_active: bool
    """Resolved value: whether requests are routed through s3proxy"""

    s3_proxy_enabled_override: Optional[bool] = None
    """Explicit S3_PROXY_ENABLED override; None means auto-detect"""
