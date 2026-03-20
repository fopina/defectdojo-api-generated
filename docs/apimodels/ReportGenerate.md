# ReportGenerate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executive_summary** | [**ExecutiveSummary**](ExecutiveSummary.md) |  | [optional] 
**product_type** | [**ProductType**](ProductType.md) |  | [optional] [readonly] 
**product** | [**Product**](Product.md) |  | [optional] [readonly] 
**engagement** | [**Engagement**](Engagement.md) |  | [optional] [readonly] 
**report_name** | **str** |  | [optional] 
**report_info** | **str** |  | [optional] 
**test** | [**Test**](Test.md) |  | [optional] [readonly] 
**endpoint** | [**Endpoint**](Endpoint.md) |  | [optional] [readonly] 
**endpoints** | [**List[Endpoint]**](Endpoint.md) |  | [optional] [readonly] 
**findings** | [**List[Finding]**](Finding.md) |  | [optional] [readonly] 
**user** | [**UserStub**](UserStub.md) |  | [optional] [readonly] 
**team_name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**host** | **str** |  | [optional] 
**finding_notes** | [**List[FindingToNotes]**](FindingToNotes.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.report_generate import ReportGenerate

# TODO update the JSON string below
json = "{}"
# create an instance of ReportGenerate from a JSON string
report_generate_instance = ReportGenerate.from_json(json)
# print the JSON string representation of the object
print(ReportGenerate.to_json())

# convert the object into a dict
report_generate_dict = report_generate_instance.to_dict()
# create an instance of ReportGenerate from a dict
report_generate_from_dict = ReportGenerate.from_dict(report_generate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


