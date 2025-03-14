# PatchedRegulationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the regulation. | [optional] 
**acronym** | **str** | A shortened representation of the name. | [optional] 
**category** | **str** | The subject of the regulation.  * &#x60;privacy&#x60; - Privacy * &#x60;finance&#x60; - Finance * &#x60;education&#x60; - Education * &#x60;medical&#x60; - Medical * &#x60;corporate&#x60; - Corporate * &#x60;other&#x60; - Other | [optional] 
**jurisdiction** | **str** | The territory over which the regulation applies. | [optional] 
**description** | **str** | Information about the regulation&#39;s purpose. | [optional] 
**reference** | **str** | An external URL for more information. | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_regulation_request import PatchedRegulationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRegulationRequest from a JSON string
patched_regulation_request_instance = PatchedRegulationRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedRegulationRequest.to_json())

# convert the object into a dict
patched_regulation_request_dict = patched_regulation_request_instance.to_dict()
# create an instance of PatchedRegulationRequest from a dict
patched_regulation_request_from_dict = PatchedRegulationRequest.from_dict(patched_regulation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


