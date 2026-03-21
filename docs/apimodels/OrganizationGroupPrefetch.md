# OrganizationGroupPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**Dict[str, DojoGroup]**](DojoGroup.md) |  | [optional] [readonly] 
**product_type** | [**Dict[str, ProductType]**](ProductType.md) |  | [optional] [readonly] 
**role** | [**Dict[str, Role]**](Role.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.organization_group_prefetch import OrganizationGroupPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationGroupPrefetch from a JSON string
organization_group_prefetch_instance = OrganizationGroupPrefetch.from_json(json)
# print the JSON string representation of the object
print(OrganizationGroupPrefetch.to_json())

# convert the object into a dict
organization_group_prefetch_dict = organization_group_prefetch_instance.to_dict()
# create an instance of OrganizationGroupPrefetch from a dict
organization_group_prefetch_from_dict = OrganizationGroupPrefetch.from_dict(organization_group_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


