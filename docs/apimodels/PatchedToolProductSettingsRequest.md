# PatchedToolProductSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**setting_url** | **str** |  | [optional] 
**product** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**tool_project_id** | **str** |  | [optional] 
**tool_configuration** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_tool_product_settings_request import PatchedToolProductSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedToolProductSettingsRequest from a JSON string
patched_tool_product_settings_request_instance = PatchedToolProductSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedToolProductSettingsRequest.to_json())

# convert the object into a dict
patched_tool_product_settings_request_dict = patched_tool_product_settings_request_instance.to_dict()
# create an instance of PatchedToolProductSettingsRequest from a dict
patched_tool_product_settings_request_from_dict = PatchedToolProductSettingsRequest.from_dict(patched_tool_product_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


