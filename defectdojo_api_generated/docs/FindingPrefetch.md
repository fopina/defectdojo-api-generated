# FindingPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_issues** | [**Dict[str, EngagementCheckList]**](EngagementCheckList.md) |  | [optional] [readonly] 
**author_issues** | [**Dict[str, EngagementCheckList]**](EngagementCheckList.md) |  | [optional] [readonly] 
**config_issues** | [**Dict[str, EngagementCheckList]**](EngagementCheckList.md) |  | [optional] [readonly] 
**crypto_issues** | [**Dict[str, EngagementCheckList]**](EngagementCheckList.md) |  | [optional] [readonly] 
**data_issues** | [**Dict[str, EngagementCheckList]**](EngagementCheckList.md) |  | [optional] [readonly] 
**defect_review_requested_by** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 
**duplicate_finding** | [**Dict[str, Finding]**](Finding.md) |  | [optional] [readonly] 
**endpoint_set** | [**Dict[str, Endpoint]**](Endpoint.md) |  | [optional] [readonly] 
**endpoints** | [**Dict[str, Endpoint]**](Endpoint.md) |  | [optional] [readonly] 
**files** | [**Dict[str, File]**](File.md) |  | [optional] [readonly] 
**finding_group_set** | [**Dict[str, FindingGroup]**](FindingGroup.md) |  | [optional] [readonly] 
**found_by** | [**Dict[str, TestType]**](TestType.md) |  | [optional] [readonly] 
**last_reviewed_by** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 
**mitigated_by** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 
**notes** | [**Dict[str, Note]**](Note.md) |  | [optional] [readonly] 
**other_issues** | [**Dict[str, EngagementCheckList]**](EngagementCheckList.md) |  | [optional] [readonly] 
**reporter** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 
**review_requested_by** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 
**reviewers** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 
**risk_acceptance_set** | [**Dict[str, RiskAcceptance]**](RiskAcceptance.md) |  | [optional] [readonly] 
**sensitive_issues** | [**Dict[str, EngagementCheckList]**](EngagementCheckList.md) |  | [optional] [readonly] 
**session_issues** | [**Dict[str, EngagementCheckList]**](EngagementCheckList.md) |  | [optional] [readonly] 
**sonarqube_issue** | [**Dict[str, SonarqubeIssue]**](SonarqubeIssue.md) |  | [optional] [readonly] 
**test** | [**Dict[str, Test]**](Test.md) |  | [optional] [readonly] 
**test_import_set** | [**Dict[str, TestImport]**](TestImport.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.finding_prefetch import FindingPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of FindingPrefetch from a JSON string
finding_prefetch_instance = FindingPrefetch.from_json(json)
# print the JSON string representation of the object
print(FindingPrefetch.to_json())

# convert the object into a dict
finding_prefetch_dict = finding_prefetch_instance.to_dict()
# create an instance of FindingPrefetch from a dict
finding_prefetch_from_dict = FindingPrefetch.from_dict(finding_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


