# CeleryQueueTaskDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_name** | **str** |  | [optional] [readonly] 
**count** | **int** |  | [optional] [readonly] 
**oldest_position** | **int** |  | [optional] [readonly] 
**newest_position** | **int** |  | [optional] [readonly] 
**oldest_eta** | **str** |  | [optional] [readonly] 
**newest_eta** | **str** |  | [optional] [readonly] 
**earliest_expires** | **str** |  | [optional] [readonly] 
**latest_expires** | **str** |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.celery_queue_task_detail import CeleryQueueTaskDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CeleryQueueTaskDetail from a JSON string
celery_queue_task_detail_instance = CeleryQueueTaskDetail.from_json(json)
# print the JSON string representation of the object
print(CeleryQueueTaskDetail.to_json())

# convert the object into a dict
celery_queue_task_detail_dict = celery_queue_task_detail_instance.to_dict()
# create an instance of CeleryQueueTaskDetail from a dict
celery_queue_task_detail_from_dict = CeleryQueueTaskDetail.from_dict(celery_queue_task_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


