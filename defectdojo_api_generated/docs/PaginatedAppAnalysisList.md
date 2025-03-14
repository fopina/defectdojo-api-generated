# PaginatedAppAnalysisList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[AppAnalysis]**](AppAnalysis.md) |  | 
**prefetch** | [**AppAnalysisPrefetch**](AppAnalysisPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_app_analysis_list import PaginatedAppAnalysisList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAppAnalysisList from a JSON string
paginated_app_analysis_list_instance = PaginatedAppAnalysisList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAppAnalysisList.to_json())

# convert the object into a dict
paginated_app_analysis_list_dict = paginated_app_analysis_list_instance.to_dict()
# create an instance of PaginatedAppAnalysisList from a dict
paginated_app_analysis_list_from_dict = PaginatedAppAnalysisList.from_dict(paginated_app_analysis_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


