# EngagementUpdateJiraEpic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epic_name** | **str** |  | [optional] 
**epic_priority** | **str** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.engagement_update_jira_epic import EngagementUpdateJiraEpic

# TODO update the JSON string below
json = "{}"
# create an instance of EngagementUpdateJiraEpic from a JSON string
engagement_update_jira_epic_instance = EngagementUpdateJiraEpic.from_json(json)
# print the JSON string representation of the object
print(EngagementUpdateJiraEpic.to_json())

# convert the object into a dict
engagement_update_jira_epic_dict = engagement_update_jira_epic_instance.to_dict()
# create an instance of EngagementUpdateJiraEpic from a dict
engagement_update_jira_epic_from_dict = EngagementUpdateJiraEpic.from_dict(engagement_update_jira_epic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


