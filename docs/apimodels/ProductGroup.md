# ProductGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**product** | **int** |  | [optional] 
**group** | **int** |  | [optional] 
**role** | **int** |  | [optional] 
**prefetch** | [**AssetGroupPrefetch**](AssetGroupPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.product_group import ProductGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ProductGroup from a JSON string
product_group_instance = ProductGroup.from_json(json)
# print the JSON string representation of the object
print(ProductGroup.to_json())

# convert the object into a dict
product_group_dict = product_group_instance.to_dict()
# create an instance of ProductGroup from a dict
product_group_from_dict = ProductGroup.from_dict(product_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


