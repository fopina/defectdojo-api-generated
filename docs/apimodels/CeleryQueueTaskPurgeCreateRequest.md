# CeleryQueueTaskPurgeCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_name** | **str** |  | 

## Example

```python
from defectdojo_api_generated.models.celery_queue_task_purge_create_request import CeleryQueueTaskPurgeCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CeleryQueueTaskPurgeCreateRequest from a JSON string
celery_queue_task_purge_create_request_instance = CeleryQueueTaskPurgeCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CeleryQueueTaskPurgeCreateRequest.to_json())

# convert the object into a dict
celery_queue_task_purge_create_request_dict = celery_queue_task_purge_create_request_instance.to_dict()
# create an instance of CeleryQueueTaskPurgeCreateRequest from a dict
celery_queue_task_purge_create_request_from_dict = CeleryQueueTaskPurgeCreateRequest.from_dict(celery_queue_task_purge_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


