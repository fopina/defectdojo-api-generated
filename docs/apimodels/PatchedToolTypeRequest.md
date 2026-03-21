# PatchedToolTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_tool_type_request import PatchedToolTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedToolTypeRequest from a JSON string
patched_tool_type_request_instance = PatchedToolTypeRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedToolTypeRequest.to_json())

# convert the object into a dict
patched_tool_type_request_dict = patched_tool_type_request_instance.to_dict()
# create an instance of PatchedToolTypeRequest from a dict
patched_tool_type_request_from_dict = PatchedToolTypeRequest.from_dict(patched_tool_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


