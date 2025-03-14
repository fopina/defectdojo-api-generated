# MetaMainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **int** |  | [optional] 
**endpoint** | **int** |  | [optional] 
**finding** | **int** |  | [optional] 
**metadata** | [**List[MetadataRequest]**](MetadataRequest.md) |  | 

## Example

```python
from defectdojo_api_generated.models.meta_main_request import MetaMainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetaMainRequest from a JSON string
meta_main_request_instance = MetaMainRequest.from_json(json)
# print the JSON string representation of the object
print(MetaMainRequest.to_json())

# convert the object into a dict
meta_main_request_dict = meta_main_request_instance.to_dict()
# create an instance of MetaMainRequest from a dict
meta_main_request_from_dict = MetaMainRequest.from_dict(meta_main_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


