# SonarqubeIssueTransition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**created** | **datetime** |  | [readonly] 
**finding_status** | **str** |  | 
**sonarqube_status** | **str** |  | 
**transitions** | **str** |  | 
**sonarqube_issue** | **int** |  | 

## Example

```python
from defectdojo_api_generated.models.sonarqube_issue_transition import SonarqubeIssueTransition

# TODO update the JSON string below
json = "{}"
# create an instance of SonarqubeIssueTransition from a JSON string
sonarqube_issue_transition_instance = SonarqubeIssueTransition.from_json(json)
# print the JSON string representation of the object
print(SonarqubeIssueTransition.to_json())

# convert the object into a dict
sonarqube_issue_transition_dict = sonarqube_issue_transition_instance.to_dict()
# create an instance of SonarqubeIssueTransition from a dict
sonarqube_issue_transition_from_dict = SonarqubeIssueTransition.from_dict(sonarqube_issue_transition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


