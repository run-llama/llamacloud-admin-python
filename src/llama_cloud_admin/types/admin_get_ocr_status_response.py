# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AdminGetOcrStatusResponse"]


class AdminGetOcrStatusResponse(BaseModel):
    """Response model for OCR service health/GPU status."""

    status: Literal["degraded", "ok", "unavailable"]

    device: Optional[str] = None

    error_message: Optional[str] = None

    gpu_available: Optional[bool] = None

    gpu_device_count: Optional[int] = None

    gpu_device_name: Optional[str] = None
