# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncPaginatedCursor", "AsyncPaginatedCursor"]

_T = TypeVar("_T")


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
