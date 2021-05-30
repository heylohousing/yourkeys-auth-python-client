# openapi_client.SalesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_reservation_post**](SalesApi.md#api_reservation_post) | **POST** /api/Reservation | 
[**api_sales_reservation_post**](SalesApi.md#api_sales_reservation_post) | **POST** /api/sales/Reservation | 
[**api_sales_reservation_upgrades_and_extras_post**](SalesApi.md#api_sales_reservation_upgrades_and_extras_post) | **POST** /api/sales/Reservation/UpgradesAndExtras | 


# **api_reservation_post**
> CreateReservationResponse api_reservation_post()



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import sales_api
from openapi_client.model.create_reservation_request import CreateReservationRequest
from openapi_client.model.create_reservation_response import CreateReservationResponse
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
    api_instance = sales_api.SalesApi(api_client)
    create_reservation_request = CreateReservationRequest(
        seller_reference="seller_reference_example",
        development_id="development_id_example",
        plot_id="plot_id_example",
        purchase_method="purchase_method_example",
        expected_exchange=dateutil_parser('1970-01-01T00:00:00.00Z'),
        expected_completion=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_of_inquiry="source_of_inquiry_example",
        purchase_path=PurchasePath(
            buyer_affiliation="buyer_affiliation_example",
            corporate_details=CorporateDetails(
                company_registration_number="company_registration_number_example",
                company_name="company_name_example",
                company_registration_country="company_registration_country_example",
            ),
        ),
        clients=[
            Client(
                primary_contact=True,
                client_party=ClientParty(
                    title="title_example",
                    first_name="first_name_example",
                    middle_name="middle_name_example",
                    surname="surname_example",
                    previous_surname="previous_surname_example",
                    gender="gender_example",
                    nationality="nationality_example",
                    country_of_birth="country_of_birth_example",
                    town_of_birth="town_of_birth_example",
                    date_of_birth=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    email="email_example",
                    landline="landline_example",
                    mobile="mobile_example",
                    addresses=[
                        ClientAddress(
                            address1="address1_example",
                            address2="address2_example",
                            town="town_example",
                            county="county_example",
                            postal_code="postal_code_example",
                            country="country_example",
                            moved_in_year=1,
                            moved_in_month=1,
                        ),
                    ],
                    employment_status="employment_status_example",
                    current_occupation="current_occupation_example",
                    current_salary="current_salary_example",
                ),
            ),
        ],
    ) # CreateReservationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_reservation_post(create_reservation_request=create_reservation_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SalesApi->api_reservation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_reservation_request** | [**CreateReservationRequest**](CreateReservationRequest.md)|  | [optional]

### Return type

[**CreateReservationResponse**](CreateReservationResponse.md)

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

# **api_sales_reservation_post**
> CreateReservationResponse api_sales_reservation_post()



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import sales_api
from openapi_client.model.create_reservation_request import CreateReservationRequest
from openapi_client.model.create_reservation_response import CreateReservationResponse
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
    api_instance = sales_api.SalesApi(api_client)
    create_reservation_request = CreateReservationRequest(
        seller_reference="seller_reference_example",
        development_id="development_id_example",
        plot_id="plot_id_example",
        purchase_method="purchase_method_example",
        expected_exchange=dateutil_parser('1970-01-01T00:00:00.00Z'),
        expected_completion=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_of_inquiry="source_of_inquiry_example",
        purchase_path=PurchasePath(
            buyer_affiliation="buyer_affiliation_example",
            corporate_details=CorporateDetails(
                company_registration_number="company_registration_number_example",
                company_name="company_name_example",
                company_registration_country="company_registration_country_example",
            ),
        ),
        clients=[
            Client(
                primary_contact=True,
                client_party=ClientParty(
                    title="title_example",
                    first_name="first_name_example",
                    middle_name="middle_name_example",
                    surname="surname_example",
                    previous_surname="previous_surname_example",
                    gender="gender_example",
                    nationality="nationality_example",
                    country_of_birth="country_of_birth_example",
                    town_of_birth="town_of_birth_example",
                    date_of_birth=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    email="email_example",
                    landline="landline_example",
                    mobile="mobile_example",
                    addresses=[
                        ClientAddress(
                            address1="address1_example",
                            address2="address2_example",
                            town="town_example",
                            county="county_example",
                            postal_code="postal_code_example",
                            country="country_example",
                            moved_in_year=1,
                            moved_in_month=1,
                        ),
                    ],
                    employment_status="employment_status_example",
                    current_occupation="current_occupation_example",
                    current_salary="current_salary_example",
                ),
            ),
        ],
    ) # CreateReservationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_sales_reservation_post(create_reservation_request=create_reservation_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SalesApi->api_sales_reservation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_reservation_request** | [**CreateReservationRequest**](CreateReservationRequest.md)|  | [optional]

### Return type

[**CreateReservationResponse**](CreateReservationResponse.md)

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

# **api_sales_reservation_upgrades_and_extras_post**
> api_sales_reservation_upgrades_and_extras_post()



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import sales_api
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
    api_instance = sales_api.SalesApi(api_client)
    seller_reference = "seller_reference_example" # str, none_type |  (optional)
    purchase_reference = "purchase_reference_example" # str, none_type |  (optional)
    development_id = "development_id_example" # str, none_type |  (optional)
    plot_id = "plot_id_example" # str, none_type |  (optional)
    file_stream = open('/path/to/file', 'rb') # file_type, none_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.api_sales_reservation_upgrades_and_extras_post(seller_reference=seller_reference, purchase_reference=purchase_reference, development_id=development_id, plot_id=plot_id, file_stream=file_stream)
    except openapi_client.ApiException as e:
        print("Exception when calling SalesApi->api_sales_reservation_upgrades_and_extras_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_reference** | **str, none_type**|  | [optional]
 **purchase_reference** | **str, none_type**|  | [optional]
 **development_id** | **str, none_type**|  | [optional]
 **plot_id** | **str, none_type**|  | [optional]
 **file_stream** | **file_type, none_type**|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

