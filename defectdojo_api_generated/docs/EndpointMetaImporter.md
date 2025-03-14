# EndpointMetaImporter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** |  | 
**create_endpoints** | **bool** |  | [optional] [default to True]
**create_tags** | **bool** |  | [optional] [default to True]
**create_dojo_meta** | **bool** |  | [optional] [default to False]
**product_name** | **str** |  | [optional] 
**product** | **int** |  | [optional] 
**product_id** | **int** |  | [readonly] 

## Example

```python
from defectdojo_api_generated.models.endpoint_meta_importer import EndpointMetaImporter

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointMetaImporter from a JSON string
endpoint_meta_importer_instance = EndpointMetaImporter.from_json(json)
# print the JSON string representation of the object
print(EndpointMetaImporter.to_json())

# convert the object into a dict
endpoint_meta_importer_dict = endpoint_meta_importer_instance.to_dict()
# create an instance of EndpointMetaImporter from a dict
endpoint_meta_importer_from_dict = EndpointMetaImporter.from_dict(endpoint_meta_importer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


