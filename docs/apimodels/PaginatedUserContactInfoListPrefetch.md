# PaginatedUserContactInfoListPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.paginated_user_contact_info_list_prefetch import PaginatedUserContactInfoListPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserContactInfoListPrefetch from a JSON string
paginated_user_contact_info_list_prefetch_instance = PaginatedUserContactInfoListPrefetch.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserContactInfoListPrefetch.to_json())

# convert the object into a dict
paginated_user_contact_info_list_prefetch_dict = paginated_user_contact_info_list_prefetch_instance.to_dict()
# create an instance of PaginatedUserContactInfoListPrefetch from a dict
paginated_user_contact_info_list_prefetch_from_dict = PaginatedUserContactInfoListPrefetch.from_dict(paginated_user_contact_info_list_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


