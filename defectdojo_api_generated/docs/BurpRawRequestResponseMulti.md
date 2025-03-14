# BurpRawRequestResponseMulti


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**burp_request_base64** | **str** |  | 
**burp_response_base64** | **str** |  | 
**finding** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.burp_raw_request_response_multi import BurpRawRequestResponseMulti

# TODO update the JSON string below
json = "{}"
# create an instance of BurpRawRequestResponseMulti from a JSON string
burp_raw_request_response_multi_instance = BurpRawRequestResponseMulti.from_json(json)
# print the JSON string representation of the object
print(BurpRawRequestResponseMulti.to_json())

# convert the object into a dict
burp_raw_request_response_multi_dict = burp_raw_request_response_multi_instance.to_dict()
# create an instance of BurpRawRequestResponseMulti from a dict
burp_raw_request_response_multi_from_dict = BurpRawRequestResponseMulti.from_dict(burp_raw_request_response_multi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


