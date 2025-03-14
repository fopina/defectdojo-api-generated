# UserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | 
**is_active** | **bool** | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | [optional] 
**is_superuser** | **bool** | Designates that this user has all permissions without explicitly assigning them. | [optional] 
**password** | **str** |  | [optional] 
**configuration_permissions** | **List[Optional[int]]** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.user_request import UserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserRequest from a JSON string
user_request_instance = UserRequest.from_json(json)
# print the JSON string representation of the object
print(UserRequest.to_json())

# convert the object into a dict
user_request_dict = user_request_instance.to_dict()
# create an instance of UserRequest from a dict
user_request_from_dict = UserRequest.from_dict(user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


