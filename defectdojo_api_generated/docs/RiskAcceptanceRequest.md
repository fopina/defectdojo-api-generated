# RiskAcceptanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Descriptive name which in the future may also be used to group risk acceptances together across engagements and products | 
**recommendation_details** | **str** | Explanation of security recommendation | [optional] 
**decision_details** | **str** | If a compensating control exists to mitigate the finding or reduce risk, then list the compensating control(s). | [optional] 
**accepted_by** | **str** | The person that accepts the risk, can be outside of DefectDojo. | [optional] 
**expiration_date** | **datetime** | When the risk acceptance expires, the findings will be reactivated (unless disabled below). | [optional] 
**expiration_date_warned** | **datetime** | (readonly) Date at which notice about the risk acceptance expiration was sent. | [optional] 
**expiration_date_handled** | **datetime** | (readonly) When the risk acceptance expiration was handled (manually or by the daily job). | [optional] 
**reactivate_expired** | **bool** | Reactivate findings when risk acceptance expires? | [optional] 
**restart_sla_expired** | **bool** | When enabled, the SLA for findings is restarted when the risk acceptance expires. | [optional] 
**owner** | **int** | User in DefectDojo owning this acceptance. Only the owner and staff users can edit the risk acceptance. | 
**accepted_findings** | **List[int]** |  | 

## Example

```python
from defectdojo_api_generated.models.risk_acceptance_request import RiskAcceptanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAcceptanceRequest from a JSON string
risk_acceptance_request_instance = RiskAcceptanceRequest.from_json(json)
# print the JSON string representation of the object
print(RiskAcceptanceRequest.to_json())

# convert the object into a dict
risk_acceptance_request_dict = risk_acceptance_request_instance.to_dict()
# create an instance of RiskAcceptanceRequest from a dict
risk_acceptance_request_from_dict = RiskAcceptanceRequest.from_dict(risk_acceptance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


