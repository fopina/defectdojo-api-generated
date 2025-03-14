# FindingProdType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 

## Example

```python
from defectdojo_api_generated.models.finding_prod_type import FindingProdType

# TODO update the JSON string below
json = "{}"
# create an instance of FindingProdType from a JSON string
finding_prod_type_instance = FindingProdType.from_json(json)
# print the JSON string representation of the object
print(FindingProdType.to_json())

# convert the object into a dict
finding_prod_type_dict = finding_prod_type_instance.to_dict()
# create an instance of FindingProdType from a dict
finding_prod_type_from_dict = FindingProdType.from_dict(finding_prod_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


