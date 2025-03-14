# PatchedCredentialMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_authn_provider** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 
**cred_id** | **int** |  | [optional] 
**product** | **int** |  | [optional] 
**finding** | **int** |  | [optional] 
**engagement** | **int** |  | [optional] 
**test** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_credential_mapping_request import PatchedCredentialMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedCredentialMappingRequest from a JSON string
patched_credential_mapping_request_instance = PatchedCredentialMappingRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedCredentialMappingRequest.to_json())

# convert the object into a dict
patched_credential_mapping_request_dict = patched_credential_mapping_request_instance.to_dict()
# create an instance of PatchedCredentialMappingRequest from a dict
patched_credential_mapping_request_from_dict = PatchedCredentialMappingRequest.from_dict(patched_credential_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


