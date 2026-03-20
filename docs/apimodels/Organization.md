# Organization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**critical_asset** | **bool** |  | [optional] [default to False]
**key_asset** | **bool** |  | [optional] [default to False]
**created** | **datetime** | Time that the object was initially created, and saved to the database | [optional] [readonly] 
**updated** | **datetime** | Time that the object was most recently saved to the database | [optional] [readonly] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**members** | **List[int]** |  | [optional] [readonly] 
**authorization_groups** | **List[int]** |  | [optional] [readonly] 
**prefetch** | [**OrganizationPrefetch**](OrganizationPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print(Organization.to_json())

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_from_dict = Organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


