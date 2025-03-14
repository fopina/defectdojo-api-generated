# PaginatedToolConfigurationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ToolConfiguration]**](ToolConfiguration.md) |  | 
**prefetch** | [**PaginatedToolConfigurationListPrefetch**](PaginatedToolConfigurationListPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_tool_configuration_list import PaginatedToolConfigurationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedToolConfigurationList from a JSON string
paginated_tool_configuration_list_instance = PaginatedToolConfigurationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedToolConfigurationList.to_json())

# convert the object into a dict
paginated_tool_configuration_list_dict = paginated_tool_configuration_list_instance.to_dict()
# create an instance of PaginatedToolConfigurationList from a dict
paginated_tool_configuration_list_from_dict = PaginatedToolConfigurationList.from_dict(paginated_tool_configuration_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


