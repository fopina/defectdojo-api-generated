# ProductTypeMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**product_type** | **int** |  | 
**user** | **int** |  | 
**role** | **int** |  | 
**prefetch** | [**PaginatedProductTypeMemberListPrefetch**](PaginatedProductTypeMemberListPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.product_type_member import ProductTypeMember

# TODO update the JSON string below
json = "{}"
# create an instance of ProductTypeMember from a JSON string
product_type_member_instance = ProductTypeMember.from_json(json)
# print the JSON string representation of the object
print(ProductTypeMember.to_json())

# convert the object into a dict
product_type_member_dict = product_type_member_instance.to_dict()
# create an instance of ProductTypeMember from a dict
product_type_member_from_dict = ProductTypeMember.from_dict(product_type_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


