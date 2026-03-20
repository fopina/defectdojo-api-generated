# PatchedEngagementPresetsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Brief description of preset. | [optional] 
**notes** | **str** | Description of what needs to be tested or setting up environment for testing | [optional] 
**scope** | **str** | Scope of Engagement testing, IP&#39;s/Resources/URL&#39;s) | [optional] 
**product** | **int** |  | [optional] 
**test_type** | **List[int]** |  | [optional] 
**network_locations** | **List[int]** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_engagement_presets_request import PatchedEngagementPresetsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedEngagementPresetsRequest from a JSON string
patched_engagement_presets_request_instance = PatchedEngagementPresetsRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedEngagementPresetsRequest.to_json())

# convert the object into a dict
patched_engagement_presets_request_dict = patched_engagement_presets_request_instance.to_dict()
# create an instance of PatchedEngagementPresetsRequest from a dict
patched_engagement_presets_request_from_dict = PatchedEngagementPresetsRequest.from_dict(patched_engagement_presets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


