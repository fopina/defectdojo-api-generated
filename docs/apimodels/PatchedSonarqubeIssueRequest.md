# PatchedSonarqubeIssueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | SonarQube issue key | [optional] 
**status** | **str** | SonarQube issue status | [optional] 
**type** | **str** | SonarQube issue type | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_sonarqube_issue_request import PatchedSonarqubeIssueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSonarqubeIssueRequest from a JSON string
patched_sonarqube_issue_request_instance = PatchedSonarqubeIssueRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedSonarqubeIssueRequest.to_json())

# convert the object into a dict
patched_sonarqube_issue_request_dict = patched_sonarqube_issue_request_instance.to_dict()
# create an instance of PatchedSonarqubeIssueRequest from a dict
patched_sonarqube_issue_request_from_dict = PatchedSonarqubeIssueRequest.from_dict(patched_sonarqube_issue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


