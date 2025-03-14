# PatchedNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | **str** |  | [optional] 
**private** | **bool** |  | [optional] 
**edited** | **bool** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_note_request import PatchedNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedNoteRequest from a JSON string
patched_note_request_instance = PatchedNoteRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedNoteRequest.to_json())

# convert the object into a dict
patched_note_request_dict = patched_note_request_instance.to_dict()
# create an instance of PatchedNoteRequest from a dict
patched_note_request_from_dict = PatchedNoteRequest.from_dict(patched_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


