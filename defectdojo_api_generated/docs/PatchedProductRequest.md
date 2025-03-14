# PatchedProductRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**prod_numeric_grade** | **int** |  | [optional] 
**business_criticality** | **str** | * &#x60;very high&#x60; - Very High * &#x60;high&#x60; - High * &#x60;medium&#x60; - Medium * &#x60;low&#x60; - Low * &#x60;very low&#x60; - Very Low * &#x60;none&#x60; - None | [optional] 
**platform** | **str** | * &#x60;web service&#x60; - API * &#x60;desktop&#x60; - Desktop * &#x60;iot&#x60; - Internet of Things * &#x60;mobile&#x60; - Mobile * &#x60;web&#x60; - Web | [optional] 
**lifecycle** | **str** | * &#x60;construction&#x60; - Construction * &#x60;production&#x60; - Production * &#x60;retirement&#x60; - Retirement | [optional] 
**origin** | **str** | * &#x60;third party library&#x60; - Third Party Library * &#x60;purchased&#x60; - Purchased * &#x60;contractor&#x60; - Contractor Developed * &#x60;internal&#x60; - Internally Developed * &#x60;open source&#x60; - Open Source * &#x60;outsourced&#x60; - Outsourced | [optional] 
**user_records** | **int** | Estimate the number of user records within the application. | [optional] 
**revenue** | **decimal.Decimal** | Estimate the application&#39;s revenue. | [optional] 
**external_audience** | **bool** | Specify if the application is used by people outside the organization. | [optional] 
**internet_accessible** | **bool** | Specify if the application is accessible from the public internet. | [optional] 
**enable_product_tag_inheritance** | **bool** | Enables product tag inheritance. Any tags added on a product will automatically be added to all Engagements, Tests, and Findings | [optional] 
**enable_simple_risk_acceptance** | **bool** | Allows simple risk acceptance by checking/unchecking a checkbox. | [optional] 
**enable_full_risk_acceptance** | **bool** | Allows full risk acceptance using a risk acceptance form, expiration date, uploaded proof, etc. | [optional] 
**disable_sla_breach_notifications** | **bool** | Disable SLA breach notifications if configured in the global settings | [optional] 
**product_manager** | **int** |  | [optional] 
**technical_contact** | **int** |  | [optional] 
**team_manager** | **int** |  | [optional] 
**prod_type** | **int** |  | [optional] 
**sla_configuration** | **int** |  | [optional] 
**regulations** | **List[int]** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.patched_product_request import PatchedProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedProductRequest from a JSON string
patched_product_request_instance = PatchedProductRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedProductRequest.to_json())

# convert the object into a dict
patched_product_request_dict = patched_product_request_instance.to_dict()
# create an instance of PatchedProductRequest from a dict
patched_product_request_from_dict = PatchedProductRequest.from_dict(patched_product_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


