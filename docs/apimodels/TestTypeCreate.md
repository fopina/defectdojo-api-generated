# TestTypeCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**static_tool** | **bool** |  | [optional] 
**dynamic_tool** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.test_type_create import TestTypeCreate

# TODO update the JSON string below
json = "{}"
# create an instance of TestTypeCreate from a JSON string
test_type_create_instance = TestTypeCreate.from_json(json)
# print the JSON string representation of the object
print(TestTypeCreate.to_json())

# convert the object into a dict
test_type_create_dict = test_type_create_instance.to_dict()
# create an instance of TestTypeCreate from a dict
test_type_create_from_dict = TestTypeCreate.from_dict(test_type_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


