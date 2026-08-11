# Organizations

Types:

```python
from llama_cloud_admin.types import (
    Organization,
    OrganizationMember,
    Role,
    UsageAndPlan,
    UserOrganizationRole,
)
```

Methods:

- <code title="post /api/v2/organizations">client.organizations.<a href="./src/llama_cloud_admin/resources/organizations/organizations.py">create</a>(\*\*<a href="src/llama_cloud_admin/types/organization_create_params.py">params</a>) -> <a href="./src/llama_cloud_admin/types/organization.py">Organization</a></code>
- <code title="put /api/v2/organizations/{organization_id}">client.organizations.<a href="./src/llama_cloud_admin/resources/organizations/organizations.py">update</a>(organization_id, \*\*<a href="src/llama_cloud_admin/types/organization_update_params.py">params</a>) -> <a href="./src/llama_cloud_admin/types/organization.py">Organization</a></code>
- <code title="get /api/v2/organizations">client.organizations.<a href="./src/llama_cloud_admin/resources/organizations/organizations.py">list</a>(\*\*<a href="src/llama_cloud_admin/types/organization_list_params.py">params</a>) -> <a href="./src/llama_cloud_admin/types/organization.py">SyncPaginatedCursor[Organization]</a></code>
- <code title="delete /api/v2/organizations/{organization_id}">client.organizations.<a href="./src/llama_cloud_admin/resources/organizations/organizations.py">delete</a>(organization_id) -> None</code>
- <code title="get /api/v2/organizations/{organization_id}">client.organizations.<a href="./src/llama_cloud_admin/resources/organizations/organizations.py">get</a>(organization_id) -> <a href="./src/llama_cloud_admin/types/organization.py">Organization</a></code>
- <code title="get /api/v1/organizations/{organization_id}/usage">client.organizations.<a href="./src/llama_cloud_admin/resources/organizations/organizations.py">get_usage</a>(organization_id, \*\*<a href="src/llama_cloud_admin/types/organization_get_usage_params.py">params</a>) -> <a href="./src/llama_cloud_admin/types/usage_and_plan.py">UsageAndPlan</a></code>

## Users

Types:

```python
from llama_cloud_admin.types.organizations import (
    UserAddResponse,
    UserListMembersResponse,
    UserListProjectsResponse,
)
```

Methods:

- <code title="delete /api/v1/organizations/{organization_id}/users/{member_user_id}">client.organizations.users.<a href="./src/llama_cloud_admin/resources/organizations/users.py">delete</a>(member_user_id, \*, organization_id, \*\*<a href="src/llama_cloud_admin/types/organizations/user_delete_params.py">params</a>) -> None</code>
- <code title="put /api/v1/organizations/{organization_id}/users">client.organizations.users.<a href="./src/llama_cloud_admin/resources/organizations/users.py">add</a>(organization_id, \*\*<a href="src/llama_cloud_admin/types/organizations/user_add_params.py">params</a>) -> <a href="./src/llama_cloud_admin/types/organizations/user_add_response.py">UserAddResponse</a></code>
- <code title="put /api/v1/organizations/{organization_id}/users/{user_id}/projects">client.organizations.users.<a href="./src/llama_cloud_admin/resources/organizations/users.py">add_to_project</a>(user_id, \*, organization_id, \*\*<a href="src/llama_cloud_admin/types/organizations/user_add_to_project_params.py">params</a>) -> object</code>
- <code title="put /api/v1/organizations/{organization_id}/users/roles">client.organizations.users.<a href="./src/llama_cloud_admin/resources/organizations/users.py">assign_role</a>(path_organization_id, \*\*<a href="src/llama_cloud_admin/types/organizations/user_assign_role_params.py">params</a>) -> <a href="./src/llama_cloud_admin/types/user_organization_role.py">UserOrganizationRole</a></code>
- <code title="get /api/v1/organizations/{organization_id}/users">client.organizations.users.<a href="./src/llama_cloud_admin/resources/organizations/users.py">list_members</a>(organization_id) -> <a href="./src/llama_cloud_admin/types/organizations/user_list_members_response.py">UserListMembersResponse</a></code>
- <code title="get /api/v1/organizations/{organization_id}/users/{user_id}/projects">client.organizations.users.<a href="./src/llama_cloud_admin/resources/organizations/users.py">list_projects</a>(user_id, \*, organization_id) -> <a href="./src/llama_cloud_admin/types/organizations/user_list_projects_response.py">UserListProjectsResponse</a></code>
- <code title="delete /api/v1/organizations/{organization_id}/users/{user_id}/projects/{project_id}">client.organizations.users.<a href="./src/llama_cloud_admin/resources/organizations/users.py">remove_from_project</a>(project_id, \*, organization_id, user_id) -> object</code>

## Roles

Types:

```python
from llama_cloud_admin.types.organizations import RoleListResponse
```

Methods:

- <code title="get /api/v1/organizations/{organization_id}/roles">client.organizations.roles.<a href="./src/llama_cloud_admin/resources/organizations/roles.py">list</a>(organization_id) -> <a href="./src/llama_cloud_admin/types/organizations/role_list_response.py">RoleListResponse</a></code>

# Projects

Types:

```python
from llama_cloud_admin.types import Project
```

Methods:

