# Asset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**findings_count** | **int** |  | [optional] [readonly] 
**findings_list** | **List[int]** |  | [optional] [readonly] 
**tags** | **List[str]** |  | [optional] 
**asset_meta** | [**List[ProductMeta]**](ProductMeta.md) |  | [optional] [readonly] 
**organization** | **int** |  | [optional] 
**asset_numeric_grade** | **int** |  | [optional] 
**enable_asset_tag_inheritance** | **bool** |  | [optional] [default to False]
**asset_managers** | **int** |  | [optional] 
**business_criticality** | **str** | * &#x60;very high&#x60; - Very High * &#x60;high&#x60; - High * &#x60;medium&#x60; - Medium * &#x60;low&#x60; - Low * &#x60;very low&#x60; - Very Low * &#x60;none&#x60; - None | [optional] 
**platform** | **str** | * &#x60;web service&#x60; - API * &#x60;desktop&#x60; - Desktop * &#x60;iot&#x60; - Internet of Things * &#x60;mobile&#x60; - Mobile * &#x60;web&#x60; - Web | [optional] 
**lifecycle** | **str** | * &#x60;construction&#x60; - Construction * &#x60;production&#x60; - Production * &#x60;retirement&#x60; - Retirement | [optional] 
**origin** | **str** | * &#x60;third party library&#x60; - Third Party Library * &#x60;purchased&#x60; - Purchased * &#x60;contractor&#x60; - Contractor Developed * &#x60;internal&#x60; - Internally Developed * &#x60;open source&#x60; - Open Source * &#x60;outsourced&#x60; - Outsourced | [optional] 
**created** | **datetime** | Time that the object was initially created, and saved to the database | [optional] [readonly] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**user_records** | **int** | Estimate the number of user records within the application. | [optional] 
**revenue** | **decimal.Decimal** | Estimate the application&#39;s revenue. | [optional] 
**external_audience** | **bool** | Specify if the application is used by people outside the organization. | [optional] 
**internet_accessible** | **bool** | Specify if the application is accessible from the public internet. | [optional] 
**enable_simple_risk_acceptance** | **bool** | Allows simple risk acceptance by checking/unchecking a checkbox. | [optional] 
**enable_full_risk_acceptance** | **bool** | Allows full risk acceptance using a risk acceptance form, expiration date, uploaded proof, etc. | [optional] 
**disable_sla_breach_notifications** | **bool** | Disable SLA breach notifications if configured in the global settings | [optional] 
**technical_contact** | **int** |  | [optional] 
**team_manager** | **int** |  | [optional] 
**sla_configuration** | **int** |  | [optional] 
**members** | **List[int]** |  | [optional] [readonly] 
**authorization_groups** | **List[int]** |  | [optional] [readonly] 
**regulations** | **List[int]** |  | [optional] 
**prefetch** | [**AssetPrefetch**](AssetPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.asset import Asset

# TODO update the JSON string below
json = "{}"
# create an instance of Asset from a JSON string
asset_instance = Asset.from_json(json)
# print the JSON string representation of the object
print(Asset.to_json())

# convert the object into a dict
asset_dict = asset_instance.to_dict()
# create an instance of Asset from a dict
asset_from_dict = Asset.from_dict(asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


