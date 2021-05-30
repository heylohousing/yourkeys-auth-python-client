# openapi_client.PassthroughApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_passthrough_generate_passthrough_url_post**](PassthroughApi.md#api_passthrough_generate_passthrough_url_post) | **POST** /api/Passthrough/GeneratePassthroughUrl | 


# **api_passthrough_generate_passthrough_url_post**
> PassthroughUrlResponse api_passthrough_generate_passthrough_url_post()



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import passthrough_api
from openapi_client.model.passthrough_url_response import PassthroughUrlResponse
from openapi_client.model.passthrough_url_request import PassthroughUrlRequest
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
    api_instance = passthrough_api.PassthroughApi(api_client)
    passthrough_url_request = PassthroughUrlRequest(
        seller_reference="seller_reference_example",
        purchase_reference="purchase_reference_example",
        development_reference="development_reference_example",
        landing_page="landing_page_example",
    ) # PassthroughUrlRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_passthrough_generate_passthrough_url_post(passthrough_url_request=passthrough_url_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PassthroughApi->api_passthrough_generate_passthrough_url_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **passthrough_url_request** | [**PassthroughUrlRequest**](PassthroughUrlRequest.md)|  | [optional]

### Return type

[**PassthroughUrlResponse**](PassthroughUrlResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

