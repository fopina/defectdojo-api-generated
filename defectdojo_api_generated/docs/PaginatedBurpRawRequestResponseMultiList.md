# PaginatedBurpRawRequestResponseMultiList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[BurpRawRequestResponseMulti]**](BurpRawRequestResponseMulti.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_burp_raw_request_response_multi_list import PaginatedBurpRawRequestResponseMultiList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBurpRawRequestResponseMultiList from a JSON string
paginated_burp_raw_request_response_multi_list_instance = PaginatedBurpRawRequestResponseMultiList.from_json(json)
# print the JSON string representation of the object
print(PaginatedBurpRawRequestResponseMultiList.to_json())

# convert the object into a dict
paginated_burp_raw_request_response_multi_list_dict = paginated_burp_raw_request_response_multi_list_instance.to_dict()
# create an instance of PaginatedBurpRawRequestResponseMultiList from a dict
paginated_burp_raw_request_response_multi_list_from_dict = PaginatedBurpRawRequestResponseMultiList.from_dict(paginated_burp_raw_request_response_multi_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


