# defectdojo_api_generated.EndpointMetaImportApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoint_meta_import_create**](EndpointMetaImportApi.md#endpoint_meta_import_create) | **POST** /api/v2/endpoint_meta_import/ | 


# **endpoint_meta_import_create**
> EndpointMetaImporter endpoint_meta_import_create(file, create_endpoints=create_endpoints, create_tags=create_tags, create_dojo_meta=create_dojo_meta, product_name=product_name, product=product)

Imports a CSV file into a product to propagate arbitrary meta and tags on endpoints.

By Names:
- Provide `product_name` of existing product

By ID:
- Provide the id of the product in the `product` parameter

In this scenario Defect Dojo will look up the product by the provided details.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.endpoint_meta_importer import EndpointMetaImporter
from defectdojo_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = defectdojo_api_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = defectdojo_api_generated.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with defectdojo_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = defectdojo_api_generated.EndpointMetaImportApi(api_client)
    file = None # bytearray | 
    create_endpoints = True # bool |  (optional) (default to True)
    create_tags = True # bool |  (optional) (default to True)
    create_dojo_meta = False # bool |  (optional) (default to False)
    product_name = 'product_name_example' # str |  (optional)
    product = 56 # int |  (optional)

    try:
        api_response = api_instance.endpoint_meta_import_create(file, create_endpoints=create_endpoints, create_tags=create_tags, create_dojo_meta=create_dojo_meta, product_name=product_name, product=product)
        print("The response of EndpointMetaImportApi->endpoint_meta_import_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointMetaImportApi->endpoint_meta_import_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **create_endpoints** | **bool**|  | [optional] [default to True]
 **create_tags** | **bool**|  | [optional] [default to True]
 **create_dojo_meta** | **bool**|  | [optional] [default to False]
 **product_name** | **str**|  | [optional] 
 **product** | **int**|  | [optional] 

### Return type

[**EndpointMetaImporter**](EndpointMetaImporter.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

