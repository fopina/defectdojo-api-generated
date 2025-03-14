# PaginatedFindingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Finding]**](Finding.md) |  | 
**prefetch** | [**FindingPrefetch**](FindingPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_finding_list import PaginatedFindingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFindingList from a JSON string
paginated_finding_list_instance = PaginatedFindingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFindingList.to_json())

# convert the object into a dict
paginated_finding_list_dict = paginated_finding_list_instance.to_dict()
# create an instance of PaginatedFindingList from a dict
paginated_finding_list_from_dict = PaginatedFindingList.from_dict(paginated_finding_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


