# ProductTypeGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_type** | **int** |  | 
**group** | **int** |  | 
**role** | **int** |  | 

## Example

```python
from defectdojo_api_generated.models.product_type_group_request import ProductTypeGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductTypeGroupRequest from a JSON string
product_type_group_request_instance = ProductTypeGroupRequest.from_json(json)
# print the JSON string representation of the object
print(ProductTypeGroupRequest.to_json())

# convert the object into a dict
product_type_group_request_dict = product_type_group_request_instance.to_dict()
# create an instance of ProductTypeGroupRequest from a dict
product_type_group_request_from_dict = ProductTypeGroupRequest.from_dict(product_type_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


