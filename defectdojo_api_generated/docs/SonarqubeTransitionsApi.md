# defectdojo_api_generated.SonarqubeTransitionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sonarqube_transitions_create**](SonarqubeTransitionsApi.md#sonarqube_transitions_create) | **POST** /api/v2/sonarqube_transitions/ | 
[**sonarqube_transitions_delete_preview_list**](SonarqubeTransitionsApi.md#sonarqube_transitions_delete_preview_list) | **GET** /api/v2/sonarqube_transitions/{id}/delete_preview/ | 
[**sonarqube_transitions_destroy**](SonarqubeTransitionsApi.md#sonarqube_transitions_destroy) | **DELETE** /api/v2/sonarqube_transitions/{id}/ | 
[**sonarqube_transitions_list**](SonarqubeTransitionsApi.md#sonarqube_transitions_list) | **GET** /api/v2/sonarqube_transitions/ | 
[**sonarqube_transitions_partial_update**](SonarqubeTransitionsApi.md#sonarqube_transitions_partial_update) | **PATCH** /api/v2/sonarqube_transitions/{id}/ | 
[**sonarqube_transitions_retrieve**](SonarqubeTransitionsApi.md#sonarqube_transitions_retrieve) | **GET** /api/v2/sonarqube_transitions/{id}/ | 
[**sonarqube_transitions_update**](SonarqubeTransitionsApi.md#sonarqube_transitions_update) | **PUT** /api/v2/sonarqube_transitions/{id}/ | 


# **sonarqube_transitions_create**
> SonarqubeIssueTransition sonarqube_transitions_create(sonarqube_issue_transition_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.sonarqube_issue_transition import SonarqubeIssueTransition
from defectdojo_api_generated.models.sonarqube_issue_transition_request import SonarqubeIssueTransitionRequest
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
    api_instance = defectdojo_api_generated.SonarqubeTransitionsApi(api_client)
    sonarqube_issue_transition_request = defectdojo_api_generated.SonarqubeIssueTransitionRequest() # SonarqubeIssueTransitionRequest | 

    try:
        api_response = api_instance.sonarqube_transitions_create(sonarqube_issue_transition_request)
        print("The response of SonarqubeTransitionsApi->sonarqube_transitions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SonarqubeTransitionsApi->sonarqube_transitions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sonarqube_issue_transition_request** | [**SonarqubeIssueTransitionRequest**](SonarqubeIssueTransitionRequest.md)|  | 

### Return type

[**SonarqubeIssueTransition**](SonarqubeIssueTransition.md)

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

# **sonarqube_transitions_delete_preview_list**
> PaginatedDeletePreviewList sonarqube_transitions_delete_preview_list(id, limit=limit, offset=offset)

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
    api_instance = defectdojo_api_generated.SonarqubeTransitionsApi(api_client)
    id = 56 # int | A unique integer value identifying this sonarqube_ issue_ transition.
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.sonarqube_transitions_delete_preview_list(id, limit=limit, offset=offset)
        print("The response of SonarqubeTransitionsApi->sonarqube_transitions_delete_preview_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SonarqubeTransitionsApi->sonarqube_transitions_delete_preview_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sonarqube_ issue_ transition. | 
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

# **sonarqube_transitions_destroy**
> sonarqube_transitions_destroy(id)

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
    api_instance = defectdojo_api_generated.SonarqubeTransitionsApi(api_client)
    id = 56 # int | A unique integer value identifying this sonarqube_ issue_ transition.

    try:
        api_instance.sonarqube_transitions_destroy(id)
    except Exception as e:
        print("Exception when calling SonarqubeTransitionsApi->sonarqube_transitions_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sonarqube_ issue_ transition. | 

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

# **sonarqube_transitions_list**
> PaginatedSonarqubeIssueTransitionList sonarqube_transitions_list(finding_status=finding_status, id=id, limit=limit, offset=offset, sonarqube_issue=sonarqube_issue, sonarqube_status=sonarqube_status, transitions=transitions)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_sonarqube_issue_transition_list import PaginatedSonarqubeIssueTransitionList
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
    api_instance = defectdojo_api_generated.SonarqubeTransitionsApi(api_client)
    finding_status = 'finding_status_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    sonarqube_issue = 56 # int |  (optional)
    sonarqube_status = 'sonarqube_status_example' # str |  (optional)
    transitions = 'transitions_example' # str |  (optional)

    try:
        api_response = api_instance.sonarqube_transitions_list(finding_status=finding_status, id=id, limit=limit, offset=offset, sonarqube_issue=sonarqube_issue, sonarqube_status=sonarqube_status, transitions=transitions)
        print("The response of SonarqubeTransitionsApi->sonarqube_transitions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SonarqubeTransitionsApi->sonarqube_transitions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finding_status** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **sonarqube_issue** | **int**|  | [optional] 
 **sonarqube_status** | **str**|  | [optional] 
 **transitions** | **str**|  | [optional] 

### Return type

[**PaginatedSonarqubeIssueTransitionList**](PaginatedSonarqubeIssueTransitionList.md)

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

# **sonarqube_transitions_partial_update**
> SonarqubeIssueTransition sonarqube_transitions_partial_update(id, patched_sonarqube_issue_transition_request=patched_sonarqube_issue_transition_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.patched_sonarqube_issue_transition_request import PatchedSonarqubeIssueTransitionRequest
from defectdojo_api_generated.models.sonarqube_issue_transition import SonarqubeIssueTransition
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
    api_instance = defectdojo_api_generated.SonarqubeTransitionsApi(api_client)
    id = 56 # int | A unique integer value identifying this sonarqube_ issue_ transition.
    patched_sonarqube_issue_transition_request = defectdojo_api_generated.PatchedSonarqubeIssueTransitionRequest() # PatchedSonarqubeIssueTransitionRequest |  (optional)

    try:
        api_response = api_instance.sonarqube_transitions_partial_update(id, patched_sonarqube_issue_transition_request=patched_sonarqube_issue_transition_request)
        print("The response of SonarqubeTransitionsApi->sonarqube_transitions_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SonarqubeTransitionsApi->sonarqube_transitions_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sonarqube_ issue_ transition. | 
 **patched_sonarqube_issue_transition_request** | [**PatchedSonarqubeIssueTransitionRequest**](PatchedSonarqubeIssueTransitionRequest.md)|  | [optional] 

### Return type

[**SonarqubeIssueTransition**](SonarqubeIssueTransition.md)

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

# **sonarqube_transitions_retrieve**
> SonarqubeIssueTransition sonarqube_transitions_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.sonarqube_issue_transition import SonarqubeIssueTransition
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
    api_instance = defectdojo_api_generated.SonarqubeTransitionsApi(api_client)
    id = 56 # int | A unique integer value identifying this sonarqube_ issue_ transition.

    try:
        api_response = api_instance.sonarqube_transitions_retrieve(id)
        print("The response of SonarqubeTransitionsApi->sonarqube_transitions_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SonarqubeTransitionsApi->sonarqube_transitions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sonarqube_ issue_ transition. | 

### Return type

[**SonarqubeIssueTransition**](SonarqubeIssueTransition.md)

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

# **sonarqube_transitions_update**
> SonarqubeIssueTransition sonarqube_transitions_update(id, sonarqube_issue_transition_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.sonarqube_issue_transition import SonarqubeIssueTransition
from defectdojo_api_generated.models.sonarqube_issue_transition_request import SonarqubeIssueTransitionRequest
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
    api_instance = defectdojo_api_generated.SonarqubeTransitionsApi(api_client)
    id = 56 # int | A unique integer value identifying this sonarqube_ issue_ transition.
    sonarqube_issue_transition_request = defectdojo_api_generated.SonarqubeIssueTransitionRequest() # SonarqubeIssueTransitionRequest | 

    try:
        api_response = api_instance.sonarqube_transitions_update(id, sonarqube_issue_transition_request)
        print("The response of SonarqubeTransitionsApi->sonarqube_transitions_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SonarqubeTransitionsApi->sonarqube_transitions_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sonarqube_ issue_ transition. | 
 **sonarqube_issue_transition_request** | [**SonarqubeIssueTransitionRequest**](SonarqubeIssueTransitionRequest.md)|  | 

### Return type

[**SonarqubeIssueTransition**](SonarqubeIssueTransition.md)

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

