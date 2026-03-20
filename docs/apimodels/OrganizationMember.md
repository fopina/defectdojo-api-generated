# OrganizationMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**organization** | **int** |  | [optional] 
**user** | **int** |  | [optional] 
**role** | **int** |  | [optional] 
**prefetch** | [**OrganizationMemberPrefetch**](OrganizationMemberPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.organization_member import OrganizationMember

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMember from a JSON string
organization_member_instance = OrganizationMember.from_json(json)
# print the JSON string representation of the object
print(OrganizationMember.to_json())

# convert the object into a dict
organization_member_dict = organization_member_instance.to_dict()
# create an instance of OrganizationMember from a dict
organization_member_from_dict = OrganizationMember.from_dict(organization_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


