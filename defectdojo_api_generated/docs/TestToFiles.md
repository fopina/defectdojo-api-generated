# TestToFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_id** | **int** |  | 
**files** | [**List[File]**](File.md) |  | 

## Example

```python
from defectdojo_api_generated.models.test_to_files import TestToFiles

# TODO update the JSON string below
json = "{}"
# create an instance of TestToFiles from a JSON string
test_to_files_instance = TestToFiles.from_json(json)
# print the JSON string representation of the object
print(TestToFiles.to_json())

# convert the object into a dict
test_to_files_dict = test_to_files_instance.to_dict()
# create an instance of TestToFiles from a dict
test_to_files_from_dict = TestToFiles.from_dict(test_to_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


