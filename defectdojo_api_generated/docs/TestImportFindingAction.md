# TestImportFindingAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**created** | **datetime** |  | [readonly] 
**modified** | **datetime** |  | [readonly] 
**action** | **str** | * &#x60;N&#x60; - created * &#x60;C&#x60; - closed * &#x60;R&#x60; - reactivated * &#x60;U&#x60; - left untouched | [optional] 
**test_import** | **int** |  | [readonly] 
**finding** | **int** |  | [readonly] 

## Example

```python
from defectdojo_api_generated.models.test_import_finding_action import TestImportFindingAction

# TODO update the JSON string below
json = "{}"
# create an instance of TestImportFindingAction from a JSON string
test_import_finding_action_instance = TestImportFindingAction.from_json(json)
# print the JSON string representation of the object
print(TestImportFindingAction.to_json())

# convert the object into a dict
test_import_finding_action_dict = test_import_finding_action_instance.to_dict()
# create an instance of TestImportFindingAction from a dict
test_import_finding_action_from_dict = TestImportFindingAction.from_dict(test_import_finding_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


