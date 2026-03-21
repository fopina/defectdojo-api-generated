# PatchedStubFindingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**var_date** | **date** |  | [optional] 
**severity** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_stub_finding_request import PatchedStubFindingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedStubFindingRequest from a JSON string
patched_stub_finding_request_instance = PatchedStubFindingRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedStubFindingRequest.to_json())

# convert the object into a dict
patched_stub_finding_request_dict = patched_stub_finding_request_instance.to_dict()
# create an instance of PatchedStubFindingRequest from a dict
patched_stub_finding_request_from_dict = PatchedStubFindingRequest.from_dict(patched_stub_finding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


