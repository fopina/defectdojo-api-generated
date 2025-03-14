# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | 
**date_joined** | **datetime** |  | [readonly] 
**last_login** | **datetime** |  | [readonly] 
**is_active** | **bool** | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | [optional] 
**is_superuser** | **bool** | Designates that this user has all permissions without explicitly assigning them. | [optional] 
**configuration_permissions** | **List[Optional[int]]** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


