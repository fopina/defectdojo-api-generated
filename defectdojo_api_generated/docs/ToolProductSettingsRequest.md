# ToolProductSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**setting_url** | **str** |  | 
**product** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**tool_project_id** | **str** |  | [optional] 
**tool_configuration** | **int** |  | 

## Example

```python
from defectdojo_api_generated.models.tool_product_settings_request import ToolProductSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ToolProductSettingsRequest from a JSON string
tool_product_settings_request_instance = ToolProductSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(ToolProductSettingsRequest.to_json())

# convert the object into a dict
tool_product_settings_request_dict = tool_product_settings_request_instance.to_dict()
# create an instance of ToolProductSettingsRequest from a dict
tool_product_settings_request_from_dict = ToolProductSettingsRequest.from_dict(tool_product_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


