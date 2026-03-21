# PaginatedOrganizationMemberList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[OrganizationMember]**](OrganizationMember.md) |  | [optional] 
**prefetch** | [**OrganizationMemberPrefetch**](OrganizationMemberPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_organization_member_list import PaginatedOrganizationMemberList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedOrganizationMemberList from a JSON string
paginated_organization_member_list_instance = PaginatedOrganizationMemberList.from_json(json)
# print the JSON string representation of the object
print(PaginatedOrganizationMemberList.to_json())

# convert the object into a dict
paginated_organization_member_list_dict = paginated_organization_member_list_instance.to_dict()
# create an instance of PaginatedOrganizationMemberList from a dict
paginated_organization_member_list_from_dict = PaginatedOrganizationMemberList.from_dict(paginated_organization_member_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


