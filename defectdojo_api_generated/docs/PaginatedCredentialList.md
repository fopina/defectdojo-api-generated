# PaginatedCredentialList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Credential]**](Credential.md) |  | 
**prefetch** | [**CredentialPrefetch**](CredentialPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_credential_list import PaginatedCredentialList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCredentialList from a JSON string
paginated_credential_list_instance = PaginatedCredentialList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCredentialList.to_json())

# convert the object into a dict
paginated_credential_list_dict = paginated_credential_list_instance.to_dict()
# create an instance of PaginatedCredentialList from a dict
paginated_credential_list_from_dict = PaginatedCredentialList.from_dict(paginated_credential_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


