# TestImportRequest


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
from defectdojo_api_generated.models.test_import_request import TestImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestImportRequest from a JSON string
test_import_request_instance = TestImportRequest.from_json(json)
# print the JSON string representation of the object
print(TestImportRequest.to_json())

# convert the object into a dict
test_import_request_dict = test_import_request_instance.to_dict()
# create an instance of TestImportRequest from a dict
test_import_request_from_dict = TestImportRequest.from_dict(test_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


