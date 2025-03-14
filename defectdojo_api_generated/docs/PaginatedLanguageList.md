# PaginatedLanguageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Language]**](Language.md) |  | 
**prefetch** | [**LanguagePrefetch**](LanguagePrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_language_list import PaginatedLanguageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLanguageList from a JSON string
paginated_language_list_instance = PaginatedLanguageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedLanguageList.to_json())

# convert the object into a dict
paginated_language_list_dict = paginated_language_list_instance.to_dict()
# create an instance of PaginatedLanguageList from a dict
paginated_language_list_from_dict = PaginatedLanguageList.from_dict(paginated_language_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


