# LanguageTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** |  | 
**color** | **str** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.language_type_request import LanguageTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageTypeRequest from a JSON string
language_type_request_instance = LanguageTypeRequest.from_json(json)
# print the JSON string representation of the object
print(LanguageTypeRequest.to_json())

# convert the object into a dict
language_type_request_dict = language_type_request_instance.to_dict()
# create an instance of LanguageTypeRequest from a dict
language_type_request_from_dict = LanguageTypeRequest.from_dict(language_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


