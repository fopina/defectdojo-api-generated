# OrganizationMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | **int** |  | [optional] 
**user** | **int** |  | [optional] 
**role** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.organization_member_request import OrganizationMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMemberRequest from a JSON string
organization_member_request_instance = OrganizationMemberRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationMemberRequest.to_json())

# convert the object into a dict
organization_member_request_dict = organization_member_request_instance.to_dict()
# create an instance of OrganizationMemberRequest from a dict
organization_member_request_from_dict = OrganizationMemberRequest.from_dict(organization_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


