# PatchedProductAPIScanConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_key_1** | **str** |  | [optional] 
**service_key_2** | **str** |  | [optional] 
**service_key_3** | **str** |  | [optional] 
**product** | **int** |  | [optional] 
**tool_configuration** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_product_api_scan_configuration_request import PatchedProductAPIScanConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedProductAPIScanConfigurationRequest from a JSON string
patched_product_api_scan_configuration_request_instance = PatchedProductAPIScanConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedProductAPIScanConfigurationRequest.to_json())

# convert the object into a dict
patched_product_api_scan_configuration_request_dict = patched_product_api_scan_configuration_request_instance.to_dict()
# create an instance of PatchedProductAPIScanConfigurationRequest from a dict
patched_product_api_scan_configuration_request_from_dict = PatchedProductAPIScanConfigurationRequest.from_dict(patched_product_api_scan_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


