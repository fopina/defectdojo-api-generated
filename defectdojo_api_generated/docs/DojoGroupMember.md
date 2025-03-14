# DojoGroupMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**group** | **int** |  | 
**user** | **int** |  | 
**role** | **int** | This role determines the permissions of the user to manage the group. | 
**prefetch** | [**DojoGroupMemberPrefetch**](DojoGroupMemberPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.dojo_group_member import DojoGroupMember

# TODO update the JSON string below
json = "{}"
# create an instance of DojoGroupMember from a JSON string
dojo_group_member_instance = DojoGroupMember.from_json(json)
# print the JSON string representation of the object
print(DojoGroupMember.to_json())

# convert the object into a dict
dojo_group_member_dict = dojo_group_member_instance.to_dict()
# create an instance of DojoGroupMember from a dict
dojo_group_member_from_dict = DojoGroupMember.from_dict(dojo_group_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


