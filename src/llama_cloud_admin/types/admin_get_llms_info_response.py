# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AdminGetLlmsInfoResponse", "LlmInfoLlmInfoItem"]


class LlmInfoLlmInfoItem(BaseModel):
    internal_model_name: Optional[str] = None

    valid: bool

    error_message: Optional[str] = None

    last_validated: Optional[datetime] = None


class AdminGetLlmsInfoResponse(BaseModel):
    llm_info: Dict[str, Dict[str, LlmInfoLlmInfoItem]]
