# PaginatedSLAConfigurationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[SLAConfiguration]**](SLAConfiguration.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_sla_configuration_list import PaginatedSLAConfigurationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSLAConfigurationList from a JSON string
paginated_sla_configuration_list_instance = PaginatedSLAConfigurationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSLAConfigurationList.to_json())

# convert the object into a dict
paginated_sla_configuration_list_dict = paginated_sla_configuration_list_instance.to_dict()
# create an instance of PaginatedSLAConfigurationList from a dict
paginated_sla_configuration_list_from_dict = PaginatedSLAConfigurationList.from_dict(paginated_sla_configuration_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


