# CeleryStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**worker_status** | **bool** |  | [optional] [readonly] 
**broker_status** | **bool** |  | [optional] [readonly] 
**queue_length** | **int** |  | [optional] [readonly] 
**task_time_limit** | **int** |  | [optional] [readonly] 
**task_soft_time_limit** | **int** |  | [optional] [readonly] 
**task_default_expires** | **int** |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.celery_status import CeleryStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CeleryStatus from a JSON string
celery_status_instance = CeleryStatus.from_json(json)
# print the JSON string representation of the object
print(CeleryStatus.to_json())

# convert the object into a dict
celery_status_dict = celery_status_instance.to_dict()
# create an instance of CeleryStatus from a dict
celery_status_from_dict = CeleryStatus.from_dict(celery_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