- <code title="post /api/v2/projects">client.projects.<a href="./src/llama_cloud_admin/resources/projects.py">create</a>(\*\*<a href="src/llama_cloud_admin/types/project_create_params.py">params</a>) -> <a href="./src/llama_cloud_admin/types/project.py">Project</a></code>
- <code title="put /api/v2/projects/{project_id}">client.projects.<a href="./src/llama_cloud_admin/resources/projects.py">update</a>(project_id, \*\*<a href="src/llama_cloud_admin/types/project_update_params.py">params</a>) -> <a href="./src/llama_cloud_admin/types/project.py">Project</a></code>
- <code title="get /api/v2/projects">client.projects.<a href="./src/llama_cloud_admin/resources/projects.py">list</a>(\*\*<a href="src/llama_cloud_admin/types/project_list_params.py">params</a>) -> <a href="./src/llama_cloud_admin/types/project.py">SyncPaginatedCursor[Project]</a></code>
- <code title="delete /api/v2/projects/{project_id}">client.projects.<a href="./src/llama_cloud_admin/resources/projects.py">delete</a>(project_id, \*\*<a href="src/llama_cloud_admin/types/project_delete_params.py">params</a>) -> None</code>
- <code title="get /api/v2/projects/{project_id}">client.projects.<a href="./src/llama_cloud_admin/resources/projects.py">get</a>(project_id, \*\*<a href="src/llama_cloud_admin/types/project_get_params.py">params</a>) -> <a href="./src/llama_cloud_admin/types/project.py">Project</a></code>

# Invites

Types:

```python
from llama_cloud_admin.types import Invite, InviteAcceptResponse
```

Methods:

- <code title="post /api/v2/invites/{invite_id}/accept">client.invites.<a href="./src/llama_cloud_admin/resources/invites.py">accept</a>(invite_id) -> <a href="./src/llama_cloud_admin/types/invite_accept_response.py">InviteAcceptResponse</a></code>
- <code title="delete /api/v2/invites/{invite_id}">client.invites.<a href="./src/llama_cloud_admin/resources/invites.py">decline</a>(invite_id) -> None</code>
- <code title="get /api/v2/invites">client.invites.<a href="./src/llama_cloud_admin/resources/invites.py">list_mine</a>(\*\*<a href="src/llama_cloud_admin/types/invite_list_mine_params.py">params</a>) -> <a href="./src/llama_cloud_admin/types/invite.py">SyncPaginatedCursor[Invite]</a></code>

# Admin

Types:

```python
from llama_cloud_admin.types import (
    AdminGetFilestoresInfoResponse,
    AdminGetLicenseInfoResponse,
    AdminGetLlamaextractFeaturesResponse,
    AdminGetLlmsInfoResponse,
    AdminGetOcrStatusResponse,
)
```

Methods:

- <code title="get /api/v1/admin/filestores/info">client.admin.<a href="./src/llama_cloud_admin/resources/admin/admin.py">get_filestores_info</a>() -> <a href="./src/llama_cloud_admin/types/admin_get_filestores_info_response.py">AdminGetFilestoresInfoResponse</a></code>
- <code title="get /api/v1/admin/license/info">client.admin.<a href="./src/llama_cloud_admin/resources/admin/admin.py">get_license_info</a>(\*\*<a href="src/llama_cloud_admin/types/admin_get_license_info_params.py">params</a>) -> <a href="./src/llama_cloud_admin/types/admin_get_license_info_response.py">AdminGetLicenseInfoResponse</a></code>
- <code title="get /api/v1/admin/llamaextract/features">client.admin.<a href="./src/llama_cloud_admin/resources/admin/admin.py">get_llamaextract_features</a>() -> <a href="./src/llama_cloud_admin/types/admin_get_llamaextract_features_response.py">AdminGetLlamaextractFeaturesResponse</a></code>
- <code title="get /api/v1/admin/llms/info">client.admin.<a href="./src/llama_cloud_admin/resources/admin/admin.py">get_llms_info</a>() -> <a href="./src/llama_cloud_admin/types/admin_get_llms_info_response.py">AdminGetLlmsInfoResponse</a></code>
- <code title="get /api/v1/admin/ocr/statusz">client.admin.<a href="./src/llama_cloud_admin/resources/admin/admin.py">get_ocr_status</a>() -> <a href="./src/llama_cloud_admin/types/admin_get_ocr_status_response.py">AdminGetOcrStatusResponse</a></code>

## Users

Types:

```python
from llama_cloud_admin.types.admin import CustomClaims, UserClaims
```

Methods:

- <code title="get /api/v1/admin/users/{user_id}/claims">client.admin.users.<a href="./src/llama_cloud_admin/resources/admin/users.py">get_claims</a>(user_id) -> <a href="./src/llama_cloud_admin/types/admin/user_claims.py">UserClaims</a></code>
- <code title="patch /api/v1/admin/users/{user_id}/claims">client.admin.users.<a href="./src/llama_cloud_admin/resources/admin/users.py">update_claims</a>(user_id, \*\*<a href="src/llama_cloud_admin/types/admin/user_update_claims_params.py">params</a>) -> <a href="./src/llama_cloud_admin/types/admin/user_claims.py">UserClaims</a></code>

## UsageMetrics

Types:

```python
from llama_cloud_admin.types.admin import UsageMetricAggregateResponse
```

Methods:

- <code title="get /api/v1/admin/usage-metrics/aggregate">client.admin.usage_metrics.<a href="./src/llama_cloud_admin/resources/admin/usage_metrics.py">aggregate</a>(\*\*<a href="src/llama_cloud_admin/types/admin/usage_metric_aggregate_params.py">params</a>) -> <a href="./src/llama_cloud_admin/types/admin/usage_metric_aggregate_response.py">UsageMetricAggregateResponse</a></code>
