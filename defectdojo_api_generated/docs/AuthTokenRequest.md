# AuthTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from defectdojo_api_generated.models.auth_token_request import AuthTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthTokenRequest from a JSON string
auth_token_request_instance = AuthTokenRequest.from_json(json)
# print the JSON string representation of the object
print(AuthTokenRequest.to_json())

# convert the object into a dict
auth_token_request_dict = auth_token_request_instance.to_dict()
# create an instance of AuthTokenRequest from a dict
auth_token_request_from_dict = AuthTokenRequest.from_dict(auth_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


