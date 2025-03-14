# PaginatedSystemSettingsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[SystemSettings]**](SystemSettings.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_system_settings_list import PaginatedSystemSettingsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSystemSettingsList from a JSON string
paginated_system_settings_list_instance = PaginatedSystemSettingsList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSystemSettingsList.to_json())

# convert the object into a dict
paginated_system_settings_list_dict = paginated_system_settings_list_instance.to_dict()
# create an instance of PaginatedSystemSettingsList from a dict
paginated_system_settings_list_from_dict = PaginatedSystemSettingsList.from_dict(paginated_system_settings_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


