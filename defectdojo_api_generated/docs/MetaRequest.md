# MetaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **int** |  | [optional] 
**endpoint** | **int** |  | [optional] 
**finding** | **int** |  | [optional] 
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from defectdojo_api_generated.models.meta_request import MetaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetaRequest from a JSON string
meta_request_instance = MetaRequest.from_json(json)
# print the JSON string representation of the object
print(MetaRequest.to_json())

# convert the object into a dict
meta_request_dict = meta_request_instance.to_dict()
# create an instance of MetaRequest from a dict
meta_request_from_dict = MetaRequest.from_dict(meta_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


