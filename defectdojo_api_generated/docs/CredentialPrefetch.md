# CredentialPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**Dict[str, FindingEnvironment]**](FindingEnvironment.md) |  | [optional] [readonly] 
**notes** | [**Dict[str, Note]**](Note.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.credential_prefetch import CredentialPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialPrefetch from a JSON string
credential_prefetch_instance = CredentialPrefetch.from_json(json)
# print the JSON string representation of the object
print(CredentialPrefetch.to_json())

# convert the object into a dict
credential_prefetch_dict = credential_prefetch_instance.to_dict()
# create an instance of CredentialPrefetch from a dict
credential_prefetch_from_dict = CredentialPrefetch.from_dict(credential_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


