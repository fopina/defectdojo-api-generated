# PatchedAssetAPIScanConfigurationRequest


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
from defectdojo_api_generated.models.patched_asset_api_scan_configuration_request import PatchedAssetAPIScanConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAssetAPIScanConfigurationRequest from a JSON string
patched_asset_api_scan_configuration_request_instance = PatchedAssetAPIScanConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedAssetAPIScanConfigurationRequest.to_json())

# convert the object into a dict
patched_asset_api_scan_configuration_request_dict = patched_asset_api_scan_configuration_request_instance.to_dict()
# create an instance of PatchedAssetAPIScanConfigurationRequest from a dict
patched_asset_api_scan_configuration_request_from_dict = PatchedAssetAPIScanConfigurationRequest.from_dict(patched_asset_api_scan_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


