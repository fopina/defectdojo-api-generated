# CredentialMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_authn_provider** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 
**cred_id** | **int** |  | 
**product** | **int** |  | [optional] 
**finding** | **int** |  | [optional] 
**engagement** | **int** |  | [optional] 
**test** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.credential_mapping_request import CredentialMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialMappingRequest from a JSON string
credential_mapping_request_instance = CredentialMappingRequest.from_json(json)
# print the JSON string representation of the object
print(CredentialMappingRequest.to_json())

# convert the object into a dict
credential_mapping_request_dict = credential_mapping_request_instance.to_dict()
# create an instance of CredentialMappingRequest from a dict
credential_mapping_request_from_dict = CredentialMappingRequest.from_dict(credential_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


