# Regulation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | The name of the regulation. | 
**acronym** | **str** | A shortened representation of the name. | 
**category** | **str** | The subject of the regulation.  * &#x60;privacy&#x60; - Privacy * &#x60;finance&#x60; - Finance * &#x60;education&#x60; - Education * &#x60;medical&#x60; - Medical * &#x60;corporate&#x60; - Corporate * &#x60;other&#x60; - Other | 
**jurisdiction** | **str** | The territory over which the regulation applies. | 
**description** | **str** | Information about the regulation&#39;s purpose. | [optional] 
**reference** | **str** | An external URL for more information. | [optional] 

## Example

```python
from defectdojo_api_generated.models.regulation import Regulation

# TODO update the JSON string below
json = "{}"
# create an instance of Regulation from a JSON string
regulation_instance = Regulation.from_json(json)
# print the JSON string representation of the object
print(Regulation.to_json())

# convert the object into a dict
regulation_dict = regulation_instance.to_dict()
# create an instance of Regulation from a dict
regulation_from_dict = Regulation.from_dict(regulation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


