# openapi_client.InventoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_inventory_blocks_delete**](InventoryApi.md#api_inventory_blocks_delete) | **DELETE** /api/Inventory/blocks | 
[**api_inventory_blocks_post**](InventoryApi.md#api_inventory_blocks_post) | **POST** /api/Inventory/blocks | 
[**api_inventory_blocks_put**](InventoryApi.md#api_inventory_blocks_put) | **PUT** /api/Inventory/blocks | 
[**api_inventory_development_livestatusupdate_put**](InventoryApi.md#api_inventory_development_livestatusupdate_put) | **PUT** /api/Inventory/development/livestatusupdate | 
[**api_inventory_developments_post**](InventoryApi.md#api_inventory_developments_post) | **POST** /api/Inventory/developments | 
[**api_inventory_developments_put**](InventoryApi.md#api_inventory_developments_put) | **PUT** /api/Inventory/developments | 
[**api_inventory_housebuilder_seller_reference_development_development_id_block_block_id_plots_get**](InventoryApi.md#api_inventory_housebuilder_seller_reference_development_development_id_block_block_id_plots_get) | **GET** /api/Inventory/housebuilder/{sellerReference}/development/{developmentId}/block/{blockId}/plots | 
[**api_inventory_housebuilder_seller_reference_development_development_id_blocks_get**](InventoryApi.md#api_inventory_housebuilder_seller_reference_development_development_id_blocks_get) | **GET** /api/Inventory/housebuilder/{sellerReference}/development/{developmentId}/blocks | 
[**api_inventory_housebuilder_seller_reference_developments_get**](InventoryApi.md#api_inventory_housebuilder_seller_reference_developments_get) | **GET** /api/Inventory/housebuilder/{sellerReference}/developments | 
[**api_inventory_plots_delete**](InventoryApi.md#api_inventory_plots_delete) | **DELETE** /api/Inventory/plots | 
[**api_inventory_plots_post**](InventoryApi.md#api_inventory_plots_post) | **POST** /api/Inventory/plots | 
[**api_inventory_plots_put**](InventoryApi.md#api_inventory_plots_put) | **PUT** /api/Inventory/plots | 


# **api_inventory_blocks_delete**
> DeleteBlocksResponse api_inventory_blocks_delete()



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import inventory_api
from openapi_client.model.delete_blocks_response import DeleteBlocksResponse
from openapi_client.model.delete_blocks_request import DeleteBlocksRequest
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
    api_instance = inventory_api.InventoryApi(api_client)
    delete_blocks_request = DeleteBlocksRequest(
        seller_reference="seller_reference_example",
        development_id="development_id_example",
        blocks=[
            DeleteBlockRequest(
                block_reference="block_reference_example",
                block_id="block_id_example",
            ),
        ],
    ) # DeleteBlocksRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_inventory_blocks_delete(delete_blocks_request=delete_blocks_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryApi->api_inventory_blocks_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_blocks_request** | [**DeleteBlocksRequest**](DeleteBlocksRequest.md)|  | [optional]

### Return type

[**DeleteBlocksResponse**](DeleteBlocksResponse.md)

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

# **api_inventory_blocks_post**
> CreateBlocksResponse api_inventory_blocks_post()



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import inventory_api
from openapi_client.model.create_blocks_response import CreateBlocksResponse
from openapi_client.model.create_blocks_request import CreateBlocksRequest
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
    api_instance = inventory_api.InventoryApi(api_client)
    create_blocks_request = CreateBlocksRequest(
        seller_reference="seller_reference_example",
        development_id="development_id_example",
        blocks=[
            CreateBlockRequest(
                block_reference="block_reference_example",
                block_name="block_name_example",
                number_of_storeys=1,
                lifts_provided=True,
            ),
        ],
    ) # CreateBlocksRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_inventory_blocks_post(create_blocks_request=create_blocks_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryApi->api_inventory_blocks_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_blocks_request** | [**CreateBlocksRequest**](CreateBlocksRequest.md)|  | [optional]

### Return type

[**CreateBlocksResponse**](CreateBlocksResponse.md)

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

# **api_inventory_blocks_put**
> UpdateBlocksResponse api_inventory_blocks_put()



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import inventory_api
from openapi_client.model.update_blocks_request import UpdateBlocksRequest
from openapi_client.model.update_blocks_response import UpdateBlocksResponse
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
    api_instance = inventory_api.InventoryApi(api_client)
    update_blocks_request = UpdateBlocksRequest(
        seller_reference="seller_reference_example",
        development_id="development_id_example",
        blocks=[
            UpdateBlockRequest(
                block_reference="block_reference_example",
                block_id="block_id_example",
                block_name="block_name_example",
                number_of_storeys=1,
                lifts_provided=True,
            ),
        ],
    ) # UpdateBlocksRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_inventory_blocks_put(update_blocks_request=update_blocks_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryApi->api_inventory_blocks_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_blocks_request** | [**UpdateBlocksRequest**](UpdateBlocksRequest.md)|  | [optional]

### Return type

[**UpdateBlocksResponse**](UpdateBlocksResponse.md)

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

# **api_inventory_development_livestatusupdate_put**
> api_inventory_development_livestatusupdate_put()



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import inventory_api
from openapi_client.model.problem_details import ProblemDetails
from openapi_client.model.set_development_live_flag_request import SetDevelopmentLiveFlagRequest
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
    api_instance = inventory_api.InventoryApi(api_client)
    set_development_live_flag_request = SetDevelopmentLiveFlagRequest(
        seller_reference="seller_reference_example",
        development_id="development_id_example",
        is_live=True,
    ) # SetDevelopmentLiveFlagRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.api_inventory_development_livestatusupdate_put(set_development_live_flag_request=set_development_live_flag_request)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryApi->api_inventory_development_livestatusupdate_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_development_live_flag_request** | [**SetDevelopmentLiveFlagRequest**](SetDevelopmentLiveFlagRequest.md)|  | [optional]

### Return type

void (empty response body)

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

# **api_inventory_developments_post**
> CreateDevelopmentsResponse api_inventory_developments_post()



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import inventory_api
from openapi_client.model.create_developments_response import CreateDevelopmentsResponse
from openapi_client.model.create_developments_request import CreateDevelopmentsRequest
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
    api_instance = inventory_api.InventoryApi(api_client)
    create_developments_request = CreateDevelopmentsRequest(
        seller_reference="seller_reference_example",
        developments=[
            CreateDevelopmentRequest(
                development_reference="development_reference_example",
                development_name="development_name_example",
                address="address_example",
                address2="address2_example",
                town="town_example",
                county="county_example",
                postcode="postcode_example",
                country="country_example",
                completion_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                phase_reference="phase_reference_example",
                help_to_buy=True,
                help_to_buy_region="help_to_buy_region_example",
                spv_name="spv_name_example",
                spv_address1="spv_address1_example",
                spv_address2="spv_address2_example",
                spv_town="spv_town_example",
                spv_county="spv_county_example",
                spv_postcode="spv_postcode_example",
                spv_vat_number="spv_vat_number_example",
                spv_country="spv_country_example",
                vendor_company_name="vendor_company_name_example",
                terms_and_conditions="terms_and_conditions_example",
                land_tax_region="land_tax_region_example",
                uk_finance_disclosure_of_incentives_form_details=CreateCmlRequest(
                    sellers_details=CmlSellerDetailsRequest(
                        names_of_organisations_individuals="names_of_organisations_individuals_example",
                        address="address_example",
                        phone="phone_example",
                    ),
                    tenure=CmlTenureRequest(
                        type_of_affordable_homes="type_of_affordable_homes_example",
                        unit_counts_of_types="unit_counts_of_types_example",
                    ),
                    construction=CmlConstructionRequest(
                        primary_materials_and_construction_method="primary_materials_and_construction_method_example",
                        energy_performance_rating="energy_performance_rating_example",
                    ),
                    warranty_professional_consultant_accreditation=CmlWarrantyProfessionalConsultantAccreditationRequest(
                        warranty_provider_or_professional_consultant="warranty_provider_or_professional_consultant_example",
                        warranty_provider_company_registration_number="warranty_provider_company_registration_number_example",
                        accreditation_system="accreditation_system_example",
                    ),
                    freeholder=CmlFreeholderRequest(
                        name_and_address="name_and_address_example",
                    ),
                    separate_lease_ground_rent_details=CmlSeparateLeaseGroundRentDetailsRequest(
                        details="details_example",
                        freeholder_name_and_address="freeholder_name_and_address_example",
                    ),
                ),
            ),
        ],
    ) # CreateDevelopmentsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_inventory_developments_post(create_developments_request=create_developments_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryApi->api_inventory_developments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_developments_request** | [**CreateDevelopmentsRequest**](CreateDevelopmentsRequest.md)|  | [optional]

### Return type

[**CreateDevelopmentsResponse**](CreateDevelopmentsResponse.md)

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

# **api_inventory_developments_put**
> UpdateDevelopmentsResponse api_inventory_developments_put()



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import inventory_api
from openapi_client.model.update_developments_request import UpdateDevelopmentsRequest
from openapi_client.model.update_developments_response import UpdateDevelopmentsResponse
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
    api_instance = inventory_api.InventoryApi(api_client)
    update_developments_request = UpdateDevelopmentsRequest(
        seller_reference="seller_reference_example",
        developments=[
            UpdateDevelopmentRequest(
                development_reference="development_reference_example",
                development_id="development_id_example",
                development_name="development_name_example",
                address="address_example",
                address2="address2_example",
                town="town_example",
                county="county_example",
                postcode="postcode_example",
                country="country_example",
                completion_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                phase_reference="phase_reference_example",
                help_to_buy=True,
                help_to_buy_region="help_to_buy_region_example",
                spv_name="spv_name_example",
                spv_address1="spv_address1_example",
                spv_address2="spv_address2_example",
                spv_town="spv_town_example",
                spv_county="spv_county_example",
                spv_postcode="spv_postcode_example",
                spv_vat_number="spv_vat_number_example",
                spv_country="spv_country_example",
                vendor_company_name="vendor_company_name_example",
                terms_and_conditions="terms_and_conditions_example",
                land_tax_region="land_tax_region_example",
                uk_finance_disclosure_of_incentives_form_details=UpdateCmlRequest(
                    sellers_details=CmlSellerDetailsRequest(
                        names_of_organisations_individuals="names_of_organisations_individuals_example",
                        address="address_example",
                        phone="phone_example",
                    ),
                    tenure=CmlTenureRequest(
                        type_of_affordable_homes="type_of_affordable_homes_example",
                        unit_counts_of_types="unit_counts_of_types_example",
                    ),
                    construction=CmlConstructionRequest(
                        primary_materials_and_construction_method="primary_materials_and_construction_method_example",
                        energy_performance_rating="energy_performance_rating_example",
                    ),
                    warranty_professional_consultant_accreditation=CmlWarrantyProfessionalConsultantAccreditationRequest(
                        warranty_provider_or_professional_consultant="warranty_provider_or_professional_consultant_example",
                        warranty_provider_company_registration_number="warranty_provider_company_registration_number_example",
                        accreditation_system="accreditation_system_example",
                    ),
                    freeholder=CmlFreeholderRequest(
                        name_and_address="name_and_address_example",
                    ),
                    separate_lease_ground_rent_details=CmlSeparateLeaseGroundRentDetailsRequest(
                        details="details_example",
                        freeholder_name_and_address="freeholder_name_and_address_example",
                    ),
                ),
            ),
        ],
    ) # UpdateDevelopmentsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_inventory_developments_put(update_developments_request=update_developments_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryApi->api_inventory_developments_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_developments_request** | [**UpdateDevelopmentsRequest**](UpdateDevelopmentsRequest.md)|  | [optional]

### Return type

[**UpdateDevelopmentsResponse**](UpdateDevelopmentsResponse.md)

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

# **api_inventory_housebuilder_seller_reference_development_development_id_block_block_id_plots_get**
> GetPlotsResponse api_inventory_housebuilder_seller_reference_development_development_id_block_block_id_plots_get(seller_reference, development_id, block_id)



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import inventory_api
from openapi_client.model.get_plots_response import GetPlotsResponse
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
    api_instance = inventory_api.InventoryApi(api_client)
    seller_reference = "sellerReference_example" # str, none_type | 
    development_id = "developmentId_example" # str, none_type | 
    block_id = "blockId_example" # str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_inventory_housebuilder_seller_reference_development_development_id_block_block_id_plots_get(seller_reference, development_id, block_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryApi->api_inventory_housebuilder_seller_reference_development_development_id_block_block_id_plots_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_reference** | **str, none_type**|  |
 **development_id** | **str, none_type**|  |
 **block_id** | **str, none_type**|  |

### Return type

[**GetPlotsResponse**](GetPlotsResponse.md)

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

# **api_inventory_housebuilder_seller_reference_development_development_id_blocks_get**
> BlocksResponse api_inventory_housebuilder_seller_reference_development_development_id_blocks_get(seller_reference, development_id)



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import inventory_api
from openapi_client.model.blocks_response import BlocksResponse
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
    api_instance = inventory_api.InventoryApi(api_client)
    seller_reference = "sellerReference_example" # str, none_type | 
    development_id = "developmentId_example" # str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_inventory_housebuilder_seller_reference_development_development_id_blocks_get(seller_reference, development_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryApi->api_inventory_housebuilder_seller_reference_development_development_id_blocks_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_reference** | **str, none_type**|  |
 **development_id** | **str, none_type**|  |

### Return type

[**BlocksResponse**](BlocksResponse.md)

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

# **api_inventory_housebuilder_seller_reference_developments_get**
> InventoryDevelopmentsResponse api_inventory_housebuilder_seller_reference_developments_get(seller_reference)



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import inventory_api
from openapi_client.model.inventory_developments_response import InventoryDevelopmentsResponse
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
    api_instance = inventory_api.InventoryApi(api_client)
    seller_reference = "sellerReference_example" # str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_inventory_housebuilder_seller_reference_developments_get(seller_reference)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryApi->api_inventory_housebuilder_seller_reference_developments_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_reference** | **str, none_type**|  |

### Return type

[**InventoryDevelopmentsResponse**](InventoryDevelopmentsResponse.md)

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

# **api_inventory_plots_delete**
> DeletePlotsResponse api_inventory_plots_delete()



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import inventory_api
from openapi_client.model.delete_plots_response import DeletePlotsResponse
from openapi_client.model.delete_plots_request import DeletePlotsRequest
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
    api_instance = inventory_api.InventoryApi(api_client)
    delete_plots_request = DeletePlotsRequest(
        seller_reference="seller_reference_example",
        development_id="development_id_example",
        block_id="block_id_example",
        plots=[
            DeletePlotRequest(
                plot_reference="plot_reference_example",
                plot_id="plot_id_example",
            ),
        ],
    ) # DeletePlotsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_inventory_plots_delete(delete_plots_request=delete_plots_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryApi->api_inventory_plots_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_plots_request** | [**DeletePlotsRequest**](DeletePlotsRequest.md)|  | [optional]

### Return type

[**DeletePlotsResponse**](DeletePlotsResponse.md)

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

# **api_inventory_plots_post**
> CreatePlotsResponse api_inventory_plots_post()



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import inventory_api
from openapi_client.model.create_plots_response import CreatePlotsResponse
from openapi_client.model.create_plots_request import CreatePlotsRequest
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
    api_instance = inventory_api.InventoryApi(api_client)
    create_plots_request = CreatePlotsRequest(
        seller_reference="seller_reference_example",
        development_id="development_id_example",
        block_id="block_id_example",
        plots=[
            CreatePlotRequest(
                plot_reference="plot_reference_example",
                plot_no="plot_no_example",
                plot_price=3.14,
                tenure="tenure_example",
                is_live=True,
                completion_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                offer_price=3.14,
                oss_meter=3.14,
                oss_ft=3.14,
                pre_sold=True,
                address="address_example",
                town="town_example",
                county="county_example",
                postcode="postcode_example",
                country="country_example",
                lease_length_year=1,
                ground_rent_review_frequency_in_years=1,
                ground_rent_methodology="ground_rent_methodology_example",
                service_charge_initial_amount=3.14,
                service_charge_payment_frequency="service_charge_payment_frequency_example",
                dwelling_type="dwelling_type_example",
                bedrooms=1,
                bathrooms=1,
                reservation_fee=3.14,
                area_metre=3.14,
                area_ft=3.14,
                lease_commencement_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                estate_charge_initial_amount=3.14,
                estate_charge_payment_frequency="estate_charge_payment_frequency_example",
                ground_rent_initial_amount=3.14,
                ground_rent_percentage=3.14,
                ground_rent_calculation_method="ground_rent_calculation_method_example",
                floor=1,
                uprn="uprn_example",
                developer_code="developer_code_example",
                energy_sap_rating="energy_sap_rating_example",
                shared_ownership=True,
            ),
        ],
    ) # CreatePlotsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_inventory_plots_post(create_plots_request=create_plots_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryApi->api_inventory_plots_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_plots_request** | [**CreatePlotsRequest**](CreatePlotsRequest.md)|  | [optional]

### Return type

[**CreatePlotsResponse**](CreatePlotsResponse.md)

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

# **api_inventory_plots_put**
> UpdatePlotsResponse api_inventory_plots_put()



### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import inventory_api
from openapi_client.model.update_plots_request import UpdatePlotsRequest
from openapi_client.model.update_plots_response import UpdatePlotsResponse
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
    api_instance = inventory_api.InventoryApi(api_client)
    update_plots_request = UpdatePlotsRequest(
        seller_reference="seller_reference_example",
        development_id="development_id_example",
        block_id="block_id_example",
        plots=[
            UpdatePlotRequest(
                plot_id="plot_id_example",
                plot_reference="plot_reference_example",
                plot_no="plot_no_example",
                plot_price=3.14,
                tenure="tenure_example",
                is_live=True,
                completion_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                offer_price=3.14,
                oss_meter=3.14,
                oss_ft=3.14,
                pre_sold=True,
                address="address_example",
                town="town_example",
                county="county_example",
                postcode="postcode_example",
                country="country_example",
                lease_length_year=1,
                ground_rent_review_frequency_in_years=1,
                ground_rent_methodology="ground_rent_methodology_example",
                service_charge_initial_amount=3.14,
                service_charge_payment_frequency="service_charge_payment_frequency_example",
                dwelling_type="dwelling_type_example",
                bedrooms=1,
                bathrooms=1,
                reservation_fee=3.14,
                area_metre=3.14,
                area_ft=3.14,
                lease_commencement_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                estate_charge_initial_amount=3.14,
                estate_charge_payment_frequency="estate_charge_payment_frequency_example",
                ground_rent_initial_amount=3.14,
                ground_rent_percentage=3.14,
                ground_rent_calculation_method="ground_rent_calculation_method_example",
                floor=1,
                uprn="uprn_example",
                developer_code="developer_code_example",
                energy_sap_rating="energy_sap_rating_example",
                shared_ownership=True,
            ),
        ],
    ) # UpdatePlotsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_inventory_plots_put(update_plots_request=update_plots_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryApi->api_inventory_plots_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_plots_request** | [**UpdatePlotsRequest**](UpdatePlotsRequest.md)|  | [optional]

### Return type

[**UpdatePlotsResponse**](UpdatePlotsResponse.md)

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

