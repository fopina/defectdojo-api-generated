# FindingToFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finding_id** | **int** |  | 
**files** | [**List[File]**](File.md) |  | 

## Example

```python
from defectdojo_api_generated.models.finding_to_files import FindingToFiles

# TODO update the JSON string below
json = "{}"
# create an instance of FindingToFiles from a JSON string
finding_to_files_instance = FindingToFiles.from_json(json)
# print the JSON string representation of the object
print(FindingToFiles.to_json())

# convert the object into a dict
finding_to_files_dict = finding_to_files_instance.to_dict()
# create an instance of FindingToFiles from a dict
finding_to_files_from_dict = FindingToFiles.from_dict(finding_to_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


