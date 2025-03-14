# NetworkLocationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | Location of network testing: Examples: VPN, Internet or Internal. | 

## Example

```python
from defectdojo_api_generated.models.network_locations_request import NetworkLocationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLocationsRequest from a JSON string
network_locations_request_instance = NetworkLocationsRequest.from_json(json)
# print the JSON string representation of the object
print(NetworkLocationsRequest.to_json())

# convert the object into a dict
network_locations_request_dict = network_locations_request_instance.to_dict()
# create an instance of NetworkLocationsRequest from a dict
network_locations_request_from_dict = NetworkLocationsRequest.from_dict(network_locations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


