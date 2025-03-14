# PatchedTestTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**static_tool** | **bool** |  | [optional] 
**dynamic_tool** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_test_type_request import PatchedTestTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTestTypeRequest from a JSON string
patched_test_type_request_instance = PatchedTestTypeRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedTestTypeRequest.to_json())

# convert the object into a dict
patched_test_type_request_dict = patched_test_type_request_instance.to_dict()
# create an instance of PatchedTestTypeRequest from a dict
patched_test_type_request_from_dict = PatchedTestTypeRequest.from_dict(patched_test_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


