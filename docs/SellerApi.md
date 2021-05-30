# openapi_client.SellerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_seller_reference_number_developments_development_id_plots_get**](SellerApi.md#api_seller_reference_number_developments_development_id_plots_get) | **GET** /api/Seller/{referenceNumber}/developments/{developmentId}/plots | Returns all plots with an AVABL status for a the supplied development that the supplied seller has access to.
[**api_seller_reference_number_developments_get**](SellerApi.md#api_seller_reference_number_developments_get) | **GET** /api/Seller/{referenceNumber}/developments | 


# **api_seller_reference_number_developments_development_id_plots_get**
> PlotsResponse api_seller_reference_number_developments_development_id_plots_get(reference_number, development_id)

Returns all plots with an AVABL status for a the supplied development that the supplied seller has access to.

### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import seller_api
from openapi_client.model.plots_response import PlotsResponse
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
    api_instance = seller_api.SellerApi(api_client)
    reference_number = "referenceNumber_example" # str, none_type | 
    development_id = "developmentId_example" # str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Returns all plots with an AVABL status for a the supplied development that the supplied seller has access to.
        api_response = api_instance.api_seller_reference_number_developments_development_id_plots_get(reference_number, development_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SellerApi->api_seller_reference_number_developments_development_id_plots_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_number** | **str, none_type**|  |
 **development_id** | **str, none_type**|  |

### Return type

[**PlotsResponse**](PlotsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_seller_reference_number_developments_get**
> SellerDevelopmentsResponse api_seller_reference_number_developments_get(reference_number)



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import seller_api
from openapi_client.model.seller_developments_response import SellerDevelopmentsResponse
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
    api_instance = seller_api.SellerApi(api_client)
    reference_number = "referenceNumber_example" # str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_seller_reference_number_developments_get(reference_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SellerApi->api_seller_reference_number_developments_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_number** | **str, none_type**|  |

### Return type

[**SellerDevelopmentsResponse**](SellerDevelopmentsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

