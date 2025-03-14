# PaginatedProductTypeGroupListPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**Dict[str, DojoGroup]**](DojoGroup.md) |  | [optional] [readonly] 
**product_type** | [**Dict[str, ProductType]**](ProductType.md) |  | [optional] [readonly] 
**role** | [**Dict[str, Role]**](Role.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.paginated_product_type_group_list_prefetch import PaginatedProductTypeGroupListPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProductTypeGroupListPrefetch from a JSON string
paginated_product_type_group_list_prefetch_instance = PaginatedProductTypeGroupListPrefetch.from_json(json)
# print the JSON string representation of the object
print(PaginatedProductTypeGroupListPrefetch.to_json())

# convert the object into a dict
paginated_product_type_group_list_prefetch_dict = paginated_product_type_group_list_prefetch_instance.to_dict()
# create an instance of PaginatedProductTypeGroupListPrefetch from a dict
paginated_product_type_group_list_prefetch_from_dict = PaginatedProductTypeGroupListPrefetch.from_dict(paginated_product_type_group_list_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


