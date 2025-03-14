# PaginatedProductAPIScanConfigurationListPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**Dict[str, Product]**](Product.md) |  | [optional] [readonly] 
**tool_configuration** | [**Dict[str, ToolConfiguration]**](ToolConfiguration.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.paginated_product_api_scan_configuration_list_prefetch import PaginatedProductAPIScanConfigurationListPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProductAPIScanConfigurationListPrefetch from a JSON string
paginated_product_api_scan_configuration_list_prefetch_instance = PaginatedProductAPIScanConfigurationListPrefetch.from_json(json)
# print the JSON string representation of the object
print(PaginatedProductAPIScanConfigurationListPrefetch.to_json())

# convert the object into a dict
paginated_product_api_scan_configuration_list_prefetch_dict = paginated_product_api_scan_configuration_list_prefetch_instance.to_dict()
# create an instance of PaginatedProductAPIScanConfigurationListPrefetch from a dict
paginated_product_api_scan_configuration_list_prefetch_from_dict = PaginatedProductAPIScanConfigurationListPrefetch.from_dict(paginated_product_api_scan_configuration_list_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


