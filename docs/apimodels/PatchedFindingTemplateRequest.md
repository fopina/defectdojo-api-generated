# PatchedFindingTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**cwe** | **int** |  | [optional] 
**cvssv3** | **str** | Common Vulnerability Scoring System version 3 (CVSSv3) score associated with this finding. | [optional] 
**cvssv3_score** | **float** | CVSSv3 score | [optional] 
**cvssv4** | **str** | Common Vulnerability Scoring System version 4 (CVSS4) score associated with this finding. | [optional] 
**cvssv4_score** | **float** | CVSSv4 score | [optional] 
**severity** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**mitigation** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**references** | **str** |  | [optional] 
**fix_available** | **bool** | Indicates if a fix is available for this vulnerability type | [optional] 
**fix_version** | **str** | Version where fix is available | [optional] 
**planned_remediation_version** | **str** | Target version for remediation | [optional] 
**effort_for_fixing** | **str** | Effort estimate for fixing (e.g., Low/Medium/High) | [optional] 
**steps_to_reproduce** | **str** | Standard reproduction steps for this vulnerability type | [optional] 
**severity_justification** | **str** | Explanation of why this severity level is appropriate | [optional] 
**component_name** | **str** | Affected component name (e.g., library name) | [optional] 
**component_version** | **str** | Affected component version | [optional] 
**notes** | **str** | Note content to add when applying this template | [optional] 
**endpoints_text** | **str** | Endpoint URLs (one per line) | [optional] 

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


