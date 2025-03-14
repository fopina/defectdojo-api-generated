# PatchedUserContactInfoRequest


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
**user** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_user_contact_info_request import PatchedUserContactInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUserContactInfoRequest from a JSON string
patched_user_contact_info_request_instance = PatchedUserContactInfoRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedUserContactInfoRequest.to_json())

# convert the object into a dict
patched_user_contact_info_request_dict = patched_user_contact_info_request_instance.to_dict()
# create an instance of PatchedUserContactInfoRequest from a dict
patched_user_contact_info_request_from_dict = PatchedUserContactInfoRequest.from_dict(patched_user_contact_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


