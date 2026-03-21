# RiskAcceptanceToNotes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**risk_acceptance_id** | **int** |  | [optional] 
**notes** | [**List[Note]**](Note.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.risk_acceptance_to_notes import RiskAcceptanceToNotes

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAcceptanceToNotes from a JSON string
risk_acceptance_to_notes_instance = RiskAcceptanceToNotes.from_json(json)
# print the JSON string representation of the object
print(RiskAcceptanceToNotes.to_json())

# convert the object into a dict
risk_acceptance_to_notes_dict = risk_acceptance_to_notes_instance.to_dict()
# create an instance of RiskAcceptanceToNotes from a dict
risk_acceptance_to_notes_from_dict = RiskAcceptanceToNotes.from_dict(risk_acceptance_to_notes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


