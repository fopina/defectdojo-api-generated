# NetworkLocations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**location** | **str** | Location of network testing: Examples: VPN, Internet or Internal. | 

## Example

```python
from defectdojo_api_generated.models.network_locations import NetworkLocations

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLocations from a JSON string
network_locations_instance = NetworkLocations.from_json(json)
# print the JSON string representation of the object
print(NetworkLocations.to_json())

# convert the object into a dict
network_locations_dict = network_locations_instance.to_dict()
# create an instance of NetworkLocations from a dict
network_locations_from_dict = NetworkLocations.from_dict(network_locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


