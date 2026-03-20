# AssetPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_groups** | [**Dict[str, DojoGroup]**](DojoGroup.md) |  | [optional] [readonly] 
**members** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 
**prod_type** | [**Dict[str, ProductType]**](ProductType.md) |  | [optional] [readonly] 
**product_manager** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 
**regulations** | [**Dict[str, Regulation]**](Regulation.md) |  | [optional] [readonly] 
**sla_configuration** | [**Dict[str, SLAConfiguration]**](SLAConfiguration.md) |  | [optional] [readonly] 
**team_manager** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 
**technical_contact** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.asset_prefetch import AssetPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of AssetPrefetch from a JSON string
asset_prefetch_instance = AssetPrefetch.from_json(json)
# print the JSON string representation of the object
print(AssetPrefetch.to_json())

# convert the object into a dict
asset_prefetch_dict = asset_prefetch_instance.to_dict()
# create an instance of AssetPrefetch from a dict
asset_prefetch_from_dict = AssetPrefetch.from_dict(asset_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


