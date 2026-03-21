# PaginatedAssetMemberList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[AssetMember]**](AssetMember.md) |  | [optional] 
**prefetch** | [**AssetMemberPrefetch**](AssetMemberPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_asset_member_list import PaginatedAssetMemberList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAssetMemberList from a JSON string
paginated_asset_member_list_instance = PaginatedAssetMemberList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAssetMemberList.to_json())

# convert the object into a dict
paginated_asset_member_list_dict = paginated_asset_member_list_instance.to_dict()
# create an instance of PaginatedAssetMemberList from a dict
paginated_asset_member_list_from_dict = PaginatedAssetMemberList.from_dict(paginated_asset_member_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


