# defectdojo_api_generated.TestImportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_imports_create**](TestImportsApi.md#test_imports_create) | **POST** /api/v2/test_imports/ | 
[**test_imports_delete_preview_list**](TestImportsApi.md#test_imports_delete_preview_list) | **GET** /api/v2/test_imports/{id}/delete_preview/ | 
[**test_imports_destroy**](TestImportsApi.md#test_imports_destroy) | **DELETE** /api/v2/test_imports/{id}/ | 
[**test_imports_list**](TestImportsApi.md#test_imports_list) | **GET** /api/v2/test_imports/ | 
[**test_imports_partial_update**](TestImportsApi.md#test_imports_partial_update) | **PATCH** /api/v2/test_imports/{id}/ | 
[**test_imports_retrieve**](TestImportsApi.md#test_imports_retrieve) | **GET** /api/v2/test_imports/{id}/ | 
[**test_imports_update**](TestImportsApi.md#test_imports_update) | **PUT** /api/v2/test_imports/{id}/ | 


# **test_imports_create**
> TestImport test_imports_create(test_import_request=test_import_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.test_import import TestImport
from defectdojo_api_generated.models.test_import_request import TestImportRequest
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
    api_instance = defectdojo_api_generated.TestImportsApi(api_client)
    test_import_request = defectdojo_api_generated.TestImportRequest() # TestImportRequest |  (optional)

    try:
        api_response = api_instance.test_imports_create(test_import_request=test_import_request)
        print("The response of TestImportsApi->test_imports_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestImportsApi->test_imports_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_import_request** | [**TestImportRequest**](TestImportRequest.md)|  | [optional] 

### Return type

[**TestImport**](TestImport.md)

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

# **test_imports_delete_preview_list**
> PaginatedDeletePreviewList test_imports_delete_preview_list(id, limit=limit, offset=offset)

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
    api_instance = defectdojo_api_generated.TestImportsApi(api_client)
    id = 56 # int | A unique integer value identifying this test_ import.
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.test_imports_delete_preview_list(id, limit=limit, offset=offset)
        print("The response of TestImportsApi->test_imports_delete_preview_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestImportsApi->test_imports_delete_preview_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test_ import. | 
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

# **test_imports_destroy**
> test_imports_destroy(id)

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
    api_instance = defectdojo_api_generated.TestImportsApi(api_client)
    id = 56 # int | A unique integer value identifying this test_ import.

    try:
        api_instance.test_imports_destroy(id)
    except Exception as e:
        print("Exception when calling TestImportsApi->test_imports_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test_ import. | 

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

# **test_imports_list**
> PaginatedTestImportList test_imports_list(branch_tag=branch_tag, build_id=build_id, commit_hash=commit_hash, findings_affected=findings_affected, limit=limit, o=o, offset=offset, test=test, test_import_finding_action__action=test_import_finding_action__action, test_import_finding_action__created=test_import_finding_action__created, test_import_finding_action__finding=test_import_finding_action__finding, version=version)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_test_import_list import PaginatedTestImportList
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
    api_instance = defectdojo_api_generated.TestImportsApi(api_client)
    branch_tag = 'branch_tag_example' # str |  (optional)
    build_id = 'build_id_example' # str |  (optional)
    commit_hash = 'commit_hash_example' # str |  (optional)
    findings_affected = [56] # List[int] |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    o = ['o_example'] # List[str] | Ordering  * `id` - Id * `-id` - Id (descending) * `created` - Created * `-created` - Created (descending) * `modified` - Modified * `-modified` - Modified (descending) * `version` - Version * `-version` - Version (descending) * `branch_tag` - Branch tag * `-branch_tag` - Branch tag (descending) * `build_id` - Build id * `-build_id` - Build id (descending) * `commit_hash` - Commit hash * `-commit_hash` - Commit hash (descending) (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    test = 56 # int |  (optional)
    test_import_finding_action__action = 'test_import_finding_action__action_example' # str | * `N` - created * `C` - closed * `R` - reactivated * `U` - left untouched (optional)
    test_import_finding_action__created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    test_import_finding_action__finding = 56 # int |  (optional)
    version = 'version_example' # str |  (optional)

    try:
        api_response = api_instance.test_imports_list(branch_tag=branch_tag, build_id=build_id, commit_hash=commit_hash, findings_affected=findings_affected, limit=limit, o=o, offset=offset, test=test, test_import_finding_action__action=test_import_finding_action__action, test_import_finding_action__created=test_import_finding_action__created, test_import_finding_action__finding=test_import_finding_action__finding, version=version)
        print("The response of TestImportsApi->test_imports_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestImportsApi->test_imports_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch_tag** | **str**|  | [optional] 
 **build_id** | **str**|  | [optional] 
 **commit_hash** | **str**|  | [optional] 
 **findings_affected** | [**List[int]**](int.md)|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **o** | [**List[str]**](str.md)| Ordering  * &#x60;id&#x60; - Id * &#x60;-id&#x60; - Id (descending) * &#x60;created&#x60; - Created * &#x60;-created&#x60; - Created (descending) * &#x60;modified&#x60; - Modified * &#x60;-modified&#x60; - Modified (descending) * &#x60;version&#x60; - Version * &#x60;-version&#x60; - Version (descending) * &#x60;branch_tag&#x60; - Branch tag * &#x60;-branch_tag&#x60; - Branch tag (descending) * &#x60;build_id&#x60; - Build id * &#x60;-build_id&#x60; - Build id (descending) * &#x60;commit_hash&#x60; - Commit hash * &#x60;-commit_hash&#x60; - Commit hash (descending) | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **test** | **int**|  | [optional] 
 **test_import_finding_action__action** | **str**| * &#x60;N&#x60; - created * &#x60;C&#x60; - closed * &#x60;R&#x60; - reactivated * &#x60;U&#x60; - left untouched | [optional] 
 **test_import_finding_action__created** | **datetime**|  | [optional] 
 **test_import_finding_action__finding** | **int**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**PaginatedTestImportList**](PaginatedTestImportList.md)

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

# **test_imports_partial_update**
> TestImport test_imports_partial_update(id, patched_test_import_request=patched_test_import_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.patched_test_import_request import PatchedTestImportRequest
from defectdojo_api_generated.models.test_import import TestImport
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
    api_instance = defectdojo_api_generated.TestImportsApi(api_client)
    id = 56 # int | A unique integer value identifying this test_ import.
    patched_test_import_request = defectdojo_api_generated.PatchedTestImportRequest() # PatchedTestImportRequest |  (optional)

    try:
        api_response = api_instance.test_imports_partial_update(id, patched_test_import_request=patched_test_import_request)
        print("The response of TestImportsApi->test_imports_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestImportsApi->test_imports_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test_ import. | 
 **patched_test_import_request** | [**PatchedTestImportRequest**](PatchedTestImportRequest.md)|  | [optional] 

### Return type

[**TestImport**](TestImport.md)

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

# **test_imports_retrieve**
> TestImport test_imports_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.test_import import TestImport
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
    api_instance = defectdojo_api_generated.TestImportsApi(api_client)
    id = 56 # int | A unique integer value identifying this test_ import.

    try:
        api_response = api_instance.test_imports_retrieve(id)
        print("The response of TestImportsApi->test_imports_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestImportsApi->test_imports_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test_ import. | 

### Return type

[**TestImport**](TestImport.md)

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

# **test_imports_update**
> TestImport test_imports_update(id, test_import_request=test_import_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.test_import import TestImport
from defectdojo_api_generated.models.test_import_request import TestImportRequest
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
    api_instance = defectdojo_api_generated.TestImportsApi(api_client)
    id = 56 # int | A unique integer value identifying this test_ import.
    test_import_request = defectdojo_api_generated.TestImportRequest() # TestImportRequest |  (optional)

    try:
        api_response = api_instance.test_imports_update(id, test_import_request=test_import_request)
        print("The response of TestImportsApi->test_imports_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestImportsApi->test_imports_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test_ import. | 
 **test_import_request** | [**TestImportRequest**](TestImportRequest.md)|  | [optional] 

### Return type

[**TestImport**](TestImport.md)

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

