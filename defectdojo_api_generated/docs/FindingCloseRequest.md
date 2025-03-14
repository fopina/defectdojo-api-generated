# FindingCloseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_mitigated** | **bool** |  | [optional] 
**mitigated** | **datetime** |  | [optional] 
**false_p** | **bool** |  | [optional] 
**out_of_scope** | **bool** |  | [optional] 
**duplicate** | **bool** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.finding_close_request import FindingCloseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FindingCloseRequest from a JSON string
finding_close_request_instance = FindingCloseRequest.from_json(json)
# print the JSON string representation of the object
print(FindingCloseRequest.to_json())

# convert the object into a dict
finding_close_request_dict = finding_close_request_instance.to_dict()
# create an instance of FindingCloseRequest from a dict
finding_close_request_from_dict = FindingCloseRequest.from_dict(finding_close_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


