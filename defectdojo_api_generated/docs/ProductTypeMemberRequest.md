# ProductTypeMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_type** | **int** |  | 
**user** | **int** |  | 
**role** | **int** |  | 

## Example

```python
from defectdojo_api_generated.models.product_type_member_request import ProductTypeMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductTypeMemberRequest from a JSON string
product_type_member_request_instance = ProductTypeMemberRequest.from_json(json)
# print the JSON string representation of the object
print(ProductTypeMemberRequest.to_json())

# convert the object into a dict
product_type_member_request_dict = product_type_member_request_instance.to_dict()
# create an instance of ProductTypeMemberRequest from a dict
product_type_member_request_from_dict = ProductTypeMemberRequest.from_dict(product_type_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


