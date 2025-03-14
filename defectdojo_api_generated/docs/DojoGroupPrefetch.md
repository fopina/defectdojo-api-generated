# DojoGroupPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_groups** | [**Dict[str, Product]**](Product.md) |  | [optional] [readonly] 
**product_type_groups** | [**Dict[str, ProductType]**](ProductType.md) |  | [optional] [readonly] 
**users** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.dojo_group_prefetch import DojoGroupPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of DojoGroupPrefetch from a JSON string
dojo_group_prefetch_instance = DojoGroupPrefetch.from_json(json)
# print the JSON string representation of the object
print(DojoGroupPrefetch.to_json())

# convert the object into a dict
dojo_group_prefetch_dict = dojo_group_prefetch_instance.to_dict()
# create an instance of DojoGroupPrefetch from a dict
dojo_group_prefetch_from_dict = DojoGroupPrefetch.from_dict(dojo_group_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


