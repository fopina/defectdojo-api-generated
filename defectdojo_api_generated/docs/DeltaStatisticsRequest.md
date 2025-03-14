# DeltaStatisticsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | [**SeverityStatusStatisticsRequest**](SeverityStatusStatisticsRequest.md) |  | 
**closed** | [**SeverityStatusStatisticsRequest**](SeverityStatusStatisticsRequest.md) |  | 
**reactivated** | [**SeverityStatusStatisticsRequest**](SeverityStatusStatisticsRequest.md) |  | 
**left_untouched** | [**SeverityStatusStatisticsRequest**](SeverityStatusStatisticsRequest.md) |  | 

## Example

```python
from defectdojo_api_generated.models.delta_statistics_request import DeltaStatisticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeltaStatisticsRequest from a JSON string
delta_statistics_request_instance = DeltaStatisticsRequest.from_json(json)
# print the JSON string representation of the object
print(DeltaStatisticsRequest.to_json())

# convert the object into a dict
delta_statistics_request_dict = delta_statistics_request_instance.to_dict()
# create an instance of DeltaStatisticsRequest from a dict
delta_statistics_request_from_dict = DeltaStatisticsRequest.from_dict(delta_statistics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


