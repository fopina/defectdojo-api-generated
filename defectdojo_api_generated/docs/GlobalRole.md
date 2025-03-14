# GlobalRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**user** | **int** |  | [optional] 
**group** | **int** |  | [optional] 
**role** | **int** | The global role will be applied to all product types and products. | [optional] 
**prefetch** | [**DojoGroupMemberPrefetch**](DojoGroupMemberPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.global_role import GlobalRole

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalRole from a JSON string
global_role_instance = GlobalRole.from_json(json)
# print the JSON string representation of the object
print(GlobalRole.to_json())

# convert the object into a dict
global_role_dict = global_role_instance.to_dict()
# create an instance of GlobalRole from a dict
global_role_from_dict = GlobalRole.from_dict(global_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


