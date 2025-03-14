# PatchedFindingTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | [optional] 
**vulnerability_ids** | [**List[VulnerabilityIdTemplateRequest]**](VulnerabilityIdTemplateRequest.md) |  | [optional] 
**title** | **str** |  | [optional] 
**cwe** | **int** |  | [optional] 
**cvssv3** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**mitigation** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**references** | **str** |  | [optional] 
**template_match** | **bool** | Enables this template for matching remediation advice. Match will be applied to all active, verified findings by CWE. | [optional] 
**template_match_title** | **bool** | Matches by title text (contains search) and CWE. | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_finding_template_request import PatchedFindingTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedFindingTemplateRequest from a JSON string
patched_finding_template_request_instance = PatchedFindingTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedFindingTemplateRequest.to_json())

# convert the object into a dict
patched_finding_template_request_dict = patched_finding_template_request_instance.to_dict()
# create an instance of PatchedFindingTemplateRequest from a dict
patched_finding_template_request_from_dict = PatchedFindingTemplateRequest.from_dict(patched_finding_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


