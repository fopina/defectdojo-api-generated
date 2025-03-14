# FindingTestType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 

## Example

```python
from defectdojo_api_generated.models.finding_test_type import FindingTestType

# TODO update the JSON string below
json = "{}"
# create an instance of FindingTestType from a JSON string
finding_test_type_instance = FindingTestType.from_json(json)
# print the JSON string representation of the object
print(FindingTestType.to_json())

# convert the object into a dict
finding_test_type_dict = finding_test_type_instance.to_dict()
# create an instance of FindingTestType from a dict
finding_test_type_from_dict = FindingTestType.from_dict(finding_test_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


