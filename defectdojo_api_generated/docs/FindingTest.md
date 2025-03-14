# FindingTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**title** | **str** |  | [optional] 
**test_type** | [**FindingTestType**](FindingTestType.md) |  | [optional] 
**engagement** | [**FindingEngagement**](FindingEngagement.md) |  | [optional] 
**environment** | [**FindingEnvironment**](FindingEnvironment.md) |  | [optional] 
**branch_tag** | **str** | Tag or branch that was tested, a reimport may update this field. | [optional] 
**build_id** | **str** | Build ID that was tested, a reimport may update this field. | [optional] 
**commit_hash** | **str** | Commit hash tested, a reimport may update this field. | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.finding_test import FindingTest

# TODO update the JSON string below
json = "{}"
# create an instance of FindingTest from a JSON string
finding_test_instance = FindingTest.from_json(json)
# print the JSON string representation of the object
print(FindingTest.to_json())

# convert the object into a dict
finding_test_dict = finding_test_instance.to_dict()
# create an instance of FindingTest from a dict
finding_test_from_dict = FindingTest.from_dict(finding_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


