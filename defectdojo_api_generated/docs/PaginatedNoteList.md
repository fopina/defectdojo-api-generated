# PaginatedNoteList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Note]**](Note.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_note_list import PaginatedNoteList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedNoteList from a JSON string
paginated_note_list_instance = PaginatedNoteList.from_json(json)
# print the JSON string representation of the object
print(PaginatedNoteList.to_json())

# convert the object into a dict
paginated_note_list_dict = paginated_note_list_instance.to_dict()
# create an instance of PaginatedNoteList from a dict
paginated_note_list_from_dict = PaginatedNoteList.from_dict(paginated_note_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


