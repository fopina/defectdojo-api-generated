# PaginatedSonarqubeIssueList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[SonarqubeIssue]**](SonarqubeIssue.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_sonarqube_issue_list import PaginatedSonarqubeIssueList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSonarqubeIssueList from a JSON string
paginated_sonarqube_issue_list_instance = PaginatedSonarqubeIssueList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSonarqubeIssueList.to_json())

# convert the object into a dict
paginated_sonarqube_issue_list_dict = paginated_sonarqube_issue_list_instance.to_dict()
# create an instance of PaginatedSonarqubeIssueList from a dict
paginated_sonarqube_issue_list_from_dict = PaginatedSonarqubeIssueList.from_dict(paginated_sonarqube_issue_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


