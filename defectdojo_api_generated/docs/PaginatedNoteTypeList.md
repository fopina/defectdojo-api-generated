# PaginatedNoteTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[NoteType]**](NoteType.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_note_type_list import PaginatedNoteTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedNoteTypeList from a JSON string
paginated_note_type_list_instance = PaginatedNoteTypeList.from_json(json)
# print the JSON string representation of the object
print(PaginatedNoteTypeList.to_json())

# convert the object into a dict
paginated_note_type_list_dict = paginated_note_type_list_instance.to_dict()
# create an instance of PaginatedNoteTypeList from a dict
paginated_note_type_list_from_dict = PaginatedNoteTypeList.from_dict(paginated_note_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


