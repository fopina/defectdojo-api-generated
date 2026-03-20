# PaginatedAssetAPIScanConfigurationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[AssetAPIScanConfiguration]**](AssetAPIScanConfiguration.md) |  | [optional] 
**prefetch** | [**AssetAPIScanConfigurationPrefetch**](AssetAPIScanConfigurationPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_asset_api_scan_configuration_list import PaginatedAssetAPIScanConfigurationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAssetAPIScanConfigurationList from a JSON string
paginated_asset_api_scan_configuration_list_instance = PaginatedAssetAPIScanConfigurationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAssetAPIScanConfigurationList.to_json())

# convert the object into a dict
paginated_asset_api_scan_configuration_list_dict = paginated_asset_api_scan_configuration_list_instance.to_dict()
# create an instance of PaginatedAssetAPIScanConfigurationList from a dict
paginated_asset_api_scan_configuration_list_from_dict = PaginatedAssetAPIScanConfigurationList.from_dict(paginated_asset_api_scan_configuration_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


