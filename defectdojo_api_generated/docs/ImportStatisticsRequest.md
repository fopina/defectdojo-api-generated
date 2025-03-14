# ImportStatisticsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**before** | [**SeverityStatusStatisticsRequest**](SeverityStatusStatisticsRequest.md) | Finding statistics as stored in Defect Dojo before the import | [optional] 
**delta** | [**DeltaStatisticsRequest**](DeltaStatisticsRequest.md) | Finding statistics of modifications made by the reimport. Only available when TRACK_IMPORT_HISTORY has not been disabled. | [optional] 
**after** | [**SeverityStatusStatisticsRequest**](SeverityStatusStatisticsRequest.md) | Finding statistics as stored in Defect Dojo after the import | 

## Example

```python
from defectdojo_api_generated.models.import_statistics_request import ImportStatisticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportStatisticsRequest from a JSON string
import_statistics_request_instance = ImportStatisticsRequest.from_json(json)
# print the JSON string representation of the object
print(ImportStatisticsRequest.to_json())

# convert the object into a dict
import_statistics_request_dict = import_statistics_request_instance.to_dict()
# create an instance of ImportStatisticsRequest from a dict
import_statistics_request_from_dict = ImportStatisticsRequest.from_dict(import_statistics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


