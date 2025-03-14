# PaginatedMetaList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Meta]**](Meta.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_meta_list import PaginatedMetaList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMetaList from a JSON string
paginated_meta_list_instance = PaginatedMetaList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMetaList.to_json())

# convert the object into a dict
paginated_meta_list_dict = paginated_meta_list_instance.to_dict()
# create an instance of PaginatedMetaList from a dict
paginated_meta_list_from_dict = PaginatedMetaList.from_dict(paginated_meta_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


