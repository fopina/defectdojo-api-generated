# ProductMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **int** |  | 
**user** | **int** |  | 
**role** | **int** |  | 

## Example

```python
from defectdojo_api_generated.models.product_member_request import ProductMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductMemberRequest from a JSON string
product_member_request_instance = ProductMemberRequest.from_json(json)
# print the JSON string representation of the object
print(ProductMemberRequest.to_json())

# convert the object into a dict
product_member_request_dict = product_member_request_instance.to_dict()
# create an instance of ProductMemberRequest from a dict
product_member_request_from_dict = ProductMemberRequest.from_dict(product_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


