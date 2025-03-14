# defectdojo_api_generated.EngagementsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**engagements_accept_risks_create**](EngagementsApi.md#engagements_accept_risks_create) | **POST** /api/v2/engagements/{id}/accept_risks/ | 
[**engagements_close_create**](EngagementsApi.md#engagements_close_create) | **POST** /api/v2/engagements/{id}/close/ | 
[**engagements_complete_checklist_create**](EngagementsApi.md#engagements_complete_checklist_create) | **POST** /api/v2/engagements/{id}/complete_checklist/ | 
[**engagements_complete_checklist_retrieve**](EngagementsApi.md#engagements_complete_checklist_retrieve) | **GET** /api/v2/engagements/{id}/complete_checklist/ | 
[**engagements_create**](EngagementsApi.md#engagements_create) | **POST** /api/v2/engagements/ | 
[**engagements_delete_preview_list**](EngagementsApi.md#engagements_delete_preview_list) | **GET** /api/v2/engagements/{id}/delete_preview/ | 
[**engagements_destroy**](EngagementsApi.md#engagements_destroy) | **DELETE** /api/v2/engagements/{id}/ | 
[**engagements_files_create**](EngagementsApi.md#engagements_files_create) | **POST** /api/v2/engagements/{id}/files/ | 
[**engagements_files_download_retrieve**](EngagementsApi.md#engagements_files_download_retrieve) | **GET** /api/v2/engagements/{id}/files/download/{file_id}/ | 
[**engagements_files_retrieve**](EngagementsApi.md#engagements_files_retrieve) | **GET** /api/v2/engagements/{id}/files/ | 
[**engagements_generate_report_create**](EngagementsApi.md#engagements_generate_report_create) | **POST** /api/v2/engagements/{id}/generate_report/ | 
[**engagements_list**](EngagementsApi.md#engagements_list) | **GET** /api/v2/engagements/ | 
[**engagements_notes_create**](EngagementsApi.md#engagements_notes_create) | **POST** /api/v2/engagements/{id}/notes/ | 
[**engagements_notes_retrieve**](EngagementsApi.md#engagements_notes_retrieve) | **GET** /api/v2/engagements/{id}/notes/ | 
[**engagements_partial_update**](EngagementsApi.md#engagements_partial_update) | **PATCH** /api/v2/engagements/{id}/ | 
[**engagements_reopen_create**](EngagementsApi.md#engagements_reopen_create) | **POST** /api/v2/engagements/{id}/reopen/ | 
[**engagements_retrieve**](EngagementsApi.md#engagements_retrieve) | **GET** /api/v2/engagements/{id}/ | 
[**engagements_update**](EngagementsApi.md#engagements_update) | **PUT** /api/v2/engagements/{id}/ | 
[**engagements_update_jira_epic_create**](EngagementsApi.md#engagements_update_jira_epic_create) | **POST** /api/v2/engagements/{id}/update_jira_epic/ | 


# **engagements_accept_risks_create**
> List[RiskAcceptance] engagements_accept_risks_create(id, accepted_risk_request)

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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.
    accepted_risk_request = [defectdojo_api_generated.AcceptedRiskRequest()] # List[AcceptedRiskRequest] | 

    try:
        api_response = api_instance.engagements_accept_risks_create(id, accepted_risk_request)
        print("The response of EngagementsApi->engagements_accept_risks_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_accept_risks_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 
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

# **engagements_close_create**
> engagements_close_create(id)

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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.

    try:
        api_instance.engagements_close_create(id)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_close_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 

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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engagements_complete_checklist_create**
> EngagementCheckList engagements_complete_checklist_create(id, engagement_check_list_request=engagement_check_list_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.engagement_check_list import EngagementCheckList
from defectdojo_api_generated.models.engagement_check_list_request import EngagementCheckListRequest
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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.
    engagement_check_list_request = defectdojo_api_generated.EngagementCheckListRequest() # EngagementCheckListRequest |  (optional)

    try:
        api_response = api_instance.engagements_complete_checklist_create(id, engagement_check_list_request=engagement_check_list_request)
        print("The response of EngagementsApi->engagements_complete_checklist_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_complete_checklist_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 
 **engagement_check_list_request** | [**EngagementCheckListRequest**](EngagementCheckListRequest.md)|  | [optional] 

### Return type

[**EngagementCheckList**](EngagementCheckList.md)

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

# **engagements_complete_checklist_retrieve**
> Engagement engagements_complete_checklist_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.engagement import Engagement
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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.

    try:
        api_response = api_instance.engagements_complete_checklist_retrieve(id)
        print("The response of EngagementsApi->engagements_complete_checklist_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_complete_checklist_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 

### Return type

[**Engagement**](Engagement.md)

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

# **engagements_create**
> Engagement engagements_create(engagement_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.engagement import Engagement
from defectdojo_api_generated.models.engagement_request import EngagementRequest
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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    engagement_request = defectdojo_api_generated.EngagementRequest() # EngagementRequest | 

    try:
        api_response = api_instance.engagements_create(engagement_request)
        print("The response of EngagementsApi->engagements_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engagement_request** | [**EngagementRequest**](EngagementRequest.md)|  | 

### Return type

[**Engagement**](Engagement.md)

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

# **engagements_delete_preview_list**
> PaginatedDeletePreviewList engagements_delete_preview_list(id, limit=limit, offset=offset)

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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.engagements_delete_preview_list(id, limit=limit, offset=offset)
        print("The response of EngagementsApi->engagements_delete_preview_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_delete_preview_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 
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

# **engagements_destroy**
> engagements_destroy(id)

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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.

    try:
        api_instance.engagements_destroy(id)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 

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

# **engagements_files_create**
> File engagements_files_create(id, title, file)

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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.
    title = 'title_example' # str | 
    file = None # bytearray | 

    try:
        api_response = api_instance.engagements_files_create(id, title, file)
        print("The response of EngagementsApi->engagements_files_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_files_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 
 **title** | **str**|  | 
 **file** | **bytearray**|  | 

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

# **engagements_files_download_retrieve**
> RawFile engagements_files_download_retrieve(file_id, id)

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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    file_id = 'file_id_example' # str | 
    id = 56 # int | A unique integer value identifying this engagement.

    try:
        api_response = api_instance.engagements_files_download_retrieve(file_id, id)
        print("The response of EngagementsApi->engagements_files_download_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_files_download_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **id** | **int**| A unique integer value identifying this engagement. | 

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

# **engagements_files_retrieve**
> EngagementToFiles engagements_files_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.engagement_to_files import EngagementToFiles
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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.

    try:
        api_response = api_instance.engagements_files_retrieve(id)
        print("The response of EngagementsApi->engagements_files_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_files_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 

### Return type

[**EngagementToFiles**](EngagementToFiles.md)

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

# **engagements_generate_report_create**
> ReportGenerate engagements_generate_report_create(id, report_generate_option_request=report_generate_option_request)

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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.
    report_generate_option_request = defectdojo_api_generated.ReportGenerateOptionRequest() # ReportGenerateOptionRequest |  (optional)

    try:
        api_response = api_instance.engagements_generate_report_create(id, report_generate_option_request=report_generate_option_request)
        print("The response of EngagementsApi->engagements_generate_report_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_generate_report_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 
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

# **engagements_list**
> PaginatedEngagementList engagements_list(active=active, api_test=api_test, has_tags=has_tags, id=id, limit=limit, name=name, not_product__tags=not_product__tags, not_tag=not_tag, not_tags=not_tags, o=o, offset=offset, pen_test=pen_test, product=product, product__prod_type=product__prod_type, product__tags=product__tags, product__tags__and=product__tags__and, report_type=report_type, requester=requester, status=status, tag=tag, tags=tags, tags__and=tags__and, target_end=target_end, target_start=target_start, threat_model=threat_model, updated=updated, version=version)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_engagement_list import PaginatedEngagementList
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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    active = True # bool |  (optional)
    api_test = True # bool |  (optional)
    has_tags = True # bool | Has tags (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    name = 'name_example' # str |  (optional)
    not_product__tags = ['not_product__tags_example'] # List[str] | Comma separated list of exact tags not present on product (optional)
    not_tag = 'not_tag_example' # str | Not Tag name contains (optional)
    not_tags = ['not_tags_example'] # List[str] | Comma separated list of exact tags not present on model (optional)
    o = ['o_example'] # List[str] | Ordering  * `name` - Engagement Name * `-name` - Engagement Name (descending) * `version` - Version * `-version` - Version (descending) * `target_start` - Target start * `-target_start` - Target start (descending) * `target_end` - Target end * `-target_end` - Target end (descending) * `status` - Status * `-status` - Status (descending) * `lead` - Lead * `-lead` - Lead (descending) * `created` - Created * `-created` - Created (descending) * `updated` - Updated * `-updated` - Updated (descending) (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    pen_test = True # bool |  (optional)
    product = 56 # int |  (optional)
    product__prod_type = [56] # List[int] | Multiple values may be separated by commas. (optional)
    product__tags = ['product__tags_example'] # List[str] | Comma separated list of exact tags present on product (uses OR for multiple values) (optional)
    product__tags__and = ['product__tags__and_example'] # List[str] | Comma separated list of exact tags to match with an AND expression present on product (optional)
    report_type = 56 # int |  (optional)
    requester = 56 # int |  (optional)
    status = 'status_example' # str | * `Not Started` - Not Started * `Blocked` - Blocked * `Cancelled` - Cancelled * `Completed` - Completed * `In Progress` - In Progress * `On Hold` - On Hold * `Waiting for Resource` - Waiting for Resource (optional)
    tag = 'tag_example' # str | Tag name contains (optional)
    tags = ['tags_example'] # List[str] | Comma separated list of exact tags (uses OR for multiple values) (optional)
    tags__and = ['tags__and_example'] # List[str] | Comma separated list of exact tags to match with an AND expression (optional)
    target_end = '2013-10-20' # date |  (optional)
    target_start = '2013-10-20' # date |  (optional)
    threat_model = True # bool |  (optional)
    updated = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    version = 'version_example' # str |  (optional)

    try:
        api_response = api_instance.engagements_list(active=active, api_test=api_test, has_tags=has_tags, id=id, limit=limit, name=name, not_product__tags=not_product__tags, not_tag=not_tag, not_tags=not_tags, o=o, offset=offset, pen_test=pen_test, product=product, product__prod_type=product__prod_type, product__tags=product__tags, product__tags__and=product__tags__and, report_type=report_type, requester=requester, status=status, tag=tag, tags=tags, tags__and=tags__and, target_end=target_end, target_start=target_start, threat_model=threat_model, updated=updated, version=version)
        print("The response of EngagementsApi->engagements_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **bool**|  | [optional] 
 **api_test** | **bool**|  | [optional] 
 **has_tags** | **bool**| Has tags | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**|  | [optional] 
 **not_product__tags** | [**List[str]**](str.md)| Comma separated list of exact tags not present on product | [optional] 
 **not_tag** | **str**| Not Tag name contains | [optional] 
 **not_tags** | [**List[str]**](str.md)| Comma separated list of exact tags not present on model | [optional] 
 **o** | [**List[str]**](str.md)| Ordering  * &#x60;name&#x60; - Engagement Name * &#x60;-name&#x60; - Engagement Name (descending) * &#x60;version&#x60; - Version * &#x60;-version&#x60; - Version (descending) * &#x60;target_start&#x60; - Target start * &#x60;-target_start&#x60; - Target start (descending) * &#x60;target_end&#x60; - Target end * &#x60;-target_end&#x60; - Target end (descending) * &#x60;status&#x60; - Status * &#x60;-status&#x60; - Status (descending) * &#x60;lead&#x60; - Lead * &#x60;-lead&#x60; - Lead (descending) * &#x60;created&#x60; - Created * &#x60;-created&#x60; - Created (descending) * &#x60;updated&#x60; - Updated * &#x60;-updated&#x60; - Updated (descending) | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **pen_test** | **bool**|  | [optional] 
 **product** | **int**|  | [optional] 
 **product__prod_type** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **product__tags** | [**List[str]**](str.md)| Comma separated list of exact tags present on product (uses OR for multiple values) | [optional] 
 **product__tags__and** | [**List[str]**](str.md)| Comma separated list of exact tags to match with an AND expression present on product | [optional] 
 **report_type** | **int**|  | [optional] 
 **requester** | **int**|  | [optional] 
 **status** | **str**| * &#x60;Not Started&#x60; - Not Started * &#x60;Blocked&#x60; - Blocked * &#x60;Cancelled&#x60; - Cancelled * &#x60;Completed&#x60; - Completed * &#x60;In Progress&#x60; - In Progress * &#x60;On Hold&#x60; - On Hold * &#x60;Waiting for Resource&#x60; - Waiting for Resource | [optional] 
 **tag** | **str**| Tag name contains | [optional] 
 **tags** | [**List[str]**](str.md)| Comma separated list of exact tags (uses OR for multiple values) | [optional] 
 **tags__and** | [**List[str]**](str.md)| Comma separated list of exact tags to match with an AND expression | [optional] 
 **target_end** | **date**|  | [optional] 
 **target_start** | **date**|  | [optional] 
 **threat_model** | **bool**|  | [optional] 
 **updated** | **datetime**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**PaginatedEngagementList**](PaginatedEngagementList.md)

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

# **engagements_notes_create**
> Note engagements_notes_create(id, add_new_note_option_request)

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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.
    add_new_note_option_request = defectdojo_api_generated.AddNewNoteOptionRequest() # AddNewNoteOptionRequest | 

    try:
        api_response = api_instance.engagements_notes_create(id, add_new_note_option_request)
        print("The response of EngagementsApi->engagements_notes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_notes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 
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

# **engagements_notes_retrieve**
> EngagementToNotes engagements_notes_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.engagement_to_notes import EngagementToNotes
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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.

    try:
        api_response = api_instance.engagements_notes_retrieve(id)
        print("The response of EngagementsApi->engagements_notes_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_notes_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 

### Return type

[**EngagementToNotes**](EngagementToNotes.md)

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

# **engagements_partial_update**
> Engagement engagements_partial_update(id, patched_engagement_request=patched_engagement_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.engagement import Engagement
from defectdojo_api_generated.models.patched_engagement_request import PatchedEngagementRequest
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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.
    patched_engagement_request = defectdojo_api_generated.PatchedEngagementRequest() # PatchedEngagementRequest |  (optional)

    try:
        api_response = api_instance.engagements_partial_update(id, patched_engagement_request=patched_engagement_request)
        print("The response of EngagementsApi->engagements_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 
 **patched_engagement_request** | [**PatchedEngagementRequest**](PatchedEngagementRequest.md)|  | [optional] 

### Return type

[**Engagement**](Engagement.md)

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

# **engagements_reopen_create**
> engagements_reopen_create(id)

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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.

    try:
        api_instance.engagements_reopen_create(id)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_reopen_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 

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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engagements_retrieve**
> Engagement engagements_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.engagement import Engagement
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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.

    try:
        api_response = api_instance.engagements_retrieve(id)
        print("The response of EngagementsApi->engagements_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 

### Return type

[**Engagement**](Engagement.md)

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

# **engagements_update**
> Engagement engagements_update(id, engagement_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.engagement import Engagement
from defectdojo_api_generated.models.engagement_request import EngagementRequest
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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.
    engagement_request = defectdojo_api_generated.EngagementRequest() # EngagementRequest | 

    try:
        api_response = api_instance.engagements_update(id, engagement_request)
        print("The response of EngagementsApi->engagements_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 
 **engagement_request** | [**EngagementRequest**](EngagementRequest.md)|  | 

### Return type

[**Engagement**](Engagement.md)

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

# **engagements_update_jira_epic_create**
> EngagementUpdateJiraEpic engagements_update_jira_epic_create(id, engagement_update_jira_epic_request=engagement_update_jira_epic_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.engagement_update_jira_epic import EngagementUpdateJiraEpic
from defectdojo_api_generated.models.engagement_update_jira_epic_request import EngagementUpdateJiraEpicRequest
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
    api_instance = defectdojo_api_generated.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.
    engagement_update_jira_epic_request = defectdojo_api_generated.EngagementUpdateJiraEpicRequest() # EngagementUpdateJiraEpicRequest |  (optional)

    try:
        api_response = api_instance.engagements_update_jira_epic_create(id, engagement_update_jira_epic_request=engagement_update_jira_epic_request)
        print("The response of EngagementsApi->engagements_update_jira_epic_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EngagementsApi->engagements_update_jira_epic_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 
 **engagement_update_jira_epic_request** | [**EngagementUpdateJiraEpicRequest**](EngagementUpdateJiraEpicRequest.md)|  | [optional] 

### Return type

[**EngagementUpdateJiraEpic**](EngagementUpdateJiraEpic.md)

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

