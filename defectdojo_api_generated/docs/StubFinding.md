# StubFinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**title** | **str** |  | 
**var_date** | **date** |  | [optional] 
**severity** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**test** | **int** |  | [readonly] 
**reporter** | **int** |  | [readonly] 

## Example

```python
from defectdojo_api_generated.models.stub_finding import StubFinding

# TODO update the JSON string below
json = "{}"
# create an instance of StubFinding from a JSON string
stub_finding_instance = StubFinding.from_json(json)
# print the JSON string representation of the object
print(StubFinding.to_json())

# convert the object into a dict
stub_finding_dict = stub_finding_instance.to_dict()
# create an instance of StubFinding from a dict
stub_finding_from_dict = StubFinding.from_dict(stub_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


