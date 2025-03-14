# PaginatedProductGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ProductGroup]**](ProductGroup.md) |  | 
**prefetch** | [**PaginatedProductGroupListPrefetch**](PaginatedProductGroupListPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_product_group_list import PaginatedProductGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProductGroupList from a JSON string
paginated_product_group_list_instance = PaginatedProductGroupList.from_json(json)
# print the JSON string representation of the object
print(PaginatedProductGroupList.to_json())

# convert the object into a dict
paginated_product_group_list_dict = paginated_product_group_list_instance.to_dict()
# create an instance of PaginatedProductGroupList from a dict
paginated_product_group_list_from_dict = PaginatedProductGroupList.from_dict(paginated_product_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


