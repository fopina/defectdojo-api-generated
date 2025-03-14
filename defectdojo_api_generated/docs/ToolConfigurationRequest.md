# ToolConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**authentication_type** | **str** | * &#x60;API&#x60; - API Key * &#x60;Password&#x60; - Username/Password * &#x60;SSH&#x60; - SSH | [optional] 
**extras** | **str** | Additional definitions that will be consumed by scanner | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**auth_title** | **str** |  | [optional] 
**ssh** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 
**tool_type** | **int** |  | 

## Example

```python
from defectdojo_api_generated.models.tool_configuration_request import ToolConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ToolConfigurationRequest from a JSON string
tool_configuration_request_instance = ToolConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(ToolConfigurationRequest.to_json())

# convert the object into a dict
tool_configuration_request_dict = tool_configuration_request_instance.to_dict()
# create an instance of ToolConfigurationRequest from a dict
tool_configuration_request_from_dict = ToolConfigurationRequest.from_dict(tool_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


