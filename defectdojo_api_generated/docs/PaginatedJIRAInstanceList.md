# PaginatedJIRAInstanceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[JIRAInstance]**](JIRAInstance.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_jira_instance_list import PaginatedJIRAInstanceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedJIRAInstanceList from a JSON string
paginated_jira_instance_list_instance = PaginatedJIRAInstanceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedJIRAInstanceList.to_json())

# convert the object into a dict
paginated_jira_instance_list_dict = paginated_jira_instance_list_instance.to_dict()
# create an instance of PaginatedJIRAInstanceList from a dict
paginated_jira_instance_list_from_dict = PaginatedJIRAInstanceList.from_dict(paginated_jira_instance_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


