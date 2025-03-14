# ReportGenerateOptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_finding_notes** | **bool** |  | [optional] [default to False]
**include_finding_images** | **bool** |  | [optional] [default to False]
**include_executive_summary** | **bool** |  | [optional] [default to False]
**include_table_of_contents** | **bool** |  | [optional] [default to False]

## Example

```python
from defectdojo_api_generated.models.report_generate_option_request import ReportGenerateOptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportGenerateOptionRequest from a JSON string
report_generate_option_request_instance = ReportGenerateOptionRequest.from_json(json)
# print the JSON string representation of the object
print(ReportGenerateOptionRequest.to_json())

# convert the object into a dict
report_generate_option_request_dict = report_generate_option_request_instance.to_dict()
# create an instance of ReportGenerateOptionRequest from a dict
report_generate_option_request_from_dict = ReportGenerateOptionRequest.from_dict(report_generate_option_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


