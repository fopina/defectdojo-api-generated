# ToolTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.tool_type_request import ToolTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ToolTypeRequest from a JSON string
tool_type_request_instance = ToolTypeRequest.from_json(json)
# print the JSON string representation of the object
print(ToolTypeRequest.to_json())

# convert the object into a dict
tool_type_request_dict = tool_type_request_instance.to_dict()
# create an instance of ToolTypeRequest from a dict
tool_type_request_from_dict = ToolTypeRequest.from_dict(tool_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


