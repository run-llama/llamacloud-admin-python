# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from .._types import SequenceNotStr

from typing import Optional

__all__ = ["APIKeyListParams"]

class APIKeyListParams(TypedDict, total=False):
    expand: SequenceNotStr[str]

    key_type: Optional[Literal["agent", "user"]]

    name: Optional[str]

    page_size: Optional[int]

    page_token: Optional[str]

    project_id: Optional[str]