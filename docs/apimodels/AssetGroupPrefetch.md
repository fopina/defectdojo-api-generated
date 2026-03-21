# AssetGroupPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**Dict[str, DojoGroup]**](DojoGroup.md) |  | [optional] [readonly] 
**product** | [**Dict[str, Product]**](Product.md) |  | [optional] [readonly] 
**role** | [**Dict[str, Role]**](Role.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.asset_group_prefetch import AssetGroupPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of AssetGroupPrefetch from a JSON string
asset_group_prefetch_instance = AssetGroupPrefetch.from_json(json)
# print the JSON string representation of the object
print(AssetGroupPrefetch.to_json())

# convert the object into a dict
asset_group_prefetch_dict = asset_group_prefetch_instance.to_dict()
# create an instance of AssetGroupPrefetch from a dict
asset_group_prefetch_from_dict = AssetGroupPrefetch.from_dict(asset_group_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


