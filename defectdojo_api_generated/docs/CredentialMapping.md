# CredentialMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**is_authn_provider** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 
**cred_id** | **int** |  | 
**product** | **int** |  | [optional] 
**finding** | **int** |  | [optional] 
**engagement** | **int** |  | [optional] 
**test** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.credential_mapping import CredentialMapping

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialMapping from a JSON string
credential_mapping_instance = CredentialMapping.from_json(json)
# print the JSON string representation of the object
print(CredentialMapping.to_json())

# convert the object into a dict
credential_mapping_dict = credential_mapping_instance.to_dict()
# create an instance of CredentialMapping from a dict
credential_mapping_from_dict = CredentialMapping.from_dict(credential_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


