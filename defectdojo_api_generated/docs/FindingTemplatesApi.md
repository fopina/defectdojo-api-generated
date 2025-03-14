# defectdojo_api_generated.FindingTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**finding_templates_create**](FindingTemplatesApi.md#finding_templates_create) | **POST** /api/v2/finding_templates/ | 
[**finding_templates_delete_preview_list**](FindingTemplatesApi.md#finding_templates_delete_preview_list) | **GET** /api/v2/finding_templates/{id}/delete_preview/ | 
[**finding_templates_destroy**](FindingTemplatesApi.md#finding_templates_destroy) | **DELETE** /api/v2/finding_templates/{id}/ | 
[**finding_templates_list**](FindingTemplatesApi.md#finding_templates_list) | **GET** /api/v2/finding_templates/ | 
[**finding_templates_partial_update**](FindingTemplatesApi.md#finding_templates_partial_update) | **PATCH** /api/v2/finding_templates/{id}/ | 
[**finding_templates_retrieve**](FindingTemplatesApi.md#finding_templates_retrieve) | **GET** /api/v2/finding_templates/{id}/ | 
[**finding_templates_update**](FindingTemplatesApi.md#finding_templates_update) | **PUT** /api/v2/finding_templates/{id}/ | 


# **finding_templates_create**
> FindingTemplate finding_templates_create(finding_template_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.finding_template import FindingTemplate
from defectdojo_api_generated.models.finding_template_request import FindingTemplateRequest
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
    api_instance = defectdojo_api_generated.FindingTemplatesApi(api_client)
    finding_template_request = defectdojo_api_generated.FindingTemplateRequest() # FindingTemplateRequest | 

    try:
        api_response = api_instance.finding_templates_create(finding_template_request)
        print("The response of FindingTemplatesApi->finding_templates_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingTemplatesApi->finding_templates_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finding_template_request** | [**FindingTemplateRequest**](FindingTemplateRequest.md)|  | 

### Return type

[**FindingTemplate**](FindingTemplate.md)

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

# **finding_templates_delete_preview_list**
> PaginatedDeletePreviewList finding_templates_delete_preview_list(id, limit=limit, offset=offset)

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
    api_instance = defectdojo_api_generated.FindingTemplatesApi(api_client)
    id = 56 # int | A unique integer value identifying this finding_ template.
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.finding_templates_delete_preview_list(id, limit=limit, offset=offset)
        print("The response of FindingTemplatesApi->finding_templates_delete_preview_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingTemplatesApi->finding_templates_delete_preview_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding_ template. | 
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

# **finding_templates_destroy**
> finding_templates_destroy(id)

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
    api_instance = defectdojo_api_generated.FindingTemplatesApi(api_client)
    id = 56 # int | A unique integer value identifying this finding_ template.

    try:
        api_instance.finding_templates_destroy(id)
    except Exception as e:
        print("Exception when calling FindingTemplatesApi->finding_templates_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding_ template. | 

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

# **finding_templates_list**
> PaginatedFindingTemplateList finding_templates_list(cwe=cwe, description=description, id=id, limit=limit, mitigation=mitigation, not_tag=not_tag, not_tags=not_tags, o=o, offset=offset, severity=severity, tag=tag, tags=tags, tags__and=tags__and, title=title)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_finding_template_list import PaginatedFindingTemplateList
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
    api_instance = defectdojo_api_generated.FindingTemplatesApi(api_client)
    cwe = 56 # int |  (optional)
    description = 'description_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    mitigation = 'mitigation_example' # str |  (optional)
    not_tag = 'not_tag_example' # str | Not Tag name contains (optional)
    not_tags = ['not_tags_example'] # List[str] | Comma separated list of exact tags not present on model (optional)
    o = ['o_example'] # List[str] | Ordering  * `title` - Title * `-title` - Title (descending) * `cwe` - Cwe * `-cwe` - Cwe (descending) (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    severity = 'severity_example' # str |  (optional)
    tag = 'tag_example' # str | Tag name contains (optional)
    tags = ['tags_example'] # List[str] | Comma separated list of exact tags (uses OR for multiple values) (optional)
    tags__and = ['tags__and_example'] # List[str] | Comma separated list of exact tags to match with an AND expression (optional)
    title = 'title_example' # str |  (optional)

    try:
        api_response = api_instance.finding_templates_list(cwe=cwe, description=description, id=id, limit=limit, mitigation=mitigation, not_tag=not_tag, not_tags=not_tags, o=o, offset=offset, severity=severity, tag=tag, tags=tags, tags__and=tags__and, title=title)
        print("The response of FindingTemplatesApi->finding_templates_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingTemplatesApi->finding_templates_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cwe** | **int**|  | [optional] 
 **description** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **mitigation** | **str**|  | [optional] 
 **not_tag** | **str**| Not Tag name contains | [optional] 
 **not_tags** | [**List[str]**](str.md)| Comma separated list of exact tags not present on model | [optional] 
 **o** | [**List[str]**](str.md)| Ordering  * &#x60;title&#x60; - Title * &#x60;-title&#x60; - Title (descending) * &#x60;cwe&#x60; - Cwe * &#x60;-cwe&#x60; - Cwe (descending) | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **severity** | **str**|  | [optional] 
 **tag** | **str**| Tag name contains | [optional] 
 **tags** | [**List[str]**](str.md)| Comma separated list of exact tags (uses OR for multiple values) | [optional] 
 **tags__and** | [**List[str]**](str.md)| Comma separated list of exact tags to match with an AND expression | [optional] 
 **title** | **str**|  | [optional] 

### Return type

[**PaginatedFindingTemplateList**](PaginatedFindingTemplateList.md)

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

# **finding_templates_partial_update**
> FindingTemplate finding_templates_partial_update(id, patched_finding_template_request=patched_finding_template_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.finding_template import FindingTemplate
from defectdojo_api_generated.models.patched_finding_template_request import PatchedFindingTemplateRequest
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
    api_instance = defectdojo_api_generated.FindingTemplatesApi(api_client)
    id = 56 # int | A unique integer value identifying this finding_ template.
    patched_finding_template_request = defectdojo_api_generated.PatchedFindingTemplateRequest() # PatchedFindingTemplateRequest |  (optional)

    try:
        api_response = api_instance.finding_templates_partial_update(id, patched_finding_template_request=patched_finding_template_request)
        print("The response of FindingTemplatesApi->finding_templates_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingTemplatesApi->finding_templates_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding_ template. | 
 **patched_finding_template_request** | [**PatchedFindingTemplateRequest**](PatchedFindingTemplateRequest.md)|  | [optional] 

### Return type

[**FindingTemplate**](FindingTemplate.md)

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

# **finding_templates_retrieve**
> FindingTemplate finding_templates_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.finding_template import FindingTemplate
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
    api_instance = defectdojo_api_generated.FindingTemplatesApi(api_client)
    id = 56 # int | A unique integer value identifying this finding_ template.

    try:
        api_response = api_instance.finding_templates_retrieve(id)
        print("The response of FindingTemplatesApi->finding_templates_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingTemplatesApi->finding_templates_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding_ template. | 

### Return type

[**FindingTemplate**](FindingTemplate.md)

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

# **finding_templates_update**
> FindingTemplate finding_templates_update(id, finding_template_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.finding_template import FindingTemplate
from defectdojo_api_generated.models.finding_template_request import FindingTemplateRequest
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
    api_instance = defectdojo_api_generated.FindingTemplatesApi(api_client)
    id = 56 # int | A unique integer value identifying this finding_ template.
    finding_template_request = defectdojo_api_generated.FindingTemplateRequest() # FindingTemplateRequest | 

    try:
        api_response = api_instance.finding_templates_update(id, finding_template_request)
        print("The response of FindingTemplatesApi->finding_templates_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingTemplatesApi->finding_templates_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding_ template. | 
 **finding_template_request** | [**FindingTemplateRequest**](FindingTemplateRequest.md)|  | 

### Return type

[**FindingTemplate**](FindingTemplate.md)

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

