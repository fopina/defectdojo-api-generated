# PaginatedProductMemberList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ProductMember]**](ProductMember.md) |  | 
**prefetch** | [**PaginatedProductMemberListPrefetch**](PaginatedProductMemberListPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_product_member_list import PaginatedProductMemberList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProductMemberList from a JSON string
paginated_product_member_list_instance = PaginatedProductMemberList.from_json(json)
# print the JSON string representation of the object
print(PaginatedProductMemberList.to_json())

# convert the object into a dict
paginated_product_member_list_dict = paginated_product_member_list_instance.to_dict()
# create an instance of PaginatedProductMemberList from a dict
paginated_product_member_list_from_dict = PaginatedProductMemberList.from_dict(paginated_product_member_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


