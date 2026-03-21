# AssetAPIScanConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **int** |  | [optional] 
**service_key_1** | **str** |  | [optional] 
**service_key_2** | **str** |  | [optional] 
**service_key_3** | **str** |  | [optional] 
**tool_configuration** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.asset_api_scan_configuration_request import AssetAPIScanConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssetAPIScanConfigurationRequest from a JSON string
asset_api_scan_configuration_request_instance = AssetAPIScanConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(AssetAPIScanConfigurationRequest.to_json())

# convert the object into a dict
asset_api_scan_configuration_request_dict = asset_api_scan_configuration_request_instance.to_dict()
# create an instance of AssetAPIScanConfigurationRequest from a dict
asset_api_scan_configuration_request_from_dict = AssetAPIScanConfigurationRequest.from_dict(asset_api_scan_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


