# SonarqubeIssueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | SonarQube issue key | 
**status** | **str** | SonarQube issue status | 
**type** | **str** | SonarQube issue type | 

## Example

```python
from defectdojo_api_generated.models.sonarqube_issue_request import SonarqubeIssueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SonarqubeIssueRequest from a JSON string
sonarqube_issue_request_instance = SonarqubeIssueRequest.from_json(json)
# print the JSON string representation of the object
print(SonarqubeIssueRequest.to_json())

# convert the object into a dict
sonarqube_issue_request_dict = sonarqube_issue_request_instance.to_dict()
# create an instance of SonarqubeIssueRequest from a dict
sonarqube_issue_request_from_dict = SonarqubeIssueRequest.from_dict(sonarqube_issue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


