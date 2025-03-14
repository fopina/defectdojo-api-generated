# FindingGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**test** | **int** |  | 
**jira_issue** | [**JIRAIssue**](JIRAIssue.md) |  | [readonly] 

## Example

```python
from defectdojo_api_generated.models.finding_group import FindingGroup

# TODO update the JSON string below
json = "{}"
# create an instance of FindingGroup from a JSON string
finding_group_instance = FindingGroup.from_json(json)
# print the JSON string representation of the object
print(FindingGroup.to_json())

# convert the object into a dict
finding_group_dict = finding_group_instance.to_dict()
# create an instance of FindingGroup from a dict
finding_group_from_dict = FindingGroup.from_dict(finding_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


