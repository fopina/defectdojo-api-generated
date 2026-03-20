# OrganizationGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**organization** | **int** |  | [optional] 
**group** | **int** |  | [optional] 
**role** | **int** |  | [optional] 
**prefetch** | [**OrganizationGroupPrefetch**](OrganizationGroupPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.organization_group import OrganizationGroup

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationGroup from a JSON string
organization_group_instance = OrganizationGroup.from_json(json)
# print the JSON string representation of the object
print(OrganizationGroup.to_json())

# convert the object into a dict
organization_group_dict = organization_group_instance.to_dict()
# create an instance of OrganizationGroup from a dict
organization_group_from_dict = OrganizationGroup.from_dict(organization_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


