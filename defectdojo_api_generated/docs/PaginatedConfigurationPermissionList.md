# PaginatedConfigurationPermissionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ConfigurationPermission]**](ConfigurationPermission.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_configuration_permission_list import PaginatedConfigurationPermissionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedConfigurationPermissionList from a JSON string
paginated_configuration_permission_list_instance = PaginatedConfigurationPermissionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedConfigurationPermissionList.to_json())

# convert the object into a dict
paginated_configuration_permission_list_dict = paginated_configuration_permission_list_instance.to_dict()
# create an instance of PaginatedConfigurationPermissionList from a dict
paginated_configuration_permission_list_from_dict = PaginatedConfigurationPermissionList.from_dict(paginated_configuration_permission_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


