# PaginatedCredentialMappingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[CredentialMapping]**](CredentialMapping.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_credential_mapping_list import PaginatedCredentialMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCredentialMappingList from a JSON string
paginated_credential_mapping_list_instance = PaginatedCredentialMappingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCredentialMappingList.to_json())

# convert the object into a dict
paginated_credential_mapping_list_dict = paginated_credential_mapping_list_instance.to_dict()
# create an instance of PaginatedCredentialMappingList from a dict
paginated_credential_mapping_list_from_dict = PaginatedCredentialMappingList.from_dict(paginated_credential_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


