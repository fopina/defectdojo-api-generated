# TestTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**static_tool** | **bool** |  | [optional] 
**dynamic_tool** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.test_type_request import TestTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestTypeRequest from a JSON string
test_type_request_instance = TestTypeRequest.from_json(json)
# print the JSON string representation of the object
print(TestTypeRequest.to_json())

# convert the object into a dict
test_type_request_dict = test_type_request_instance.to_dict()
# create an instance of TestTypeRequest from a dict
test_type_request_from_dict = TestTypeRequest.from_dict(test_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


