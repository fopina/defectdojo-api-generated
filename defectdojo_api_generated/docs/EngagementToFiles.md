# EngagementToFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engagement_id** | **int** |  | 
**files** | [**List[File]**](File.md) |  | 

## Example

```python
from defectdojo_api_generated.models.engagement_to_files import EngagementToFiles

# TODO update the JSON string below
json = "{}"
# create an instance of EngagementToFiles from a JSON string
engagement_to_files_instance = EngagementToFiles.from_json(json)
# print the JSON string representation of the object
print(EngagementToFiles.to_json())

# convert the object into a dict
engagement_to_files_dict = engagement_to_files_instance.to_dict()
# create an instance of EngagementToFiles from a dict
engagement_to_files_from_dict = EngagementToFiles.from_dict(engagement_to_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


