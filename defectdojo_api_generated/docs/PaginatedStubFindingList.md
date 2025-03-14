# PaginatedStubFindingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[StubFinding]**](StubFinding.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_stub_finding_list import PaginatedStubFindingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedStubFindingList from a JSON string
paginated_stub_finding_list_instance = PaginatedStubFindingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedStubFindingList.to_json())

# convert the object into a dict
paginated_stub_finding_list_dict = paginated_stub_finding_list_instance.to_dict()
# create an instance of PaginatedStubFindingList from a dict
paginated_stub_finding_list_from_dict = PaginatedStubFindingList.from_dict(paginated_stub_finding_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


