# defectdojo_api_generated.CeleryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queue_details_list**](CeleryApi.md#queue_details_list) | **GET** /api/v2/celery/queue/details/ | Get per-task breakdown of the Celery queue
[**queue_purge_create**](CeleryApi.md#queue_purge_create) | **POST** /api/v2/celery/queue/purge/ | Purge all pending Celery tasks from the queue
[**queue_task_purge_create**](CeleryApi.md#queue_task_purge_create) | **POST** /api/v2/celery/queue/task/purge/ | Purge all queued tasks with a given task name
[**status_retrieve**](CeleryApi.md#status_retrieve) | **GET** /api/v2/celery/status/ | Get Celery worker and queue status


# **queue_details_list**
> List[CeleryQueueTaskDetail] queue_details_list()

Get per-task breakdown of the Celery queue

Scans every message in the queue (O(N)) and returns task name, count, and oldest/newest queue positions. May be slow for large queues.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.celery_queue_task_detail import CeleryQueueTaskDetail
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
    api_instance = defectdojo_api_generated.CeleryApi(api_client)

    try:
        # Get per-task breakdown of the Celery queue
        api_response = api_instance.queue_details_list()
        print("The response of CeleryApi->queue_details_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CeleryApi->queue_details_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CeleryQueueTaskDetail]**](CeleryQueueTaskDetail.md)

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

# **queue_purge_create**
> CeleryQueuePurgeCreate200Response queue_purge_create()

Purge all pending Celery tasks from the queue

Removes all pending tasks from the default Celery queue. Tasks already being executed by workers are not affected. Note: if deduplication tasks were queued, you may need to re-run deduplication manually via `python manage.py dedupe`.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.celery_queue_purge_create200_response import CeleryQueuePurgeCreate200Response
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
    api_instance = defectdojo_api_generated.CeleryApi(api_client)

    try:
        # Purge all pending Celery tasks from the queue
        api_response = api_instance.queue_purge_create()
        print("The response of CeleryApi->queue_purge_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CeleryApi->queue_purge_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CeleryQueuePurgeCreate200Response**](CeleryQueuePurgeCreate200Response.md)

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

# **queue_task_purge_create**
> CeleryQueuePurgeCreate200Response queue_task_purge_create(celery_queue_task_purge_create_request=celery_queue_task_purge_create_request)

Purge all queued tasks with a given task name

Removes all pending tasks matching the given task name from the default Celery queue.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.celery_queue_purge_create200_response import CeleryQueuePurgeCreate200Response
from defectdojo_api_generated.models.celery_queue_task_purge_create_request import CeleryQueueTaskPurgeCreateRequest
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
    api_instance = defectdojo_api_generated.CeleryApi(api_client)
    celery_queue_task_purge_create_request = defectdojo_api_generated.CeleryQueueTaskPurgeCreateRequest() # CeleryQueueTaskPurgeCreateRequest |  (optional)

    try:
        # Purge all queued tasks with a given task name
        api_response = api_instance.queue_task_purge_create(celery_queue_task_purge_create_request=celery_queue_task_purge_create_request)
        print("The response of CeleryApi->queue_task_purge_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CeleryApi->queue_task_purge_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **celery_queue_task_purge_create_request** | [**CeleryQueueTaskPurgeCreateRequest**](CeleryQueueTaskPurgeCreateRequest.md)|  | [optional] 

### Return type

[**CeleryQueuePurgeCreate200Response**](CeleryQueuePurgeCreate200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_retrieve**
> CeleryStatus status_retrieve()

Get Celery worker and queue status

Returns Celery worker liveness, pending queue length, and the active task timeout/expiry configuration. Uses the Celery control channel (pidbox) for worker status so it works correctly even when the task queue is clogged.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.celery_status import CeleryStatus
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
    api_instance = defectdojo_api_generated.CeleryApi(api_client)

    try:
        # Get Celery worker and queue status
        api_response = api_instance.status_retrieve()
        print("The response of CeleryApi->status_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CeleryApi->status_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CeleryStatus**](CeleryStatus.md)

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

