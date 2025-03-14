# PatchedJIRAInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_name** | **str** | Enter a name to give to this configuration | [optional] 
**url** | **str** | For more information how to configure Jira, read the DefectDojo documentation. | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**default_issue_type** | **str** | You can define extra issue types in settings.py  * &#x60;Task&#x60; - Task * &#x60;Story&#x60; - Story * &#x60;Epic&#x60; - Epic * &#x60;Spike&#x60; - Spike * &#x60;Bug&#x60; - Bug * &#x60;Security&#x60; - Security | [optional] 
**issue_template_dir** | **str** | Choose the folder containing the Django templates used to render the JIRA issue description. These are stored in dojo/templates/issue-trackers. Leave empty to use the default jira_full templates. | [optional] 
**epic_name_id** | **int** | To obtain the &#39;Epic name id&#39; visit https://&lt;YOUR JIRA URL&gt;/rest/api/2/field and search for Epic Name. Copy the number out of cf[number] and paste it here. | [optional] 
**open_status_key** | **int** | Transition ID to Re-Open JIRA issues, visit https://&lt;YOUR JIRA URL&gt;/rest/api/latest/issue/&lt;ANY VALID ISSUE KEY&gt;/transitions?expand&#x3D;transitions.fields to find the ID for your JIRA instance | [optional] 
**close_status_key** | **int** | Transition ID to Close JIRA issues, visit https://&lt;YOUR JIRA URL&gt;/rest/api/latest/issue/&lt;ANY VALID ISSUE KEY&gt;/transitions?expand&#x3D;transitions.fields to find the ID for your JIRA instance | [optional] 
**info_mapping_severity** | **str** | Maps to the &#39;Priority&#39; field in Jira. For example: Info | [optional] 
**low_mapping_severity** | **str** | Maps to the &#39;Priority&#39; field in Jira. For example: Low | [optional] 
**medium_mapping_severity** | **str** | Maps to the &#39;Priority&#39; field in Jira. For example: Medium | [optional] 
**high_mapping_severity** | **str** | Maps to the &#39;Priority&#39; field in Jira. For example: High | [optional] 
**critical_mapping_severity** | **str** | Maps to the &#39;Priority&#39; field in Jira. For example: Critical | [optional] 
**finding_text** | **str** | Additional text that will be added to the finding in Jira. For example including how the finding was created or who to contact for more information. | [optional] 
**accepted_mapping_resolution** | **str** | JIRA resolution names (comma-separated values) that maps to an Accepted Finding | [optional] 
**false_positive_mapping_resolution** | **str** | JIRA resolution names (comma-separated values) that maps to a False Positive Finding | [optional] 
**global_jira_sla_notification** | **bool** | This setting can be overidden at the Product level | [optional] 
**finding_jira_sync** | **bool** | If enabled, this will sync changes to a Finding automatically to JIRA | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_jira_instance_request import PatchedJIRAInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedJIRAInstanceRequest from a JSON string
patched_jira_instance_request_instance = PatchedJIRAInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedJIRAInstanceRequest.to_json())

# convert the object into a dict
patched_jira_instance_request_dict = patched_jira_instance_request_instance.to_dict()
# create an instance of PatchedJIRAInstanceRequest from a dict
patched_jira_instance_request_from_dict = PatchedJIRAInstanceRequest.from_dict(patched_jira_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


