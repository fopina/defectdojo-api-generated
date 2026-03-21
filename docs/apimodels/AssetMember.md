# AssetMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**asset** | **int** |  | [optional] 
**user** | **int** |  | [optional] 
**role** | **int** |  | [optional] 
**prefetch** | [**AssetMemberPrefetch**](AssetMemberPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.asset_member import AssetMember

# TODO update the JSON string below
json = "{}"
# create an instance of AssetMember from a JSON string
asset_member_instance = AssetMember.from_json(json)
# print the JSON string representation of the object
print(AssetMember.to_json())

# convert the object into a dict
asset_member_dict = asset_member_instance.to_dict()
# create an instance of AssetMember from a dict
asset_member_from_dict = AssetMember.from_dict(asset_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


