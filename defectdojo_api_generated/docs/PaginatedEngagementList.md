# PaginatedEngagementList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Engagement]**](Engagement.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_engagement_list import PaginatedEngagementList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEngagementList from a JSON string
paginated_engagement_list_instance = PaginatedEngagementList.from_json(json)
# print the JSON string representation of the object
print(PaginatedEngagementList.to_json())

# convert the object into a dict
paginated_engagement_list_dict = paginated_engagement_list_instance.to_dict()
# create an instance of PaginatedEngagementList from a dict
paginated_engagement_list_from_dict = PaginatedEngagementList.from_dict(paginated_engagement_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


