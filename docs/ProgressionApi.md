# openapi_client.ProgressionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_progression_purchase_referencenumber_code_put**](ProgressionApi.md#api_progression_purchase_referencenumber_code_put) | **PUT** /api/progression/purchase/{referencenumber}/{code} | 


# **api_progression_purchase_referencenumber_code_put**
> api_progression_purchase_referencenumber_code_put(referencenumber, code)



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import progression_api
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
    api_instance = progression_api.ProgressionApi(api_client)
    referencenumber = "referencenumber_example" # str | 
    code = "code_example" # str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_progression_purchase_referencenumber_code_put(referencenumber, code)
    except openapi_client.ApiException as e:
        print("Exception when calling ProgressionApi->api_progression_purchase_referencenumber_code_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **referencenumber** | **str**|  |
 **code** | **str, none_type**|  |

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

