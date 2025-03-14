# Product


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**findings_count** | **int** |  | [readonly] 
**findings_list** | **List[int]** |  | [readonly] 
**tags** | **List[str]** |  | [optional] 
**product_meta** | [**List[ProductMeta]**](ProductMeta.md) |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | 
**created** | **datetime** |  | [readonly] 
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
**prod_type** | **int** |  | 
**sla_configuration** | **int** |  | [optional] 
**members** | **List[int]** |  | [readonly] 
**authorization_groups** | **List[int]** |  | [readonly] 
**regulations** | **List[int]** |  | [optional] 
**prefetch** | [**PaginatedProductListPrefetch**](PaginatedProductListPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.product import Product

# TODO update the JSON string below
json = "{}"
# create an instance of Product from a JSON string
product_instance = Product.from_json(json)
# print the JSON string representation of the object
print(Product.to_json())

# convert the object into a dict
product_dict = product_instance.to_dict()
# create an instance of Product from a dict
product_from_dict = Product.from_dict(product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


