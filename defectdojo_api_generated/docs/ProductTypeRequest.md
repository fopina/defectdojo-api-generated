# ProductTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**critical_product** | **bool** |  | [optional] 
**key_product** | **bool** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.product_type_request import ProductTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductTypeRequest from a JSON string
product_type_request_instance = ProductTypeRequest.from_json(json)
# print the JSON string representation of the object
print(ProductTypeRequest.to_json())

# convert the object into a dict
product_type_request_dict = product_type_request_instance.to_dict()
# create an instance of ProductTypeRequest from a dict
product_type_request_from_dict = ProductTypeRequest.from_dict(product_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


