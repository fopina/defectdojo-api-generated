# PaginatedToolProductSettingsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ToolProductSettings]**](ToolProductSettings.md) |  | 
**prefetch** | [**PaginatedToolProductSettingsListPrefetch**](PaginatedToolProductSettingsListPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_tool_product_settings_list import PaginatedToolProductSettingsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedToolProductSettingsList from a JSON string
paginated_tool_product_settings_list_instance = PaginatedToolProductSettingsList.from_json(json)
# print the JSON string representation of the object
print(PaginatedToolProductSettingsList.to_json())

# convert the object into a dict
paginated_tool_product_settings_list_dict = paginated_tool_product_settings_list_instance.to_dict()
# create an instance of PaginatedToolProductSettingsList from a dict
paginated_tool_product_settings_list_from_dict = PaginatedToolProductSettingsList.from_dict(paginated_tool_product_settings_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


