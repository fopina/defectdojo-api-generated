# UserProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User**](User.md) |  | 
**user_contact_info** | [**UserContactInfo**](UserContactInfo.md) |  | [optional] 
**global_role** | [**GlobalRole**](GlobalRole.md) |  | [optional] 
**dojo_group_member** | [**List[DojoGroupMember]**](DojoGroupMember.md) |  | 
**product_type_member** | [**List[ProductTypeMember]**](ProductTypeMember.md) |  | 
**product_member** | [**List[ProductMember]**](ProductMember.md) |  | 

## Example

```python
from defectdojo_api_generated.models.user_profile import UserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfile from a JSON string
user_profile_instance = UserProfile.from_json(json)
# print the JSON string representation of the object
print(UserProfile.to_json())

# convert the object into a dict
user_profile_dict = user_profile_instance.to_dict()
# create an instance of UserProfile from a dict
user_profile_from_dict = UserProfile.from_dict(user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


