# PaginatedToolConfigurationListPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_type** | [**Dict[str, ToolType]**](ToolType.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.paginated_tool_configuration_list_prefetch import PaginatedToolConfigurationListPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedToolConfigurationListPrefetch from a JSON string
paginated_tool_configuration_list_prefetch_instance = PaginatedToolConfigurationListPrefetch.from_json(json)
# print the JSON string representation of the object
print(PaginatedToolConfigurationListPrefetch.to_json())

# convert the object into a dict
paginated_tool_configuration_list_prefetch_dict = paginated_tool_configuration_list_prefetch_instance.to_dict()
# create an instance of PaginatedToolConfigurationListPrefetch from a dict
paginated_tool_configuration_list_prefetch_from_dict = PaginatedToolConfigurationListPrefetch.from_dict(paginated_tool_configuration_list_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


