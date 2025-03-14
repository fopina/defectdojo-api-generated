# PaginatedToolTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ToolType]**](ToolType.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_tool_type_list import PaginatedToolTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedToolTypeList from a JSON string
paginated_tool_type_list_instance = PaginatedToolTypeList.from_json(json)
# print the JSON string representation of the object
print(PaginatedToolTypeList.to_json())

# convert the object into a dict
paginated_tool_type_list_dict = paginated_tool_type_list_instance.to_dict()
# create an instance of PaginatedToolTypeList from a dict
paginated_tool_type_list_from_dict = PaginatedToolTypeList.from_dict(paginated_tool_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


