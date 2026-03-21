# PatchedLanguageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **int** |  | [optional] 
**blank** | **int** |  | [optional] 
**comment** | **int** |  | [optional] 
**code** | **int** |  | [optional] 
**language** | **int** |  | [optional] 
**product** | **int** |  | [optional] 
**user** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_language_request import PatchedLanguageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedLanguageRequest from a JSON string
patched_language_request_instance = PatchedLanguageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedLanguageRequest.to_json())

# convert the object into a dict
patched_language_request_dict = patched_language_request_instance.to_dict()
# create an instance of PatchedLanguageRequest from a dict
patched_language_request_from_dict = PatchedLanguageRequest.from_dict(patched_language_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


