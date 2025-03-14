# ProductMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**product** | **int** |  | 
**user** | **int** |  | 
**role** | **int** |  | 
**prefetch** | [**PaginatedProductMemberListPrefetch**](PaginatedProductMemberListPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.product_member import ProductMember

# TODO update the JSON string below
json = "{}"
# create an instance of ProductMember from a JSON string
product_member_instance = ProductMember.from_json(json)
# print the JSON string representation of the object
print(ProductMember.to_json())

# convert the object into a dict
product_member_dict = product_member_instance.to_dict()
# create an instance of ProductMember from a dict
product_member_from_dict = ProductMember.from_dict(product_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


