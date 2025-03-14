# FindingClose


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
from defectdojo_api_generated.models.finding_close import FindingClose

# TODO update the JSON string below
json = "{}"
# create an instance of FindingClose from a JSON string
finding_close_instance = FindingClose.from_json(json)
# print the JSON string representation of the object
print(FindingClose.to_json())

# convert the object into a dict
finding_close_dict = finding_close_instance.to_dict()
# create an instance of FindingClose from a dict
finding_close_from_dict = FindingClose.from_dict(finding_close_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


