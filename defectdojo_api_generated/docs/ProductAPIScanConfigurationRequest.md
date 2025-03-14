# ProductAPIScanConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_key_1** | **str** |  | [optional] 
**service_key_2** | **str** |  | [optional] 
**service_key_3** | **str** |  | [optional] 
**product** | **int** |  | 
**tool_configuration** | **int** |  | 

## Example

```python
from defectdojo_api_generated.models.product_api_scan_configuration_request import ProductAPIScanConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAPIScanConfigurationRequest from a JSON string
product_api_scan_configuration_request_instance = ProductAPIScanConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(ProductAPIScanConfigurationRequest.to_json())

# convert the object into a dict
product_api_scan_configuration_request_dict = product_api_scan_configuration_request_instance.to_dict()
# create an instance of ProductAPIScanConfigurationRequest from a dict
product_api_scan_configuration_request_from_dict = ProductAPIScanConfigurationRequest.from_dict(product_api_scan_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


