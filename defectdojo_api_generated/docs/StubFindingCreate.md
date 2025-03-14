# StubFindingCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**test** | **int** |  | 
**title** | **str** |  | 
**var_date** | **date** |  | [optional] 
**severity** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**reporter** | **int** |  | [readonly] 

## Example

```python
from defectdojo_api_generated.models.stub_finding_create import StubFindingCreate

# TODO update the JSON string below
json = "{}"
# create an instance of StubFindingCreate from a JSON string
stub_finding_create_instance = StubFindingCreate.from_json(json)
# print the JSON string representation of the object
print(StubFindingCreate.to_json())

# convert the object into a dict
stub_finding_create_dict = stub_finding_create_instance.to_dict()
# create an instance of StubFindingCreate from a dict
stub_finding_create_from_dict = StubFindingCreate.from_dict(stub_finding_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


