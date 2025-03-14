# PaginatedGlobalRoleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[GlobalRole]**](GlobalRole.md) |  | 
**prefetch** | [**DojoGroupMemberPrefetch**](DojoGroupMemberPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_global_role_list import PaginatedGlobalRoleList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGlobalRoleList from a JSON string
paginated_global_role_list_instance = PaginatedGlobalRoleList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGlobalRoleList.to_json())

# convert the object into a dict
paginated_global_role_list_dict = paginated_global_role_list_instance.to_dict()
# create an instance of PaginatedGlobalRoleList from a dict
paginated_global_role_list_from_dict = PaginatedGlobalRoleList.from_dict(paginated_global_role_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


