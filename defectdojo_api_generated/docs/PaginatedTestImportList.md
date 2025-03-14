# PaginatedTestImportList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[TestImport]**](TestImport.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_test_import_list import PaginatedTestImportList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTestImportList from a JSON string
paginated_test_import_list_instance = PaginatedTestImportList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTestImportList.to_json())

# convert the object into a dict
paginated_test_import_list_dict = paginated_test_import_list_instance.to_dict()
# create an instance of PaginatedTestImportList from a dict
paginated_test_import_list_from_dict = PaginatedTestImportList.from_dict(paginated_test_import_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


