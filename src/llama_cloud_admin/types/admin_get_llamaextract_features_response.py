# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AdminGetLlamaextractFeaturesResponse", "AvailableMode", "SchemaGeneration"]


class AvailableMode(BaseModel):
    mode: str

    parse_mode: str

    status: Literal["available", "unavailable"]

    available_extract_models: Optional[List[str]] = None

    available_parse_models: Optional[List[str]] = None

    missing_extract_models: Optional[List[str]] = None

    missing_parse_models: Optional[List[str]] = None


class SchemaGeneration(BaseModel):
    model: str

    status: Literal["available", "unavailable"]


class AdminGetLlamaextractFeaturesResponse(BaseModel):
    available_modes: List[AvailableMode]

    schema_generation: SchemaGeneration
