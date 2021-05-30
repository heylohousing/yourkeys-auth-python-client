# openapi_client.LogoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logo_development_main_account_development_id_get**](LogoApi.md#logo_development_main_account_development_id_get) | **GET** /Logo/development-main-account/{developmentId} | 
[**logo_seller_developer_id_get**](LogoApi.md#logo_seller_developer_id_get) | **GET** /Logo/seller/{developerId} | 


# **logo_development_main_account_development_id_get**
> logo_development_main_account_development_id_get(development_id)



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import logo_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logo_api.LogoApi(api_client)
    development_id = "developmentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.logo_development_main_account_development_id_get(development_id)
    except openapi_client.ApiException as e:
        print("Exception when calling LogoApi->logo_development_main_account_development_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **development_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logo_seller_developer_id_get**
> logo_seller_developer_id_get(developer_id)



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import logo_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logo_api.LogoApi(api_client)
    developer_id = "developerId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.logo_seller_developer_id_get(developer_id)
    except openapi_client.ApiException as e:
        print("Exception when calling LogoApi->logo_seller_developer_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **developer_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

