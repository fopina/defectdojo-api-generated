# PaginatedNotificationsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Notifications]**](Notifications.md) |  | 
**prefetch** | [**AppAnalysisPrefetch**](AppAnalysisPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_notifications_list import PaginatedNotificationsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedNotificationsList from a JSON string
paginated_notifications_list_instance = PaginatedNotificationsList.from_json(json)
# print the JSON string representation of the object
print(PaginatedNotificationsList.to_json())

# convert the object into a dict
paginated_notifications_list_dict = paginated_notifications_list_instance.to_dict()
# create an instance of PaginatedNotificationsList from a dict
paginated_notifications_list_from_dict = PaginatedNotificationsList.from_dict(paginated_notifications_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


