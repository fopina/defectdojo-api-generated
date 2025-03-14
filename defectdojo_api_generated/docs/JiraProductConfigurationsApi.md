# defectdojo_api_generated.JiraProductConfigurationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jira_product_configurations_create**](JiraProductConfigurationsApi.md#jira_product_configurations_create) | **POST** /api/v2/jira_product_configurations/ | 
[**jira_product_configurations_delete_preview_list**](JiraProductConfigurationsApi.md#jira_product_configurations_delete_preview_list) | **GET** /api/v2/jira_product_configurations/{id}/delete_preview/ | 
[**jira_product_configurations_destroy**](JiraProductConfigurationsApi.md#jira_product_configurations_destroy) | **DELETE** /api/v2/jira_product_configurations/{id}/ | 
[**jira_product_configurations_list**](JiraProductConfigurationsApi.md#jira_product_configurations_list) | **GET** /api/v2/jira_product_configurations/ | 
[**jira_product_configurations_partial_update**](JiraProductConfigurationsApi.md#jira_product_configurations_partial_update) | **PATCH** /api/v2/jira_product_configurations/{id}/ | 
[**jira_product_configurations_retrieve**](JiraProductConfigurationsApi.md#jira_product_configurations_retrieve) | **GET** /api/v2/jira_product_configurations/{id}/ | 
[**jira_product_configurations_update**](JiraProductConfigurationsApi.md#jira_product_configurations_update) | **PUT** /api/v2/jira_product_configurations/{id}/ | 


# **jira_product_configurations_create**
> JIRAProject jira_product_configurations_create(jira_project_request=jira_project_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.jira_project import JIRAProject
from defectdojo_api_generated.models.jira_project_request import JIRAProjectRequest
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
    api_instance = defectdojo_api_generated.JiraProductConfigurationsApi(api_client)
    jira_project_request = defectdojo_api_generated.JIRAProjectRequest() # JIRAProjectRequest |  (optional)

    try:
        api_response = api_instance.jira_product_configurations_create(jira_project_request=jira_project_request)
        print("The response of JiraProductConfigurationsApi->jira_product_configurations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jira_project_request** | [**JIRAProjectRequest**](JIRAProjectRequest.md)|  | [optional] 

### Return type

[**JIRAProject**](JIRAProject.md)

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

# **jira_product_configurations_delete_preview_list**
> PaginatedDeletePreviewList jira_product_configurations_delete_preview_list(id, limit=limit, offset=offset)

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
    api_instance = defectdojo_api_generated.JiraProductConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this jir a_ project.
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.jira_product_configurations_delete_preview_list(id, limit=limit, offset=offset)
        print("The response of JiraProductConfigurationsApi->jira_product_configurations_delete_preview_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_delete_preview_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ project. | 
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

# **jira_product_configurations_destroy**
> jira_product_configurations_destroy(id)

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
    api_instance = defectdojo_api_generated.JiraProductConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this jir a_ project.

    try:
        api_instance.jira_product_configurations_destroy(id)
    except Exception as e:
        print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ project. | 

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

# **jira_product_configurations_list**
> PaginatedJIRAProjectList jira_product_configurations_list(component=component, enable_engagement_epic_mapping=enable_engagement_epic_mapping, enabled=enabled, engagement=engagement, id=id, jira_instance=jira_instance, limit=limit, offset=offset, prefetch=prefetch, product=product, project_key=project_key, push_all_issues=push_all_issues, push_notes=push_notes)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_jira_project_list import PaginatedJIRAProjectList
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
    api_instance = defectdojo_api_generated.JiraProductConfigurationsApi(api_client)
    component = 'component_example' # str |  (optional)
    enable_engagement_epic_mapping = True # bool |  (optional)
    enabled = True # bool |  (optional)
    engagement = 56 # int |  (optional)
    id = 56 # int |  (optional)
    jira_instance = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    prefetch = ['prefetch_example'] # List[str] | List of fields for which to prefetch model instances and add those to the response (optional)
    product = 56 # int |  (optional)
    project_key = 'project_key_example' # str |  (optional)
    push_all_issues = True # bool |  (optional)
    push_notes = True # bool |  (optional)

    try:
        api_response = api_instance.jira_product_configurations_list(component=component, enable_engagement_epic_mapping=enable_engagement_epic_mapping, enabled=enabled, engagement=engagement, id=id, jira_instance=jira_instance, limit=limit, offset=offset, prefetch=prefetch, product=product, project_key=project_key, push_all_issues=push_all_issues, push_notes=push_notes)
        print("The response of JiraProductConfigurationsApi->jira_product_configurations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component** | **str**|  | [optional] 
 **enable_engagement_epic_mapping** | **bool**|  | [optional] 
 **enabled** | **bool**|  | [optional] 
 **engagement** | **int**|  | [optional] 
 **id** | **int**|  | [optional] 
 **jira_instance** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **prefetch** | [**List[str]**](str.md)| List of fields for which to prefetch model instances and add those to the response | [optional] 
 **product** | **int**|  | [optional] 
 **project_key** | **str**|  | [optional] 
 **push_all_issues** | **bool**|  | [optional] 
 **push_notes** | **bool**|  | [optional] 

### Return type

[**PaginatedJIRAProjectList**](PaginatedJIRAProjectList.md)

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

# **jira_product_configurations_partial_update**
> JIRAProject jira_product_configurations_partial_update(id, patched_jira_project_request=patched_jira_project_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.jira_project import JIRAProject
from defectdojo_api_generated.models.patched_jira_project_request import PatchedJIRAProjectRequest
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
    api_instance = defectdojo_api_generated.JiraProductConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this jir a_ project.
    patched_jira_project_request = defectdojo_api_generated.PatchedJIRAProjectRequest() # PatchedJIRAProjectRequest |  (optional)

    try:
        api_response = api_instance.jira_product_configurations_partial_update(id, patched_jira_project_request=patched_jira_project_request)
        print("The response of JiraProductConfigurationsApi->jira_product_configurations_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ project. | 
 **patched_jira_project_request** | [**PatchedJIRAProjectRequest**](PatchedJIRAProjectRequest.md)|  | [optional] 

### Return type

[**JIRAProject**](JIRAProject.md)

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

# **jira_product_configurations_retrieve**
> JIRAProject jira_product_configurations_retrieve(id, prefetch=prefetch)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.jira_project import JIRAProject
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
    api_instance = defectdojo_api_generated.JiraProductConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this jir a_ project.
    prefetch = ['prefetch_example'] # List[str] | List of fields for which to prefetch model instances and add those to the response (optional)

    try:
        api_response = api_instance.jira_product_configurations_retrieve(id, prefetch=prefetch)
        print("The response of JiraProductConfigurationsApi->jira_product_configurations_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ project. | 
 **prefetch** | [**List[str]**](str.md)| List of fields for which to prefetch model instances and add those to the response | [optional] 

### Return type

[**JIRAProject**](JIRAProject.md)

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

# **jira_product_configurations_update**
> JIRAProject jira_product_configurations_update(id, jira_project_request=jira_project_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.jira_project import JIRAProject
from defectdojo_api_generated.models.jira_project_request import JIRAProjectRequest
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
    api_instance = defectdojo_api_generated.JiraProductConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this jir a_ project.
    jira_project_request = defectdojo_api_generated.JIRAProjectRequest() # JIRAProjectRequest |  (optional)

    try:
        api_response = api_instance.jira_product_configurations_update(id, jira_project_request=jira_project_request)
        print("The response of JiraProductConfigurationsApi->jira_product_configurations_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ project. | 
 **jira_project_request** | [**JIRAProjectRequest**](JIRAProjectRequest.md)|  | [optional] 

### Return type

[**JIRAProject**](JIRAProject.md)

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

