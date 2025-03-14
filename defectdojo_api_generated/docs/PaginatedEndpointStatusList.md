# PaginatedEndpointStatusList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[EndpointStatus]**](EndpointStatus.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_endpoint_status_list import PaginatedEndpointStatusList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEndpointStatusList from a JSON string
paginated_endpoint_status_list_instance = PaginatedEndpointStatusList.from_json(json)
# print the JSON string representation of the object
print(PaginatedEndpointStatusList.to_json())

# convert the object into a dict
paginated_endpoint_status_list_dict = paginated_endpoint_status_list_instance.to_dict()
# create an instance of PaginatedEndpointStatusList from a dict
paginated_endpoint_status_list_from_dict = PaginatedEndpointStatusList.from_dict(paginated_endpoint_status_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


