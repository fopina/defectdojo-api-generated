# UserStub


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.user_stub import UserStub

# TODO update the JSON string below
json = "{}"
# create an instance of UserStub from a JSON string
user_stub_instance = UserStub.from_json(json)
# print the JSON string representation of the object
print(UserStub.to_json())

# convert the object into a dict
user_stub_dict = user_stub_instance.to_dict()
# create an instance of UserStub from a dict
user_stub_from_dict = UserStub.from_dict(user_stub_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


