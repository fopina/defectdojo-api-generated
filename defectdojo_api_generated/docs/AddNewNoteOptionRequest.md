# AddNewNoteOptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | **str** |  | 
**private** | **bool** |  | [optional] 
**note_type** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.add_new_note_option_request import AddNewNoteOptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddNewNoteOptionRequest from a JSON string
add_new_note_option_request_instance = AddNewNoteOptionRequest.from_json(json)
# print the JSON string representation of the object
print(AddNewNoteOptionRequest.to_json())

# convert the object into a dict
add_new_note_option_request_dict = add_new_note_option_request_instance.to_dict()
# create an instance of AddNewNoteOptionRequest from a dict
add_new_note_option_request_from_dict = AddNewNoteOptionRequest.from_dict(add_new_note_option_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


