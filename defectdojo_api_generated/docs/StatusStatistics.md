# StatusStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **int** |  | 
**verified** | **int** |  | 
**duplicate** | **int** |  | 
**false_p** | **int** |  | 
**out_of_scope** | **int** |  | 
**is_mitigated** | **int** |  | 
**risk_accepted** | **int** |  | 
**total** | **int** |  | 

## Example

```python
from defectdojo_api_generated.models.status_statistics import StatusStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of StatusStatistics from a JSON string
status_statistics_instance = StatusStatistics.from_json(json)
# print the JSON string representation of the object
print(StatusStatistics.to_json())

# convert the object into a dict
status_statistics_dict = status_statistics_instance.to_dict()
# create an instance of StatusStatistics from a dict
status_statistics_from_dict = StatusStatistics.from_dict(status_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


