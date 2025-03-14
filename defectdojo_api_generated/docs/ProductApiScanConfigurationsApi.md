# defectdojo_api_generated.ProductApiScanConfigurationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_api_scan_configurations_create**](ProductApiScanConfigurationsApi.md#product_api_scan_configurations_create) | **POST** /api/v2/product_api_scan_configurations/ | 
[**product_api_scan_configurations_delete_preview_list**](ProductApiScanConfigurationsApi.md#product_api_scan_configurations_delete_preview_list) | **GET** /api/v2/product_api_scan_configurations/{id}/delete_preview/ | 
[**product_api_scan_configurations_destroy**](ProductApiScanConfigurationsApi.md#product_api_scan_configurations_destroy) | **DELETE** /api/v2/product_api_scan_configurations/{id}/ | 
[**product_api_scan_configurations_list**](ProductApiScanConfigurationsApi.md#product_api_scan_configurations_list) | **GET** /api/v2/product_api_scan_configurations/ | 
[**product_api_scan_configurations_partial_update**](ProductApiScanConfigurationsApi.md#product_api_scan_configurations_partial_update) | **PATCH** /api/v2/product_api_scan_configurations/{id}/ | 
[**product_api_scan_configurations_retrieve**](ProductApiScanConfigurationsApi.md#product_api_scan_configurations_retrieve) | **GET** /api/v2/product_api_scan_configurations/{id}/ | 
[**product_api_scan_configurations_update**](ProductApiScanConfigurationsApi.md#product_api_scan_configurations_update) | **PUT** /api/v2/product_api_scan_configurations/{id}/ | 


# **product_api_scan_configurations_create**
> ProductAPIScanConfiguration product_api_scan_configurations_create(product_api_scan_configuration_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.product_api_scan_configuration import ProductAPIScanConfiguration
from defectdojo_api_generated.models.product_api_scan_configuration_request import ProductAPIScanConfigurationRequest
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
    api_instance = defectdojo_api_generated.ProductApiScanConfigurationsApi(api_client)
    product_api_scan_configuration_request = defectdojo_api_generated.ProductAPIScanConfigurationRequest() # ProductAPIScanConfigurationRequest | 

    try:
        api_response = api_instance.product_api_scan_configurations_create(product_api_scan_configuration_request)
        print("The response of ProductApiScanConfigurationsApi->product_api_scan_configurations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApiScanConfigurationsApi->product_api_scan_configurations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_api_scan_configuration_request** | [**ProductAPIScanConfigurationRequest**](ProductAPIScanConfigurationRequest.md)|  | 

### Return type

[**ProductAPIScanConfiguration**](ProductAPIScanConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_api_scan_configurations_delete_preview_list**
> PaginatedDeletePreviewList product_api_scan_configurations_delete_preview_list(id, limit=limit, offset=offset)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_delete_preview_list import PaginatedDeletePreviewList
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
    api_instance = defectdojo_api_generated.ProductApiScanConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this product_ap i_ scan_ configuration.
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.product_api_scan_configurations_delete_preview_list(id, limit=limit, offset=offset)
        print("The response of ProductApiScanConfigurationsApi->product_api_scan_configurations_delete_preview_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApiScanConfigurationsApi->product_api_scan_configurations_delete_preview_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product_ap i_ scan_ configuration. | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedDeletePreviewList**](PaginatedDeletePreviewList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_api_scan_configurations_destroy**
> product_api_scan_configurations_destroy(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
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
    api_instance = defectdojo_api_generated.ProductApiScanConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this product_ap i_ scan_ configuration.

    try:
        api_instance.product_api_scan_configurations_destroy(id)
    except Exception as e:
        print("Exception when calling ProductApiScanConfigurationsApi->product_api_scan_configurations_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product_ap i_ scan_ configuration. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_api_scan_configurations_list**
> PaginatedProductAPIScanConfigurationList product_api_scan_configurations_list(id=id, limit=limit, offset=offset, prefetch=prefetch, product=product, service_key_1=service_key_1, service_key_2=service_key_2, service_key_3=service_key_3, tool_configuration=tool_configuration)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_product_api_scan_configuration_list import PaginatedProductAPIScanConfigurationList
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
    api_instance = defectdojo_api_generated.ProductApiScanConfigurationsApi(api_client)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    prefetch = ['prefetch_example'] # List[str] | List of fields for which to prefetch model instances and add those to the response (optional)
    product = 56 # int |  (optional)
    service_key_1 = 'service_key_1_example' # str |  (optional)
    service_key_2 = 'service_key_2_example' # str |  (optional)
    service_key_3 = 'service_key_3_example' # str |  (optional)
    tool_configuration = 56 # int |  (optional)

    try:
        api_response = api_instance.product_api_scan_configurations_list(id=id, limit=limit, offset=offset, prefetch=prefetch, product=product, service_key_1=service_key_1, service_key_2=service_key_2, service_key_3=service_key_3, tool_configuration=tool_configuration)
        print("The response of ProductApiScanConfigurationsApi->product_api_scan_configurations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApiScanConfigurationsApi->product_api_scan_configurations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **prefetch** | [**List[str]**](str.md)| List of fields for which to prefetch model instances and add those to the response | [optional] 
 **product** | **int**|  | [optional] 
 **service_key_1** | **str**|  | [optional] 
 **service_key_2** | **str**|  | [optional] 
 **service_key_3** | **str**|  | [optional] 
 **tool_configuration** | **int**|  | [optional] 

### Return type

[**PaginatedProductAPIScanConfigurationList**](PaginatedProductAPIScanConfigurationList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_api_scan_configurations_partial_update**
> ProductAPIScanConfiguration product_api_scan_configurations_partial_update(id, patched_product_api_scan_configuration_request=patched_product_api_scan_configuration_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.patched_product_api_scan_configuration_request import PatchedProductAPIScanConfigurationRequest
from defectdojo_api_generated.models.product_api_scan_configuration import ProductAPIScanConfiguration
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
    api_instance = defectdojo_api_generated.ProductApiScanConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this product_ap i_ scan_ configuration.
    patched_product_api_scan_configuration_request = defectdojo_api_generated.PatchedProductAPIScanConfigurationRequest() # PatchedProductAPIScanConfigurationRequest |  (optional)

    try:
        api_response = api_instance.product_api_scan_configurations_partial_update(id, patched_product_api_scan_configuration_request=patched_product_api_scan_configuration_request)
        print("The response of ProductApiScanConfigurationsApi->product_api_scan_configurations_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApiScanConfigurationsApi->product_api_scan_configurations_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product_ap i_ scan_ configuration. | 
 **patched_product_api_scan_configuration_request** | [**PatchedProductAPIScanConfigurationRequest**](PatchedProductAPIScanConfigurationRequest.md)|  | [optional] 

### Return type

[**ProductAPIScanConfiguration**](ProductAPIScanConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_api_scan_configurations_retrieve**
> ProductAPIScanConfiguration product_api_scan_configurations_retrieve(id, prefetch=prefetch)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.product_api_scan_configuration import ProductAPIScanConfiguration
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
    api_instance = defectdojo_api_generated.ProductApiScanConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this product_ap i_ scan_ configuration.
    prefetch = ['prefetch_example'] # List[str] | List of fields for which to prefetch model instances and add those to the response (optional)

    try:
        api_response = api_instance.product_api_scan_configurations_retrieve(id, prefetch=prefetch)
        print("The response of ProductApiScanConfigurationsApi->product_api_scan_configurations_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApiScanConfigurationsApi->product_api_scan_configurations_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product_ap i_ scan_ configuration. | 
 **prefetch** | [**List[str]**](str.md)| List of fields for which to prefetch model instances and add those to the response | [optional] 

### Return type

[**ProductAPIScanConfiguration**](ProductAPIScanConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_api_scan_configurations_update**
> ProductAPIScanConfiguration product_api_scan_configurations_update(id, product_api_scan_configuration_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.product_api_scan_configuration import ProductAPIScanConfiguration
from defectdojo_api_generated.models.product_api_scan_configuration_request import ProductAPIScanConfigurationRequest
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
    api_instance = defectdojo_api_generated.ProductApiScanConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this product_ap i_ scan_ configuration.
    product_api_scan_configuration_request = defectdojo_api_generated.ProductAPIScanConfigurationRequest() # ProductAPIScanConfigurationRequest | 

    try:
        api_response = api_instance.product_api_scan_configurations_update(id, product_api_scan_configuration_request)
        print("The response of ProductApiScanConfigurationsApi->product_api_scan_configurations_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApiScanConfigurationsApi->product_api_scan_configurations_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product_ap i_ scan_ configuration. | 
 **product_api_scan_configuration_request** | [**ProductAPIScanConfigurationRequest**](ProductAPIScanConfigurationRequest.md)|  | 

### Return type

[**ProductAPIScanConfiguration**](ProductAPIScanConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

