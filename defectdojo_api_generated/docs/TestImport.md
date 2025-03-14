# TestImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**test_import_finding_action_set** | [**List[TestImportFindingAction]**](TestImportFindingAction.md) |  | [readonly] 
**created** | **datetime** |  | [readonly] 
**modified** | **datetime** |  | [readonly] 
**import_settings** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**build_id** | **str** | Build ID that was tested, a reimport may update this field. | [optional] 
**commit_hash** | **str** | Commit hash tested, a reimport may update this field. | [optional] 
**branch_tag** | **str** | Tag or branch that was tested, a reimport may update this field. | [optional] 
**test** | **int** |  | [readonly] 
**findings_affected** | **List[int]** |  | [readonly] 

## Example

```python
from defectdojo_api_generated.models.test_import import TestImport

# TODO update the JSON string below
json = "{}"
# create an instance of TestImport from a JSON string
test_import_instance = TestImport.from_json(json)
# print the JSON string representation of the object
print(TestImport.to_json())

# convert the object into a dict
test_import_dict = test_import_instance.to_dict()
# create an instance of TestImport from a dict
test_import_from_dict = TestImport.from_dict(test_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


