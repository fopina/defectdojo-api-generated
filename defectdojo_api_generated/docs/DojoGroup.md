# DojoGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**configuration_permissions** | **List[Optional[int]]** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**social_provider** | **str** | Group imported from a social provider.  * &#x60;AzureAD&#x60; - AzureAD * &#x60;Remote&#x60; - Remote | [optional] 
**users** | **List[int]** |  | [readonly] 
**prefetch** | [**DojoGroupPrefetch**](DojoGroupPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.dojo_group import DojoGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DojoGroup from a JSON string
dojo_group_instance = DojoGroup.from_json(json)
# print the JSON string representation of the object
print(DojoGroup.to_json())

# convert the object into a dict
dojo_group_dict = dojo_group_instance.to_dict()
# create an instance of DojoGroup from a dict
dojo_group_from_dict = DojoGroup.from_dict(dojo_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


