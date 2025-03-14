# PaginatedRiskAcceptanceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RiskAcceptance]**](RiskAcceptance.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_risk_acceptance_list import PaginatedRiskAcceptanceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRiskAcceptanceList from a JSON string
paginated_risk_acceptance_list_instance = PaginatedRiskAcceptanceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRiskAcceptanceList.to_json())

# convert the object into a dict
paginated_risk_acceptance_list_dict = paginated_risk_acceptance_list_instance.to_dict()
# create an instance of PaginatedRiskAcceptanceList from a dict
paginated_risk_acceptance_list_from_dict = PaginatedRiskAcceptanceList.from_dict(paginated_risk_acceptance_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


