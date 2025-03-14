# DeltaStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | [**SeverityStatusStatistics**](SeverityStatusStatistics.md) |  | 
**closed** | [**SeverityStatusStatistics**](SeverityStatusStatistics.md) |  | 
**reactivated** | [**SeverityStatusStatistics**](SeverityStatusStatistics.md) |  | 
**left_untouched** | [**SeverityStatusStatistics**](SeverityStatusStatistics.md) |  | 

## Example

```python
from defectdojo_api_generated.models.delta_statistics import DeltaStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of DeltaStatistics from a JSON string
delta_statistics_instance = DeltaStatistics.from_json(json)
# print the JSON string representation of the object
print(DeltaStatistics.to_json())

# convert the object into a dict
delta_statistics_dict = delta_statistics_instance.to_dict()
# create an instance of DeltaStatistics from a dict
delta_statistics_from_dict = DeltaStatistics.from_dict(delta_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


