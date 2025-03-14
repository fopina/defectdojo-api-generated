# SeverityStatusStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**StatusStatistics**](StatusStatistics.md) |  | 
**low** | [**StatusStatistics**](StatusStatistics.md) |  | 
**medium** | [**StatusStatistics**](StatusStatistics.md) |  | 
**high** | [**StatusStatistics**](StatusStatistics.md) |  | 
**critical** | [**StatusStatistics**](StatusStatistics.md) |  | 
**total** | [**StatusStatistics**](StatusStatistics.md) |  | 

## Example

```python
from defectdojo_api_generated.models.severity_status_statistics import SeverityStatusStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of SeverityStatusStatistics from a JSON string
severity_status_statistics_instance = SeverityStatusStatistics.from_json(json)
# print the JSON string representation of the object
print(SeverityStatusStatistics.to_json())

# convert the object into a dict
severity_status_statistics_dict = severity_status_statistics_instance.to_dict()
# create an instance of SeverityStatusStatistics from a dict
severity_status_statistics_from_dict = SeverityStatusStatistics.from_dict(severity_status_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


