# PaginatedToolProductSettingsListPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | [**Dict[str, Note]**](Note.md) |  | [optional] [readonly] 
**product** | [**Dict[str, Product]**](Product.md) |  | [optional] [readonly] 
**tool_configuration** | [**Dict[str, ToolConfiguration]**](ToolConfiguration.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.paginated_tool_product_settings_list_prefetch import PaginatedToolProductSettingsListPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedToolProductSettingsListPrefetch from a JSON string
paginated_tool_product_settings_list_prefetch_instance = PaginatedToolProductSettingsListPrefetch.from_json(json)
# print the JSON string representation of the object
print(PaginatedToolProductSettingsListPrefetch.to_json())

# convert the object into a dict
paginated_tool_product_settings_list_prefetch_dict = paginated_tool_product_settings_list_prefetch_instance.to_dict()
# create an instance of PaginatedToolProductSettingsListPrefetch from a dict
paginated_tool_product_settings_list_prefetch_from_dict = PaginatedToolProductSettingsListPrefetch.from_dict(paginated_tool_product_settings_list_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


