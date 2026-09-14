# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, Dict

from datetime import datetime

__all__ = ["AdminGetLlmsInfoResponse", "LlmInfoLlmInfoItem"]

class LlmInfoLlmInfoItem(BaseModel):
    internal_model_name: Optional[str] = None

    valid: bool

    error_message: Optional[str] = None

    last_validated: Optional[datetime] = None

class AdminGetLlmsInfoResponse(BaseModel):
    llm_info: Dict[str, Dict[str, LlmInfoLlmInfoItem]]