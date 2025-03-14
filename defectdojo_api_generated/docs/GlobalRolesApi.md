# defectdojo_api_generated.GlobalRolesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**global_roles_create**](GlobalRolesApi.md#global_roles_create) | **POST** /api/v2/global_roles/ | 
[**global_roles_delete_preview_list**](GlobalRolesApi.md#global_roles_delete_preview_list) | **GET** /api/v2/global_roles/{id}/delete_preview/ | 
[**global_roles_destroy**](GlobalRolesApi.md#global_roles_destroy) | **DELETE** /api/v2/global_roles/{id}/ | 
[**global_roles_list**](GlobalRolesApi.md#global_roles_list) | **GET** /api/v2/global_roles/ | 
[**global_roles_partial_update**](GlobalRolesApi.md#global_roles_partial_update) | **PATCH** /api/v2/global_roles/{id}/ | 
[**global_roles_retrieve**](GlobalRolesApi.md#global_roles_retrieve) | **GET** /api/v2/global_roles/{id}/ | 
[**global_roles_update**](GlobalRolesApi.md#global_roles_update) | **PUT** /api/v2/global_roles/{id}/ | 


# **global_roles_create**
> GlobalRole global_roles_create(global_role_request=global_role_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.global_role import GlobalRole
from defectdojo_api_generated.models.global_role_request import GlobalRoleRequest
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
    api_instance = defectdojo_api_generated.GlobalRolesApi(api_client)
    global_role_request = defectdojo_api_generated.GlobalRoleRequest() # GlobalRoleRequest |  (optional)

    try:
        api_response = api_instance.global_roles_create(global_role_request=global_role_request)
        print("The response of GlobalRolesApi->global_roles_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalRolesApi->global_roles_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_role_request** | [**GlobalRoleRequest**](GlobalRoleRequest.md)|  | [optional] 

### Return type

[**GlobalRole**](GlobalRole.md)

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

# **global_roles_delete_preview_list**
> PaginatedDeletePreviewList global_roles_delete_preview_list(id, limit=limit, offset=offset)

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
    api_instance = defectdojo_api_generated.GlobalRolesApi(api_client)
    id = 56 # int | A unique integer value identifying this global_ role.
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.global_roles_delete_preview_list(id, limit=limit, offset=offset)
        print("The response of GlobalRolesApi->global_roles_delete_preview_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalRolesApi->global_roles_delete_preview_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this global_ role. | 
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

# **global_roles_destroy**
> global_roles_destroy(id)

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
    api_instance = defectdojo_api_generated.GlobalRolesApi(api_client)
    id = 56 # int | A unique integer value identifying this global_ role.

    try:
        api_instance.global_roles_destroy(id)
    except Exception as e:
        print("Exception when calling GlobalRolesApi->global_roles_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this global_ role. | 

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

# **global_roles_list**
> PaginatedGlobalRoleList global_roles_list(group=group, id=id, limit=limit, offset=offset, prefetch=prefetch, role=role, user=user)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_global_role_list import PaginatedGlobalRoleList
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
    api_instance = defectdojo_api_generated.GlobalRolesApi(api_client)
    group = 56 # int |  (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    prefetch = ['prefetch_example'] # List[str] | List of fields for which to prefetch model instances and add those to the response (optional)
    role = 56 # int |  (optional)
    user = 56 # int |  (optional)

    try:
        api_response = api_instance.global_roles_list(group=group, id=id, limit=limit, offset=offset, prefetch=prefetch, role=role, user=user)
        print("The response of GlobalRolesApi->global_roles_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalRolesApi->global_roles_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **int**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **prefetch** | [**List[str]**](str.md)| List of fields for which to prefetch model instances and add those to the response | [optional] 
 **role** | **int**|  | [optional] 
 **user** | **int**|  | [optional] 

### Return type

[**PaginatedGlobalRoleList**](PaginatedGlobalRoleList.md)

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

# **global_roles_partial_update**
> GlobalRole global_roles_partial_update(id, patched_global_role_request=patched_global_role_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.global_role import GlobalRole
from defectdojo_api_generated.models.patched_global_role_request import PatchedGlobalRoleRequest
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
    api_instance = defectdojo_api_generated.GlobalRolesApi(api_client)
    id = 56 # int | A unique integer value identifying this global_ role.
    patched_global_role_request = defectdojo_api_generated.PatchedGlobalRoleRequest() # PatchedGlobalRoleRequest |  (optional)

    try:
        api_response = api_instance.global_roles_partial_update(id, patched_global_role_request=patched_global_role_request)
        print("The response of GlobalRolesApi->global_roles_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalRolesApi->global_roles_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this global_ role. | 
 **patched_global_role_request** | [**PatchedGlobalRoleRequest**](PatchedGlobalRoleRequest.md)|  | [optional] 

### Return type

[**GlobalRole**](GlobalRole.md)

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

# **global_roles_retrieve**
> GlobalRole global_roles_retrieve(id, prefetch=prefetch)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.global_role import GlobalRole
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
    api_instance = defectdojo_api_generated.GlobalRolesApi(api_client)
    id = 56 # int | A unique integer value identifying this global_ role.
    prefetch = ['prefetch_example'] # List[str] | List of fields for which to prefetch model instances and add those to the response (optional)

    try:
        api_response = api_instance.global_roles_retrieve(id, prefetch=prefetch)
        print("The response of GlobalRolesApi->global_roles_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalRolesApi->global_roles_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this global_ role. | 
 **prefetch** | [**List[str]**](str.md)| List of fields for which to prefetch model instances and add those to the response | [optional] 

### Return type

[**GlobalRole**](GlobalRole.md)

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

# **global_roles_update**
> GlobalRole global_roles_update(id, global_role_request=global_role_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.global_role import GlobalRole
from defectdojo_api_generated.models.global_role_request import GlobalRoleRequest
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
    api_instance = defectdojo_api_generated.GlobalRolesApi(api_client)
    id = 56 # int | A unique integer value identifying this global_ role.
    global_role_request = defectdojo_api_generated.GlobalRoleRequest() # GlobalRoleRequest |  (optional)

    try:
        api_response = api_instance.global_roles_update(id, global_role_request=global_role_request)
        print("The response of GlobalRolesApi->global_roles_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalRolesApi->global_roles_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this global_ role. | 
 **global_role_request** | [**GlobalRoleRequest**](GlobalRoleRequest.md)|  | [optional] 

### Return type

[**GlobalRole**](GlobalRole.md)

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

