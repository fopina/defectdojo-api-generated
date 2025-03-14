# MetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from defectdojo_api_generated.models.metadata_request import MetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataRequest from a JSON string
metadata_request_instance = MetadataRequest.from_json(json)
# print the JSON string representation of the object
print(MetadataRequest.to_json())

# convert the object into a dict
metadata_request_dict = metadata_request_instance.to_dict()
# create an instance of MetadataRequest from a dict
metadata_request_from_dict = MetadataRequest.from_dict(metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


