# PaginatedJIRAIssueList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[JIRAIssue]**](JIRAIssue.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_jira_issue_list import PaginatedJIRAIssueList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedJIRAIssueList from a JSON string
paginated_jira_issue_list_instance = PaginatedJIRAIssueList.from_json(json)
# print the JSON string representation of the object
print(PaginatedJIRAIssueList.to_json())

# convert the object into a dict
paginated_jira_issue_list_dict = paginated_jira_issue_list_instance.to_dict()
# create an instance of PaginatedJIRAIssueList from a dict
paginated_jira_issue_list_from_dict = PaginatedJIRAIssueList.from_dict(paginated_jira_issue_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


