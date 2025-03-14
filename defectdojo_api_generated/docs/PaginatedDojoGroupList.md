# PaginatedDojoGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DojoGroup]**](DojoGroup.md) |  | 
**prefetch** | [**DojoGroupPrefetch**](DojoGroupPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_dojo_group_list import PaginatedDojoGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDojoGroupList from a JSON string
paginated_dojo_group_list_instance = PaginatedDojoGroupList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDojoGroupList.to_json())

# convert the object into a dict
paginated_dojo_group_list_dict = paginated_dojo_group_list_instance.to_dict()
# create an instance of PaginatedDojoGroupList from a dict
paginated_dojo_group_list_from_dict = PaginatedDojoGroupList.from_dict(paginated_dojo_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


