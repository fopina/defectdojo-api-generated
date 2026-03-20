# TestTypeCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**static_tool** | **bool** |  | [optional] 
**dynamic_tool** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.test_type_create_request import TestTypeCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestTypeCreateRequest from a JSON string
test_type_create_request_instance = TestTypeCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TestTypeCreateRequest.to_json())

# convert the object into a dict
test_type_create_request_dict = test_type_create_request_instance.to_dict()
# create an instance of TestTypeCreateRequest from a dict
test_type_create_request_from_dict = TestTypeCreateRequest.from_dict(test_type_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


