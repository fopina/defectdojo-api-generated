# EngagementUpdateJiraEpicRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epic_name** | **str** |  | [optional] 
**epic_priority** | **str** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.engagement_update_jira_epic_request import EngagementUpdateJiraEpicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EngagementUpdateJiraEpicRequest from a JSON string
engagement_update_jira_epic_request_instance = EngagementUpdateJiraEpicRequest.from_json(json)
# print the JSON string representation of the object
print(EngagementUpdateJiraEpicRequest.to_json())

# convert the object into a dict
engagement_update_jira_epic_request_dict = engagement_update_jira_epic_request_instance.to_dict()
# create an instance of EngagementUpdateJiraEpicRequest from a dict
engagement_update_jira_epic_request_from_dict = EngagementUpdateJiraEpicRequest.from_dict(engagement_update_jira_epic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


