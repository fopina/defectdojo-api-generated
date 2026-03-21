# EngagementCheckListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_management** | **str** |  | [optional] 
**encryption_crypto** | **str** |  | [optional] 
**configuration_management** | **str** |  | [optional] 
**authentication** | **str** |  | [optional] 
**authorization_and_access_control** | **str** |  | [optional] 
**data_input_sanitization_validation** | **str** |  | [optional] 
**sensitive_data** | **str** |  | [optional] 
**other** | **str** |  | [optional] 
**session_issues** | **List[int]** |  | [optional] 
**crypto_issues** | **List[int]** |  | [optional] 
**config_issues** | **List[int]** |  | [optional] 
**auth_issues** | **List[int]** |  | [optional] 
**author_issues** | **List[int]** |  | [optional] 
**data_issues** | **List[int]** |  | [optional] 
**sensitive_issues** | **List[int]** |  | [optional] 
**other_issues** | **List[int]** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.engagement_check_list_request import EngagementCheckListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EngagementCheckListRequest from a JSON string
engagement_check_list_request_instance = EngagementCheckListRequest.from_json(json)
# print the JSON string representation of the object
print(EngagementCheckListRequest.to_json())

# convert the object into a dict
engagement_check_list_request_dict = engagement_check_list_request_instance.to_dict()
# create an instance of EngagementCheckListRequest from a dict
engagement_check_list_request_from_dict = EngagementCheckListRequest.from_dict(engagement_check_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


