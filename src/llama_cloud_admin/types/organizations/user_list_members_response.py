# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..organization_member import OrganizationMember

__all__ = ["UserListMembersResponse"]

UserListMembersResponse: TypeAlias = List[OrganizationMember]
