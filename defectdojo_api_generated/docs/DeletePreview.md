# DeletePreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**name** | **str** |  | [readonly] 

## Example

```python
from defectdojo_api_generated.models.delete_preview import DeletePreview

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePreview from a JSON string
delete_preview_instance = DeletePreview.from_json(json)
# print the JSON string representation of the object
print(DeletePreview.to_json())

# convert the object into a dict
delete_preview_dict = delete_preview_instance.to_dict()
# create an instance of DeletePreview from a dict
delete_preview_from_dict = DeletePreview.from_dict(delete_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


