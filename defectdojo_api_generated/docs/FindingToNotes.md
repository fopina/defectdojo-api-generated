# FindingToNotes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finding_id** | **int** |  | 
**notes** | [**List[Note]**](Note.md) |  | 

## Example

```python
from defectdojo_api_generated.models.finding_to_notes import FindingToNotes

# TODO update the JSON string below
json = "{}"
# create an instance of FindingToNotes from a JSON string
finding_to_notes_instance = FindingToNotes.from_json(json)
# print the JSON string representation of the object
print(FindingToNotes.to_json())

# convert the object into a dict
finding_to_notes_dict = finding_to_notes_instance.to_dict()
# create an instance of FindingToNotes from a dict
finding_to_notes_from_dict = FindingToNotes.from_dict(finding_to_notes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


