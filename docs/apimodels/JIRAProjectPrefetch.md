# JIRAProjectPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engagement** | [**Dict[str, FindingEngagement]**](FindingEngagement.md) |  | [optional] [readonly] 
**jira_instance** | [**Dict[str, JIRAInstance]**](JIRAInstance.md) |  | [optional] [readonly] 
**product** | [**Dict[str, Product]**](Product.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.jira_project_prefetch import JIRAProjectPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of JIRAProjectPrefetch from a JSON string
jira_project_prefetch_instance = JIRAProjectPrefetch.from_json(json)
# print the JSON string representation of the object
print(JIRAProjectPrefetch.to_json())

# convert the object into a dict
jira_project_prefetch_dict = jira_project_prefetch_instance.to_dict()
# create an instance of JIRAProjectPrefetch from a dict
jira_project_prefetch_from_dict = JIRAProjectPrefetch.from_dict(jira_project_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


