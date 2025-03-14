# PatchedProductTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**critical_product** | **bool** |  | [optional] 
**key_product** | **bool** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_product_type_request import PatchedProductTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedProductTypeRequest from a JSON string
patched_product_type_request_instance = PatchedProductTypeRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedProductTypeRequest.to_json())

# convert the object into a dict
patched_product_type_request_dict = patched_product_type_request_instance.to_dict()
# create an instance of PatchedProductTypeRequest from a dict
patched_product_type_request_from_dict = PatchedProductTypeRequest.from_dict(patched_product_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


