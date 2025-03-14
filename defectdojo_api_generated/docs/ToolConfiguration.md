# ToolConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**authentication_type** | **str** | * &#x60;API&#x60; - API Key * &#x60;Password&#x60; - Username/Password * &#x60;SSH&#x60; - SSH | [optional] 
**extras** | **str** | Additional definitions that will be consumed by scanner | [optional] 
**username** | **str** |  | [optional] 
**auth_title** | **str** |  | [optional] 
**tool_type** | **int** |  | 
**prefetch** | [**PaginatedToolConfigurationListPrefetch**](PaginatedToolConfigurationListPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.tool_configuration import ToolConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ToolConfiguration from a JSON string
tool_configuration_instance = ToolConfiguration.from_json(json)
# print the JSON string representation of the object
print(ToolConfiguration.to_json())

# convert the object into a dict
tool_configuration_dict = tool_configuration_instance.to_dict()
# create an instance of ToolConfiguration from a dict
tool_configuration_from_dict = ToolConfiguration.from_dict(tool_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


