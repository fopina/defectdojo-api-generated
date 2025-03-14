# PaginatedNotificationWebhooksList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[NotificationWebhooks]**](NotificationWebhooks.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_notification_webhooks_list import PaginatedNotificationWebhooksList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedNotificationWebhooksList from a JSON string
paginated_notification_webhooks_list_instance = PaginatedNotificationWebhooksList.from_json(json)
# print the JSON string representation of the object
print(PaginatedNotificationWebhooksList.to_json())

# convert the object into a dict
paginated_notification_webhooks_list_dict = paginated_notification_webhooks_list_instance.to_dict()
# create an instance of PaginatedNotificationWebhooksList from a dict
paginated_notification_webhooks_list_from_dict = PaginatedNotificationWebhooksList.from_dict(paginated_notification_webhooks_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


