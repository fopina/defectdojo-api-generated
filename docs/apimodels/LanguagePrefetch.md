# LanguagePrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | [**Dict[str, LanguageType]**](LanguageType.md) |  | [optional] [readonly] 
**product** | [**Dict[str, Product]**](Product.md) |  | [optional] [readonly] 
**user** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.language_prefetch import LanguagePrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of LanguagePrefetch from a JSON string
language_prefetch_instance = LanguagePrefetch.from_json(json)
# print the JSON string representation of the object
print(LanguagePrefetch.to_json())

# convert the object into a dict
language_prefetch_dict = language_prefetch_instance.to_dict()
# create an instance of LanguagePrefetch from a dict
language_prefetch_from_dict = LanguagePrefetch.from_dict(language_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


