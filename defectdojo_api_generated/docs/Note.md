# Note


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**author** | [**UserStub**](UserStub.md) |  | [readonly] 
**editor** | [**UserStub**](UserStub.md) |  | [readonly] 
**history** | [**List[NoteHistory]**](NoteHistory.md) |  | [readonly] 
**note_type** | [**NoteType**](NoteType.md) |  | [readonly] 
**entry** | **str** |  | 
**var_date** | **datetime** |  | [readonly] 
**private** | **bool** |  | [optional] 
**edited** | **bool** |  | [optional] 
**edit_time** | **datetime** |  | [readonly] 

## Example

```python
from defectdojo_api_generated.models.note import Note

# TODO update the JSON string below
json = "{}"
# create an instance of Note from a JSON string
note_instance = Note.from_json(json)
# print the JSON string representation of the object
print(Note.to_json())

# convert the object into a dict
note_dict = note_instance.to_dict()
# create an instance of Note from a dict
note_from_dict = Note.from_dict(note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


