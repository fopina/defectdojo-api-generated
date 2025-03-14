# DojoGroupMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **int** |  | 
**user** | **int** |  | 
**role** | **int** | This role determines the permissions of the user to manage the group. | 

## Example

```python
from defectdojo_api_generated.models.dojo_group_member_request import DojoGroupMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DojoGroupMemberRequest from a JSON string
dojo_group_member_request_instance = DojoGroupMemberRequest.from_json(json)
# print the JSON string representation of the object
print(DojoGroupMemberRequest.to_json())

# convert the object into a dict
dojo_group_member_request_dict = dojo_group_member_request_instance.to_dict()
# create an instance of DojoGroupMemberRequest from a dict
dojo_group_member_request_from_dict = DojoGroupMemberRequest.from_dict(dojo_group_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


