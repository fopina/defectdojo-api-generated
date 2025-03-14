# FindingTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**tags** | **List[str]** |  | [optional] 
**vulnerability_ids** | [**List[VulnerabilityIdTemplate]**](VulnerabilityIdTemplate.md) |  | [optional] 
**title** | **str** |  | 
**cwe** | **int** |  | [optional] 
**cvssv3** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**mitigation** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**references** | **str** |  | [optional] 
**last_used** | **datetime** |  | [readonly] 
**numerical_severity** | **str** |  | [readonly] 
**template_match** | **bool** | Enables this template for matching remediation advice. Match will be applied to all active, verified findings by CWE. | [optional] 
**template_match_title** | **bool** | Matches by title text (contains search) and CWE. | [optional] 

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


