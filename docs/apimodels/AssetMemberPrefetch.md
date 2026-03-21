# AssetMemberPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**Dict[str, Product]**](Product.md) |  | [optional] [readonly] 
**role** | [**Dict[str, Role]**](Role.md) |  | [optional] [readonly] 
**user** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.asset_member_prefetch import AssetMemberPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of AssetMemberPrefetch from a JSON string
asset_member_prefetch_instance = AssetMemberPrefetch.from_json(json)
# print the JSON string representation of the object
print(AssetMemberPrefetch.to_json())

# convert the object into a dict
asset_member_prefetch_dict = asset_member_prefetch_instance.to_dict()
# create an instance of AssetMemberPrefetch from a dict
asset_member_prefetch_from_dict = AssetMemberPrefetch.from_dict(asset_member_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


