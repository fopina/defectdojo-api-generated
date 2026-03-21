# AnnouncementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | This dismissable message will be displayed on all pages for authenticated users. It can contain basic html tags, for example &lt;a href&#x3D;&#39;https://www.fred.com&#39; style&#x3D;&#39;color: #337ab7;&#39; target&#x3D;&#39;_blank&#39;&gt;https://example.com&lt;/a&gt; | [optional] 
**style** | **str** | The style of banner to display. (info, success, warning, danger)  * &#x60;info&#x60; - Info * &#x60;success&#x60; - Success * &#x60;warning&#x60; - Warning * &#x60;danger&#x60; - Danger | [optional] 
**dismissable** | **bool** | Ticking this box allows users to dismiss the current announcement | [optional] 

## Example

```python
from defectdojo_api_generated.models.announcement_request import AnnouncementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementRequest from a JSON string
announcement_request_instance = AnnouncementRequest.from_json(json)
# print the JSON string representation of the object
print(AnnouncementRequest.to_json())

# convert the object into a dict
announcement_request_dict = announcement_request_instance.to_dict()
# create an instance of AnnouncementRequest from a dict
announcement_request_from_dict = AnnouncementRequest.from_dict(announcement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


