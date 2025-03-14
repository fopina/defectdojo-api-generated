# AppAnalysisRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**confidence** | **int** |  | [optional] 
**version** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**website_found** | **str** |  | [optional] 
**product** | **int** |  | 
**user** | **int** |  | 

## Example

```python
from defectdojo_api_generated.models.app_analysis_request import AppAnalysisRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAnalysisRequest from a JSON string
app_analysis_request_instance = AppAnalysisRequest.from_json(json)
# print the JSON string representation of the object
print(AppAnalysisRequest.to_json())

# convert the object into a dict
app_analysis_request_dict = app_analysis_request_instance.to_dict()
# create an instance of AppAnalysisRequest from a dict
app_analysis_request_from_dict = AppAnalysisRequest.from_dict(app_analysis_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


