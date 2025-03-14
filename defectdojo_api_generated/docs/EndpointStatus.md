# EndpointStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**var_date** | **date** |  | [optional] 
**last_modified** | **datetime** |  | [readonly] 
**mitigated** | **bool** |  | [optional] 
**mitigated_time** | **datetime** |  | [readonly] 
**false_positive** | **bool** |  | [optional] 
**out_of_scope** | **bool** |  | [optional] 
**risk_accepted** | **bool** |  | [optional] 
**mitigated_by** | **int** |  | [optional] 
**endpoint** | **int** |  | 
**finding** | **int** |  | 

## Example

```python
from defectdojo_api_generated.models.endpoint_status import EndpointStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointStatus from a JSON string
endpoint_status_instance = EndpointStatus.from_json(json)
# print the JSON string representation of the object
print(EndpointStatus.to_json())

# convert the object into a dict
endpoint_status_dict = endpoint_status_instance.to_dict()
# create an instance of EndpointStatus from a dict
endpoint_status_from_dict = EndpointStatus.from_dict(endpoint_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


