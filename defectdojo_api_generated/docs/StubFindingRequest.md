# StubFindingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**var_date** | **date** |  | [optional] 
**severity** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.stub_finding_request import StubFindingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StubFindingRequest from a JSON string
stub_finding_request_instance = StubFindingRequest.from_json(json)
# print the JSON string representation of the object
print(StubFindingRequest.to_json())

# convert the object into a dict
stub_finding_request_dict = stub_finding_request_instance.to_dict()
# create an instance of StubFindingRequest from a dict
stub_finding_request_from_dict = StubFindingRequest.from_dict(stub_finding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


