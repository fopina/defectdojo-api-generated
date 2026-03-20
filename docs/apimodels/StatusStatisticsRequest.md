# StatusStatisticsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **int** |  | [optional] 
**verified** | **int** |  | [optional] 
**duplicate** | **int** |  | [optional] 
**false_p** | **int** |  | [optional] 
**out_of_scope** | **int** |  | [optional] 
**is_mitigated** | **int** |  | [optional] 
**risk_accepted** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.status_statistics_request import StatusStatisticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StatusStatisticsRequest from a JSON string
status_statistics_request_instance = StatusStatisticsRequest.from_json(json)
# print the JSON string representation of the object
print(StatusStatisticsRequest.to_json())

# convert the object into a dict
status_statistics_request_dict = status_statistics_request_instance.to_dict()
# create an instance of StatusStatisticsRequest from a dict
status_statistics_request_from_dict = StatusStatisticsRequest.from_dict(status_statistics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


