# PaginatedDojoGroupMemberList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DojoGroupMember]**](DojoGroupMember.md) |  | 
**prefetch** | [**DojoGroupMemberPrefetch**](DojoGroupMemberPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_dojo_group_member_list import PaginatedDojoGroupMemberList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDojoGroupMemberList from a JSON string
paginated_dojo_group_member_list_instance = PaginatedDojoGroupMemberList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDojoGroupMemberList.to_json())

# convert the object into a dict
paginated_dojo_group_member_list_dict = paginated_dojo_group_member_list_instance.to_dict()
# create an instance of PaginatedDojoGroupMemberList from a dict
paginated_dojo_group_member_list_from_dict = PaginatedDojoGroupMemberList.from_dict(paginated_dojo_group_member_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


