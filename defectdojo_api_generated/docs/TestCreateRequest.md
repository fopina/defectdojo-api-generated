# TestCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engagement** | **int** |  | 
**notes** | **List[Optional[int]]** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**scan_type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**target_start** | **datetime** |  | 
**target_end** | **datetime** |  | 
**percent_complete** | **int** |  | [optional] 
**version** | **str** |  | [optional] 
**build_id** | **str** | Build ID that was tested, a reimport may update this field. | [optional] 
**commit_hash** | **str** | Commit hash tested, a reimport may update this field. | [optional] 
**branch_tag** | **str** | Tag or branch that was tested, a reimport may update this field. | [optional] 
**lead** | **int** |  | [optional] 
**test_type** | **int** |  | 
**environment** | **int** |  | [optional] 
**api_scan_configuration** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.test_create_request import TestCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestCreateRequest from a JSON string
test_create_request_instance = TestCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TestCreateRequest.to_json())

# convert the object into a dict
test_create_request_dict = test_create_request_instance.to_dict()
# create an instance of TestCreateRequest from a dict
test_create_request_from_dict = TestCreateRequest.from_dict(test_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


