# ProductMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from defectdojo_api_generated.models.product_meta import ProductMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ProductMeta from a JSON string
product_meta_instance = ProductMeta.from_json(json)
# print the JSON string representation of the object
print(ProductMeta.to_json())

# convert the object into a dict
product_meta_dict = product_meta_instance.to_dict()
# create an instance of ProductMeta from a dict
product_meta_from_dict = ProductMeta.from_dict(product_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


