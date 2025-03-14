# BurpRawRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**req_resp** | **List[Dict[str, str]]** |  | 

## Example

```python
from defectdojo_api_generated.models.burp_raw_request_response import BurpRawRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BurpRawRequestResponse from a JSON string
burp_raw_request_response_instance = BurpRawRequestResponse.from_json(json)
# print the JSON string representation of the object
print(BurpRawRequestResponse.to_json())

# convert the object into a dict
burp_raw_request_response_dict = burp_raw_request_response_instance.to_dict()
# create an instance of BurpRawRequestResponse from a dict
burp_raw_request_response_from_dict = BurpRawRequestResponse.from_dict(burp_raw_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


