# TestToNotes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_id** | **int** |  | 
**notes** | [**List[Note]**](Note.md) |  | 

## Example

```python
from defectdojo_api_generated.models.test_to_notes import TestToNotes

# TODO update the JSON string below
json = "{}"
# create an instance of TestToNotes from a JSON string
test_to_notes_instance = TestToNotes.from_json(json)
# print the JSON string representation of the object
print(TestToNotes.to_json())

# convert the object into a dict
test_to_notes_dict = test_to_notes_instance.to_dict()
# create an instance of TestToNotes from a dict
test_to_notes_from_dict = TestToNotes.from_dict(test_to_notes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


