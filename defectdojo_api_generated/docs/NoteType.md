# NoteType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | 
**is_single** | **bool** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_mandatory** | **bool** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.note_type import NoteType

# TODO update the JSON string below
json = "{}"
# create an instance of NoteType from a JSON string
note_type_instance = NoteType.from_json(json)
# print the JSON string representation of the object
print(NoteType.to_json())

# convert the object into a dict
note_type_dict = note_type_instance.to_dict()
# create an instance of NoteType from a dict
note_type_from_dict = NoteType.from_dict(note_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


