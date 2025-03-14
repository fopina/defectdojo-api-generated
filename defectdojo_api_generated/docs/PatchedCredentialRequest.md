# PatchedCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**authentication** | **str** | * &#x60;Form&#x60; - Form Authentication * &#x60;SSO&#x60; - SSO Redirect | [optional] 
**http_authentication** | **str** | * &#x60;Basic&#x60; - Basic * &#x60;NTLM&#x60; - NTLM | [optional] 
**description** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**login_regex** | **str** |  | [optional] 
**logout_regex** | **str** |  | [optional] 
**is_valid** | **bool** |  | [optional] 
**environment** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_credential_request import PatchedCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedCredentialRequest from a JSON string
patched_credential_request_instance = PatchedCredentialRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedCredentialRequest.to_json())

# convert the object into a dict
patched_credential_request_dict = patched_credential_request_instance.to_dict()
# create an instance of PatchedCredentialRequest from a dict
patched_credential_request_from_dict = PatchedCredentialRequest.from_dict(patched_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


