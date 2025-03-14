# PatchedEngagementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**version** | **str** | Version of the product the engagement tested. | [optional] 
**first_contacted** | **date** |  | [optional] 
**target_start** | **date** |  | [optional] 
**target_end** | **date** |  | [optional] 
**reason** | **str** |  | [optional] 
**tracker** | **str** | Link to epic or ticket system with changes to version. | [optional] 
**test_strategy** | **str** |  | [optional] 
**threat_model** | **bool** |  | [optional] 
**api_test** | **bool** |  | [optional] 
**pen_test** | **bool** |  | [optional] 
**check_list** | **bool** |  | [optional] 
**status** | **str** | * &#x60;Not Started&#x60; - Not Started * &#x60;Blocked&#x60; - Blocked * &#x60;Cancelled&#x60; - Cancelled * &#x60;Completed&#x60; - Completed * &#x60;In Progress&#x60; - In Progress * &#x60;On Hold&#x60; - On Hold * &#x60;Waiting for Resource&#x60; - Waiting for Resource | [optional] 
**engagement_type** | **str** | * &#x60;Interactive&#x60; - Interactive * &#x60;CI/CD&#x60; - CI/CD | [optional] 
**build_id** | **str** | Build ID of the product the engagement tested. | [optional] 
**commit_hash** | **str** | Commit hash from repo | [optional] 
**branch_tag** | **str** | Tag or branch of the product the engagement tested. | [optional] 
**source_code_management_uri** | **str** | Resource link to source code | [optional] 
**deduplication_on_engagement** | **bool** | If enabled deduplication will only mark a finding in this engagement as duplicate of another finding if both findings are in this engagement. If disabled, deduplication is on the product level. | [optional] 
**lead** | **int** |  | [optional] 
**requester** | **int** |  | [optional] 
**preset** | **int** | Settings and notes for performing this engagement. | [optional] 
**report_type** | **int** |  | [optional] 
**product** | **int** |  | [optional] 
**build_server** | **int** | Build server responsible for CI/CD test | [optional] 
**source_code_management_server** | **int** | Source code server for CI/CD test | [optional] 
**orchestration_engine** | **int** | Orchestration service responsible for CI/CD test | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_engagement_request import PatchedEngagementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedEngagementRequest from a JSON string
patched_engagement_request_instance = PatchedEngagementRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedEngagementRequest.to_json())

# convert the object into a dict
patched_engagement_request_dict = patched_engagement_request_instance.to_dict()
# create an instance of PatchedEngagementRequest from a dict
patched_engagement_request_from_dict = PatchedEngagementRequest.from_dict(patched_engagement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


