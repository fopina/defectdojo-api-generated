# AssetGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**asset** | **int** |  | [optional] 
**group** | **int** |  | [optional] 
**role** | **int** |  | [optional] 
**prefetch** | [**AssetGroupPrefetch**](AssetGroupPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.asset_group import AssetGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AssetGroup from a JSON string
asset_group_instance = AssetGroup.from_json(json)
# print the JSON string representation of the object
print(AssetGroup.to_json())

# convert the object into a dict
asset_group_dict = asset_group_instance.to_dict()
# create an instance of AssetGroup from a dict
asset_group_from_dict = AssetGroup.from_dict(asset_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


