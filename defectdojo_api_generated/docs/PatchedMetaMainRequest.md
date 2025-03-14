# PatchedMetaMainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **int** |  | [optional] 
**endpoint** | **int** |  | [optional] 
**finding** | **int** |  | [optional] 
**metadata** | [**List[MetadataRequest]**](MetadataRequest.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_meta_main_request import PatchedMetaMainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMetaMainRequest from a JSON string
patched_meta_main_request_instance = PatchedMetaMainRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedMetaMainRequest.to_json())

# convert the object into a dict
patched_meta_main_request_dict = patched_meta_main_request_instance.to_dict()
# create an instance of PatchedMetaMainRequest from a dict
patched_meta_main_request_from_dict = PatchedMetaMainRequest.from_dict(patched_meta_main_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


