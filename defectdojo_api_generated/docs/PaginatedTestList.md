# PaginatedTestList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Test]**](Test.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_test_list import PaginatedTestList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTestList from a JSON string
paginated_test_list_instance = PaginatedTestList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTestList.to_json())

# convert the object into a dict
paginated_test_list_dict = paginated_test_list_instance.to_dict()
# create an instance of PaginatedTestList from a dict
paginated_test_list_from_dict = PaginatedTestList.from_dict(paginated_test_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


