# PatchedTestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | [optional] 
**scan_type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**target_start** | **datetime** |  | [optional] 
**target_end** | **datetime** |  | [optional] 
**percent_complete** | **int** |  | [optional] 
**version** | **str** |  | [optional] 
**build_id** | **str** | Build ID that was tested, a reimport may update this field. | [optional] 
**commit_hash** | **str** | Commit hash tested, a reimport may update this field. | [optional] 
**branch_tag** | **str** | Tag or branch that was tested, a reimport may update this field. | [optional] 
**lead** | **int** |  | [optional] 
**test_type** | **int** |  | [optional] 
**environment** | **int** |  | [optional] 
**api_scan_configuration** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_test_request import PatchedTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTestRequest from a JSON string
patched_test_request_instance = PatchedTestRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedTestRequest.to_json())

# convert the object into a dict
patched_test_request_dict = patched_test_request_instance.to_dict()
# create an instance of PatchedTestRequest from a dict
patched_test_request_from_dict = PatchedTestRequest.from_dict(patched_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


