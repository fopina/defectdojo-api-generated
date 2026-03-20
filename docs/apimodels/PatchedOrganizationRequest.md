# PatchedOrganizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**critical_asset** | **bool** |  | [optional] [default to False]
**key_asset** | **bool** |  | [optional] [default to False]
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_organization_request import PatchedOrganizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedOrganizationRequest from a JSON string
patched_organization_request_instance = PatchedOrganizationRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedOrganizationRequest.to_json())

# convert the object into a dict
patched_organization_request_dict = patched_organization_request_instance.to_dict()
# create an instance of PatchedOrganizationRequest from a dict
patched_organization_request_from_dict = PatchedOrganizationRequest.from_dict(patched_organization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


