# yk_auth_client.AuthorizationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_authorization_add_default_business_groups_post**](AuthorizationApi.md#api_authorization_add_default_business_groups_post) | **POST** /api/Authorization/AddDefaultBusinessGroups | 
[**api_authorization_add_development_user_post**](AuthorizationApi.md#api_authorization_add_development_user_post) | **POST** /api/Authorization/AddDevelopmentUser | 
[**api_authorization_add_development_users_post**](AuthorizationApi.md#api_authorization_add_development_users_post) | **POST** /api/Authorization/AddDevelopmentUsers | 
[**api_authorization_add_group_permissions_post**](AuthorizationApi.md#api_authorization_add_group_permissions_post) | **POST** /api/Authorization/AddGroupPermissions | 
[**api_authorization_add_group_post**](AuthorizationApi.md#api_authorization_add_group_post) | **POST** /api/Authorization/AddGroup | 
[**api_authorization_add_user_units_post**](AuthorizationApi.md#api_authorization_add_user_units_post) | **POST** /api/Authorization/AddUserUnits | 
[**api_authorization_check_user_access_get**](AuthorizationApi.md#api_authorization_check_user_access_get) | **GET** /api/Authorization/CheckUserAccess | 
[**api_authorization_delete_all_for_user_delete**](AuthorizationApi.md#api_authorization_delete_all_for_user_delete) | **DELETE** /api/Authorization/DeleteAllForUser | 
[**api_authorization_delete_development_user_delete**](AuthorizationApi.md#api_authorization_delete_development_user_delete) | **DELETE** /api/Authorization/DeleteDevelopmentUser | 
[**api_authorization_delete_group_delete**](AuthorizationApi.md#api_authorization_delete_group_delete) | **DELETE** /api/Authorization/DeleteGroup | 
[**api_authorization_delete_group_permissions_delete**](AuthorizationApi.md#api_authorization_delete_group_permissions_delete) | **DELETE** /api/Authorization/DeleteGroupPermissions | 
[**api_authorization_delete_user_units_delete**](AuthorizationApi.md#api_authorization_delete_user_units_delete) | **DELETE** /api/Authorization/DeleteUserUnits | 
[**api_authorization_get_permission_groups_get**](AuthorizationApi.md#api_authorization_get_permission_groups_get) | **GET** /api/Authorization/GetPermissionGroups | 
[**api_authorization_get_permissions_get**](AuthorizationApi.md#api_authorization_get_permissions_get) | **GET** /api/Authorization/GetPermissions | 
[**api_authorization_get_user_access_get**](AuthorizationApi.md#api_authorization_get_user_access_get) | **GET** /api/Authorization/GetUserAccess | 
[**api_authorization_list_all_for_development_get**](AuthorizationApi.md#api_authorization_list_all_for_development_get) | **GET** /api/Authorization/ListAllForDevelopment | 
[**api_authorization_list_all_for_user_get**](AuthorizationApi.md#api_authorization_list_all_for_user_get) | **GET** /api/Authorization/ListAllForUser | 
[**api_authorization_list_all_for_users_get**](AuthorizationApi.md#api_authorization_list_all_for_users_get) | **GET** /api/Authorization/ListAllForUsers | 
[**api_authorization_list_units_get**](AuthorizationApi.md#api_authorization_list_units_get) | **GET** /api/Authorization/ListUnits | 
[**api_authorization_set_development_user_group_put**](AuthorizationApi.md#api_authorization_set_development_user_group_put) | **PUT** /api/Authorization/SetDevelopmentUserGroup | 
[**api_authorization_set_group_permissions_put**](AuthorizationApi.md#api_authorization_set_group_permissions_put) | **PUT** /api/Authorization/SetGroupPermissions | 
[**api_authorization_set_user_units_put**](AuthorizationApi.md#api_authorization_set_user_units_put) | **PUT** /api/Authorization/SetUserUnits | 


# **api_authorization_add_default_business_groups_post**
> [BusinessPermissionGroup] api_authorization_add_default_business_groups_post()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.business_permission_group import BusinessPermissionGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_add_default_business_groups_post(body=body)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_add_default_business_groups_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

### Return type

[**[BusinessPermissionGroup]**](BusinessPermissionGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_add_development_user_post**
> BusinessPermissionGroupDevelopmentUser api_authorization_add_development_user_post()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.business_permission_group_development_user import BusinessPermissionGroupDevelopmentUser
from yk_auth_client.model.add_development_user_request import AddDevelopmentUserRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    add_development_user_request = AddDevelopmentUserRequest(
        user_id="user_id_example",
        development_id="development_id_example",
        business_permission_group_id="business_permission_group_id_example",
        all_units=True,
        unit_ids=[
            "unit_ids_example",
        ],
    ) # AddDevelopmentUserRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_add_development_user_post(add_development_user_request=add_development_user_request)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_add_development_user_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_development_user_request** | [**AddDevelopmentUserRequest**](AddDevelopmentUserRequest.md)|  | [optional]

### Return type

[**BusinessPermissionGroupDevelopmentUser**](BusinessPermissionGroupDevelopmentUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_add_development_users_post**
> [BusinessPermissionGroupDevelopmentUser] api_authorization_add_development_users_post()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.business_permission_group_development_user import BusinessPermissionGroupDevelopmentUser
from yk_auth_client.model.add_multiple_development_users_request import AddMultipleDevelopmentUsersRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    add_multiple_development_users_request = AddMultipleDevelopmentUsersRequest(
        requests=[
            AddDevelopmentUserRequest(
                user_id="user_id_example",
                development_id="development_id_example",
                business_permission_group_id="business_permission_group_id_example",
                all_units=True,
                unit_ids=[
                    "unit_ids_example",
                ],
            ),
        ],
    ) # AddMultipleDevelopmentUsersRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_add_development_users_post(add_multiple_development_users_request=add_multiple_development_users_request)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_add_development_users_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_multiple_development_users_request** | [**AddMultipleDevelopmentUsersRequest**](AddMultipleDevelopmentUsersRequest.md)|  | [optional]

### Return type

[**[BusinessPermissionGroupDevelopmentUser]**](BusinessPermissionGroupDevelopmentUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_add_group_permissions_post**
> [BusinessPermissionGroupPermission] api_authorization_add_group_permissions_post()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.business_permission_group_permission import BusinessPermissionGroupPermission
from yk_auth_client.model.add_group_permissions_request import AddGroupPermissionsRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    add_group_permissions_request = AddGroupPermissionsRequest(
        business_permission_group_id="business_permission_group_id_example",
        permission_ids=[
            "permission_ids_example",
        ],
    ) # AddGroupPermissionsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_add_group_permissions_post(add_group_permissions_request=add_group_permissions_request)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_add_group_permissions_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_group_permissions_request** | [**AddGroupPermissionsRequest**](AddGroupPermissionsRequest.md)|  | [optional]

### Return type

[**[BusinessPermissionGroupPermission]**](BusinessPermissionGroupPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_add_group_post**
> BusinessPermissionGroup api_authorization_add_group_post()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.business_permission_group import BusinessPermissionGroup
from yk_auth_client.model.add_group_request import AddGroupRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    add_group_request = AddGroupRequest(
        business_account_id="business_account_id_example",
        name="name_example",
        description="description_example",
        permission_ids=[
            "permission_ids_example",
        ],
    ) # AddGroupRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_add_group_post(add_group_request=add_group_request)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_add_group_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_group_request** | [**AddGroupRequest**](AddGroupRequest.md)|  | [optional]

### Return type

[**BusinessPermissionGroup**](BusinessPermissionGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_add_user_units_post**
> [UserUnit] api_authorization_add_user_units_post()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.user_unit import UserUnit
from yk_auth_client.model.add_user_units_request import AddUserUnitsRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    add_user_units_request = AddUserUnitsRequest(
        user_id="user_id_example",
        development_id="development_id_example",
        unit_ids=[
            "unit_ids_example",
        ],
    ) # AddUserUnitsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_add_user_units_post(add_user_units_request=add_user_units_request)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_add_user_units_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_units_request** | [**AddUserUnitsRequest**](AddUserUnitsRequest.md)|  | [optional]

### Return type

[**[UserUnit]**](UserUnit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_check_user_access_get**
> bool api_authorization_check_user_access_get()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.permission_name import PermissionName
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    user_id = "userId_example" # str |  (optional)
    development_id = "developmentId_example" # str |  (optional)
    permission = PermissionName(0) # PermissionName |  (optional)
    development_unit_id = "developmentUnitId_example" # str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_check_user_access_get(user_id=user_id, development_id=development_id, permission=permission, development_unit_id=development_unit_id)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_check_user_access_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional]
 **development_id** | **str**|  | [optional]
 **permission** | **PermissionName**|  | [optional]
 **development_unit_id** | **str, none_type**|  | [optional]

### Return type

**bool**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_delete_all_for_user_delete**
> bool api_authorization_delete_all_for_user_delete()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    user_id = "userId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_delete_all_for_user_delete(user_id=user_id)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_delete_all_for_user_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional]

### Return type

**bool**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_delete_development_user_delete**
> bool api_authorization_delete_development_user_delete()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.delete_development_user_request import DeleteDevelopmentUserRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    delete_development_user_request = DeleteDevelopmentUserRequest(
        user_id="user_id_example",
        development_id="development_id_example",
    ) # DeleteDevelopmentUserRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_delete_development_user_delete(delete_development_user_request=delete_development_user_request)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_delete_development_user_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_development_user_request** | [**DeleteDevelopmentUserRequest**](DeleteDevelopmentUserRequest.md)|  | [optional]

### Return type

**bool**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_delete_group_delete**
> bool api_authorization_delete_group_delete()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    business_permission_group_id = "businessPermissionGroupId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_delete_group_delete(business_permission_group_id=business_permission_group_id)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_delete_group_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_permission_group_id** | **str**|  | [optional]

### Return type

**bool**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_delete_group_permissions_delete**
> bool api_authorization_delete_group_permissions_delete()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.delete_group_permissions_request import DeleteGroupPermissionsRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    delete_group_permissions_request = DeleteGroupPermissionsRequest(
        business_permission_group_id="business_permission_group_id_example",
        permission_ids=[
            "permission_ids_example",
        ],
    ) # DeleteGroupPermissionsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_delete_group_permissions_delete(delete_group_permissions_request=delete_group_permissions_request)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_delete_group_permissions_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_group_permissions_request** | [**DeleteGroupPermissionsRequest**](DeleteGroupPermissionsRequest.md)|  | [optional]

### Return type

**bool**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_delete_user_units_delete**
> bool api_authorization_delete_user_units_delete()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.delete_user_units_request import DeleteUserUnitsRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    delete_user_units_request = DeleteUserUnitsRequest(
        user_id="user_id_example",
        development_id="development_id_example",
        unit_ids=[
            "unit_ids_example",
        ],
    ) # DeleteUserUnitsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_delete_user_units_delete(delete_user_units_request=delete_user_units_request)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_delete_user_units_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_user_units_request** | [**DeleteUserUnitsRequest**](DeleteUserUnitsRequest.md)|  | [optional]

### Return type

**bool**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_get_permission_groups_get**
> [BusinessPermissionGroup] api_authorization_get_permission_groups_get()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.business_permission_group import BusinessPermissionGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    business_account_id = "businessAccountId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_get_permission_groups_get(business_account_id=business_account_id)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_get_permission_groups_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_account_id** | **str**|  | [optional]

### Return type

[**[BusinessPermissionGroup]**](BusinessPermissionGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_get_permissions_get**
> [Permission] api_authorization_get_permissions_get()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.permission import Permission
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_authorization_get_permissions_get()
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_get_permissions_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Permission]**](Permission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_get_user_access_get**
> BusinessPermissionGroupDevelopmentUser api_authorization_get_user_access_get()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.business_permission_group_development_user import BusinessPermissionGroupDevelopmentUser
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    user_id = "userId_example" # str |  (optional)
    development_id = "developmentId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_get_user_access_get(user_id=user_id, development_id=development_id)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_get_user_access_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional]
 **development_id** | **str**|  | [optional]

### Return type

[**BusinessPermissionGroupDevelopmentUser**](BusinessPermissionGroupDevelopmentUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_list_all_for_development_get**
> [BusinessPermissionGroupDevelopmentUser] api_authorization_list_all_for_development_get()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.business_permission_group_development_user import BusinessPermissionGroupDevelopmentUser
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    development_id = "developmentId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_list_all_for_development_get(development_id=development_id)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_list_all_for_development_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **development_id** | **str**|  | [optional]

### Return type

[**[BusinessPermissionGroupDevelopmentUser]**](BusinessPermissionGroupDevelopmentUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_list_all_for_user_get**
> [BusinessPermissionGroupDevelopmentUser] api_authorization_list_all_for_user_get()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.business_permission_group_development_user import BusinessPermissionGroupDevelopmentUser
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    user_id = "userId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_list_all_for_user_get(user_id=user_id)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_list_all_for_user_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional]

### Return type

[**[BusinessPermissionGroupDevelopmentUser]**](BusinessPermissionGroupDevelopmentUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_list_all_for_users_get**
> [BusinessPermissionGroupDevelopmentUser] api_authorization_list_all_for_users_get()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.business_permission_group_development_user import BusinessPermissionGroupDevelopmentUser
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    user_ids = "userIds_example" # str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_list_all_for_users_get(user_ids=user_ids)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_list_all_for_users_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_ids** | **str, none_type**|  | [optional]

### Return type

[**[BusinessPermissionGroupDevelopmentUser]**](BusinessPermissionGroupDevelopmentUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_list_units_get**
> [UserUnit] api_authorization_list_units_get()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.user_unit import UserUnit
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    user_id = "userId_example" # str |  (optional)
    development_id = "developmentId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_list_units_get(user_id=user_id, development_id=development_id)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_list_units_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional]
 **development_id** | **str**|  | [optional]

### Return type

[**[UserUnit]**](UserUnit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_set_development_user_group_put**
> BusinessPermissionGroupDevelopmentUser api_authorization_set_development_user_group_put()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.business_permission_group_development_user import BusinessPermissionGroupDevelopmentUser
from yk_auth_client.model.set_development_user_group_request import SetDevelopmentUserGroupRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    set_development_user_group_request = SetDevelopmentUserGroupRequest(
        user_id="user_id_example",
        development_id="development_id_example",
        business_permission_group_id="business_permission_group_id_example",
        all_units=True,
        unit_ids=[
            "unit_ids_example",
        ],
    ) # SetDevelopmentUserGroupRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_set_development_user_group_put(set_development_user_group_request=set_development_user_group_request)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_set_development_user_group_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_development_user_group_request** | [**SetDevelopmentUserGroupRequest**](SetDevelopmentUserGroupRequest.md)|  | [optional]

### Return type

[**BusinessPermissionGroupDevelopmentUser**](BusinessPermissionGroupDevelopmentUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_set_group_permissions_put**
> [BusinessPermissionGroupPermission] api_authorization_set_group_permissions_put()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.business_permission_group_permission import BusinessPermissionGroupPermission
from yk_auth_client.model.set_group_permissions_request import SetGroupPermissionsRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    set_group_permissions_request = SetGroupPermissionsRequest(
        business_permission_group_id="business_permission_group_id_example",
        permission_ids=[
            "permission_ids_example",
        ],
    ) # SetGroupPermissionsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_set_group_permissions_put(set_group_permissions_request=set_group_permissions_request)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_set_group_permissions_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_group_permissions_request** | [**SetGroupPermissionsRequest**](SetGroupPermissionsRequest.md)|  | [optional]

### Return type

[**[BusinessPermissionGroupPermission]**](BusinessPermissionGroupPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_set_user_units_put**
> [UserUnit] api_authorization_set_user_units_put()



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authorization_api
from yk_auth_client.model.set_user_units_request import SetUserUnitsRequest
from yk_auth_client.model.user_unit import UserUnit
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_auth_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)
    set_user_units_request = SetUserUnitsRequest(
        user_id="user_id_example",
        development_id="development_id_example",
        all_units=True,
        unit_ids=[
            "unit_ids_example",
        ],
    ) # SetUserUnitsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_authorization_set_user_units_put(set_user_units_request=set_user_units_request)
        pprint(api_response)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthorizationApi->api_authorization_set_user_units_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_user_units_request** | [**SetUserUnitsRequest**](SetUserUnitsRequest.md)|  | [optional]

### Return type

[**[UserUnit]**](UserUnit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

