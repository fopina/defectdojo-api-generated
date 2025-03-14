# PaginatedLanguageTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[LanguageType]**](LanguageType.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_language_type_list import PaginatedLanguageTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLanguageTypeList from a JSON string
paginated_language_type_list_instance = PaginatedLanguageTypeList.from_json(json)
# print the JSON string representation of the object
print(PaginatedLanguageTypeList.to_json())

# convert the object into a dict
paginated_language_type_list_dict = paginated_language_type_list_instance.to_dict()
# create an instance of PaginatedLanguageTypeList from a dict
paginated_language_type_list_from_dict = PaginatedLanguageTypeList.from_dict(paginated_language_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


