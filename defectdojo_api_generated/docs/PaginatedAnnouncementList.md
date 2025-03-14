# PaginatedAnnouncementList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Announcement]**](Announcement.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_announcement_list import PaginatedAnnouncementList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAnnouncementList from a JSON string
paginated_announcement_list_instance = PaginatedAnnouncementList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAnnouncementList.to_json())

# convert the object into a dict
paginated_announcement_list_dict = paginated_announcement_list_instance.to_dict()
# create an instance of PaginatedAnnouncementList from a dict
paginated_announcement_list_from_dict = PaginatedAnnouncementList.from_dict(paginated_announcement_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


