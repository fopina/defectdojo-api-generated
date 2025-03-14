# BurpRawRequestResponseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**req_resp** | **List[Dict[str, str]]** |  | 

## Example

```python
from defectdojo_api_generated.models.burp_raw_request_response_request import BurpRawRequestResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BurpRawRequestResponseRequest from a JSON string
burp_raw_request_response_request_instance = BurpRawRequestResponseRequest.from_json(json)
# print the JSON string representation of the object
print(BurpRawRequestResponseRequest.to_json())

# convert the object into a dict
burp_raw_request_response_request_dict = burp_raw_request_response_request_instance.to_dict()
# create an instance of BurpRawRequestResponseRequest from a dict
burp_raw_request_response_request_from_dict = BurpRawRequestResponseRequest.from_dict(burp_raw_request_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


