# TestType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**tags** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**static_tool** | **bool** |  | [optional] 
**dynamic_tool** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.test_type import TestType

# TODO update the JSON string below
json = "{}"
# create an instance of TestType from a JSON string
test_type_instance = TestType.from_json(json)
# print the JSON string representation of the object
print(TestType.to_json())

# convert the object into a dict
test_type_dict = test_type_instance.to_dict()
# create an instance of TestType from a dict
test_type_from_dict = TestType.from_dict(test_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


