# PaginatedUserContactInfoList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[UserContactInfo]**](UserContactInfo.md) |  | 
**prefetch** | [**PaginatedUserContactInfoListPrefetch**](PaginatedUserContactInfoListPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_user_contact_info_list import PaginatedUserContactInfoList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserContactInfoList from a JSON string
paginated_user_contact_info_list_instance = PaginatedUserContactInfoList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserContactInfoList.to_json())

# convert the object into a dict
paginated_user_contact_info_list_dict = paginated_user_contact_info_list_instance.to_dict()
# create an instance of PaginatedUserContactInfoList from a dict
paginated_user_contact_info_list_from_dict = PaginatedUserContactInfoList.from_dict(paginated_user_contact_info_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


