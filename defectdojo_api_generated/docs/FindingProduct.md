# FindingProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**prod_type** | [**FindingProdType**](FindingProdType.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.finding_product import FindingProduct

# TODO update the JSON string below
json = "{}"
# create an instance of FindingProduct from a JSON string
finding_product_instance = FindingProduct.from_json(json)
# print the JSON string representation of the object
print(FindingProduct.to_json())

# convert the object into a dict
finding_product_dict = finding_product_instance.to_dict()
# create an instance of FindingProduct from a dict
finding_product_from_dict = FindingProduct.from_dict(finding_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


