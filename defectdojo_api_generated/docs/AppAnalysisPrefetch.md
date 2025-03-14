# AppAnalysisPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**Dict[str, Product]**](Product.md) |  | [optional] [readonly] 
**user** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.app_analysis_prefetch import AppAnalysisPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of AppAnalysisPrefetch from a JSON string
app_analysis_prefetch_instance = AppAnalysisPrefetch.from_json(json)
# print the JSON string representation of the object
print(AppAnalysisPrefetch.to_json())

# convert the object into a dict
app_analysis_prefetch_dict = app_analysis_prefetch_instance.to_dict()
# create an instance of AppAnalysisPrefetch from a dict
app_analysis_prefetch_from_dict = AppAnalysisPrefetch.from_dict(app_analysis_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


