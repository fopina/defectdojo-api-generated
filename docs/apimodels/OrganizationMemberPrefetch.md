# OrganizationMemberPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_type** | [**Dict[str, ProductType]**](ProductType.md) |  | [optional] [readonly] 
**role** | [**Dict[str, Role]**](Role.md) |  | [optional] [readonly] 
**user** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.organization_member_prefetch import OrganizationMemberPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMemberPrefetch from a JSON string
organization_member_prefetch_instance = OrganizationMemberPrefetch.from_json(json)
# print the JSON string representation of the object
print(OrganizationMemberPrefetch.to_json())

# convert the object into a dict
organization_member_prefetch_dict = organization_member_prefetch_instance.to_dict()
# create an instance of OrganizationMemberPrefetch from a dict
organization_member_prefetch_from_dict = OrganizationMemberPrefetch.from_dict(organization_member_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


