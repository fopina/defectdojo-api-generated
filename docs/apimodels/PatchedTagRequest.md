# PatchedTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_tag_request import PatchedTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTagRequest from a JSON string
patched_tag_request_instance = PatchedTagRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedTagRequest.to_json())

# convert the object into a dict
patched_tag_request_dict = patched_tag_request_instance.to_dict()
# create an instance of PatchedTagRequest from a dict
patched_tag_request_from_dict = PatchedTagRequest.from_dict(patched_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


