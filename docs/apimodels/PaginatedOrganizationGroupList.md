# PaginatedOrganizationGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[OrganizationGroup]**](OrganizationGroup.md) |  | [optional] 
**prefetch** | [**OrganizationGroupPrefetch**](OrganizationGroupPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_organization_group_list import PaginatedOrganizationGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedOrganizationGroupList from a JSON string
paginated_organization_group_list_instance = PaginatedOrganizationGroupList.from_json(json)
# print the JSON string representation of the object
print(PaginatedOrganizationGroupList.to_json())

# convert the object into a dict
paginated_organization_group_list_dict = paginated_organization_group_list_instance.to_dict()
# create an instance of PaginatedOrganizationGroupList from a dict
paginated_organization_group_list_from_dict = PaginatedOrganizationGroupList.from_dict(paginated_organization_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


