# PatchedSystemSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_deduplication** | **bool** | With this setting turned on, DefectDojo deduplicates findings by comparing endpoints, cwe fields, and titles. If two findings share a URL and have the same CWE or title, DefectDojo marks the recent finding as a duplicate. When deduplication is enabled, a list of deduplicated findings is added to the engagement view. | [optional] 
**delete_duplicates** | **bool** | Requires next setting: maximum number of duplicates to retain. | [optional] 
**max_dupes** | **int** | When enabled, if a single issue reaches the maximum number of duplicates, the oldest will be deleted. Duplicate will not be deleted when left empty. A value of 0 will remove all duplicates. | [optional] 
**email_from** | **str** |  | [optional] 
**enable_jira** | **bool** |  | [optional] 
**enable_jira_web_hook** | **bool** | Please note: It is strongly recommended to use a secret below and / or IP whitelist the JIRA server using a proxy such as Nginx. | [optional] 
**disable_jira_webhook_secret** | **bool** | Allows incoming requests without a secret (discouraged legacy behaviour) | [optional] 
**jira_webhook_secret** | **str** | Secret needed in URL for incoming JIRA Webhook | [optional] 
**jira_minimum_severity** | **str** | * &#x60;Critical&#x60; - Critical * &#x60;High&#x60; - High * &#x60;Medium&#x60; - Medium * &#x60;Low&#x60; - Low * &#x60;Info&#x60; - Info | [optional] 
**jira_labels** | **str** | JIRA issue labels space seperated | [optional] 
**add_vulnerability_id_to_jira_label** | **bool** |  | [optional] 
**enable_github** | **bool** |  | [optional] 
**enable_slack_notifications** | **bool** |  | [optional] 
**slack_channel** | **str** | Optional. Needed if you want to send global notifications. | [optional] 
**slack_token** | **str** | Token required for interacting with Slack. Get one at https://api.slack.com/tokens | [optional] 
**slack_username** | **str** | Optional. Will take your bot name otherwise. | [optional] 
**enable_msteams_notifications** | **bool** |  | [optional] 
**msteams_url** | **str** | The full URL of the incoming webhook | [optional] 
**enable_mail_notifications** | **bool** |  | [optional] 
**mail_notifications_to** | **str** |  | [optional] 
**enable_webhooks_notifications** | **bool** |  | [optional] 
**webhooks_notifications_timeout** | **int** | How many seconds will DefectDojo waits for response from webhook endpoint | [optional] 
**enforce_verified_status** | **bool** | When enabled, features such as product grading, jira integration, metrics, and reports will only interact with verified findings. This setting will override individually scoped verified toggles. | [optional] 
**enforce_verified_status_jira** | **bool** | When enabled, findings must have a verified status to be pushed to jira. | [optional] 
**enforce_verified_status_product_grading** | **bool** | When enabled, findings must have a verified status to be considered as part of a product&#39;s grading. | [optional] 
**enforce_verified_status_metrics** | **bool** | When enabled, findings must have a verified status to be counted in metric calculations, be included in reports, and filters. | [optional] 
**false_positive_history** | **bool** | (EXPERIMENTAL) DefectDojo will automatically mark the finding as a false positive if an equal finding (according to its dedupe algorithm) has been previously marked as a false positive on the same product. ATTENTION: Although the deduplication algorithm is used to determine if a finding should be marked as a false positive, this feature will not work if deduplication is enabled since it doesn&#39;t make sense to use both. | [optional] 
**retroactive_false_positive_history** | **bool** | (EXPERIMENTAL) FP History will also retroactively mark/unmark all existing equal findings in the same product as a false positives. Only works if the False Positive History feature is also enabled. | [optional] 
**url_prefix** | **str** | URL prefix if DefectDojo is installed in it&#39;s own virtual subdirectory. | [optional] 
**team_name** | **str** |  | [optional] 
**enable_product_grade** | **bool** | Displays a grade letter next to a product to show the overall health. | [optional] 
**product_grade_a** | **int** | Percentage score for an &#39;A&#39; &gt;&#x3D; | [optional] 
**product_grade_b** | **int** | Percentage score for a &#39;B&#39; &gt;&#x3D; | [optional] 
**product_grade_c** | **int** | Percentage score for a &#39;C&#39; &gt;&#x3D; | [optional] 
**product_grade_d** | **int** | Percentage score for a &#39;D&#39; &gt;&#x3D; | [optional] 
**product_grade_f** | **int** | Percentage score for an &#39;F&#39; &lt;&#x3D; | [optional] 
**enable_product_tag_inheritance** | **bool** | Enables product tag inheritance globally for all products. Any tags added on a product will automatically be added to all Engagements, Tests, and Findings | [optional] 
**enable_benchmark** | **bool** | Enables Benchmarks such as the OWASP ASVS (Application Security Verification Standard) | [optional] 
**enable_similar_findings** | **bool** | Enable the query of similar findings on the view finding page. This feature can involve potentially large queries and negatively impact performance | [optional] 
**engagement_auto_close** | **bool** | Closes an engagement after 3 days (default) past due date including last update. | [optional] 
**engagement_auto_close_days** | **int** | Closes an engagement after the specified number of days past due date including last update. | [optional] 
**enable_finding_sla** | **bool** | Enables Finding SLA&#39;s for time to remediate. | [optional] 
**enable_notify_sla_active** | **bool** | Enables Notify when time to remediate according to Finding SLA&#39;s is breached for active Findings. | [optional] 
**enable_notify_sla_active_verified** | **bool** | Enables Notify when time to remediate according to Finding SLA&#39;s is breached for active, verified Findings. | [optional] 
**enable_notify_sla_jira_only** | **bool** | Enables Notify when time to remediate according to Finding SLA&#39;s is breached for Findings that are linked to JIRA issues. Notification is disabled for Findings not linked to JIRA issues | [optional] 
**enable_notify_sla_exponential_backoff** | **bool** | Enable an exponential backoff strategy for SLA breach notifications, e.g. 1, 2, 4, 8, etc. Otherwise it alerts every day | [optional] 
**allow_anonymous_survey_repsonse** | **bool** | Enable anyone with a link to the survey to answer a survey | [optional] 
**disclaimer_notifications** | **str** | Include this custom disclaimer on all notifications | [optional] 
**disclaimer_reports** | **str** | Include this custom disclaimer on generated reports | [optional] 
**disclaimer_reports_forced** | **bool** | Disclaimer will be added to all reports even if user didn&#39;t selected &#39;Include disclaimer&#39;. | [optional] 
**disclaimer_notes** | **str** | Include this custom disclaimer next to input form for notes | [optional] 
**risk_acceptance_form_default_days** | **int** | Default expiry period for risk acceptance form. | [optional] 
**risk_acceptance_notify_before_expiration** | **int** | Notify X days before risk acceptance expires. Leave empty to disable. | [optional] 
**enable_credentials** | **bool** | With this setting turned off, credentials will be disabled in the user interface. | [optional] 
**enable_questionnaires** | **bool** | With this setting turned off, questionnaires will be disabled in the user interface. | [optional] 
**enable_checklists** | **bool** | With this setting turned off, checklists will be disabled in the user interface. | [optional] 
**enable_endpoint_metadata_import** | **bool** | With this setting turned off, endpoint metadata import will be disabled in the user interface. | [optional] 
**enable_user_profile_editable** | **bool** | When turned on users can edit their profiles | [optional] 
**enable_product_tracking_files** | **bool** | With this setting turned off, the product tracking files will be disabled in the user interface. | [optional] 
**enable_finding_groups** | **bool** | With this setting turned off, the Finding Groups will be disabled. | [optional] 
**enable_ui_table_based_searching** | **bool** | With this setting enabled, table headings will contain sort buttons for the current page of data in addition to sorting buttons that consider data from all pages. | [optional] 
**enable_calendar** | **bool** | With this setting turned off, the Calendar will be disabled in the user interface. | [optional] 
**enable_cvss3_display** | **bool** | With this setting turned off, CVSS3 fields will be hidden in the user interface. | [optional] 
**enable_cvss4_display** | **bool** | With this setting turned off, CVSS4 fields will be hidden in the user interface. | [optional] 
**default_group_email_pattern** | **str** | New users will only be assigned to the default group, when their email address matches this regex pattern. This is optional condition. | [optional] 
**minimum_password_length** | **int** | Requires user to set passwords greater than minimum length. | [optional] 
**maximum_password_length** | **int** | Requires user to set passwords less than maximum length. | [optional] 
**number_character_required** | **bool** | Requires user passwords to contain at least one digit (0-9). | [optional] 
**special_character_required** | **bool** | Requires user passwords to contain at least one special character (()[]{}|\\&#x60;~!@#$%^&amp;*_-+&#x3D;;:&#39;\&quot;,&lt;&gt;./?). | [optional] 
**lowercase_character_required** | **bool** | Requires user passwords to contain at least one lowercase letter (a-z). | [optional] 
**uppercase_character_required** | **bool** | Requires user passwords to contain at least one uppercase letter (A-Z). | [optional] 
**non_common_password_required** | **bool** | Requires user passwords to not be part of list of common passwords. | [optional] 
**api_expose_error_details** | **bool** | When turned on, the API will expose error details in the response. | [optional] 
**filter_string_matching** | **bool** | When turned on, all filter operations in the UI will require string matches rather than ID. This is a performance enhancement to avoid fetching objects unnecessarily. | [optional] 
**default_group** | **int** | New users will be assigned to this group. | [optional] 
**default_group_role** | **int** | New users will be assigned to their default group with this role. | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_system_settings_request import PatchedSystemSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSystemSettingsRequest from a JSON string
patched_system_settings_request_instance = PatchedSystemSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedSystemSettingsRequest.to_json())

# convert the object into a dict
patched_system_settings_request_dict = patched_system_settings_request_instance.to_dict()
# create an instance of PatchedSystemSettingsRequest from a dict
patched_system_settings_request_from_dict = PatchedSystemSettingsRequest.from_dict(patched_system_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


