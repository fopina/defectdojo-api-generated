# UserStubRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.user_stub_request import UserStubRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserStubRequest from a JSON string
user_stub_request_instance = UserStubRequest.from_json(json)
# print the JSON string representation of the object
print(UserStubRequest.to_json())

# convert the object into a dict
user_stub_request_dict = user_stub_request_instance.to_dict()
# create an instance of UserStubRequest from a dict
user_stub_request_from_dict = UserStubRequest.from_dict(user_stub_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


