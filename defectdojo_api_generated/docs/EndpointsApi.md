# defectdojo_api_generated.EndpointsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoints_create**](EndpointsApi.md#endpoints_create) | **POST** /api/v2/endpoints/ | 
[**endpoints_delete_preview_list**](EndpointsApi.md#endpoints_delete_preview_list) | **GET** /api/v2/endpoints/{id}/delete_preview/ | 
[**endpoints_destroy**](EndpointsApi.md#endpoints_destroy) | **DELETE** /api/v2/endpoints/{id}/ | 
[**endpoints_generate_report_create**](EndpointsApi.md#endpoints_generate_report_create) | **POST** /api/v2/endpoints/{id}/generate_report/ | 
[**endpoints_list**](EndpointsApi.md#endpoints_list) | **GET** /api/v2/endpoints/ | 
[**endpoints_partial_update**](EndpointsApi.md#endpoints_partial_update) | **PATCH** /api/v2/endpoints/{id}/ | 
[**endpoints_retrieve**](EndpointsApi.md#endpoints_retrieve) | **GET** /api/v2/endpoints/{id}/ | 
[**endpoints_update**](EndpointsApi.md#endpoints_update) | **PUT** /api/v2/endpoints/{id}/ | 


# **endpoints_create**
> Endpoint endpoints_create(endpoint_request=endpoint_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.endpoint import Endpoint
from defectdojo_api_generated.models.endpoint_request import EndpointRequest
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
    api_instance = defectdojo_api_generated.EndpointsApi(api_client)
    endpoint_request = defectdojo_api_generated.EndpointRequest() # EndpointRequest |  (optional)

    try:
        api_response = api_instance.endpoints_create(endpoint_request=endpoint_request)
        print("The response of EndpointsApi->endpoints_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_request** | [**EndpointRequest**](EndpointRequest.md)|  | [optional] 

### Return type

[**Endpoint**](Endpoint.md)

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

# **endpoints_delete_preview_list**
> PaginatedDeletePreviewList endpoints_delete_preview_list(id, limit=limit, offset=offset)

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
    api_instance = defectdojo_api_generated.EndpointsApi(api_client)
    id = 56 # int | A unique integer value identifying this endpoint.
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.endpoints_delete_preview_list(id, limit=limit, offset=offset)
        print("The response of EndpointsApi->endpoints_delete_preview_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_delete_preview_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this endpoint. | 
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

# **endpoints_destroy**
> endpoints_destroy(id)

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
    api_instance = defectdojo_api_generated.EndpointsApi(api_client)
    id = 56 # int | A unique integer value identifying this endpoint.

    try:
        api_instance.endpoints_destroy(id)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this endpoint. | 

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

# **endpoints_generate_report_create**
> ReportGenerate endpoints_generate_report_create(id, report_generate_option_request=report_generate_option_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.report_generate import ReportGenerate
from defectdojo_api_generated.models.report_generate_option_request import ReportGenerateOptionRequest
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
    api_instance = defectdojo_api_generated.EndpointsApi(api_client)
    id = 56 # int | A unique integer value identifying this endpoint.
    report_generate_option_request = defectdojo_api_generated.ReportGenerateOptionRequest() # ReportGenerateOptionRequest |  (optional)

    try:
        api_response = api_instance.endpoints_generate_report_create(id, report_generate_option_request=report_generate_option_request)
        print("The response of EndpointsApi->endpoints_generate_report_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_generate_report_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this endpoint. | 
 **report_generate_option_request** | [**ReportGenerateOptionRequest**](ReportGenerateOptionRequest.md)|  | [optional] 

### Return type

[**ReportGenerate**](ReportGenerate.md)

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

# **endpoints_list**
> PaginatedEndpointList endpoints_list(fragment=fragment, has_tags=has_tags, host=host, id=id, limit=limit, not_tag=not_tag, not_tags=not_tags, o=o, offset=offset, path=path, port=port, product=product, protocol=protocol, query=query, tag=tag, tags=tags, tags__and=tags__and, userinfo=userinfo)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_endpoint_list import PaginatedEndpointList
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
    api_instance = defectdojo_api_generated.EndpointsApi(api_client)
    fragment = 'fragment_example' # str |  (optional)
    has_tags = True # bool | Has tags (optional)
    host = 'host_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    not_tag = 'not_tag_example' # str | Not Tag name contains (optional)
    not_tags = ['not_tags_example'] # List[str] | Comma separated list of exact tags not present on model (optional)
    o = ['o_example'] # List[str] | Ordering  * `host` - Host * `-host` - Host (descending) * `product` - Product * `-product` - Product (descending) * `id` - Id * `-id` - Id (descending) (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    path = 'path_example' # str |  (optional)
    port = 56 # int |  (optional)
    product = 56 # int |  (optional)
    protocol = 'protocol_example' # str |  (optional)
    query = 'query_example' # str |  (optional)
    tag = 'tag_example' # str | Tag name contains (optional)
    tags = ['tags_example'] # List[str] | Comma separated list of exact tags (uses OR for multiple values) (optional)
    tags__and = ['tags__and_example'] # List[str] | Comma separated list of exact tags to match with an AND expression (optional)
    userinfo = 'userinfo_example' # str |  (optional)

    try:
        api_response = api_instance.endpoints_list(fragment=fragment, has_tags=has_tags, host=host, id=id, limit=limit, not_tag=not_tag, not_tags=not_tags, o=o, offset=offset, path=path, port=port, product=product, protocol=protocol, query=query, tag=tag, tags=tags, tags__and=tags__and, userinfo=userinfo)
        print("The response of EndpointsApi->endpoints_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fragment** | **str**|  | [optional] 
 **has_tags** | **bool**| Has tags | [optional] 
 **host** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **not_tag** | **str**| Not Tag name contains | [optional] 
 **not_tags** | [**List[str]**](str.md)| Comma separated list of exact tags not present on model | [optional] 
 **o** | [**List[str]**](str.md)| Ordering  * &#x60;host&#x60; - Host * &#x60;-host&#x60; - Host (descending) * &#x60;product&#x60; - Product * &#x60;-product&#x60; - Product (descending) * &#x60;id&#x60; - Id * &#x60;-id&#x60; - Id (descending) | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **path** | **str**|  | [optional] 
 **port** | **int**|  | [optional] 
 **product** | **int**|  | [optional] 
 **protocol** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 
 **tag** | **str**| Tag name contains | [optional] 
 **tags** | [**List[str]**](str.md)| Comma separated list of exact tags (uses OR for multiple values) | [optional] 
 **tags__and** | [**List[str]**](str.md)| Comma separated list of exact tags to match with an AND expression | [optional] 
 **userinfo** | **str**|  | [optional] 

### Return type

[**PaginatedEndpointList**](PaginatedEndpointList.md)

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

# **endpoints_partial_update**
> Endpoint endpoints_partial_update(id, patched_endpoint_request=patched_endpoint_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.endpoint import Endpoint
from defectdojo_api_generated.models.patched_endpoint_request import PatchedEndpointRequest
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
    api_instance = defectdojo_api_generated.EndpointsApi(api_client)
    id = 56 # int | A unique integer value identifying this endpoint.
    patched_endpoint_request = defectdojo_api_generated.PatchedEndpointRequest() # PatchedEndpointRequest |  (optional)

    try:
        api_response = api_instance.endpoints_partial_update(id, patched_endpoint_request=patched_endpoint_request)
        print("The response of EndpointsApi->endpoints_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this endpoint. | 
 **patched_endpoint_request** | [**PatchedEndpointRequest**](PatchedEndpointRequest.md)|  | [optional] 

### Return type

[**Endpoint**](Endpoint.md)

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

# **endpoints_retrieve**
> Endpoint endpoints_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.endpoint import Endpoint
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
    api_instance = defectdojo_api_generated.EndpointsApi(api_client)
    id = 56 # int | A unique integer value identifying this endpoint.

    try:
        api_response = api_instance.endpoints_retrieve(id)
        print("The response of EndpointsApi->endpoints_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this endpoint. | 

### Return type

[**Endpoint**](Endpoint.md)

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

# **endpoints_update**
> Endpoint endpoints_update(id, endpoint_request=endpoint_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.endpoint import Endpoint
from defectdojo_api_generated.models.endpoint_request import EndpointRequest
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
    api_instance = defectdojo_api_generated.EndpointsApi(api_client)
    id = 56 # int | A unique integer value identifying this endpoint.
    endpoint_request = defectdojo_api_generated.EndpointRequest() # EndpointRequest |  (optional)

    try:
        api_response = api_instance.endpoints_update(id, endpoint_request=endpoint_request)
        print("The response of EndpointsApi->endpoints_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this endpoint. | 
 **endpoint_request** | [**EndpointRequest**](EndpointRequest.md)|  | [optional] 

### Return type

[**Endpoint**](Endpoint.md)

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

