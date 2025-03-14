# GlobalRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** |  | [optional] 
**group** | **int** |  | [optional] 
**role** | **int** | The global role will be applied to all product types and products. | [optional] 

## Example

```python
from defectdojo_api_generated.models.global_role_request import GlobalRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalRoleRequest from a JSON string
global_role_request_instance = GlobalRoleRequest.from_json(json)
# print the JSON string representation of the object
print(GlobalRoleRequest.to_json())

# convert the object into a dict
global_role_request_dict = global_role_request_instance.to_dict()
# create an instance of GlobalRoleRequest from a dict
global_role_request_from_dict = GlobalRoleRequest.from_dict(global_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


