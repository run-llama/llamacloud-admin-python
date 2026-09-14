# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TypeVar, Generic, List, Optional

from typing_extensions import override

import re
from typing_extensions import TypedDict, Literal, Annotated, Protocol, runtime_checkable

from httpx import URL, Response

from ._models import BaseModel
from ._utils import PropertyInfo, is_mapping
from ._base_client import BasePage, BaseSyncPage, BaseAsyncPage, PageInfo

__all__ = ["SyncPaginatedCursor", "AsyncPaginatedCursor", "SyncPaginatedPageNumber", "AsyncPaginatedPageNumber"]

_T = TypeVar('_T')

class SyncPaginatedCursor(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    next_page_token: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_page_token = self.next_page_token
        if not next_page_token:
          return None

        return PageInfo(params={"page_token": next_page_token})

class AsyncPaginatedCursor(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    next_page_token: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_page_token = self.next_page_token
        if not next_page_token:
          return None

        return PageInfo(params={"page_token": next_page_token})

class SyncPaginatedPageNumber(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    pages: Optional[int] = None
    page: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page
        if current_page is None:
            current_page = 1

        total_pages = self.pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={
            "page": current_page + 1
        })

class AsyncPaginatedPageNumber(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    pages: Optional[int] = None
    page: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page
        if current_page is None:
            current_page = 1

        total_pages = self.pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={
            "page": current_page + 1
        })