# RiskAcceptance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**recommendation** | **str** |  | [readonly] 
**decision** | **str** |  | [readonly] 
**path** | **str** |  | [readonly] 
**name** | **str** | Descriptive name which in the future may also be used to group risk acceptances together across engagements and products | 
**recommendation_details** | **str** | Explanation of security recommendation | [optional] 
**decision_details** | **str** | If a compensating control exists to mitigate the finding or reduce risk, then list the compensating control(s). | [optional] 
**accepted_by** | **str** | The person that accepts the risk, can be outside of DefectDojo. | [optional] 
**expiration_date** | **datetime** | When the risk acceptance expires, the findings will be reactivated (unless disabled below). | [optional] 
**expiration_date_warned** | **datetime** | (readonly) Date at which notice about the risk acceptance expiration was sent. | [optional] 
**expiration_date_handled** | **datetime** | (readonly) When the risk acceptance expiration was handled (manually or by the daily job). | [optional] 
**reactivate_expired** | **bool** | Reactivate findings when risk acceptance expires? | [optional] 
**restart_sla_expired** | **bool** | When enabled, the SLA for findings is restarted when the risk acceptance expires. | [optional] 
**created** | **datetime** |  | [readonly] 
**updated** | **datetime** |  | [readonly] 
**owner** | **int** | User in DefectDojo owning this acceptance. Only the owner and staff users can edit the risk acceptance. | 
**accepted_findings** | **List[int]** |  | 
**notes** | **List[int]** |  | [readonly] 

## Example

```python
from defectdojo_api_generated.models.risk_acceptance import RiskAcceptance

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAcceptance from a JSON string
risk_acceptance_instance = RiskAcceptance.from_json(json)
# print the JSON string representation of the object
print(RiskAcceptance.to_json())

# convert the object into a dict
risk_acceptance_dict = risk_acceptance_instance.to_dict()
# create an instance of RiskAcceptance from a dict
risk_acceptance_from_dict = RiskAcceptance.from_dict(risk_acceptance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


