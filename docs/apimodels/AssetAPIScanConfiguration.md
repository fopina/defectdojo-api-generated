# AssetAPIScanConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**asset** | **int** |  | [optional] 
**service_key_1** | **str** |  | [optional] 
**service_key_2** | **str** |  | [optional] 
**service_key_3** | **str** |  | [optional] 
**tool_configuration** | **int** |  | [optional] 
**prefetch** | [**AssetAPIScanConfigurationPrefetch**](AssetAPIScanConfigurationPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.asset_api_scan_configuration import AssetAPIScanConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AssetAPIScanConfiguration from a JSON string
asset_api_scan_configuration_instance = AssetAPIScanConfiguration.from_json(json)
# print the JSON string representation of the object
print(AssetAPIScanConfiguration.to_json())

# convert the object into a dict
asset_api_scan_configuration_dict = asset_api_scan_configuration_instance.to_dict()
# create an instance of AssetAPIScanConfiguration from a dict
asset_api_scan_configuration_from_dict = AssetAPIScanConfiguration.from_dict(asset_api_scan_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


