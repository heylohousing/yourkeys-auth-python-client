# openapi_client.EventApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_progression_purchase_referencenumber_event_eventcode_put**](EventApi.md#api_progression_purchase_referencenumber_event_eventcode_put) | **PUT** /api/progression/purchase/{referencenumber}/event/{eventcode} | 


# **api_progression_purchase_referencenumber_event_eventcode_put**
> api_progression_purchase_referencenumber_event_eventcode_put(referencenumber, eventcode)



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import event_api
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
    api_instance = event_api.EventApi(api_client)
    referencenumber = "referencenumber_example" # str | 
    eventcode = "eventcode_example" # str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_progression_purchase_referencenumber_event_eventcode_put(referencenumber, eventcode)
    except openapi_client.ApiException as e:
        print("Exception when calling EventApi->api_progression_purchase_referencenumber_event_eventcode_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **referencenumber** | **str**|  |
 **eventcode** | **str, none_type**|  |

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

