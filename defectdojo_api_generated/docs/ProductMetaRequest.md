# ProductMetaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from defectdojo_api_generated.models.product_meta_request import ProductMetaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductMetaRequest from a JSON string
product_meta_request_instance = ProductMetaRequest.from_json(json)
# print the JSON string representation of the object
print(ProductMetaRequest.to_json())

# convert the object into a dict
product_meta_request_dict = product_meta_request_instance.to_dict()
# create an instance of ProductMetaRequest from a dict
product_meta_request_from_dict = ProductMetaRequest.from_dict(product_meta_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


