# FindingMetaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from defectdojo_api_generated.models.finding_meta_request import FindingMetaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FindingMetaRequest from a JSON string
finding_meta_request_instance = FindingMetaRequest.from_json(json)
# print the JSON string representation of the object
print(FindingMetaRequest.to_json())

# convert the object into a dict
finding_meta_request_dict = finding_meta_request_instance.to_dict()
# create an instance of FindingMetaRequest from a dict
finding_meta_request_from_dict = FindingMetaRequest.from_dict(finding_meta_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


