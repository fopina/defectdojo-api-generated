# ReportGenerate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executive_summary** | [**ExecutiveSummary**](ExecutiveSummary.md) |  | 
**product_type** | [**ProductType**](ProductType.md) |  | [readonly] 
**product** | [**Product**](Product.md) |  | [readonly] 
**engagement** | [**Engagement**](Engagement.md) |  | [readonly] 
**report_name** | **str** |  | 
**report_info** | **str** |  | 
**test** | [**Test**](Test.md) |  | [readonly] 
**endpoint** | [**Endpoint**](Endpoint.md) |  | [readonly] 
**endpoints** | [**List[Endpoint]**](Endpoint.md) |  | [readonly] 
**findings** | [**List[Finding]**](Finding.md) |  | [readonly] 
**user** | [**UserStub**](UserStub.md) |  | [readonly] 
**team_name** | **str** |  | 
**title** | **str** |  | 
**user_id** | **int** |  | 
**host** | **str** |  | 
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


