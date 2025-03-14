# PaginatedProductListPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_groups** | [**Dict[str, DojoGroup]**](DojoGroup.md) |  | [optional] [readonly] 
**members** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 
**prod_type** | [**Dict[str, ProductType]**](ProductType.md) |  | [optional] [readonly] 
**product_manager** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 
**regulations** | [**Dict[str, Regulation]**](Regulation.md) |  | [optional] [readonly] 
**sla_configuration** | [**Dict[str, SLAConfiguration]**](SLAConfiguration.md) |  | [optional] [readonly] 
**team_manager** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 
**technical_contact** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.paginated_product_list_prefetch import PaginatedProductListPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProductListPrefetch from a JSON string
paginated_product_list_prefetch_instance = PaginatedProductListPrefetch.from_json(json)
# print the JSON string representation of the object
print(PaginatedProductListPrefetch.to_json())

# convert the object into a dict
paginated_product_list_prefetch_dict = paginated_product_list_prefetch_instance.to_dict()
# create an instance of PaginatedProductListPrefetch from a dict
paginated_product_list_prefetch_from_dict = PaginatedProductListPrefetch.from_dict(paginated_product_list_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


