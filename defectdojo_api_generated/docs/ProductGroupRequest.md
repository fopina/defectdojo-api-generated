# ProductGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **int** |  | 
**group** | **int** |  | 
**role** | **int** |  | 

## Example

```python
from defectdojo_api_generated.models.product_group_request import ProductGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductGroupRequest from a JSON string
product_group_request_instance = ProductGroupRequest.from_json(json)
# print the JSON string representation of the object
print(ProductGroupRequest.to_json())

# convert the object into a dict
product_group_request_dict = product_group_request_instance.to_dict()
# create an instance of ProductGroupRequest from a dict
product_group_request_from_dict = ProductGroupRequest.from_dict(product_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


