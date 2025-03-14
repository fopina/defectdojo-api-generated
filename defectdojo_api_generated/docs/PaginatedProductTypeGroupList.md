# PaginatedProductTypeGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ProductTypeGroup]**](ProductTypeGroup.md) |  | 
**prefetch** | [**PaginatedProductTypeGroupListPrefetch**](PaginatedProductTypeGroupListPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_product_type_group_list import PaginatedProductTypeGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProductTypeGroupList from a JSON string
paginated_product_type_group_list_instance = PaginatedProductTypeGroupList.from_json(json)
# print the JSON string representation of the object
print(PaginatedProductTypeGroupList.to_json())

# convert the object into a dict
paginated_product_type_group_list_dict = paginated_product_type_group_list_instance.to_dict()
# create an instance of PaginatedProductTypeGroupList from a dict
paginated_product_type_group_list_from_dict = PaginatedProductTypeGroupList.from_dict(paginated_product_type_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


