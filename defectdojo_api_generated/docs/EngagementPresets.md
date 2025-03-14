# EngagementPresets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**title** | **str** | Brief description of preset. | [optional] 
**notes** | **str** | Description of what needs to be tested or setting up environment for testing | [optional] 
**scope** | **str** | Scope of Engagement testing, IP&#39;s/Resources/URL&#39;s) | [optional] 
**created** | **datetime** |  | [readonly] 
**product** | **int** |  | 
**test_type** | **List[int]** |  | [optional] 
**network_locations** | **List[int]** |  | [optional] 
**prefetch** | [**EngagementPresetsPrefetch**](EngagementPresetsPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.engagement_presets import EngagementPresets

# TODO update the JSON string below
json = "{}"
# create an instance of EngagementPresets from a JSON string
engagement_presets_instance = EngagementPresets.from_json(json)
# print the JSON string representation of the object
print(EngagementPresets.to_json())

# convert the object into a dict
engagement_presets_dict = engagement_presets_instance.to_dict()
# create an instance of EngagementPresets from a dict
engagement_presets_from_dict = EngagementPresets.from_dict(engagement_presets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


