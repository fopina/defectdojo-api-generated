# ProductType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**created** | **datetime** | Time that the object was initially created, and saved to the database | [optional] [readonly] 
**updated** | **datetime** | Time that the object was most recently saved to the database | [optional] [readonly] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**critical_product** | **bool** |  | [optional] 
**key_product** | **bool** |  | [optional] 
**members** | **List[int]** |  | [optional] [readonly] 
**authorization_groups** | **List[int]** |  | [optional] [readonly] 
**prefetch** | [**OrganizationPrefetch**](OrganizationPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.product_type import ProductType

# TODO update the JSON string below
json = "{}"
# create an instance of ProductType from a JSON string
product_type_instance = ProductType.from_json(json)
# print the JSON string representation of the object
print(ProductType.to_json())

# convert the object into a dict
product_type_dict = product_type_instance.to_dict()
# create an instance of ProductType from a dict
product_type_from_dict = ProductType.from_dict(product_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


