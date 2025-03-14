# PatchedJIRAIssueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jira_id** | **str** |  | [optional] 
**jira_key** | **str** |  | [optional] 
**jira_creation** | **datetime** | The date a Jira issue was created from this finding. | [optional] 
**jira_change** | **datetime** | The date the linked Jira issue was last modified. | [optional] 
**jira_project** | **int** |  | [optional] 
**finding** | **int** |  | [optional] 
**engagement** | **int** |  | [optional] 
**finding_group** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_jira_issue_request import PatchedJIRAIssueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedJIRAIssueRequest from a JSON string
patched_jira_issue_request_instance = PatchedJIRAIssueRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedJIRAIssueRequest.to_json())

# convert the object into a dict
patched_jira_issue_request_dict = patched_jira_issue_request_instance.to_dict()
# create an instance of PatchedJIRAIssueRequest from a dict
patched_jira_issue_request_from_dict = PatchedJIRAIssueRequest.from_dict(patched_jira_issue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


