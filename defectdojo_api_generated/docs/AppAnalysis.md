# AppAnalysis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**tags** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**confidence** | **int** |  | [optional] 
**version** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**website_found** | **str** |  | [optional] 
**created** | **datetime** |  | [readonly] 
**product** | **int** |  | 
**user** | **int** |  | 
**prefetch** | [**AppAnalysisPrefetch**](AppAnalysisPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.app_analysis import AppAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of AppAnalysis from a JSON string
app_analysis_instance = AppAnalysis.from_json(json)
# print the JSON string representation of the object
print(AppAnalysis.to_json())

# convert the object into a dict
app_analysis_dict = app_analysis_instance.to_dict()
# create an instance of AppAnalysis from a dict
app_analysis_from_dict = AppAnalysis.from_dict(app_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


