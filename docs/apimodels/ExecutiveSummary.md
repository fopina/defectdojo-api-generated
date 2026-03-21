# ExecutiveSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engagement_name** | **str** |  | [optional] 
**engagement_target_start** | **date** |  | [optional] 
**engagement_target_end** | **date** |  | [optional] 
**test_type_name** | **str** |  | [optional] 
**test_target_start** | **datetime** |  | [optional] 
**test_target_end** | **datetime** |  | [optional] 
**test_environment_name** | **str** |  | [optional] 
**test_strategy_ref** | **str** |  | [optional] 
**total_findings** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.executive_summary import ExecutiveSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutiveSummary from a JSON string
executive_summary_instance = ExecutiveSummary.from_json(json)
# print the JSON string representation of the object
print(ExecutiveSummary.to_json())

# convert the object into a dict
executive_summary_dict = executive_summary_instance.to_dict()
# create an instance of ExecutiveSummary from a dict
executive_summary_from_dict = ExecutiveSummary.from_dict(executive_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


