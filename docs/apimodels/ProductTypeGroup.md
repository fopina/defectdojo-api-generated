# ProductTypeGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**product_type** | **int** |  | [optional] 
**group** | **int** |  | [optional] 
**role** | **int** |  | [optional] 
**prefetch** | [**OrganizationGroupPrefetch**](OrganizationGroupPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.product_type_group import ProductTypeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ProductTypeGroup from a JSON string
product_type_group_instance = ProductTypeGroup.from_json(json)
# print the JSON string representation of the object
print(ProductTypeGroup.to_json())

# convert the object into a dict
product_type_group_dict = product_type_group_instance.to_dict()
# create an instance of ProductTypeGroup from a dict
product_type_group_from_dict = ProductTypeGroup.from_dict(product_type_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


