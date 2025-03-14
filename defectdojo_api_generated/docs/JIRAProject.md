# JIRAProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**project_key** | **str** |  | [optional] 
**issue_template_dir** | **str** | Choose the folder containing the Django templates used to render the JIRA issue description. These are stored in dojo/templates/issue-trackers. Leave empty to use the default jira_full templates. | [optional] 
**component** | **str** |  | [optional] 
**custom_fields** | **object** | JIRA custom field JSON mapping of Id to value, e.g. {\&quot;customfield_10122\&quot;: [{\&quot;name\&quot;: \&quot;8.0.1\&quot;}]} | [optional] 
**default_assignee** | **str** | JIRA default assignee (name). If left blank then it defaults to whatever is configured in JIRA. | [optional] 
**jira_labels** | **str** | JIRA issue labels space seperated | [optional] 
**add_vulnerability_id_to_jira_label** | **bool** |  | [optional] 
**push_all_issues** | **bool** | Automatically create JIRA tickets for verified findings, assuming enforce_verified_status is True, or for all findings otherwise. Once linked, the JIRA ticket will continue to sync, regardless of status in DefectDojo. | [optional] 
**enable_engagement_epic_mapping** | **bool** |  | [optional] 
**epic_issue_type_name** | **str** | The name of the of structure that represents an Epic | [optional] 
**push_notes** | **bool** |  | [optional] 
**product_jira_sla_notification** | **bool** |  | [optional] 
**risk_acceptance_expiration_notification** | **bool** |  | [optional] 
**enabled** | **bool** | When disabled, Findings will no longer be pushed to Jira, even if they have already been pushed previously. | [optional] 
**jira_instance** | **int** |  | [optional] 
**product** | **int** |  | [optional] 
**engagement** | **int** |  | [optional] 
**prefetch** | [**JIRAProjectPrefetch**](JIRAProjectPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.jira_project import JIRAProject

# TODO update the JSON string below
json = "{}"
# create an instance of JIRAProject from a JSON string
jira_project_instance = JIRAProject.from_json(json)
# print the JSON string representation of the object
print(JIRAProject.to_json())

# convert the object into a dict
jira_project_dict = jira_project_instance.to_dict()
# create an instance of JIRAProject from a dict
jira_project_from_dict = JIRAProject.from_dict(jira_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


