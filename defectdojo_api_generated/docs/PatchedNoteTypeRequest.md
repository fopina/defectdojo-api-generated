# PatchedNoteTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_single** | **bool** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_mandatory** | **bool** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_note_type_request import PatchedNoteTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedNoteTypeRequest from a JSON string
patched_note_type_request_instance = PatchedNoteTypeRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedNoteTypeRequest.to_json())

# convert the object into a dict
patched_note_type_request_dict = patched_note_type_request_instance.to_dict()
# create an instance of PatchedNoteTypeRequest from a dict
patched_note_type_request_from_dict = PatchedNoteTypeRequest.from_dict(patched_note_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


