# SonarqubeIssue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**key** | **str** | SonarQube issue key | 
**status** | **str** | SonarQube issue status | 
**type** | **str** | SonarQube issue type | 

## Example

```python
from defectdojo_api_generated.models.sonarqube_issue import SonarqubeIssue

# TODO update the JSON string below
json = "{}"
# create an instance of SonarqubeIssue from a JSON string
sonarqube_issue_instance = SonarqubeIssue.from_json(json)
# print the JSON string representation of the object
print(SonarqubeIssue.to_json())

# convert the object into a dict
sonarqube_issue_dict = sonarqube_issue_instance.to_dict()
# create an instance of SonarqubeIssue from a dict
sonarqube_issue_from_dict = SonarqubeIssue.from_dict(sonarqube_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


