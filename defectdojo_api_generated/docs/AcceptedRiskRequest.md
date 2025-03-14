# AcceptedRiskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vulnerability_id** | **str** | An id of a vulnerability in a security advisory associated with this finding. Can be a Common Vulnerabilities and Exposure (CVE) or from other sources. | 
**justification** | **str** | Justification for accepting findings with this vulnerability id | 
**accepted_by** | **str** | Name or email of person who accepts the risk | 

## Example

```python
from defectdojo_api_generated.models.accepted_risk_request import AcceptedRiskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptedRiskRequest from a JSON string
accepted_risk_request_instance = AcceptedRiskRequest.from_json(json)
# print the JSON string representation of the object
print(AcceptedRiskRequest.to_json())

# convert the object into a dict
accepted_risk_request_dict = accepted_risk_request_instance.to_dict()
# create an instance of AcceptedRiskRequest from a dict
accepted_risk_request_from_dict = AcceptedRiskRequest.from_dict(accepted_risk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


