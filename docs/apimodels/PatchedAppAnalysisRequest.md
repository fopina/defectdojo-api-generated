# PatchedAppAnalysisRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**confidence** | **int** |  | [optional] 
**version** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**website_found** | **str** |  | [optional] 
**product** | **int** |  | [optional] 
**user** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_app_analysis_request import PatchedAppAnalysisRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAppAnalysisRequest from a JSON string
patched_app_analysis_request_instance = PatchedAppAnalysisRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedAppAnalysisRequest.to_json())

# convert the object into a dict
patched_app_analysis_request_dict = patched_app_analysis_request_instance.to_dict()
# create an instance of PatchedAppAnalysisRequest from a dict
patched_app_analysis_request_from_dict = PatchedAppAnalysisRequest.from_dict(patched_app_analysis_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


