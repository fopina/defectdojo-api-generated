# EngagementToNotes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engagement_id** | **int** |  | 
**notes** | [**List[Note]**](Note.md) |  | 

## Example

```python
from defectdojo_api_generated.models.engagement_to_notes import EngagementToNotes

# TODO update the JSON string below
json = "{}"
# create an instance of EngagementToNotes from a JSON string
engagement_to_notes_instance = EngagementToNotes.from_json(json)
# print the JSON string representation of the object
print(EngagementToNotes.to_json())

# convert the object into a dict
engagement_to_notes_dict = engagement_to_notes_instance.to_dict()
# create an instance of EngagementToNotes from a dict
engagement_to_notes_from_dict = EngagementToNotes.from_dict(engagement_to_notes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


