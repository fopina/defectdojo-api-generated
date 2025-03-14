# ToolProductSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**setting_url** | **str** |  | 
**product** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**tool_project_id** | **str** |  | [optional] 
**tool_configuration** | **int** |  | 
**notes** | **List[int]** |  | [readonly] 
**prefetch** | [**PaginatedToolProductSettingsListPrefetch**](PaginatedToolProductSettingsListPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.tool_product_settings import ToolProductSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ToolProductSettings from a JSON string
tool_product_settings_instance = ToolProductSettings.from_json(json)
# print the JSON string representation of the object
print(ToolProductSettings.to_json())

# convert the object into a dict
tool_product_settings_dict = tool_product_settings_instance.to_dict()
# create an instance of ToolProductSettings from a dict
tool_product_settings_from_dict = ToolProductSettings.from_dict(tool_product_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


