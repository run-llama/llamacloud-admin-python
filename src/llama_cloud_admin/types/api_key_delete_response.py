# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["APIKeyDeleteResponse"]


class APIKeyDeleteResponse(BaseModel):
    """Confirmation that a resource was deleted."""

    cache_ttl_seconds: int
    """Maximum seconds until cached information expires"""

    success: bool
    """Whether the resource was deleted"""
