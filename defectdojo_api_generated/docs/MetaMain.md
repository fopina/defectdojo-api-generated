# MetaMain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**product** | **int** |  | [optional] 
**endpoint** | **int** |  | [optional] 
**finding** | **int** |  | [optional] 
**metadata** | [**List[Metadata]**](Metadata.md) |  | 

## Example

```python
from defectdojo_api_generated.models.meta_main import MetaMain

# TODO update the JSON string below
json = "{}"
# create an instance of MetaMain from a JSON string
meta_main_instance = MetaMain.from_json(json)
# print the JSON string representation of the object
print(MetaMain.to_json())

# convert the object into a dict
meta_main_dict = meta_main_instance.to_dict()
# create an instance of MetaMain from a dict
meta_main_from_dict = MetaMain.from_dict(meta_main_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


