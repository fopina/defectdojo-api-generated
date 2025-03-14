# CredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**username** | **str** |  | 
**role** | **str** |  | 
**authentication** | **str** | * &#x60;Form&#x60; - Form Authentication * &#x60;SSO&#x60; - SSO Redirect | [optional] 
**http_authentication** | **str** | * &#x60;Basic&#x60; - Basic * &#x60;NTLM&#x60; - NTLM | [optional] 
**description** | **str** |  | [optional] 
**url** | **str** |  | 
**login_regex** | **str** |  | [optional] 
**logout_regex** | **str** |  | [optional] 
**is_valid** | **bool** |  | [optional] 
**environment** | **int** |  | 

## Example

```python
from defectdojo_api_generated.models.credential_request import CredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialRequest from a JSON string
credential_request_instance = CredentialRequest.from_json(json)
# print the JSON string representation of the object
print(CredentialRequest.to_json())

# convert the object into a dict
credential_request_dict = credential_request_instance.to_dict()
# create an instance of CredentialRequest from a dict
credential_request_from_dict = CredentialRequest.from_dict(credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


