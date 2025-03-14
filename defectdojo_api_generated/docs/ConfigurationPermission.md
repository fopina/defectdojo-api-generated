# ConfigurationPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**codename** | **str** |  | 

## Example

```python
from defectdojo_api_generated.models.configuration_permission import ConfigurationPermission

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationPermission from a JSON string
configuration_permission_instance = ConfigurationPermission.from_json(json)
# print the JSON string representation of the object
print(ConfigurationPermission.to_json())

# convert the object into a dict
configuration_permission_dict = configuration_permission_instance.to_dict()
# create an instance of ConfigurationPermission from a dict
configuration_permission_from_dict = ConfigurationPermission.from_dict(configuration_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


