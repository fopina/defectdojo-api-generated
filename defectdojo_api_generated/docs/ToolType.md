# ToolType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.tool_type import ToolType

# TODO update the JSON string below
json = "{}"
# create an instance of ToolType from a JSON string
tool_type_instance = ToolType.from_json(json)
# print the JSON string representation of the object
print(ToolType.to_json())

# convert the object into a dict
tool_type_dict = tool_type_instance.to_dict()
# create an instance of ToolType from a dict
tool_type_from_dict = ToolType.from_dict(tool_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


