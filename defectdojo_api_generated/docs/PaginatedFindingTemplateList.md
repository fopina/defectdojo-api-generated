# PaginatedFindingTemplateList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FindingTemplate]**](FindingTemplate.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_finding_template_list import PaginatedFindingTemplateList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFindingTemplateList from a JSON string
paginated_finding_template_list_instance = PaginatedFindingTemplateList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFindingTemplateList.to_json())

# convert the object into a dict
paginated_finding_template_list_dict = paginated_finding_template_list_instance.to_dict()
# create an instance of PaginatedFindingTemplateList from a dict
paginated_finding_template_list_from_dict = PaginatedFindingTemplateList.from_dict(paginated_finding_template_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


