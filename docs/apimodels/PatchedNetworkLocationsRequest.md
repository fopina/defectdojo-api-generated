# PatchedNetworkLocationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | Location of network testing: Examples: VPN, Internet or Internal. | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_network_locations_request import PatchedNetworkLocationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedNetworkLocationsRequest from a JSON string
patched_network_locations_request_instance = PatchedNetworkLocationsRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedNetworkLocationsRequest.to_json())

# convert the object into a dict
patched_network_locations_request_dict = patched_network_locations_request_instance.to_dict()
# create an instance of PatchedNetworkLocationsRequest from a dict
patched_network_locations_request_from_dict = PatchedNetworkLocationsRequest.from_dict(patched_network_locations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


