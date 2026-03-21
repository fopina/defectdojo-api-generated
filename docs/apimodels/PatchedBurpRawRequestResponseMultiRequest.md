# PatchedBurpRawRequestResponseMultiRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**burp_request_base64** | **str** |  | [optional] 
**burp_response_base64** | **str** |  | [optional] 
**finding** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_burp_raw_request_response_multi_request import PatchedBurpRawRequestResponseMultiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedBurpRawRequestResponseMultiRequest from a JSON string
patched_burp_raw_request_response_multi_request_instance = PatchedBurpRawRequestResponseMultiRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedBurpRawRequestResponseMultiRequest.to_json())

# convert the object into a dict
patched_burp_raw_request_response_multi_request_dict = patched_burp_raw_request_response_multi_request_instance.to_dict()
# create an instance of PatchedBurpRawRequestResponseMultiRequest from a dict
patched_burp_raw_request_response_multi_request_from_dict = PatchedBurpRawRequestResponseMultiRequest.from_dict(patched_burp_raw_request_response_multi_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


