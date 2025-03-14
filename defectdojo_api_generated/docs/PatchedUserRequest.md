# PatchedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**is_active** | **bool** | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | [optional] 
**is_superuser** | **bool** | Designates that this user has all permissions without explicitly assigning them. | [optional] 
**password** | **str** |  | [optional] 
**configuration_permissions** | **List[Optional[int]]** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_user_request import PatchedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUserRequest from a JSON string
patched_user_request_instance = PatchedUserRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedUserRequest.to_json())

# convert the object into a dict
patched_user_request_dict = patched_user_request_instance.to_dict()
# create an instance of PatchedUserRequest from a dict
patched_user_request_from_dict = PatchedUserRequest.from_dict(patched_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


