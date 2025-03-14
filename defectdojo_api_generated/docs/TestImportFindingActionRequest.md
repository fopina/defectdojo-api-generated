# TestImportFindingActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | * &#x60;N&#x60; - created * &#x60;C&#x60; - closed * &#x60;R&#x60; - reactivated * &#x60;U&#x60; - left untouched | [optional] 

## Example

```python
from defectdojo_api_generated.models.test_import_finding_action_request import TestImportFindingActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestImportFindingActionRequest from a JSON string
test_import_finding_action_request_instance = TestImportFindingActionRequest.from_json(json)
# print the JSON string representation of the object
print(TestImportFindingActionRequest.to_json())

# convert the object into a dict
test_import_finding_action_request_dict = test_import_finding_action_request_instance.to_dict()
# create an instance of TestImportFindingActionRequest from a dict
test_import_finding_action_request_from_dict = TestImportFindingActionRequest.from_dict(test_import_finding_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


