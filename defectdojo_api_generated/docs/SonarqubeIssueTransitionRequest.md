# SonarqubeIssueTransitionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finding_status** | **str** |  | 
**sonarqube_status** | **str** |  | 
**transitions** | **str** |  | 
**sonarqube_issue** | **int** |  | 

## Example

```python
from defectdojo_api_generated.models.sonarqube_issue_transition_request import SonarqubeIssueTransitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SonarqubeIssueTransitionRequest from a JSON string
sonarqube_issue_transition_request_instance = SonarqubeIssueTransitionRequest.from_json(json)
# print the JSON string representation of the object
print(SonarqubeIssueTransitionRequest.to_json())

# convert the object into a dict
sonarqube_issue_transition_request_dict = sonarqube_issue_transition_request_instance.to_dict()
# create an instance of SonarqubeIssueTransitionRequest from a dict
sonarqube_issue_transition_request_from_dict = SonarqubeIssueTransitionRequest.from_dict(sonarqube_issue_transition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


