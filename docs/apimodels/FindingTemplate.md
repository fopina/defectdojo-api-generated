# FindingTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**tags** | **List[str]** |  | [optional] 
**vulnerability_ids** | **List[str]** |  | [optional] [readonly] 
**endpoints** | **List[str]** |  | [optional] [readonly] 
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
**last_used** | **datetime** |  | [optional] [readonly] 
**numerical_severity** | **str** |  | [optional] [readonly] 
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
from defectdojo_api_generated.models.finding_template import FindingTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of FindingTemplate from a JSON string
finding_template_instance = FindingTemplate.from_json(json)
# print the JSON string representation of the object
print(FindingTemplate.to_json())

# convert the object into a dict
finding_template_dict = finding_template_instance.to_dict()
# create an instance of FindingTemplate from a dict
finding_template_from_dict = FindingTemplate.from_dict(finding_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


