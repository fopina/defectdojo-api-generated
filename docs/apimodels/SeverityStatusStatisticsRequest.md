# SeverityStatusStatisticsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**StatusStatisticsRequest**](StatusStatisticsRequest.md) |  | [optional] 
**low** | [**StatusStatisticsRequest**](StatusStatisticsRequest.md) |  | [optional] 
**medium** | [**StatusStatisticsRequest**](StatusStatisticsRequest.md) |  | [optional] 
**high** | [**StatusStatisticsRequest**](StatusStatisticsRequest.md) |  | [optional] 
**critical** | [**StatusStatisticsRequest**](StatusStatisticsRequest.md) |  | [optional] 
**total** | [**StatusStatisticsRequest**](StatusStatisticsRequest.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.severity_status_statistics_request import SeverityStatusStatisticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SeverityStatusStatisticsRequest from a JSON string
severity_status_statistics_request_instance = SeverityStatusStatisticsRequest.from_json(json)
# print the JSON string representation of the object
print(SeverityStatusStatisticsRequest.to_json())

# convert the object into a dict
severity_status_statistics_request_dict = severity_status_statistics_request_instance.to_dict()
# create an instance of SeverityStatusStatisticsRequest from a dict
severity_status_statistics_request_from_dict = SeverityStatusStatisticsRequest.from_dict(severity_status_statistics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


