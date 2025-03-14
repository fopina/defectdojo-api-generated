# PaginatedProductTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ProductType]**](ProductType.md) |  | 
**prefetch** | [**PaginatedProductTypeListPrefetch**](PaginatedProductTypeListPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_product_type_list import PaginatedProductTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProductTypeList from a JSON string
paginated_product_type_list_instance = PaginatedProductTypeList.from_json(json)
# print the JSON string representation of the object
print(PaginatedProductTypeList.to_json())

# convert the object into a dict
paginated_product_type_list_dict = paginated_product_type_list_instance.to_dict()
# create an instance of PaginatedProductTypeList from a dict
paginated_product_type_list_from_dict = PaginatedProductTypeList.from_dict(paginated_product_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


