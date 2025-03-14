# DevelopmentEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 

## Example

```python
from defectdojo_api_generated.models.development_environment import DevelopmentEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of DevelopmentEnvironment from a JSON string
development_environment_instance = DevelopmentEnvironment.from_json(json)
# print the JSON string representation of the object
print(DevelopmentEnvironment.to_json())

# convert the object into a dict
development_environment_dict = development_environment_instance.to_dict()
# create an instance of DevelopmentEnvironment from a dict
development_environment_from_dict = DevelopmentEnvironment.from_dict(development_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


