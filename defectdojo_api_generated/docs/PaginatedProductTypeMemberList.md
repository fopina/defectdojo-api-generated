# PaginatedProductTypeMemberList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ProductTypeMember]**](ProductTypeMember.md) |  | 
**prefetch** | [**PaginatedProductTypeMemberListPrefetch**](PaginatedProductTypeMemberListPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_product_type_member_list import PaginatedProductTypeMemberList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProductTypeMemberList from a JSON string
paginated_product_type_member_list_instance = PaginatedProductTypeMemberList.from_json(json)
# print the JSON string representation of the object
print(PaginatedProductTypeMemberList.to_json())

# convert the object into a dict
paginated_product_type_member_list_dict = paginated_product_type_member_list_instance.to_dict()
# create an instance of PaginatedProductTypeMemberList from a dict
paginated_product_type_member_list_from_dict = PaginatedProductTypeMemberList.from_dict(paginated_product_type_member_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


