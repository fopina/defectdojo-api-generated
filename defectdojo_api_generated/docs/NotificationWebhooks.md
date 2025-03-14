# NotificationWebhooks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | Name of the incoming webhook | [optional] 
**url** | **str** | The full URL of the incoming webhook | [optional] 
**header_name** | **str** | Name of the header required for interacting with Webhook endpoint | [optional] 
**header_value** | **str** | Content of the header required for interacting with Webhook endpoint | [optional] 
**status** | **str** | Status of the incoming webhook | [readonly] 
**first_error** | **datetime** | If endpoint is active, when error happened first time | [readonly] 
**last_error** | **datetime** | If endpoint is active, when error happened last time | [readonly] 
**note** | **str** | Description of the latest error | [readonly] 
**owner** | **int** | Owner/receiver of notification, if empty processed as system notification | [optional] 

## Example

```python
from defectdojo_api_generated.models.notification_webhooks import NotificationWebhooks

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationWebhooks from a JSON string
notification_webhooks_instance = NotificationWebhooks.from_json(json)
# print the JSON string representation of the object
print(NotificationWebhooks.to_json())

# convert the object into a dict
notification_webhooks_dict = notification_webhooks_instance.to_dict()
# create an instance of NotificationWebhooks from a dict
notification_webhooks_from_dict = NotificationWebhooks.from_dict(notification_webhooks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


