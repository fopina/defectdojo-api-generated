# PatchedEndpointStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**mitigated** | **bool** |  | [optional] 
**false_positive** | **bool** |  | [optional] 
**out_of_scope** | **bool** |  | [optional] 
**risk_accepted** | **bool** |  | [optional] 
**mitigated_by** | **int** |  | [optional] 
**endpoint** | **int** |  | [optional] 
**finding** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_endpoint_status_request import PatchedEndpointStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedEndpointStatusRequest from a JSON string
patched_endpoint_status_request_instance = PatchedEndpointStatusRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedEndpointStatusRequest.to_json())

# convert the object into a dict
patched_endpoint_status_request_dict = patched_endpoint_status_request_instance.to_dict()
# create an instance of PatchedEndpointStatusRequest from a dict
patched_endpoint_status_request_from_dict = PatchedEndpointStatusRequest.from_dict(patched_endpoint_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


