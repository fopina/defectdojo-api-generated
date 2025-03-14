# PaginatedNetworkLocationsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[NetworkLocations]**](NetworkLocations.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_network_locations_list import PaginatedNetworkLocationsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedNetworkLocationsList from a JSON string
paginated_network_locations_list_instance = PaginatedNetworkLocationsList.from_json(json)
# print the JSON string representation of the object
print(PaginatedNetworkLocationsList.to_json())

# convert the object into a dict
paginated_network_locations_list_dict = paginated_network_locations_list_instance.to_dict()
# create an instance of PaginatedNetworkLocationsList from a dict
paginated_network_locations_list_from_dict = PaginatedNetworkLocationsList.from_dict(paginated_network_locations_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


