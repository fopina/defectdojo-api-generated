# UserContactInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**phone_number** | **str** | Phone number must be entered in the format: &#39;+999999999&#39;. Up to 15 digits allowed. | [optional] 
**cell_number** | **str** | Phone number must be entered in the format: &#39;+999999999&#39;. Up to 15 digits allowed. | [optional] 
**twitter_username** | **str** |  | [optional] 
**github_username** | **str** |  | [optional] 
**slack_username** | **str** | Email address associated with your slack account | [optional] 
**slack_user_id** | **str** |  | [optional] 
**block_execution** | **bool** | Instead of async deduping a finding the findings will be deduped synchronously and will &#39;block&#39; the user until completion. | [optional] 
**force_password_reset** | **bool** | Forces this user to reset their password on next login. | [optional] 
**user** | **int** |  | 

## Example

```python
from defectdojo_api_generated.models.user_contact_info_request import UserContactInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserContactInfoRequest from a JSON string
user_contact_info_request_instance = UserContactInfoRequest.from_json(json)
# print the JSON string representation of the object
print(UserContactInfoRequest.to_json())

# convert the object into a dict
user_contact_info_request_dict = user_contact_info_request_instance.to_dict()
# create an instance of UserContactInfoRequest from a dict
user_contact_info_request_from_dict = UserContactInfoRequest.from_dict(user_contact_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


