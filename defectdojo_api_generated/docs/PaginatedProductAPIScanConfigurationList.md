# PaginatedProductAPIScanConfigurationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ProductAPIScanConfiguration]**](ProductAPIScanConfiguration.md) |  | 
**prefetch** | [**PaginatedProductAPIScanConfigurationListPrefetch**](PaginatedProductAPIScanConfigurationListPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_product_api_scan_configuration_list import PaginatedProductAPIScanConfigurationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProductAPIScanConfigurationList from a JSON string
paginated_product_api_scan_configuration_list_instance = PaginatedProductAPIScanConfigurationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedProductAPIScanConfigurationList.to_json())

# convert the object into a dict
paginated_product_api_scan_configuration_list_dict = paginated_product_api_scan_configuration_list_instance.to_dict()
# create an instance of PaginatedProductAPIScanConfigurationList from a dict
paginated_product_api_scan_configuration_list_from_dict = PaginatedProductAPIScanConfigurationList.from_dict(paginated_product_api_scan_configuration_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


