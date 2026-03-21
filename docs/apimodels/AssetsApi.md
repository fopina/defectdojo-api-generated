# defectdojo_api_generated.AssetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](AssetsApi.md#create) | **POST** /api/v2/assets/ | 
[**delete_preview_list**](AssetsApi.md#delete_preview_list) | **GET** /api/v2/assets/{id}/delete_preview/ | 
[**destroy**](AssetsApi.md#destroy) | **DELETE** /api/v2/assets/{id}/ | 
[**generate_report_create**](AssetsApi.md#generate_report_create) | **POST** /api/v2/assets/{id}/generate_report/ | 
[**list**](AssetsApi.md#list) | **GET** /api/v2/assets/ | 
[**partial_update**](AssetsApi.md#partial_update) | **PATCH** /api/v2/assets/{id}/ | 
[**retrieve**](AssetsApi.md#retrieve) | **GET** /api/v2/assets/{id}/ | 
[**update**](AssetsApi.md#update) | **PUT** /api/v2/assets/{id}/ | 


# **create**
> Asset create(asset_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.asset import Asset
from defectdojo_api_generated.models.asset_request import AssetRequest
from defectdojo_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = defectdojo_api_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = defectdojo_api_generated.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with defectdojo_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = defectdojo_api_generated.AssetsApi(api_client)
    asset_request = defectdojo_api_generated.AssetRequest() # AssetRequest | 

    try:
        api_response = api_instance.create(asset_request)
        print("The response of AssetsApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_request** | [**AssetRequest**](AssetRequest.md)|  | 

### Return type

[**Asset**](Asset.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_preview_list**
> PaginatedDeletePreviewList delete_preview_list(id, limit=limit, offset=offset)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_delete_preview_list import PaginatedDeletePreviewList
from defectdojo_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = defectdojo_api_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = defectdojo_api_generated.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with defectdojo_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = defectdojo_api_generated.AssetsApi(api_client)
    id = 56 # int | A unique integer value identifying this product.
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.delete_preview_list(id, limit=limit, offset=offset)
        print("The response of AssetsApi->delete_preview_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->delete_preview_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedDeletePreviewList**](PaginatedDeletePreviewList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> destroy(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = defectdojo_api_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = defectdojo_api_generated.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with defectdojo_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = defectdojo_api_generated.AssetsApi(api_client)
    id = 56 # int | A unique integer value identifying this product.

    try:
        api_instance.destroy(id)
    except Exception as e:
        print("Exception when calling AssetsApi->destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_report_create**
> ReportGenerate generate_report_create(id, report_generate_option_request=report_generate_option_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.report_generate import ReportGenerate
from defectdojo_api_generated.models.report_generate_option_request import ReportGenerateOptionRequest
from defectdojo_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = defectdojo_api_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = defectdojo_api_generated.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with defectdojo_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = defectdojo_api_generated.AssetsApi(api_client)
    id = 56 # int | A unique integer value identifying this product.
    report_generate_option_request = defectdojo_api_generated.ReportGenerateOptionRequest() # ReportGenerateOptionRequest |  (optional)

    try:
        api_response = api_instance.generate_report_create(id, report_generate_option_request=report_generate_option_request)
        print("The response of AssetsApi->generate_report_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->generate_report_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 
 **report_generate_option_request** | [**ReportGenerateOptionRequest**](ReportGenerateOptionRequest.md)|  | [optional] 

### Return type

[**ReportGenerate**](ReportGenerate.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedAssetList list(asset_manager=asset_manager, asset_numeric_grade=asset_numeric_grade, business_criticality=business_criticality, created=created, description=description, external_audience=external_audience, has_tags=has_tags, id=id, internet_accessible=internet_accessible, lifecycle=lifecycle, limit=limit, name=name, name_exact=name_exact, not_tag=not_tag, not_tags=not_tags, o=o, offset=offset, organization=organization, origin=origin, outside_of_sla=outside_of_sla, platform=platform, prefetch=prefetch, regulations=regulations, revenue=revenue, tag=tag, tags=tags, tags__and=tags__and, team_manager=team_manager, technical_contact=technical_contact, tid=tid, updated=updated, user_records=user_records)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_asset_list import PaginatedAssetList
from defectdojo_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = defectdojo_api_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = defectdojo_api_generated.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with defectdojo_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = defectdojo_api_generated.AssetsApi(api_client)
    asset_manager = [56] # List[int] | Multiple values may be separated by commas. (optional)
    asset_numeric_grade = [56] # List[int] | Multiple values may be separated by commas. (optional)
    business_criticality = ['business_criticality_example'] # List[Optional[str]] | * `very high` - Very High * `high` - High * `medium` - Medium * `low` - Low * `very low` - Very Low * `none` - None (optional)
    created = '2013-10-20T19:20:30+01:00' # datetime | Time that the object was initially created, and saved to the database  * `None` - Any date * `1` - Today * `2` - Past 7 days * `3` - Past 30 days * `4` - Past 90 days * `5` - Current month * `6` - Current year * `7` - Past year (optional)
    description = 'description_example' # str |  (optional)
    external_audience = True # bool |  (optional)
    has_tags = True # bool | Has tags (optional)
    id = [56] # List[int] | Multiple values may be separated by commas. (optional)
    internet_accessible = True # bool |  (optional)
    lifecycle = ['lifecycle_example'] # List[Optional[str]] | * `construction` - Construction * `production` - Production * `retirement` - Retirement (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    name = 'name_example' # str |  (optional)
    name_exact = 'name_exact_example' # str |  (optional)
    not_tag = 'not_tag_example' # str | Not Tag name contains (optional)
    not_tags = ['not_tags_example'] # List[str] | Comma separated list of exact tags not present on Product (optional)
    o = ['o_example'] # List[str] | Ordering  * `id` - Id * `-id` - Id (descending) * `tid` - Tid * `-tid` - Tid (descending) * `name` - Name * `-name` - Name (descending) * `created` - Created * `-created` - Created (descending) * `asset_numeric_grade` - Asset numeric grade * `-asset_numeric_grade` - Asset numeric grade (descending) * `business_criticality` - Business criticality * `-business_criticality` - Business criticality (descending) * `platform` - Platform * `-platform` - Platform (descending) * `lifecycle` - Lifecycle * `-lifecycle` - Lifecycle (descending) * `origin` - Origin * `-origin` - Origin (descending) * `revenue` - Revenue * `-revenue` - Revenue (descending) * `external_audience` - External audience * `-external_audience` - External audience (descending) * `internet_accessible` - Internet accessible * `-internet_accessible` - Internet accessible (descending) * `asset_manager` - Asset manager * `-asset_manager` - Asset manager (descending) * `asset_manager__first_name` - Asset manager  first name * `-asset_manager__first_name` - Asset manager  first name (descending) * `asset_manager__last_name` - Asset manager  last name * `-asset_manager__last_name` - Asset manager  last name (descending) * `technical_contact` - Technical contact * `-technical_contact` - Technical contact (descending) * `technical_contact__first_name` - Technical contact  first name * `-technical_contact__first_name` - Technical contact  first name (descending) * `technical_contact__last_name` - Technical contact  last name * `-technical_contact__last_name` - Technical contact  last name (descending) * `team_manager` - Team manager * `-team_manager` - Team manager (descending) * `team_manager__first_name` - Team manager  first name * `-team_manager__first_name` - Team manager  first name (descending) * `team_manager__last_name` - Team manager  last name * `-team_manager__last_name` - Team manager  last name (descending) * `organization` - Organization * `-organization` - Organization (descending) * `organization__name` - Organization  name * `-organization__name` - Organization  name (descending) * `updated` - Updated * `-updated` - Updated (descending) * `user_records` - User records * `-user_records` - User records (descending) (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    organization = [56] # List[int] | Multiple values may be separated by commas. (optional)
    origin = ['origin_example'] # List[Optional[str]] | * `third party library` - Third Party Library * `purchased` - Purchased * `contractor` - Contractor Developed * `internal` - Internally Developed * `open source` - Open Source * `outsourced` - Outsourced (optional)
    outside_of_sla = 3.4 # float |  (optional)
    platform = ['platform_example'] # List[Optional[str]] | * `web service` - API * `desktop` - Desktop * `iot` - Internet of Things * `mobile` - Mobile * `web` - Web (optional)
    prefetch = ['prefetch_example'] # List[str] | List of fields for which to prefetch model instances and add those to the response (optional)
    regulations = [56] # List[int] | Multiple values may be separated by commas. (optional)
    revenue = 3.4 # float |  (optional)
    tag = 'tag_example' # str | Tag name contains (optional)
    tags = ['tags_example'] # List[str] | Comma separated list of exact tags (uses OR for multiple values) (optional)
    tags__and = ['tags__and_example'] # List[str] | Comma separated list of exact tags to match with an AND expression (optional)
    team_manager = [56] # List[int] | Multiple values may be separated by commas. (optional)
    technical_contact = [56] # List[int] | Multiple values may be separated by commas. (optional)
    tid = [56] # List[int] | Multiple values may be separated by commas. (optional)
    updated = '2013-10-20T19:20:30+01:00' # datetime | Time that the object was most recently saved to the database  * `None` - Any date * `1` - Today * `2` - Past 7 days * `3` - Past 30 days * `4` - Past 90 days * `5` - Current month * `6` - Current year * `7` - Past year (optional)
    user_records = [56] # List[int] | Multiple values may be separated by commas. (optional)

    try:
        api_response = api_instance.list(asset_manager=asset_manager, asset_numeric_grade=asset_numeric_grade, business_criticality=business_criticality, created=created, description=description, external_audience=external_audience, has_tags=has_tags, id=id, internet_accessible=internet_accessible, lifecycle=lifecycle, limit=limit, name=name, name_exact=name_exact, not_tag=not_tag, not_tags=not_tags, o=o, offset=offset, organization=organization, origin=origin, outside_of_sla=outside_of_sla, platform=platform, prefetch=prefetch, regulations=regulations, revenue=revenue, tag=tag, tags=tags, tags__and=tags__and, team_manager=team_manager, technical_contact=technical_contact, tid=tid, updated=updated, user_records=user_records)
        print("The response of AssetsApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_manager** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **asset_numeric_grade** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **business_criticality** | [**List[Optional[str]]**](str.md)| * &#x60;very high&#x60; - Very High * &#x60;high&#x60; - High * &#x60;medium&#x60; - Medium * &#x60;low&#x60; - Low * &#x60;very low&#x60; - Very Low * &#x60;none&#x60; - None | [optional] 
 **created** | **datetime**| Time that the object was initially created, and saved to the database  * &#x60;None&#x60; - Any date * &#x60;1&#x60; - Today * &#x60;2&#x60; - Past 7 days * &#x60;3&#x60; - Past 30 days * &#x60;4&#x60; - Past 90 days * &#x60;5&#x60; - Current month * &#x60;6&#x60; - Current year * &#x60;7&#x60; - Past year | [optional] 
 **description** | **str**|  | [optional] 
 **external_audience** | **bool**|  | [optional] 
 **has_tags** | **bool**| Has tags | [optional] 
 **id** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **internet_accessible** | **bool**|  | [optional] 
 **lifecycle** | [**List[Optional[str]]**](str.md)| * &#x60;construction&#x60; - Construction * &#x60;production&#x60; - Production * &#x60;retirement&#x60; - Retirement | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**|  | [optional] 
 **name_exact** | **str**|  | [optional] 
 **not_tag** | **str**| Not Tag name contains | [optional] 
 **not_tags** | [**List[str]**](str.md)| Comma separated list of exact tags not present on Product | [optional] 
 **o** | [**List[str]**](str.md)| Ordering  * &#x60;id&#x60; - Id * &#x60;-id&#x60; - Id (descending) * &#x60;tid&#x60; - Tid * &#x60;-tid&#x60; - Tid (descending) * &#x60;name&#x60; - Name * &#x60;-name&#x60; - Name (descending) * &#x60;created&#x60; - Created * &#x60;-created&#x60; - Created (descending) * &#x60;asset_numeric_grade&#x60; - Asset numeric grade * &#x60;-asset_numeric_grade&#x60; - Asset numeric grade (descending) * &#x60;business_criticality&#x60; - Business criticality * &#x60;-business_criticality&#x60; - Business criticality (descending) * &#x60;platform&#x60; - Platform * &#x60;-platform&#x60; - Platform (descending) * &#x60;lifecycle&#x60; - Lifecycle * &#x60;-lifecycle&#x60; - Lifecycle (descending) * &#x60;origin&#x60; - Origin * &#x60;-origin&#x60; - Origin (descending) * &#x60;revenue&#x60; - Revenue * &#x60;-revenue&#x60; - Revenue (descending) * &#x60;external_audience&#x60; - External audience * &#x60;-external_audience&#x60; - External audience (descending) * &#x60;internet_accessible&#x60; - Internet accessible * &#x60;-internet_accessible&#x60; - Internet accessible (descending) * &#x60;asset_manager&#x60; - Asset manager * &#x60;-asset_manager&#x60; - Asset manager (descending) * &#x60;asset_manager__first_name&#x60; - Asset manager  first name * &#x60;-asset_manager__first_name&#x60; - Asset manager  first name (descending) * &#x60;asset_manager__last_name&#x60; - Asset manager  last name * &#x60;-asset_manager__last_name&#x60; - Asset manager  last name (descending) * &#x60;technical_contact&#x60; - Technical contact * &#x60;-technical_contact&#x60; - Technical contact (descending) * &#x60;technical_contact__first_name&#x60; - Technical contact  first name * &#x60;-technical_contact__first_name&#x60; - Technical contact  first name (descending) * &#x60;technical_contact__last_name&#x60; - Technical contact  last name * &#x60;-technical_contact__last_name&#x60; - Technical contact  last name (descending) * &#x60;team_manager&#x60; - Team manager * &#x60;-team_manager&#x60; - Team manager (descending) * &#x60;team_manager__first_name&#x60; - Team manager  first name * &#x60;-team_manager__first_name&#x60; - Team manager  first name (descending) * &#x60;team_manager__last_name&#x60; - Team manager  last name * &#x60;-team_manager__last_name&#x60; - Team manager  last name (descending) * &#x60;organization&#x60; - Organization * &#x60;-organization&#x60; - Organization (descending) * &#x60;organization__name&#x60; - Organization  name * &#x60;-organization__name&#x60; - Organization  name (descending) * &#x60;updated&#x60; - Updated * &#x60;-updated&#x60; - Updated (descending) * &#x60;user_records&#x60; - User records * &#x60;-user_records&#x60; - User records (descending) | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **organization** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **origin** | [**List[Optional[str]]**](str.md)| * &#x60;third party library&#x60; - Third Party Library * &#x60;purchased&#x60; - Purchased * &#x60;contractor&#x60; - Contractor Developed * &#x60;internal&#x60; - Internally Developed * &#x60;open source&#x60; - Open Source * &#x60;outsourced&#x60; - Outsourced | [optional] 
 **outside_of_sla** | **float**|  | [optional] 
 **platform** | [**List[Optional[str]]**](str.md)| * &#x60;web service&#x60; - API * &#x60;desktop&#x60; - Desktop * &#x60;iot&#x60; - Internet of Things * &#x60;mobile&#x60; - Mobile * &#x60;web&#x60; - Web | [optional] 
 **prefetch** | [**List[str]**](str.md)| List of fields for which to prefetch model instances and add those to the response | [optional] 
 **regulations** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **revenue** | **float**|  | [optional] 
 **tag** | **str**| Tag name contains | [optional] 
 **tags** | [**List[str]**](str.md)| Comma separated list of exact tags (uses OR for multiple values) | [optional] 
 **tags__and** | [**List[str]**](str.md)| Comma separated list of exact tags to match with an AND expression | [optional] 
 **team_manager** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **technical_contact** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **tid** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **updated** | **datetime**| Time that the object was most recently saved to the database  * &#x60;None&#x60; - Any date * &#x60;1&#x60; - Today * &#x60;2&#x60; - Past 7 days * &#x60;3&#x60; - Past 30 days * &#x60;4&#x60; - Past 90 days * &#x60;5&#x60; - Current month * &#x60;6&#x60; - Current year * &#x60;7&#x60; - Past year | [optional] 
 **user_records** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 

### Return type

[**PaginatedAssetList**](PaginatedAssetList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update**
> Asset partial_update(id, patched_asset_request=patched_asset_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.asset import Asset
from defectdojo_api_generated.models.patched_asset_request import PatchedAssetRequest
from defectdojo_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = defectdojo_api_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = defectdojo_api_generated.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with defectdojo_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = defectdojo_api_generated.AssetsApi(api_client)
    id = 56 # int | A unique integer value identifying this product.
    patched_asset_request = defectdojo_api_generated.PatchedAssetRequest() # PatchedAssetRequest |  (optional)

    try:
        api_response = api_instance.partial_update(id, patched_asset_request=patched_asset_request)
        print("The response of AssetsApi->partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 
 **patched_asset_request** | [**PatchedAssetRequest**](PatchedAssetRequest.md)|  | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve**
> Asset retrieve(id, prefetch=prefetch)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.asset import Asset
from defectdojo_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = defectdojo_api_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = defectdojo_api_generated.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with defectdojo_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = defectdojo_api_generated.AssetsApi(api_client)
    id = 56 # int | A unique integer value identifying this product.
    prefetch = ['prefetch_example'] # List[str] | List of fields for which to prefetch model instances and add those to the response (optional)

    try:
        api_response = api_instance.retrieve(id, prefetch=prefetch)
        print("The response of AssetsApi->retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 
 **prefetch** | [**List[str]**](str.md)| List of fields for which to prefetch model instances and add those to the response | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Asset update(id, asset_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.asset import Asset
from defectdojo_api_generated.models.asset_request import AssetRequest
from defectdojo_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = defectdojo_api_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = defectdojo_api_generated.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with defectdojo_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = defectdojo_api_generated.AssetsApi(api_client)
    id = 56 # int | A unique integer value identifying this product.
    asset_request = defectdojo_api_generated.AssetRequest() # AssetRequest | 

    try:
        api_response = api_instance.update(id, asset_request)
        print("The response of AssetsApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 
 **asset_request** | [**AssetRequest**](AssetRequest.md)|  | 

### Return type

[**Asset**](Asset.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

