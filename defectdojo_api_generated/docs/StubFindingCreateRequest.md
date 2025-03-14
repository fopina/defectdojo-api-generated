# StubFindingCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test** | **int** |  | 
**title** | **str** |  | 
**var_date** | **date** |  | [optional] 
**severity** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.stub_finding_create_request import StubFindingCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StubFindingCreateRequest from a JSON string
stub_finding_create_request_instance = StubFindingCreateRequest.from_json(json)
# print the JSON string representation of the object
print(StubFindingCreateRequest.to_json())

# convert the object into a dict
stub_finding_create_request_dict = stub_finding_create_request_instance.to_dict()
# create an instance of StubFindingCreateRequest from a dict
stub_finding_create_request_from_dict = StubFindingCreateRequest.from_dict(stub_finding_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


