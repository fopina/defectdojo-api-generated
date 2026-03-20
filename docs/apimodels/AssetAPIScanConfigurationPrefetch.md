# AssetAPIScanConfigurationPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**Dict[str, Product]**](Product.md) |  | [optional] [readonly] 
**tool_configuration** | [**Dict[str, ToolConfiguration]**](ToolConfiguration.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.asset_api_scan_configuration_prefetch import AssetAPIScanConfigurationPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of AssetAPIScanConfigurationPrefetch from a JSON string
asset_api_scan_configuration_prefetch_instance = AssetAPIScanConfigurationPrefetch.from_json(json)
# print the JSON string representation of the object
print(AssetAPIScanConfigurationPrefetch.to_json())

# convert the object into a dict
asset_api_scan_configuration_prefetch_dict = asset_api_scan_configuration_prefetch_instance.to_dict()
# create an instance of AssetAPIScanConfigurationPrefetch from a dict
asset_api_scan_configuration_prefetch_from_dict = AssetAPIScanConfigurationPrefetch.from_dict(asset_api_scan_configuration_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


