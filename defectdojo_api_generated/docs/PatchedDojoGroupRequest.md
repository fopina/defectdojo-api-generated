# PatchedDojoGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_permissions** | **List[Optional[int]]** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**social_provider** | **str** | Group imported from a social provider.  * &#x60;AzureAD&#x60; - AzureAD * &#x60;Remote&#x60; - Remote | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_dojo_group_request import PatchedDojoGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDojoGroupRequest from a JSON string
patched_dojo_group_request_instance = PatchedDojoGroupRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedDojoGroupRequest.to_json())

# convert the object into a dict
patched_dojo_group_request_dict = patched_dojo_group_request_instance.to_dict()
# create an instance of PatchedDojoGroupRequest from a dict
patched_dojo_group_request_from_dict = PatchedDojoGroupRequest.from_dict(patched_dojo_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


