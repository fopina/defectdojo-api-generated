# PatchedGlobalRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** |  | [optional] 
**group** | **int** |  | [optional] 
**role** | **int** | The global role will be applied to all product types and products. | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_global_role_request import PatchedGlobalRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGlobalRoleRequest from a JSON string
patched_global_role_request_instance = PatchedGlobalRoleRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedGlobalRoleRequest.to_json())

# convert the object into a dict
patched_global_role_request_dict = patched_global_role_request_instance.to_dict()
# create an instance of PatchedGlobalRoleRequest from a dict
patched_global_role_request_from_dict = PatchedGlobalRoleRequest.from_dict(patched_global_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


