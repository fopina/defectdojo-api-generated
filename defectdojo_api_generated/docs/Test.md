# Test


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**tags** | **List[str]** |  | [optional] 
**test_type_name** | **str** |  | [readonly] 
**finding_groups** | [**List[FindingGroup]**](FindingGroup.md) |  | [readonly] 
**scan_type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**target_start** | **datetime** |  | 
**target_end** | **datetime** |  | 
**estimated_time** | **str** |  | [readonly] 
**actual_time** | **str** |  | [readonly] 
**percent_complete** | **int** |  | [optional] 
**updated** | **datetime** |  | [readonly] 
**created** | **datetime** |  | [readonly] 
**version** | **str** |  | [optional] 
**build_id** | **str** | Build ID that was tested, a reimport may update this field. | [optional] 
**commit_hash** | **str** | Commit hash tested, a reimport may update this field. | [optional] 
**branch_tag** | **str** | Tag or branch that was tested, a reimport may update this field. | [optional] 
**engagement** | **int** |  | [readonly] 
**lead** | **int** |  | [optional] 
**test_type** | **int** |  | 
**environment** | **int** |  | [optional] 
**api_scan_configuration** | **int** |  | [optional] 
**notes** | [**List[Note]**](Note.md) |  | [readonly] 
**files** | [**List[File]**](File.md) |  | [readonly] 

## Example

```python
from defectdojo_api_generated.models.test import Test

# TODO update the JSON string below
json = "{}"
# create an instance of Test from a JSON string
test_instance = Test.from_json(json)
# print the JSON string representation of the object
print(Test.to_json())

# convert the object into a dict
test_dict = test_instance.to_dict()
# create an instance of Test from a dict
test_from_dict = Test.from_dict(test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


