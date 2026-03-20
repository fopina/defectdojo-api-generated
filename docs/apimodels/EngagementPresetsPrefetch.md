# EngagementPresetsPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_locations** | [**Dict[str, NetworkLocations]**](NetworkLocations.md) |  | [optional] [readonly] 
**product** | [**Dict[str, Product]**](Product.md) |  | [optional] [readonly] 
**test_type** | [**Dict[str, TestType]**](TestType.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.engagement_presets_prefetch import EngagementPresetsPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of EngagementPresetsPrefetch from a JSON string
engagement_presets_prefetch_instance = EngagementPresetsPrefetch.from_json(json)
# print the JSON string representation of the object
print(EngagementPresetsPrefetch.to_json())

# convert the object into a dict
engagement_presets_prefetch_dict = engagement_presets_prefetch_instance.to_dict()
# create an instance of EngagementPresetsPrefetch from a dict
engagement_presets_prefetch_from_dict = EngagementPresetsPrefetch.from_dict(engagement_presets_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


