# PaginatedTestTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[TestType]**](TestType.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_test_type_list import PaginatedTestTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTestTypeList from a JSON string
paginated_test_type_list_instance = PaginatedTestTypeList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTestTypeList.to_json())

# convert the object into a dict
paginated_test_type_list_dict = paginated_test_type_list_instance.to_dict()
# create an instance of PaginatedTestTypeList from a dict
paginated_test_type_list_from_dict = PaginatedTestTypeList.from_dict(paginated_test_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


