# PaginatedEngagementPresetsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[EngagementPresets]**](EngagementPresets.md) |  | 
**prefetch** | [**EngagementPresetsPrefetch**](EngagementPresetsPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_engagement_presets_list import PaginatedEngagementPresetsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEngagementPresetsList from a JSON string
paginated_engagement_presets_list_instance = PaginatedEngagementPresetsList.from_json(json)
# print the JSON string representation of the object
print(PaginatedEngagementPresetsList.to_json())

# convert the object into a dict
paginated_engagement_presets_list_dict = paginated_engagement_presets_list_instance.to_dict()
# create an instance of PaginatedEngagementPresetsList from a dict
paginated_engagement_presets_list_from_dict = PaginatedEngagementPresetsList.from_dict(paginated_engagement_presets_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


