# FileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** |  | 
**title** | **str** |  | 

## Example

```python
from defectdojo_api_generated.models.file_request import FileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileRequest from a JSON string
file_request_instance = FileRequest.from_json(json)
# print the JSON string representation of the object
print(FileRequest.to_json())

# convert the object into a dict
file_request_dict = file_request_instance.to_dict()
# create an instance of FileRequest from a dict
file_request_from_dict = FileRequest.from_dict(file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


