# LanguageType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**language** | **str** |  | 
**color** | **str** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.language_type import LanguageType

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageType from a JSON string
language_type_instance = LanguageType.from_json(json)
# print the JSON string representation of the object
print(LanguageType.to_json())

# convert the object into a dict
language_type_dict = language_type_instance.to_dict()
# create an instance of LanguageType from a dict
language_type_from_dict = LanguageType.from_dict(language_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


