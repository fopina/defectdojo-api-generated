# FindingEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 

## Example

```python
from defectdojo_api_generated.models.finding_environment import FindingEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of FindingEnvironment from a JSON string
finding_environment_instance = FindingEnvironment.from_json(json)
# print the JSON string representation of the object
print(FindingEnvironment.to_json())

# convert the object into a dict
finding_environment_dict = finding_environment_instance.to_dict()
# create an instance of FindingEnvironment from a dict
finding_environment_from_dict = FindingEnvironment.from_dict(finding_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


