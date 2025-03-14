# FindingGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**test** | **int** |  | 

## Example

```python
from defectdojo_api_generated.models.finding_group_request import FindingGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FindingGroupRequest from a JSON string
finding_group_request_instance = FindingGroupRequest.from_json(json)
# print the JSON string representation of the object
print(FindingGroupRequest.to_json())

# convert the object into a dict
finding_group_request_dict = finding_group_request_instance.to_dict()
# create an instance of FindingGroupRequest from a dict
finding_group_request_from_dict = FindingGroupRequest.from_dict(finding_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


