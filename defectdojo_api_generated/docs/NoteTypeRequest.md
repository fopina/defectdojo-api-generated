# NoteTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**is_single** | **bool** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_mandatory** | **bool** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.note_type_request import NoteTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NoteTypeRequest from a JSON string
note_type_request_instance = NoteTypeRequest.from_json(json)
# print the JSON string representation of the object
print(NoteTypeRequest.to_json())

# convert the object into a dict
note_type_request_dict = note_type_request_instance.to_dict()
# create an instance of NoteTypeRequest from a dict
note_type_request_from_dict = NoteTypeRequest.from_dict(note_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


