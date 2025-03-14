# PaginatedDeletePreviewList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DeletePreview]**](DeletePreview.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_delete_preview_list import PaginatedDeletePreviewList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDeletePreviewList from a JSON string
paginated_delete_preview_list_instance = PaginatedDeletePreviewList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDeletePreviewList.to_json())

# convert the object into a dict
paginated_delete_preview_list_dict = paginated_delete_preview_list_instance.to_dict()
# create an instance of PaginatedDeletePreviewList from a dict
paginated_delete_preview_list_from_dict = PaginatedDeletePreviewList.from_dict(paginated_delete_preview_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


