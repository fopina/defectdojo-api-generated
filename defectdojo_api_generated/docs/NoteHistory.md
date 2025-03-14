# NoteHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**current_editor** | [**UserStub**](UserStub.md) |  | [readonly] 
**note_type** | [**NoteType**](NoteType.md) |  | [readonly] 
**data** | **str** |  | 
**time** | **datetime** |  | [readonly] 

## Example

```python
from defectdojo_api_generated.models.note_history import NoteHistory

# TODO update the JSON string below
json = "{}"
# create an instance of NoteHistory from a JSON string
note_history_instance = NoteHistory.from_json(json)
# print the JSON string representation of the object
print(NoteHistory.to_json())

# convert the object into a dict
note_history_dict = note_history_instance.to_dict()
# create an instance of NoteHistory from a dict
note_history_from_dict = NoteHistory.from_dict(note_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


