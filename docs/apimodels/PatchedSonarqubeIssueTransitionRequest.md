# PatchedSonarqubeIssueTransitionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finding_status** | **str** |  | [optional] 
**sonarqube_status** | **str** |  | [optional] 
**transitions** | **str** |  | [optional] 
**sonarqube_issue** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_sonarqube_issue_transition_request import PatchedSonarqubeIssueTransitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSonarqubeIssueTransitionRequest from a JSON string
patched_sonarqube_issue_transition_request_instance = PatchedSonarqubeIssueTransitionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedSonarqubeIssueTransitionRequest.to_json())

# convert the object into a dict
patched_sonarqube_issue_transition_request_dict = patched_sonarqube_issue_transition_request_instance.to_dict()
# create an instance of PatchedSonarqubeIssueTransitionRequest from a dict
patched_sonarqube_issue_transition_request_from_dict = PatchedSonarqubeIssueTransitionRequest.from_dict(patched_sonarqube_issue_transition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


