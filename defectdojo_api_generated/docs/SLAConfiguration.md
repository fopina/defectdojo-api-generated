# SLAConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | A unique name for the set of SLAs. | 
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
from defectdojo_api_generated.models.sla_configuration import SLAConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SLAConfiguration from a JSON string
sla_configuration_instance = SLAConfiguration.from_json(json)
# print the JSON string representation of the object
print(SLAConfiguration.to_json())

# convert the object into a dict
sla_configuration_dict = sla_configuration_instance.to_dict()
# create an instance of SLAConfiguration from a dict
sla_configuration_from_dict = SLAConfiguration.from_dict(sla_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


