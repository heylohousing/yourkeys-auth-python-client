# yk_auth_client.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_authenticate_post**](AuthenticationApi.md#api_authenticate_post) | **POST** /api/Authenticate | Authenticate a user based on the supplied credentials.
[**api_refresh_authentication_post**](AuthenticationApi.md#api_refresh_authentication_post) | **POST** /api/RefreshAuthentication | Generate a new identity token based on the supplied refresh token.


# **api_authenticate_post**
> api_authenticate_post()

Authenticate a user based on the supplied credentials.

Sample request:        POST /api/Authenticate      {         \"username\": \"example_user\",         \"password\": \"p455w0rd!\"      }

### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authentication_api
from yk_auth_client.model.basic_auth_request import BasicAuthRequest
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
    api_instance = authentication_api.AuthenticationApi(api_client)
    basic_auth_request = BasicAuthRequest(
        username="username_example",
        password="password_example",
    ) # BasicAuthRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Authenticate a user based on the supplied credentials.
        api_instance.api_authenticate_post(basic_auth_request=basic_auth_request)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthenticationApi->api_authenticate_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **basic_auth_request** | [**BasicAuthRequest**](BasicAuthRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sample response:                    {          \&quot;IdToken\&quot;: \&quot;an identification token that can be used in the authorisation header to make a call to a Yourkeys public API endpoint\&quot;,          \&quot;TokenType\&quot;: \&quot;Bearer\&quot;,          \&quot;ExpiresSeconds\&quot;: 3600,          \&quot;RefreshToken\&quot;: \&quot;a refresh token that can be used to generate a new identification token once the identification token has expired\&quot;      } |  -  |
**401** | Unauthorised; invalid credentials supplied. |  -  |
**403** | Error message detailing an issue with the user account. |  -  |
**500** | Error message detailing an issue with the Yourkeys system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_refresh_authentication_post**
> api_refresh_authentication_post()

Generate a new identity token based on the supplied refresh token.

Sample request:        POST /api/Authenticate      {         \"refreshToken\": \"example_token\"      }

### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_auth_client
from yk_auth_client.api import authentication_api
from yk_auth_client.model.refresh_auth_request import RefreshAuthRequest
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
    api_instance = authentication_api.AuthenticationApi(api_client)
    refresh_auth_request = RefreshAuthRequest(
        refresh_token="refresh_token_example",
    ) # RefreshAuthRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate a new identity token based on the supplied refresh token.
        api_instance.api_refresh_authentication_post(refresh_auth_request=refresh_auth_request)
    except yk_auth_client.ApiException as e:
        print("Exception when calling AuthenticationApi->api_refresh_authentication_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_auth_request** | [**RefreshAuthRequest**](RefreshAuthRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sample response:                    {          \&quot;IdToken\&quot;: \&quot;an identification token that can be used in the authorisation header to make a call to a Yourkeys public API endpoint\&quot;,          \&quot;TokenType\&quot;: \&quot;Bearer\&quot;,          \&quot;ExpiresSeconds\&quot;: 3600,          \&quot;RefreshToken\&quot;: null      } |  -  |
**401** | Unauthorised; invalid refresh token supplied. |  -  |
**403** | Error message detailing an issue with the user account. |  -  |
**500** | Error message detailing an issue with the Yourkeys system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

