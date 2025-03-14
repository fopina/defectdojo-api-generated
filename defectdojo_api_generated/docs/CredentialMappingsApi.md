# defectdojo_api_generated.CredentialMappingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credential_mappings_create**](CredentialMappingsApi.md#credential_mappings_create) | **POST** /api/v2/credential_mappings/ | 
[**credential_mappings_delete_preview_list**](CredentialMappingsApi.md#credential_mappings_delete_preview_list) | **GET** /api/v2/credential_mappings/{id}/delete_preview/ | 
[**credential_mappings_destroy**](CredentialMappingsApi.md#credential_mappings_destroy) | **DELETE** /api/v2/credential_mappings/{id}/ | 
[**credential_mappings_list**](CredentialMappingsApi.md#credential_mappings_list) | **GET** /api/v2/credential_mappings/ | 
[**credential_mappings_partial_update**](CredentialMappingsApi.md#credential_mappings_partial_update) | **PATCH** /api/v2/credential_mappings/{id}/ | 
[**credential_mappings_retrieve**](CredentialMappingsApi.md#credential_mappings_retrieve) | **GET** /api/v2/credential_mappings/{id}/ | 
[**credential_mappings_update**](CredentialMappingsApi.md#credential_mappings_update) | **PUT** /api/v2/credential_mappings/{id}/ | 


# **credential_mappings_create**
> CredentialMapping credential_mappings_create(credential_mapping_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.credential_mapping import CredentialMapping
from defectdojo_api_generated.models.credential_mapping_request import CredentialMappingRequest
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
    api_instance = defectdojo_api_generated.CredentialMappingsApi(api_client)
    credential_mapping_request = defectdojo_api_generated.CredentialMappingRequest() # CredentialMappingRequest | 

    try:
        api_response = api_instance.credential_mappings_create(credential_mapping_request)
        print("The response of CredentialMappingsApi->credential_mappings_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialMappingsApi->credential_mappings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_mapping_request** | [**CredentialMappingRequest**](CredentialMappingRequest.md)|  | 

### Return type

[**CredentialMapping**](CredentialMapping.md)

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

# **credential_mappings_delete_preview_list**
> PaginatedDeletePreviewList credential_mappings_delete_preview_list(id, limit=limit, offset=offset)

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
    api_instance = defectdojo_api_generated.CredentialMappingsApi(api_client)
    id = 56 # int | A unique integer value identifying this cred_ mapping.
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.credential_mappings_delete_preview_list(id, limit=limit, offset=offset)
        print("The response of CredentialMappingsApi->credential_mappings_delete_preview_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialMappingsApi->credential_mappings_delete_preview_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cred_ mapping. | 
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

# **credential_mappings_destroy**
> credential_mappings_destroy(id)

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
    api_instance = defectdojo_api_generated.CredentialMappingsApi(api_client)
    id = 56 # int | A unique integer value identifying this cred_ mapping.

    try:
        api_instance.credential_mappings_destroy(id)
    except Exception as e:
        print("Exception when calling CredentialMappingsApi->credential_mappings_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cred_ mapping. | 

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

# **credential_mappings_list**
> PaginatedCredentialMappingList credential_mappings_list(cred_id=cred_id, engagement=engagement, finding=finding, is_authn_provider=is_authn_provider, limit=limit, offset=offset, product=product, test=test, url=url)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_credential_mapping_list import PaginatedCredentialMappingList
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
    api_instance = defectdojo_api_generated.CredentialMappingsApi(api_client)
    cred_id = 56 # int |  (optional)
    engagement = 56 # int |  (optional)
    finding = 56 # int |  (optional)
    is_authn_provider = True # bool |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    product = 56 # int |  (optional)
    test = 56 # int |  (optional)
    url = 'url_example' # str |  (optional)

    try:
        api_response = api_instance.credential_mappings_list(cred_id=cred_id, engagement=engagement, finding=finding, is_authn_provider=is_authn_provider, limit=limit, offset=offset, product=product, test=test, url=url)
        print("The response of CredentialMappingsApi->credential_mappings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialMappingsApi->credential_mappings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_id** | **int**|  | [optional] 
 **engagement** | **int**|  | [optional] 
 **finding** | **int**|  | [optional] 
 **is_authn_provider** | **bool**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **product** | **int**|  | [optional] 
 **test** | **int**|  | [optional] 
 **url** | **str**|  | [optional] 

### Return type

[**PaginatedCredentialMappingList**](PaginatedCredentialMappingList.md)

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

# **credential_mappings_partial_update**
> CredentialMapping credential_mappings_partial_update(id, patched_credential_mapping_request=patched_credential_mapping_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.credential_mapping import CredentialMapping
from defectdojo_api_generated.models.patched_credential_mapping_request import PatchedCredentialMappingRequest
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
    api_instance = defectdojo_api_generated.CredentialMappingsApi(api_client)
    id = 56 # int | A unique integer value identifying this cred_ mapping.
    patched_credential_mapping_request = defectdojo_api_generated.PatchedCredentialMappingRequest() # PatchedCredentialMappingRequest |  (optional)

    try:
        api_response = api_instance.credential_mappings_partial_update(id, patched_credential_mapping_request=patched_credential_mapping_request)
        print("The response of CredentialMappingsApi->credential_mappings_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialMappingsApi->credential_mappings_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cred_ mapping. | 
 **patched_credential_mapping_request** | [**PatchedCredentialMappingRequest**](PatchedCredentialMappingRequest.md)|  | [optional] 

### Return type

[**CredentialMapping**](CredentialMapping.md)

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

# **credential_mappings_retrieve**
> CredentialMapping credential_mappings_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.credential_mapping import CredentialMapping
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
    api_instance = defectdojo_api_generated.CredentialMappingsApi(api_client)
    id = 56 # int | A unique integer value identifying this cred_ mapping.

    try:
        api_response = api_instance.credential_mappings_retrieve(id)
        print("The response of CredentialMappingsApi->credential_mappings_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialMappingsApi->credential_mappings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cred_ mapping. | 

### Return type

[**CredentialMapping**](CredentialMapping.md)

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

# **credential_mappings_update**
> CredentialMapping credential_mappings_update(id, credential_mapping_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.credential_mapping import CredentialMapping
from defectdojo_api_generated.models.credential_mapping_request import CredentialMappingRequest
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
    api_instance = defectdojo_api_generated.CredentialMappingsApi(api_client)
    id = 56 # int | A unique integer value identifying this cred_ mapping.
    credential_mapping_request = defectdojo_api_generated.CredentialMappingRequest() # CredentialMappingRequest | 

    try:
        api_response = api_instance.credential_mappings_update(id, credential_mapping_request)
        print("The response of CredentialMappingsApi->credential_mappings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialMappingsApi->credential_mappings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cred_ mapping. | 
 **credential_mapping_request** | [**CredentialMappingRequest**](CredentialMappingRequest.md)|  | 

### Return type

[**CredentialMapping**](CredentialMapping.md)

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

