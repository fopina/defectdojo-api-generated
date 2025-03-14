# FindingRelatedFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test** | [**FindingTest**](FindingTest.md) |  | [readonly] 
**jira** | [**JIRAIssue**](JIRAIssue.md) |  | [readonly] 

## Example

```python
from defectdojo_api_generated.models.finding_related_fields import FindingRelatedFields

# TODO update the JSON string below
json = "{}"
# create an instance of FindingRelatedFields from a JSON string
finding_related_fields_instance = FindingRelatedFields.from_json(json)
# print the JSON string representation of the object
print(FindingRelatedFields.to_json())

# convert the object into a dict
finding_related_fields_dict = finding_related_fields_instance.to_dict()
# create an instance of FindingRelatedFields from a dict
finding_related_fields_from_dict = FindingRelatedFields.from_dict(finding_related_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


