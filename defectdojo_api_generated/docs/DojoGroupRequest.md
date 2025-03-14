# DojoGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_permissions** | **List[Optional[int]]** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**social_provider** | **str** | Group imported from a social provider.  * &#x60;AzureAD&#x60; - AzureAD * &#x60;Remote&#x60; - Remote | [optional] 

## Example

```python
from defectdojo_api_generated.models.dojo_group_request import DojoGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DojoGroupRequest from a JSON string
dojo_group_request_instance = DojoGroupRequest.from_json(json)
# print the JSON string representation of the object
print(DojoGroupRequest.to_json())

# convert the object into a dict
dojo_group_request_dict = dojo_group_request_instance.to_dict()
# create an instance of DojoGroupRequest from a dict
dojo_group_request_from_dict = DojoGroupRequest.from_dict(dojo_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


