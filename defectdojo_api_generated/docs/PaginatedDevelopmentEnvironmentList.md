# PaginatedDevelopmentEnvironmentList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DevelopmentEnvironment]**](DevelopmentEnvironment.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_development_environment_list import PaginatedDevelopmentEnvironmentList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDevelopmentEnvironmentList from a JSON string
paginated_development_environment_list_instance = PaginatedDevelopmentEnvironmentList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDevelopmentEnvironmentList.to_json())

# convert the object into a dict
paginated_development_environment_list_dict = paginated_development_environment_list_instance.to_dict()
# create an instance of PaginatedDevelopmentEnvironmentList from a dict
paginated_development_environment_list_from_dict = PaginatedDevelopmentEnvironmentList.from_dict(paginated_development_environment_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


