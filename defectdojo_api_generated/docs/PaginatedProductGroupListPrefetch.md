# PaginatedProductGroupListPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**Dict[str, DojoGroup]**](DojoGroup.md) |  | [optional] [readonly] 
**product** | [**Dict[str, Product]**](Product.md) |  | [optional] [readonly] 
**role** | [**Dict[str, Role]**](Role.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.paginated_product_group_list_prefetch import PaginatedProductGroupListPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProductGroupListPrefetch from a JSON string
paginated_product_group_list_prefetch_instance = PaginatedProductGroupListPrefetch.from_json(json)
# print the JSON string representation of the object
print(PaginatedProductGroupListPrefetch.to_json())

# convert the object into a dict
paginated_product_group_list_prefetch_dict = paginated_product_group_list_prefetch_instance.to_dict()
# create an instance of PaginatedProductGroupListPrefetch from a dict
paginated_product_group_list_prefetch_from_dict = PaginatedProductGroupListPrefetch.from_dict(paginated_product_group_list_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


