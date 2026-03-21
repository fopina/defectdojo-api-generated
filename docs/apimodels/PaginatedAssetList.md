# PaginatedAssetList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Asset]**](Asset.md) |  | [optional] 
**prefetch** | [**AssetPrefetch**](AssetPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_asset_list import PaginatedAssetList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAssetList from a JSON string
paginated_asset_list_instance = PaginatedAssetList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAssetList.to_json())

# convert the object into a dict
paginated_asset_list_dict = paginated_asset_list_instance.to_dict()
# create an instance of PaginatedAssetList from a dict
paginated_asset_list_from_dict = PaginatedAssetList.from_dict(paginated_asset_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


