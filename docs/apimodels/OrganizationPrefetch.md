# OrganizationPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_groups** | [**Dict[str, DojoGroup]**](DojoGroup.md) |  | [optional] [readonly] 
**members** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.organization_prefetch import OrganizationPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationPrefetch from a JSON string
organization_prefetch_instance = OrganizationPrefetch.from_json(json)
# print the JSON string representation of the object
print(OrganizationPrefetch.to_json())

# convert the object into a dict
organization_prefetch_dict = organization_prefetch_instance.to_dict()
# create an instance of OrganizationPrefetch from a dict
organization_prefetch_from_dict = OrganizationPrefetch.from_dict(organization_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


