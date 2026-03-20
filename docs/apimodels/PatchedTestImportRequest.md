# PatchedTestImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_settings** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**build_id** | **str** | Build ID that was tested, a reimport may update this field. | [optional] 
**commit_hash** | **str** | Commit hash tested, a reimport may update this field. | [optional] 
**branch_tag** | **str** | Tag or branch that was tested, a reimport may update this field. | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_test_import_request import PatchedTestImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTestImportRequest from a JSON string
patched_test_import_request_instance = PatchedTestImportRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedTestImportRequest.to_json())

# convert the object into a dict
patched_test_import_request_dict = patched_test_import_request_instance.to_dict()
# create an instance of PatchedTestImportRequest from a dict
patched_test_import_request_from_dict = PatchedTestImportRequest.from_dict(patched_test_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


