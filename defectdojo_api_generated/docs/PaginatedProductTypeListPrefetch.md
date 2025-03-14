# PaginatedProductTypeListPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_groups** | [**Dict[str, DojoGroup]**](DojoGroup.md) |  | [optional] [readonly] 
**members** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.paginated_product_type_list_prefetch import PaginatedProductTypeListPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProductTypeListPrefetch from a JSON string
paginated_product_type_list_prefetch_instance = PaginatedProductTypeListPrefetch.from_json(json)
# print the JSON string representation of the object
print(PaginatedProductTypeListPrefetch.to_json())

# convert the object into a dict
paginated_product_type_list_prefetch_dict = paginated_product_type_list_prefetch_instance.to_dict()
# create an instance of PaginatedProductTypeListPrefetch from a dict
paginated_product_type_list_prefetch_from_dict = PaginatedProductTypeListPrefetch.from_dict(paginated_product_type_list_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


