# FindingEngagement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**product** | [**FindingProduct**](FindingProduct.md) |  | [optional] 
**target_start** | **date** |  | 
**target_end** | **date** |  | 
**branch_tag** | **str** | Tag or branch of the product the engagement tested. | [optional] 
**engagement_type** | **str** | * &#x60;Interactive&#x60; - Interactive * &#x60;CI/CD&#x60; - CI/CD | [optional] 
**build_id** | **str** | Build ID of the product the engagement tested. | [optional] 
**commit_hash** | **str** | Commit hash from repo | [optional] 
**version** | **str** | Version of the product the engagement tested. | [optional] 
**created** | **datetime** |  | [readonly] 
**updated** | **datetime** |  | [readonly] 

## Example

```python
from defectdojo_api_generated.models.finding_engagement import FindingEngagement

# TODO update the JSON string below
json = "{}"
# create an instance of FindingEngagement from a JSON string
finding_engagement_instance = FindingEngagement.from_json(json)
# print the JSON string representation of the object
print(FindingEngagement.to_json())

# convert the object into a dict
finding_engagement_dict = finding_engagement_instance.to_dict()
# create an instance of FindingEngagement from a dict
finding_engagement_from_dict = FindingEngagement.from_dict(finding_engagement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


