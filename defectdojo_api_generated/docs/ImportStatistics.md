# ImportStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**before** | [**SeverityStatusStatistics**](SeverityStatusStatistics.md) | Finding statistics as stored in Defect Dojo before the import | [optional] 
**delta** | [**DeltaStatistics**](DeltaStatistics.md) | Finding statistics of modifications made by the reimport. Only available when TRACK_IMPORT_HISTORY has not been disabled. | [optional] 
**after** | [**SeverityStatusStatistics**](SeverityStatusStatistics.md) | Finding statistics as stored in Defect Dojo after the import | 

## Example

```python
from defectdojo_api_generated.models.import_statistics import ImportStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of ImportStatistics from a JSON string
import_statistics_instance = ImportStatistics.from_json(json)
# print the JSON string representation of the object
print(ImportStatistics.to_json())

# convert the object into a dict
import_statistics_dict = import_statistics_instance.to_dict()
# create an instance of ImportStatistics from a dict
import_statistics_from_dict = ImportStatistics.from_dict(import_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


