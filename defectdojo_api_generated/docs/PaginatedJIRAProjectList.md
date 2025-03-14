# PaginatedJIRAProjectList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[JIRAProject]**](JIRAProject.md) |  | 
**prefetch** | [**JIRAProjectPrefetch**](JIRAProjectPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.paginated_jira_project_list import PaginatedJIRAProjectList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedJIRAProjectList from a JSON string
paginated_jira_project_list_instance = PaginatedJIRAProjectList.from_json(json)
# print the JSON string representation of the object
print(PaginatedJIRAProjectList.to_json())

# convert the object into a dict
paginated_jira_project_list_dict = paginated_jira_project_list_instance.to_dict()
# create an instance of PaginatedJIRAProjectList from a dict
paginated_jira_project_list_from_dict = PaginatedJIRAProjectList.from_dict(paginated_jira_project_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


