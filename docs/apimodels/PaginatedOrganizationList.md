# PaginatedOrganizationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Organization]**](Organization.md) |  | [optional] 
**prefetch** | [**OrganizationPrefetch**](OrganizationPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_organization_list import PaginatedOrganizationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedOrganizationList from a JSON string
paginated_organization_list_instance = PaginatedOrganizationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedOrganizationList.to_json())

# convert the object into a dict
paginated_organization_list_dict = paginated_organization_list_instance.to_dict()
# create an instance of PaginatedOrganizationList from a dict
paginated_organization_list_from_dict = PaginatedOrganizationList.from_dict(paginated_organization_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


