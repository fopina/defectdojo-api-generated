# PatchedLanguageTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** |  | [optional] 
**color** | **str** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_language_type_request import PatchedLanguageTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedLanguageTypeRequest from a JSON string
patched_language_type_request_instance = PatchedLanguageTypeRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedLanguageTypeRequest.to_json())

# convert the object into a dict
patched_language_type_request_dict = patched_language_type_request_instance.to_dict()
# create an instance of PatchedLanguageTypeRequest from a dict
patched_language_type_request_from_dict = PatchedLanguageTypeRequest.from_dict(patched_language_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


