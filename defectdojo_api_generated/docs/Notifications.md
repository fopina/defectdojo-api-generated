# Notifications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**product** | **int** |  | [optional] 
**user** | **int** |  | [optional] 
**product_type_added** | **List[str]** |  | [optional] [default to ["alert"]]
**product_added** | **List[str]** |  | [optional] [default to ["alert"]]
**engagement_added** | **List[str]** |  | [optional] [default to ["alert"]]
**test_added** | **List[str]** |  | [optional] [default to ["alert"]]
**scan_added** | **List[str]** |  | [optional] [default to ["alert"]]
**jira_update** | **List[str]** |  | [optional] [default to ["alert"]]
**upcoming_engagement** | **List[str]** |  | [optional] [default to ["alert"]]
**stale_engagement** | **List[str]** |  | [optional] [default to ["alert"]]
**auto_close_engagement** | **List[str]** |  | [optional] [default to ["alert"]]
**close_engagement** | **List[str]** |  | [optional] [default to ["alert"]]
**user_mentioned** | **List[str]** |  | [optional] [default to ["alert"]]
**code_review** | **List[str]** |  | [optional] [default to ["alert"]]
**review_requested** | **List[str]** |  | [optional] [default to ["alert"]]
**other** | **List[str]** |  | [optional] [default to ["alert"]]
**sla_breach** | **List[str]** |  | [optional] [default to ["alert"]]
**sla_breach_combined** | **List[str]** |  | [optional] [default to ["alert"]]
**risk_acceptance_expiration** | **List[str]** |  | [optional] [default to ["alert"]]
**template** | **bool** |  | [optional] [default to False]
**scan_added_empty** | **str** | Triggered whenever an (re-)import has been done (even if that created/updated/closed no findings).  * &#x60;slack&#x60; - slack * &#x60;msteams&#x60; - msteams * &#x60;mail&#x60; - mail * &#x60;webhooks&#x60; - webhooks * &#x60;alert&#x60; - alert | [optional] 
**prefetch** | [**AppAnalysisPrefetch**](AppAnalysisPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.notifications import Notifications

# TODO update the JSON string below
json = "{}"
# create an instance of Notifications from a JSON string
notifications_instance = Notifications.from_json(json)
# print the JSON string representation of the object
print(Notifications.to_json())

# convert the object into a dict
notifications_dict = notifications_instance.to_dict()
# create an instance of Notifications from a dict
notifications_from_dict = Notifications.from_dict(notifications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


