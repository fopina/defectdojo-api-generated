# defectdojo_api_generated.TestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_risks_create**](TestsApi.md#accept_risks_create) | **POST** /api/v2/tests/{id}/accept_risks/ | 
[**create**](TestsApi.md#create) | **POST** /api/v2/tests/ | 
[**delete_preview_list**](TestsApi.md#delete_preview_list) | **GET** /api/v2/tests/{id}/delete_preview/ | 
[**destroy**](TestsApi.md#destroy) | **DELETE** /api/v2/tests/{id}/ | 
[**files_create**](TestsApi.md#files_create) | **POST** /api/v2/tests/{id}/files/ | 
[**files_download_retrieve**](TestsApi.md#files_download_retrieve) | **GET** /api/v2/tests/{id}/files/download/{file_id}/ | 
[**files_retrieve**](TestsApi.md#files_retrieve) | **GET** /api/v2/tests/{id}/files/ | 
[**generate_report_create**](TestsApi.md#generate_report_create) | **POST** /api/v2/tests/{id}/generate_report/ | 
[**list**](TestsApi.md#list) | **GET** /api/v2/tests/ | 
[**notes_create**](TestsApi.md#notes_create) | **POST** /api/v2/tests/{id}/notes/ | 
[**notes_retrieve**](TestsApi.md#notes_retrieve) | **GET** /api/v2/tests/{id}/notes/ | 
[**partial_update**](TestsApi.md#partial_update) | **PATCH** /api/v2/tests/{id}/ | 
[**retrieve**](TestsApi.md#retrieve) | **GET** /api/v2/tests/{id}/ | 
[**update**](TestsApi.md#update) | **PUT** /api/v2/tests/{id}/ | 


# **accept_risks_create**
> List[RiskAcceptance] accept_risks_create(id, accepted_risk_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.accepted_risk_request import AcceptedRiskRequest
from defectdojo_api_generated.models.risk_acceptance import RiskAcceptance
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
    api_instance = defectdojo_api_generated.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
    accepted_risk_request = [defectdojo_api_generated.AcceptedRiskRequest()] # List[AcceptedRiskRequest] | 

    try:
        api_response = api_instance.accept_risks_create(id, accepted_risk_request)
        print("The response of TestsApi->accept_risks_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestsApi->accept_risks_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
 **accepted_risk_request** | [**List[AcceptedRiskRequest]**](AcceptedRiskRequest.md)|  | 

### Return type

[**List[RiskAcceptance]**](RiskAcceptance.md)

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

# **create**
> TestCreate create(test_create_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.test_create import TestCreate
from defectdojo_api_generated.models.test_create_request import TestCreateRequest
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
    api_instance = defectdojo_api_generated.TestsApi(api_client)
    test_create_request = defectdojo_api_generated.TestCreateRequest() # TestCreateRequest | 

    try:
        api_response = api_instance.create(test_create_request)
        print("The response of TestsApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestsApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_create_request** | [**TestCreateRequest**](TestCreateRequest.md)|  | 

### Return type

[**TestCreate**](TestCreate.md)

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

# **delete_preview_list**
> PaginatedDeletePreviewList delete_preview_list(id, limit=limit, offset=offset)

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
    api_instance = defectdojo_api_generated.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.delete_preview_list(id, limit=limit, offset=offset)
        print("The response of TestsApi->delete_preview_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestsApi->delete_preview_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
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

# **destroy**
> destroy(id)

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
    api_instance = defectdojo_api_generated.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.

    try:
        api_instance.destroy(id)
    except Exception as e:
        print("Exception when calling TestsApi->destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 

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

# **files_create**
> File files_create(id, title=title, file=file)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.file import File
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
    api_instance = defectdojo_api_generated.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
    title = 'title_example' # str |  (optional)
    file = None # bytearray |  (optional)

    try:
        api_response = api_instance.files_create(id, title=title, file=file)
        print("The response of TestsApi->files_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestsApi->files_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
 **title** | **str**|  | [optional] 
 **file** | **bytearray**|  | [optional] 

### Return type

[**File**](File.md)

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

# **files_download_retrieve**
> RawFile files_download_retrieve(file_id, id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.raw_file import RawFile
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
    api_instance = defectdojo_api_generated.TestsApi(api_client)
    file_id = 'file_id_example' # str | 
    id = 56 # int | A unique integer value identifying this test.

    try:
        api_response = api_instance.files_download_retrieve(file_id, id)
        print("The response of TestsApi->files_download_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestsApi->files_download_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **id** | **int**| A unique integer value identifying this test. | 

### Return type

[**RawFile**](RawFile.md)

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

# **files_retrieve**
> TestToFiles files_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.test_to_files import TestToFiles
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
    api_instance = defectdojo_api_generated.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.

    try:
        api_response = api_instance.files_retrieve(id)
        print("The response of TestsApi->files_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestsApi->files_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 

### Return type

[**TestToFiles**](TestToFiles.md)

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

# **generate_report_create**
> ReportGenerate generate_report_create(id, report_generate_option_request=report_generate_option_request)

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
    api_instance = defectdojo_api_generated.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
    report_generate_option_request = defectdojo_api_generated.ReportGenerateOptionRequest() # ReportGenerateOptionRequest |  (optional)

    try:
        api_response = api_instance.generate_report_create(id, report_generate_option_request=report_generate_option_request)
        print("The response of TestsApi->generate_report_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestsApi->generate_report_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
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

# **list**
> PaginatedTestList list(api_scan_configuration=api_scan_configuration, branch_tag=branch_tag, build_id=build_id, commit_hash=commit_hash, engagement=engagement, engagement__product__tags=engagement__product__tags, engagement__product__tags__and=engagement__product__tags__and, engagement__tags=engagement__tags, engagement__tags__and=engagement__tags__and, has_tags=has_tags, id=id, limit=limit, not_engagement__product__tags=not_engagement__product__tags, not_engagement__tags=not_engagement__tags, not_tag=not_tag, not_tags=not_tags, notes=notes, o=o, offset=offset, percent_complete=percent_complete, scan_type=scan_type, tag=tag, tags=tags, tags__and=tags__and, target_end=target_end, target_start=target_start, test_type=test_type, title=title, version=version)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_test_list import PaginatedTestList
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
    api_instance = defectdojo_api_generated.TestsApi(api_client)
    api_scan_configuration = 56 # int |  (optional)
    branch_tag = 'branch_tag_example' # str |  (optional)
    build_id = 'build_id_example' # str |  (optional)
    commit_hash = 'commit_hash_example' # str |  (optional)
    engagement = 56 # int |  (optional)
    engagement__product__tags = ['engagement__product__tags_example'] # List[str] | Comma separated list of exact tags present on Product (uses OR for multiple values) (optional)
    engagement__product__tags__and = ['engagement__product__tags__and_example'] # List[str] | Comma separated list of exact tags to match with an AND expression present on Product (optional)
    engagement__tags = ['engagement__tags_example'] # List[str] | Comma separated list of exact tags present on engagement (uses OR for multiple values) (optional)
    engagement__tags__and = ['engagement__tags__and_example'] # List[str] | Comma separated list of exact tags to match with an AND expression present on engagement (optional)
    has_tags = True # bool | Has tags (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    not_engagement__product__tags = ['not_engagement__product__tags_example'] # List[str] | Comma separated list of exact tags not present on Product (optional)
    not_engagement__tags = ['not_engagement__tags_example'] # List[str] | Comma separated list of exact tags not present on engagement (optional)
    not_tag = 'not_tag_example' # str | Not Tag name contains (optional)
    not_tags = ['not_tags_example'] # List[str] | Comma separated list of exact tags not present on model (optional)
    notes = [56] # List[int] |  (optional)
    o = ['o_example'] # List[str] | Ordering  * `title` - Title * `-title` - Title (descending) * `version` - Version * `-version` - Version (descending) * `target_start` - Target start * `-target_start` - Target start (descending) * `target_end` - Target end * `-target_end` - Target end (descending) * `test_type` - Test type * `-test_type` - Test type (descending) * `lead` - Lead * `-lead` - Lead (descending) * `branch_tag` - Branch tag * `-branch_tag` - Branch tag (descending) * `build_id` - Build id * `-build_id` - Build id (descending) * `commit_hash` - Commit hash * `-commit_hash` - Commit hash (descending) * `api_scan_configuration` - Api scan configuration * `-api_scan_configuration` - Api scan configuration (descending) * `engagement` - Engagement * `-engagement` - Engagement (descending) * `created` - Created * `-created` - Created (descending) * `updated` - Updated * `-updated` - Updated (descending) (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    percent_complete = 56 # int |  (optional)
    scan_type = 'scan_type_example' # str |  (optional)
    tag = 'tag_example' # str | Tag name contains (optional)
    tags = ['tags_example'] # List[str] | Comma separated list of exact tags (uses OR for multiple values) (optional)
    tags__and = ['tags__and_example'] # List[str] | Comma separated list of exact tags to match with an AND expression (optional)
    target_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    target_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    test_type = 56 # int |  (optional)
    title = 'title_example' # str |  (optional)
    version = 'version_example' # str |  (optional)

    try:
        api_response = api_instance.list(api_scan_configuration=api_scan_configuration, branch_tag=branch_tag, build_id=build_id, commit_hash=commit_hash, engagement=engagement, engagement__product__tags=engagement__product__tags, engagement__product__tags__and=engagement__product__tags__and, engagement__tags=engagement__tags, engagement__tags__and=engagement__tags__and, has_tags=has_tags, id=id, limit=limit, not_engagement__product__tags=not_engagement__product__tags, not_engagement__tags=not_engagement__tags, not_tag=not_tag, not_tags=not_tags, notes=notes, o=o, offset=offset, percent_complete=percent_complete, scan_type=scan_type, tag=tag, tags=tags, tags__and=tags__and, target_end=target_end, target_start=target_start, test_type=test_type, title=title, version=version)
        print("The response of TestsApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestsApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_scan_configuration** | **int**|  | [optional] 
 **branch_tag** | **str**|  | [optional] 
 **build_id** | **str**|  | [optional] 
 **commit_hash** | **str**|  | [optional] 
 **engagement** | **int**|  | [optional] 
 **engagement__product__tags** | [**List[str]**](str.md)| Comma separated list of exact tags present on Product (uses OR for multiple values) | [optional] 
 **engagement__product__tags__and** | [**List[str]**](str.md)| Comma separated list of exact tags to match with an AND expression present on Product | [optional] 
 **engagement__tags** | [**List[str]**](str.md)| Comma separated list of exact tags present on engagement (uses OR for multiple values) | [optional] 
 **engagement__tags__and** | [**List[str]**](str.md)| Comma separated list of exact tags to match with an AND expression present on engagement | [optional] 
 **has_tags** | **bool**| Has tags | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **not_engagement__product__tags** | [**List[str]**](str.md)| Comma separated list of exact tags not present on Product | [optional] 
 **not_engagement__tags** | [**List[str]**](str.md)| Comma separated list of exact tags not present on engagement | [optional] 
 **not_tag** | **str**| Not Tag name contains | [optional] 
 **not_tags** | [**List[str]**](str.md)| Comma separated list of exact tags not present on model | [optional] 
 **notes** | [**List[int]**](int.md)|  | [optional] 
 **o** | [**List[str]**](str.md)| Ordering  * &#x60;title&#x60; - Title * &#x60;-title&#x60; - Title (descending) * &#x60;version&#x60; - Version * &#x60;-version&#x60; - Version (descending) * &#x60;target_start&#x60; - Target start * &#x60;-target_start&#x60; - Target start (descending) * &#x60;target_end&#x60; - Target end * &#x60;-target_end&#x60; - Target end (descending) * &#x60;test_type&#x60; - Test type * &#x60;-test_type&#x60; - Test type (descending) * &#x60;lead&#x60; - Lead * &#x60;-lead&#x60; - Lead (descending) * &#x60;branch_tag&#x60; - Branch tag * &#x60;-branch_tag&#x60; - Branch tag (descending) * &#x60;build_id&#x60; - Build id * &#x60;-build_id&#x60; - Build id (descending) * &#x60;commit_hash&#x60; - Commit hash * &#x60;-commit_hash&#x60; - Commit hash (descending) * &#x60;api_scan_configuration&#x60; - Api scan configuration * &#x60;-api_scan_configuration&#x60; - Api scan configuration (descending) * &#x60;engagement&#x60; - Engagement * &#x60;-engagement&#x60; - Engagement (descending) * &#x60;created&#x60; - Created * &#x60;-created&#x60; - Created (descending) * &#x60;updated&#x60; - Updated * &#x60;-updated&#x60; - Updated (descending) | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **percent_complete** | **int**|  | [optional] 
 **scan_type** | **str**|  | [optional] 
 **tag** | **str**| Tag name contains | [optional] 
 **tags** | [**List[str]**](str.md)| Comma separated list of exact tags (uses OR for multiple values) | [optional] 
 **tags__and** | [**List[str]**](str.md)| Comma separated list of exact tags to match with an AND expression | [optional] 
 **target_end** | **datetime**|  | [optional] 
 **target_start** | **datetime**|  | [optional] 
 **test_type** | **int**|  | [optional] 
 **title** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**PaginatedTestList**](PaginatedTestList.md)

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

# **notes_create**
> Note notes_create(id, add_new_note_option_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.add_new_note_option_request import AddNewNoteOptionRequest
from defectdojo_api_generated.models.note import Note
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
    api_instance = defectdojo_api_generated.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
    add_new_note_option_request = defectdojo_api_generated.AddNewNoteOptionRequest() # AddNewNoteOptionRequest | 

    try:
        api_response = api_instance.notes_create(id, add_new_note_option_request)
        print("The response of TestsApi->notes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestsApi->notes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
 **add_new_note_option_request** | [**AddNewNoteOptionRequest**](AddNewNoteOptionRequest.md)|  | 

### Return type

[**Note**](Note.md)

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

# **notes_retrieve**
> TestToNotes notes_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.test_to_notes import TestToNotes
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
    api_instance = defectdojo_api_generated.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.

    try:
        api_response = api_instance.notes_retrieve(id)
        print("The response of TestsApi->notes_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestsApi->notes_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 

### Return type

[**TestToNotes**](TestToNotes.md)

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

# **partial_update**
> Test partial_update(id, patched_test_request=patched_test_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.patched_test_request import PatchedTestRequest
from defectdojo_api_generated.models.test import Test
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
    api_instance = defectdojo_api_generated.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
    patched_test_request = defectdojo_api_generated.PatchedTestRequest() # PatchedTestRequest |  (optional)

    try:
        api_response = api_instance.partial_update(id, patched_test_request=patched_test_request)
        print("The response of TestsApi->partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestsApi->partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
 **patched_test_request** | [**PatchedTestRequest**](PatchedTestRequest.md)|  | [optional] 

### Return type

[**Test**](Test.md)

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

# **retrieve**
> Test retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.test import Test
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
    api_instance = defectdojo_api_generated.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.

    try:
        api_response = api_instance.retrieve(id)
        print("The response of TestsApi->retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestsApi->retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 

### Return type

[**Test**](Test.md)

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

# **update**
> Test update(id, test_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.test import Test
from defectdojo_api_generated.models.test_request import TestRequest
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
    api_instance = defectdojo_api_generated.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
    test_request = defectdojo_api_generated.TestRequest() # TestRequest | 

    try:
        api_response = api_instance.update(id, test_request)
        print("The response of TestsApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestsApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
 **test_request** | [**TestRequest**](TestRequest.md)|  | 

### Return type

[**Test**](Test.md)

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

