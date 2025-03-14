# defectdojo_api_generated.RiskAcceptanceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**risk_acceptance_create**](RiskAcceptanceApi.md#risk_acceptance_create) | **POST** /api/v2/risk_acceptance/ | 
[**risk_acceptance_delete_preview_list**](RiskAcceptanceApi.md#risk_acceptance_delete_preview_list) | **GET** /api/v2/risk_acceptance/{id}/delete_preview/ | 
[**risk_acceptance_destroy**](RiskAcceptanceApi.md#risk_acceptance_destroy) | **DELETE** /api/v2/risk_acceptance/{id}/ | 
[**risk_acceptance_download_proof_retrieve**](RiskAcceptanceApi.md#risk_acceptance_download_proof_retrieve) | **GET** /api/v2/risk_acceptance/{id}/download_proof/ | 
[**risk_acceptance_list**](RiskAcceptanceApi.md#risk_acceptance_list) | **GET** /api/v2/risk_acceptance/ | 
[**risk_acceptance_partial_update**](RiskAcceptanceApi.md#risk_acceptance_partial_update) | **PATCH** /api/v2/risk_acceptance/{id}/ | 
[**risk_acceptance_retrieve**](RiskAcceptanceApi.md#risk_acceptance_retrieve) | **GET** /api/v2/risk_acceptance/{id}/ | 
[**risk_acceptance_update**](RiskAcceptanceApi.md#risk_acceptance_update) | **PUT** /api/v2/risk_acceptance/{id}/ | 


# **risk_acceptance_create**
> RiskAcceptance risk_acceptance_create(risk_acceptance_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.risk_acceptance import RiskAcceptance
from defectdojo_api_generated.models.risk_acceptance_request import RiskAcceptanceRequest
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
    api_instance = defectdojo_api_generated.RiskAcceptanceApi(api_client)
    risk_acceptance_request = defectdojo_api_generated.RiskAcceptanceRequest() # RiskAcceptanceRequest | 

    try:
        api_response = api_instance.risk_acceptance_create(risk_acceptance_request)
        print("The response of RiskAcceptanceApi->risk_acceptance_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskAcceptanceApi->risk_acceptance_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_acceptance_request** | [**RiskAcceptanceRequest**](RiskAcceptanceRequest.md)|  | 

### Return type

[**RiskAcceptance**](RiskAcceptance.md)

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

# **risk_acceptance_delete_preview_list**
> PaginatedDeletePreviewList risk_acceptance_delete_preview_list(id, limit=limit, offset=offset)

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
    api_instance = defectdojo_api_generated.RiskAcceptanceApi(api_client)
    id = 56 # int | A unique integer value identifying this risk_ acceptance.
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.risk_acceptance_delete_preview_list(id, limit=limit, offset=offset)
        print("The response of RiskAcceptanceApi->risk_acceptance_delete_preview_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskAcceptanceApi->risk_acceptance_delete_preview_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this risk_ acceptance. | 
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

# **risk_acceptance_destroy**
> risk_acceptance_destroy(id)

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
    api_instance = defectdojo_api_generated.RiskAcceptanceApi(api_client)
    id = 56 # int | A unique integer value identifying this risk_ acceptance.

    try:
        api_instance.risk_acceptance_destroy(id)
    except Exception as e:
        print("Exception when calling RiskAcceptanceApi->risk_acceptance_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this risk_ acceptance. | 

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

# **risk_acceptance_download_proof_retrieve**
> RiskAcceptanceProof risk_acceptance_download_proof_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.risk_acceptance_proof import RiskAcceptanceProof
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
    api_instance = defectdojo_api_generated.RiskAcceptanceApi(api_client)
    id = 56 # int | A unique integer value identifying this risk_ acceptance.

    try:
        api_response = api_instance.risk_acceptance_download_proof_retrieve(id)
        print("The response of RiskAcceptanceApi->risk_acceptance_download_proof_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskAcceptanceApi->risk_acceptance_download_proof_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this risk_ acceptance. | 

### Return type

[**RiskAcceptanceProof**](RiskAcceptanceProof.md)

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

# **risk_acceptance_list**
> PaginatedRiskAcceptanceList risk_acceptance_list(accepted_by=accepted_by, accepted_findings=accepted_findings, decision=decision, decision_details=decision_details, expiration_date=expiration_date, expiration_date_handled=expiration_date_handled, expiration_date_warned=expiration_date_warned, limit=limit, name=name, notes=notes, o=o, offset=offset, owner=owner, reactivate_expired=reactivate_expired, recommendation=recommendation, recommendation_details=recommendation_details, restart_sla_expired=restart_sla_expired)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_risk_acceptance_list import PaginatedRiskAcceptanceList
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
    api_instance = defectdojo_api_generated.RiskAcceptanceApi(api_client)
    accepted_by = 'accepted_by_example' # str |  (optional)
    accepted_findings = [56] # List[int] |  (optional)
    decision = 'decision_example' # str | Risk treatment decision by risk owner  * `A` - Accept (The risk is acknowledged, yet remains) * `V` - Avoid (Do not engage with whatever creates the risk) * `M` - Mitigate (The risk still exists, yet compensating controls make it less of a threat) * `F` - Fix (The risk is eradicated) * `T` - Transfer (The risk is transferred to a 3rd party) (optional)
    decision_details = 'decision_details_example' # str |  (optional)
    expiration_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    expiration_date_handled = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    expiration_date_warned = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    name = 'name_example' # str |  (optional)
    notes = [56] # List[int] |  (optional)
    o = ['o_example'] # List[str] | Ordering  * `name` - Name * `-name` - Name (descending) (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    owner = 56 # int |  (optional)
    reactivate_expired = True # bool |  (optional)
    recommendation = 'recommendation_example' # str | Recommendation from the security team.  * `A` - Accept (The risk is acknowledged, yet remains) * `V` - Avoid (Do not engage with whatever creates the risk) * `M` - Mitigate (The risk still exists, yet compensating controls make it less of a threat) * `F` - Fix (The risk is eradicated) * `T` - Transfer (The risk is transferred to a 3rd party) (optional)
    recommendation_details = 'recommendation_details_example' # str |  (optional)
    restart_sla_expired = True # bool |  (optional)

    try:
        api_response = api_instance.risk_acceptance_list(accepted_by=accepted_by, accepted_findings=accepted_findings, decision=decision, decision_details=decision_details, expiration_date=expiration_date, expiration_date_handled=expiration_date_handled, expiration_date_warned=expiration_date_warned, limit=limit, name=name, notes=notes, o=o, offset=offset, owner=owner, reactivate_expired=reactivate_expired, recommendation=recommendation, recommendation_details=recommendation_details, restart_sla_expired=restart_sla_expired)
        print("The response of RiskAcceptanceApi->risk_acceptance_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskAcceptanceApi->risk_acceptance_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accepted_by** | **str**|  | [optional] 
 **accepted_findings** | [**List[int]**](int.md)|  | [optional] 
 **decision** | **str**| Risk treatment decision by risk owner  * &#x60;A&#x60; - Accept (The risk is acknowledged, yet remains) * &#x60;V&#x60; - Avoid (Do not engage with whatever creates the risk) * &#x60;M&#x60; - Mitigate (The risk still exists, yet compensating controls make it less of a threat) * &#x60;F&#x60; - Fix (The risk is eradicated) * &#x60;T&#x60; - Transfer (The risk is transferred to a 3rd party) | [optional] 
 **decision_details** | **str**|  | [optional] 
 **expiration_date** | **datetime**|  | [optional] 
 **expiration_date_handled** | **datetime**|  | [optional] 
 **expiration_date_warned** | **datetime**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**|  | [optional] 
 **notes** | [**List[int]**](int.md)|  | [optional] 
 **o** | [**List[str]**](str.md)| Ordering  * &#x60;name&#x60; - Name * &#x60;-name&#x60; - Name (descending) | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **owner** | **int**|  | [optional] 
 **reactivate_expired** | **bool**|  | [optional] 
 **recommendation** | **str**| Recommendation from the security team.  * &#x60;A&#x60; - Accept (The risk is acknowledged, yet remains) * &#x60;V&#x60; - Avoid (Do not engage with whatever creates the risk) * &#x60;M&#x60; - Mitigate (The risk still exists, yet compensating controls make it less of a threat) * &#x60;F&#x60; - Fix (The risk is eradicated) * &#x60;T&#x60; - Transfer (The risk is transferred to a 3rd party) | [optional] 
 **recommendation_details** | **str**|  | [optional] 
 **restart_sla_expired** | **bool**|  | [optional] 

### Return type

[**PaginatedRiskAcceptanceList**](PaginatedRiskAcceptanceList.md)

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

# **risk_acceptance_partial_update**
> RiskAcceptance risk_acceptance_partial_update(id, patched_risk_acceptance_request=patched_risk_acceptance_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.patched_risk_acceptance_request import PatchedRiskAcceptanceRequest
from defectdojo_api_generated.models.risk_acceptance import RiskAcceptance
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
    api_instance = defectdojo_api_generated.RiskAcceptanceApi(api_client)
    id = 56 # int | A unique integer value identifying this risk_ acceptance.
    patched_risk_acceptance_request = defectdojo_api_generated.PatchedRiskAcceptanceRequest() # PatchedRiskAcceptanceRequest |  (optional)

    try:
        api_response = api_instance.risk_acceptance_partial_update(id, patched_risk_acceptance_request=patched_risk_acceptance_request)
        print("The response of RiskAcceptanceApi->risk_acceptance_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskAcceptanceApi->risk_acceptance_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this risk_ acceptance. | 
 **patched_risk_acceptance_request** | [**PatchedRiskAcceptanceRequest**](PatchedRiskAcceptanceRequest.md)|  | [optional] 

### Return type

[**RiskAcceptance**](RiskAcceptance.md)

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

# **risk_acceptance_retrieve**
> RiskAcceptance risk_acceptance_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.risk_acceptance import RiskAcceptance
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
    api_instance = defectdojo_api_generated.RiskAcceptanceApi(api_client)
    id = 56 # int | A unique integer value identifying this risk_ acceptance.

    try:
        api_response = api_instance.risk_acceptance_retrieve(id)
        print("The response of RiskAcceptanceApi->risk_acceptance_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskAcceptanceApi->risk_acceptance_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this risk_ acceptance. | 

### Return type

[**RiskAcceptance**](RiskAcceptance.md)

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

# **risk_acceptance_update**
> RiskAcceptance risk_acceptance_update(id, risk_acceptance_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.risk_acceptance import RiskAcceptance
from defectdojo_api_generated.models.risk_acceptance_request import RiskAcceptanceRequest
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
    api_instance = defectdojo_api_generated.RiskAcceptanceApi(api_client)
    id = 56 # int | A unique integer value identifying this risk_ acceptance.
    risk_acceptance_request = defectdojo_api_generated.RiskAcceptanceRequest() # RiskAcceptanceRequest | 

    try:
        api_response = api_instance.risk_acceptance_update(id, risk_acceptance_request)
        print("The response of RiskAcceptanceApi->risk_acceptance_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskAcceptanceApi->risk_acceptance_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this risk_ acceptance. | 
 **risk_acceptance_request** | [**RiskAcceptanceRequest**](RiskAcceptanceRequest.md)|  | 

### Return type

[**RiskAcceptance**](RiskAcceptance.md)

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

