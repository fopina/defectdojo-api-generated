# FindingVerifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** |  | [optional] 
**note_type** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.finding_verify_request import FindingVerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FindingVerifyRequest from a JSON string
finding_verify_request_instance = FindingVerifyRequest.from_json(json)
# print the JSON string representation of the object
print(FindingVerifyRequest.to_json())

# convert the object into a dict
finding_verify_request_dict = finding_verify_request_instance.to_dict()
# create an instance of FindingVerifyRequest from a dict
finding_verify_request_from_dict = FindingVerifyRequest.from_dict(finding_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


