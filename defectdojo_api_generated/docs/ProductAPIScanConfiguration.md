# ProductAPIScanConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**service_key_1** | **str** |  | [optional] 
**service_key_2** | **str** |  | [optional] 
**service_key_3** | **str** |  | [optional] 
**product** | **int** |  | 
**tool_configuration** | **int** |  | 
**prefetch** | [**PaginatedProductAPIScanConfigurationListPrefetch**](PaginatedProductAPIScanConfigurationListPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.product_api_scan_configuration import ProductAPIScanConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAPIScanConfiguration from a JSON string
product_api_scan_configuration_instance = ProductAPIScanConfiguration.from_json(json)
# print the JSON string representation of the object
print(ProductAPIScanConfiguration.to_json())

# convert the object into a dict
product_api_scan_configuration_dict = product_api_scan_configuration_instance.to_dict()
# create an instance of ProductAPIScanConfiguration from a dict
product_api_scan_configuration_from_dict = ProductAPIScanConfiguration.from_dict(product_api_scan_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


