# AssetMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **int** |  | [optional] 
**user** | **int** |  | [optional] 
**role** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.asset_member_request import AssetMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssetMemberRequest from a JSON string
asset_member_request_instance = AssetMemberRequest.from_json(json)
# print the JSON string representation of the object
print(AssetMemberRequest.to_json())

# convert the object into a dict
asset_member_request_dict = asset_member_request_instance.to_dict()
# create an instance of AssetMemberRequest from a dict
asset_member_request_from_dict = AssetMemberRequest.from_dict(asset_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


