# defectdojo_api_generated.NotificationWebhooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notification_webhooks_create**](NotificationWebhooksApi.md#notification_webhooks_create) | **POST** /api/v2/notification_webhooks/ | 
[**notification_webhooks_delete_preview_list**](NotificationWebhooksApi.md#notification_webhooks_delete_preview_list) | **GET** /api/v2/notification_webhooks/{id}/delete_preview/ | 
[**notification_webhooks_destroy**](NotificationWebhooksApi.md#notification_webhooks_destroy) | **DELETE** /api/v2/notification_webhooks/{id}/ | 
[**notification_webhooks_list**](NotificationWebhooksApi.md#notification_webhooks_list) | **GET** /api/v2/notification_webhooks/ | 
[**notification_webhooks_partial_update**](NotificationWebhooksApi.md#notification_webhooks_partial_update) | **PATCH** /api/v2/notification_webhooks/{id}/ | 
[**notification_webhooks_retrieve**](NotificationWebhooksApi.md#notification_webhooks_retrieve) | **GET** /api/v2/notification_webhooks/{id}/ | 
[**notification_webhooks_update**](NotificationWebhooksApi.md#notification_webhooks_update) | **PUT** /api/v2/notification_webhooks/{id}/ | 


# **notification_webhooks_create**
> NotificationWebhooks notification_webhooks_create(notification_webhooks_request=notification_webhooks_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.notification_webhooks import NotificationWebhooks
from defectdojo_api_generated.models.notification_webhooks_request import NotificationWebhooksRequest
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
    api_instance = defectdojo_api_generated.NotificationWebhooksApi(api_client)
    notification_webhooks_request = defectdojo_api_generated.NotificationWebhooksRequest() # NotificationWebhooksRequest |  (optional)

    try:
        api_response = api_instance.notification_webhooks_create(notification_webhooks_request=notification_webhooks_request)
        print("The response of NotificationWebhooksApi->notification_webhooks_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationWebhooksApi->notification_webhooks_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_webhooks_request** | [**NotificationWebhooksRequest**](NotificationWebhooksRequest.md)|  | [optional] 

### Return type

[**NotificationWebhooks**](NotificationWebhooks.md)

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

# **notification_webhooks_delete_preview_list**
> PaginatedDeletePreviewList notification_webhooks_delete_preview_list(id, limit=limit, offset=offset)

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
    api_instance = defectdojo_api_generated.NotificationWebhooksApi(api_client)
    id = 56 # int | A unique integer value identifying this notification_ webhooks.
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.notification_webhooks_delete_preview_list(id, limit=limit, offset=offset)
        print("The response of NotificationWebhooksApi->notification_webhooks_delete_preview_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationWebhooksApi->notification_webhooks_delete_preview_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notification_ webhooks. | 
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

# **notification_webhooks_destroy**
> notification_webhooks_destroy(id)

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
    api_instance = defectdojo_api_generated.NotificationWebhooksApi(api_client)
    id = 56 # int | A unique integer value identifying this notification_ webhooks.

    try:
        api_instance.notification_webhooks_destroy(id)
    except Exception as e:
        print("Exception when calling NotificationWebhooksApi->notification_webhooks_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notification_ webhooks. | 

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

# **notification_webhooks_list**
> PaginatedNotificationWebhooksList notification_webhooks_list(first_error=first_error, header_name=header_name, header_value=header_value, last_error=last_error, limit=limit, name=name, note=note, offset=offset, owner=owner, status=status, url=url)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_notification_webhooks_list import PaginatedNotificationWebhooksList
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
    api_instance = defectdojo_api_generated.NotificationWebhooksApi(api_client)
    first_error = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    header_name = 'header_name_example' # str |  (optional)
    header_value = 'header_value_example' # str |  (optional)
    last_error = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    name = 'name_example' # str |  (optional)
    note = 'note_example' # str |  (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    owner = 56 # int |  (optional)
    status = 'status_example' # str | Status of the incoming webhook  * `active` - Active * `active_tmp` - Active but 5xx (or similar) error detected * `inactive_tmp` - Temporary inactive because of 5xx (or similar) error * `inactive_permanent` - Permanently inactive (optional)
    url = 'url_example' # str |  (optional)

    try:
        api_response = api_instance.notification_webhooks_list(first_error=first_error, header_name=header_name, header_value=header_value, last_error=last_error, limit=limit, name=name, note=note, offset=offset, owner=owner, status=status, url=url)
        print("The response of NotificationWebhooksApi->notification_webhooks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationWebhooksApi->notification_webhooks_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_error** | **datetime**|  | [optional] 
 **header_name** | **str**|  | [optional] 
 **header_value** | **str**|  | [optional] 
 **last_error** | **datetime**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**|  | [optional] 
 **note** | **str**|  | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **owner** | **int**|  | [optional] 
 **status** | **str**| Status of the incoming webhook  * &#x60;active&#x60; - Active * &#x60;active_tmp&#x60; - Active but 5xx (or similar) error detected * &#x60;inactive_tmp&#x60; - Temporary inactive because of 5xx (or similar) error * &#x60;inactive_permanent&#x60; - Permanently inactive | [optional] 
 **url** | **str**|  | [optional] 

### Return type

[**PaginatedNotificationWebhooksList**](PaginatedNotificationWebhooksList.md)

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

# **notification_webhooks_partial_update**
> NotificationWebhooks notification_webhooks_partial_update(id, patched_notification_webhooks_request=patched_notification_webhooks_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.notification_webhooks import NotificationWebhooks
from defectdojo_api_generated.models.patched_notification_webhooks_request import PatchedNotificationWebhooksRequest
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
    api_instance = defectdojo_api_generated.NotificationWebhooksApi(api_client)
    id = 56 # int | A unique integer value identifying this notification_ webhooks.
    patched_notification_webhooks_request = defectdojo_api_generated.PatchedNotificationWebhooksRequest() # PatchedNotificationWebhooksRequest |  (optional)

    try:
        api_response = api_instance.notification_webhooks_partial_update(id, patched_notification_webhooks_request=patched_notification_webhooks_request)
        print("The response of NotificationWebhooksApi->notification_webhooks_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationWebhooksApi->notification_webhooks_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notification_ webhooks. | 
 **patched_notification_webhooks_request** | [**PatchedNotificationWebhooksRequest**](PatchedNotificationWebhooksRequest.md)|  | [optional] 

### Return type

[**NotificationWebhooks**](NotificationWebhooks.md)

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

# **notification_webhooks_retrieve**
> NotificationWebhooks notification_webhooks_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.notification_webhooks import NotificationWebhooks
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
    api_instance = defectdojo_api_generated.NotificationWebhooksApi(api_client)
    id = 56 # int | A unique integer value identifying this notification_ webhooks.

    try:
        api_response = api_instance.notification_webhooks_retrieve(id)
        print("The response of NotificationWebhooksApi->notification_webhooks_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationWebhooksApi->notification_webhooks_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notification_ webhooks. | 

### Return type

[**NotificationWebhooks**](NotificationWebhooks.md)

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

# **notification_webhooks_update**
> NotificationWebhooks notification_webhooks_update(id, notification_webhooks_request=notification_webhooks_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.notification_webhooks import NotificationWebhooks
from defectdojo_api_generated.models.notification_webhooks_request import NotificationWebhooksRequest
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
    api_instance = defectdojo_api_generated.NotificationWebhooksApi(api_client)
    id = 56 # int | A unique integer value identifying this notification_ webhooks.
    notification_webhooks_request = defectdojo_api_generated.NotificationWebhooksRequest() # NotificationWebhooksRequest |  (optional)

    try:
        api_response = api_instance.notification_webhooks_update(id, notification_webhooks_request=notification_webhooks_request)
        print("The response of NotificationWebhooksApi->notification_webhooks_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationWebhooksApi->notification_webhooks_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notification_ webhooks. | 
 **notification_webhooks_request** | [**NotificationWebhooksRequest**](NotificationWebhooksRequest.md)|  | [optional] 

### Return type

[**NotificationWebhooks**](NotificationWebhooks.md)

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

