# JIRAIssueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jira_id** | **str** |  | 
**jira_key** | **str** |  | 
**jira_creation** | **datetime** | The date a Jira issue was created from this finding. | [optional] 
**jira_change** | **datetime** | The date the linked Jira issue was last modified. | [optional] 
**jira_project** | **int** |  | [optional] 
**finding** | **int** |  | [optional] 
**engagement** | **int** |  | [optional] 
**finding_group** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.jira_issue_request import JIRAIssueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JIRAIssueRequest from a JSON string
jira_issue_request_instance = JIRAIssueRequest.from_json(json)
# print the JSON string representation of the object
print(JIRAIssueRequest.to_json())

# convert the object into a dict
jira_issue_request_dict = jira_issue_request_instance.to_dict()
# create an instance of JIRAIssueRequest from a dict
jira_issue_request_from_dict = JIRAIssueRequest.from_dict(jira_issue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


