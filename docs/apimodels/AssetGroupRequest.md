# AssetGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **int** |  | [optional] 
**group** | **int** |  | [optional] 
**role** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.asset_group_request import AssetGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssetGroupRequest from a JSON string
asset_group_request_instance = AssetGroupRequest.from_json(json)
# print the JSON string representation of the object
print(AssetGroupRequest.to_json())

# convert the object into a dict
asset_group_request_dict = asset_group_request_instance.to_dict()
# create an instance of AssetGroupRequest from a dict
asset_group_request_from_dict = AssetGroupRequest.from_dict(asset_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


