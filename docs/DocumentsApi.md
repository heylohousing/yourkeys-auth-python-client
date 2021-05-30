# openapi_client.DocumentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_reservation_referencenumber_documents_instructionpack_fileid_get**](DocumentsApi.md#api_reservation_referencenumber_documents_instructionpack_fileid_get) | **GET** /api/reservation/{referencenumber}/documents/instructionpack/{fileid} | 
[**api_reservation_referencenumber_documents_instructionpack_get**](DocumentsApi.md#api_reservation_referencenumber_documents_instructionpack_get) | **GET** /api/reservation/{referencenumber}/documents/instructionpack | 


# **api_reservation_referencenumber_documents_instructionpack_fileid_get**
> api_reservation_referencenumber_documents_instructionpack_fileid_get(referencenumber, fileid)



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import documents_api
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
    api_instance = documents_api.DocumentsApi(api_client)
    referencenumber = "referencenumber_example" # str | 
    fileid = "fileid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_reservation_referencenumber_documents_instructionpack_fileid_get(referencenumber, fileid)
    except openapi_client.ApiException as e:
        print("Exception when calling DocumentsApi->api_reservation_referencenumber_documents_instructionpack_fileid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **referencenumber** | **str**|  |
 **fileid** | **str**|  |

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

# **api_reservation_referencenumber_documents_instructionpack_get**
> api_reservation_referencenumber_documents_instructionpack_get(referencenumber)



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import documents_api
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
    api_instance = documents_api.DocumentsApi(api_client)
    referencenumber = "referencenumber_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_reservation_referencenumber_documents_instructionpack_get(referencenumber)
    except openapi_client.ApiException as e:
        print("Exception when calling DocumentsApi->api_reservation_referencenumber_documents_instructionpack_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **referencenumber** | **str**|  |

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

