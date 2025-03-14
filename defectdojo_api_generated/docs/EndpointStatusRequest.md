# EndpointStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**mitigated** | **bool** |  | [optional] 
**false_positive** | **bool** |  | [optional] 
**out_of_scope** | **bool** |  | [optional] 
**risk_accepted** | **bool** |  | [optional] 
**mitigated_by** | **int** |  | [optional] 
**endpoint** | **int** |  | 
**finding** | **int** |  | 

## Example

```python
from defectdojo_api_generated.models.endpoint_status_request import EndpointStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointStatusRequest from a JSON string
endpoint_status_request_instance = EndpointStatusRequest.from_json(json)
# print the JSON string representation of the object
print(EndpointStatusRequest.to_json())

# convert the object into a dict
endpoint_status_request_dict = endpoint_status_request_instance.to_dict()
# create an instance of EndpointStatusRequest from a dict
endpoint_status_request_from_dict = EndpointStatusRequest.from_dict(endpoint_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


