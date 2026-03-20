# DojoGroupMemberPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**Dict[str, DojoGroup]**](DojoGroup.md) |  | [optional] [readonly] 
**role** | [**Dict[str, Role]**](Role.md) |  | [optional] [readonly] 
**user** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.dojo_group_member_prefetch import DojoGroupMemberPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of DojoGroupMemberPrefetch from a JSON string
dojo_group_member_prefetch_instance = DojoGroupMemberPrefetch.from_json(json)
# print the JSON string representation of the object
print(DojoGroupMemberPrefetch.to_json())

# convert the object into a dict
dojo_group_member_prefetch_dict = dojo_group_member_prefetch_instance.to_dict()
# create an instance of DojoGroupMemberPrefetch from a dict
dojo_group_member_prefetch_from_dict = DojoGroupMemberPrefetch.from_dict(dojo_group_member_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


