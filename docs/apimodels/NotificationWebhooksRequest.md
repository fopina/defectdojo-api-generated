# NotificationWebhooksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the incoming webhook | [optional] 
**url** | **str** | The full URL of the incoming webhook | [optional] 
**header_name** | **str** | Name of the header required for interacting with Webhook endpoint | [optional] 
**header_value** | **str** | Content of the header required for interacting with Webhook endpoint | [optional] 
**owner** | **int** | Owner/receiver of notification, if empty processed as system notification | [optional] 

## Example

```python
from defectdojo_api_generated.models.notification_webhooks_request import NotificationWebhooksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationWebhooksRequest from a JSON string
notification_webhooks_request_instance = NotificationWebhooksRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationWebhooksRequest.to_json())

# convert the object into a dict
notification_webhooks_request_dict = notification_webhooks_request_instance.to_dict()
# create an instance of NotificationWebhooksRequest from a dict
notification_webhooks_request_from_dict = NotificationWebhooksRequest.from_dict(notification_webhooks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


