# defectdojo_api_generated.UserContactInfosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_contact_infos_create**](UserContactInfosApi.md#user_contact_infos_create) | **POST** /api/v2/user_contact_infos/ | 
[**user_contact_infos_delete_preview_list**](UserContactInfosApi.md#user_contact_infos_delete_preview_list) | **GET** /api/v2/user_contact_infos/{id}/delete_preview/ | 
[**user_contact_infos_destroy**](UserContactInfosApi.md#user_contact_infos_destroy) | **DELETE** /api/v2/user_contact_infos/{id}/ | 
[**user_contact_infos_list**](UserContactInfosApi.md#user_contact_infos_list) | **GET** /api/v2/user_contact_infos/ | 
[**user_contact_infos_partial_update**](UserContactInfosApi.md#user_contact_infos_partial_update) | **PATCH** /api/v2/user_contact_infos/{id}/ | 
[**user_contact_infos_retrieve**](UserContactInfosApi.md#user_contact_infos_retrieve) | **GET** /api/v2/user_contact_infos/{id}/ | 
[**user_contact_infos_update**](UserContactInfosApi.md#user_contact_infos_update) | **PUT** /api/v2/user_contact_infos/{id}/ | 


# **user_contact_infos_create**
> UserContactInfo user_contact_infos_create(user_contact_info_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.user_contact_info import UserContactInfo
from defectdojo_api_generated.models.user_contact_info_request import UserContactInfoRequest
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
    api_instance = defectdojo_api_generated.UserContactInfosApi(api_client)
    user_contact_info_request = defectdojo_api_generated.UserContactInfoRequest() # UserContactInfoRequest | 

    try:
        api_response = api_instance.user_contact_infos_create(user_contact_info_request)
        print("The response of UserContactInfosApi->user_contact_infos_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserContactInfosApi->user_contact_infos_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_contact_info_request** | [**UserContactInfoRequest**](UserContactInfoRequest.md)|  | 

### Return type

[**UserContactInfo**](UserContactInfo.md)

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

# **user_contact_infos_delete_preview_list**
> PaginatedDeletePreviewList user_contact_infos_delete_preview_list(id, limit=limit, offset=offset)

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
    api_instance = defectdojo_api_generated.UserContactInfosApi(api_client)
    id = 56 # int | A unique integer value identifying this user contact info.
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.user_contact_infos_delete_preview_list(id, limit=limit, offset=offset)
        print("The response of UserContactInfosApi->user_contact_infos_delete_preview_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserContactInfosApi->user_contact_infos_delete_preview_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user contact info. | 
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

# **user_contact_infos_destroy**
> user_contact_infos_destroy(id)

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
    api_instance = defectdojo_api_generated.UserContactInfosApi(api_client)
    id = 56 # int | A unique integer value identifying this user contact info.

    try:
        api_instance.user_contact_infos_destroy(id)
    except Exception as e:
        print("Exception when calling UserContactInfosApi->user_contact_infos_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user contact info. | 

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

# **user_contact_infos_list**
> PaginatedUserContactInfoList user_contact_infos_list(block_execution=block_execution, cell_number=cell_number, force_password_reset=force_password_reset, github_username=github_username, limit=limit, offset=offset, phone_number=phone_number, prefetch=prefetch, slack_user_id=slack_user_id, slack_username=slack_username, title=title, twitter_username=twitter_username, user=user)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_user_contact_info_list import PaginatedUserContactInfoList
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
    api_instance = defectdojo_api_generated.UserContactInfosApi(api_client)
    block_execution = True # bool |  (optional)
    cell_number = 'cell_number_example' # str |  (optional)
    force_password_reset = True # bool |  (optional)
    github_username = 'github_username_example' # str |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    phone_number = 'phone_number_example' # str |  (optional)
    prefetch = ['prefetch_example'] # List[str] | List of fields for which to prefetch model instances and add those to the response (optional)
    slack_user_id = 'slack_user_id_example' # str |  (optional)
    slack_username = 'slack_username_example' # str |  (optional)
    title = 'title_example' # str |  (optional)
    twitter_username = 'twitter_username_example' # str |  (optional)
    user = 56 # int |  (optional)

    try:
        api_response = api_instance.user_contact_infos_list(block_execution=block_execution, cell_number=cell_number, force_password_reset=force_password_reset, github_username=github_username, limit=limit, offset=offset, phone_number=phone_number, prefetch=prefetch, slack_user_id=slack_user_id, slack_username=slack_username, title=title, twitter_username=twitter_username, user=user)
        print("The response of UserContactInfosApi->user_contact_infos_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserContactInfosApi->user_contact_infos_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_execution** | **bool**|  | [optional] 
 **cell_number** | **str**|  | [optional] 
 **force_password_reset** | **bool**|  | [optional] 
 **github_username** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **phone_number** | **str**|  | [optional] 
 **prefetch** | [**List[str]**](str.md)| List of fields for which to prefetch model instances and add those to the response | [optional] 
 **slack_user_id** | **str**|  | [optional] 
 **slack_username** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **twitter_username** | **str**|  | [optional] 
 **user** | **int**|  | [optional] 

### Return type

[**PaginatedUserContactInfoList**](PaginatedUserContactInfoList.md)

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

# **user_contact_infos_partial_update**
> UserContactInfo user_contact_infos_partial_update(id, patched_user_contact_info_request=patched_user_contact_info_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.patched_user_contact_info_request import PatchedUserContactInfoRequest
from defectdojo_api_generated.models.user_contact_info import UserContactInfo
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
    api_instance = defectdojo_api_generated.UserContactInfosApi(api_client)
    id = 56 # int | A unique integer value identifying this user contact info.
    patched_user_contact_info_request = defectdojo_api_generated.PatchedUserContactInfoRequest() # PatchedUserContactInfoRequest |  (optional)

    try:
        api_response = api_instance.user_contact_infos_partial_update(id, patched_user_contact_info_request=patched_user_contact_info_request)
        print("The response of UserContactInfosApi->user_contact_infos_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserContactInfosApi->user_contact_infos_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user contact info. | 
 **patched_user_contact_info_request** | [**PatchedUserContactInfoRequest**](PatchedUserContactInfoRequest.md)|  | [optional] 

### Return type

[**UserContactInfo**](UserContactInfo.md)

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

# **user_contact_infos_retrieve**
> UserContactInfo user_contact_infos_retrieve(id, prefetch=prefetch)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.user_contact_info import UserContactInfo
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
    api_instance = defectdojo_api_generated.UserContactInfosApi(api_client)
    id = 56 # int | A unique integer value identifying this user contact info.
    prefetch = ['prefetch_example'] # List[str] | List of fields for which to prefetch model instances and add those to the response (optional)

    try:
        api_response = api_instance.user_contact_infos_retrieve(id, prefetch=prefetch)
        print("The response of UserContactInfosApi->user_contact_infos_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserContactInfosApi->user_contact_infos_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user contact info. | 
 **prefetch** | [**List[str]**](str.md)| List of fields for which to prefetch model instances and add those to the response | [optional] 

### Return type

[**UserContactInfo**](UserContactInfo.md)

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

# **user_contact_infos_update**
> UserContactInfo user_contact_infos_update(id, user_contact_info_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.user_contact_info import UserContactInfo
from defectdojo_api_generated.models.user_contact_info_request import UserContactInfoRequest
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
    api_instance = defectdojo_api_generated.UserContactInfosApi(api_client)
    id = 56 # int | A unique integer value identifying this user contact info.
    user_contact_info_request = defectdojo_api_generated.UserContactInfoRequest() # UserContactInfoRequest | 

    try:
        api_response = api_instance.user_contact_infos_update(id, user_contact_info_request)
        print("The response of UserContactInfosApi->user_contact_infos_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserContactInfosApi->user_contact_infos_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user contact info. | 
 **user_contact_info_request** | [**UserContactInfoRequest**](UserContactInfoRequest.md)|  | 

### Return type

[**UserContactInfo**](UserContactInfo.md)

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

