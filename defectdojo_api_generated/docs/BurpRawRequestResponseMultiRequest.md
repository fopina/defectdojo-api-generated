# BurpRawRequestResponseMultiRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**burp_request_base64** | **str** |  | 
**burp_response_base64** | **str** |  | 
**finding** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.burp_raw_request_response_multi_request import BurpRawRequestResponseMultiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BurpRawRequestResponseMultiRequest from a JSON string
burp_raw_request_response_multi_request_instance = BurpRawRequestResponseMultiRequest.from_json(json)
# print the JSON string representation of the object
print(BurpRawRequestResponseMultiRequest.to_json())

# convert the object into a dict
burp_raw_request_response_multi_request_dict = burp_raw_request_response_multi_request_instance.to_dict()
# create an instance of BurpRawRequestResponseMultiRequest from a dict
burp_raw_request_response_multi_request_from_dict = BurpRawRequestResponseMultiRequest.from_dict(burp_raw_request_response_multi_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


