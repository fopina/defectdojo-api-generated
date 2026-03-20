# PatchedEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | [optional] 
**protocol** | **str** | The communication protocol/scheme such as &#39;http&#39;, &#39;ftp&#39;, &#39;dns&#39;, etc. | [optional] 
**userinfo** | **str** | User info as &#39;alice&#39;, &#39;bob&#39;, etc. | [optional] 
**host** | **str** | The host name or IP address. It must not include the port number. For example &#39;127.0.0.1&#39;, &#39;localhost&#39;, &#39;yourdomain.com&#39;. | [optional] 
**port** | **int** | The network port associated with the endpoint. | [optional] 
**path** | **str** | The location of the resource, it must not start with a &#39;/&#39;. For example endpoint/420/edit | [optional] 
**query** | **str** | The query string, the question mark should be omitted.For example &#39;group&#x3D;4&amp;team&#x3D;8&#39; | [optional] 
**fragment** | **str** | The fragment identifier which follows the hash mark. The hash mark should be omitted. For example &#39;section-13&#39;, &#39;paragraph-2&#39;. | [optional] 
**product** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_endpoint_request import PatchedEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedEndpointRequest from a JSON string
patched_endpoint_request_instance = PatchedEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedEndpointRequest.to_json())

# convert the object into a dict
patched_endpoint_request_dict = patched_endpoint_request_instance.to_dict()
# create an instance of PatchedEndpointRequest from a dict
patched_endpoint_request_from_dict = PatchedEndpointRequest.from_dict(patched_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


