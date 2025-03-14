# LanguageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **int** |  | [optional] 
**blank** | **int** |  | [optional] 
**comment** | **int** |  | [optional] 
**code** | **int** |  | [optional] 
**language** | **int** |  | 
**product** | **int** |  | 
**user** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.language_request import LanguageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageRequest from a JSON string
language_request_instance = LanguageRequest.from_json(json)
# print the JSON string representation of the object
print(LanguageRequest.to_json())

# convert the object into a dict
language_request_dict = language_request_instance.to_dict()
# create an instance of LanguageRequest from a dict
language_request_from_dict = LanguageRequest.from_dict(language_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


