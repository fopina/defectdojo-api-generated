# PatchedSLAConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A unique name for the set of SLAs. | [optional] 
**description** | **str** |  | [optional] 
**critical** | **int** | The number of days to remediate a critical finding. | [optional] 
**enforce_critical** | **bool** | When enabled, critical findings will be assigned an SLA expiration date based on the critical finding SLA days within this SLA configuration. | [optional] 
**high** | **int** | The number of days to remediate a high finding. | [optional] 
**enforce_high** | **bool** | When enabled, high findings will be assigned an SLA expiration date based on the high finding SLA days within this SLA configuration. | [optional] 
**medium** | **int** | The number of days to remediate a medium finding. | [optional] 
**enforce_medium** | **bool** | When enabled, medium findings will be assigned an SLA expiration date based on the medium finding SLA days within this SLA configuration. | [optional] 
**low** | **int** | The number of days to remediate a low finding. | [optional] 
**enforce_low** | **bool** | When enabled, low findings will be assigned an SLA expiration date based on the low finding SLA days within this SLA configuration. | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_sla_configuration_request import PatchedSLAConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSLAConfigurationRequest from a JSON string
patched_sla_configuration_request_instance = PatchedSLAConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedSLAConfigurationRequest.to_json())

# convert the object into a dict
patched_sla_configuration_request_dict = patched_sla_configuration_request_instance.to_dict()
# create an instance of PatchedSLAConfigurationRequest from a dict
patched_sla_configuration_request_from_dict = PatchedSLAConfigurationRequest.from_dict(patched_sla_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


