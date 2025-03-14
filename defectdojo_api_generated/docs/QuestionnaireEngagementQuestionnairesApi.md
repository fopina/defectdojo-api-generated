# defectdojo_api_generated.QuestionnaireEngagementQuestionnairesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**questionnaire_engagement_questionnaires_link_engagement_create**](QuestionnaireEngagementQuestionnairesApi.md#questionnaire_engagement_questionnaires_link_engagement_create) | **POST** /api/v2/questionnaire_engagement_questionnaires/{id}/link_engagement/{engagement_id}/ | 
[**questionnaire_engagement_questionnaires_list**](QuestionnaireEngagementQuestionnairesApi.md#questionnaire_engagement_questionnaires_list) | **GET** /api/v2/questionnaire_engagement_questionnaires/ | 
[**questionnaire_engagement_questionnaires_retrieve**](QuestionnaireEngagementQuestionnairesApi.md#questionnaire_engagement_questionnaires_retrieve) | **GET** /api/v2/questionnaire_engagement_questionnaires/{id}/ | 


# **questionnaire_engagement_questionnaires_link_engagement_create**
> QuestionnaireAnsweredSurvey questionnaire_engagement_questionnaires_link_engagement_create(engagement_id, id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.questionnaire_answered_survey import QuestionnaireAnsweredSurvey
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
    api_instance = defectdojo_api_generated.QuestionnaireEngagementQuestionnairesApi(api_client)
    engagement_id = 56 # int | 
    id = 56 # int | A unique integer value identifying this Engagement Survey.

    try:
        api_response = api_instance.questionnaire_engagement_questionnaires_link_engagement_create(engagement_id, id)
        print("The response of QuestionnaireEngagementQuestionnairesApi->questionnaire_engagement_questionnaires_link_engagement_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionnaireEngagementQuestionnairesApi->questionnaire_engagement_questionnaires_link_engagement_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engagement_id** | **int**|  | 
 **id** | **int**| A unique integer value identifying this Engagement Survey. | 

### Return type

[**QuestionnaireAnsweredSurvey**](QuestionnaireAnsweredSurvey.md)

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

# **questionnaire_engagement_questionnaires_list**
> PaginatedQuestionnaireEngagementSurveyList questionnaire_engagement_questionnaires_list(limit=limit, offset=offset)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_questionnaire_engagement_survey_list import PaginatedQuestionnaireEngagementSurveyList
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
    api_instance = defectdojo_api_generated.QuestionnaireEngagementQuestionnairesApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.questionnaire_engagement_questionnaires_list(limit=limit, offset=offset)
        print("The response of QuestionnaireEngagementQuestionnairesApi->questionnaire_engagement_questionnaires_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionnaireEngagementQuestionnairesApi->questionnaire_engagement_questionnaires_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedQuestionnaireEngagementSurveyList**](PaginatedQuestionnaireEngagementSurveyList.md)

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

# **questionnaire_engagement_questionnaires_retrieve**
> QuestionnaireEngagementSurvey questionnaire_engagement_questionnaires_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.questionnaire_engagement_survey import QuestionnaireEngagementSurvey
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
    api_instance = defectdojo_api_generated.QuestionnaireEngagementQuestionnairesApi(api_client)
    id = 56 # int | A unique integer value identifying this Engagement Survey.

    try:
        api_response = api_instance.questionnaire_engagement_questionnaires_retrieve(id)
        print("The response of QuestionnaireEngagementQuestionnairesApi->questionnaire_engagement_questionnaires_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionnaireEngagementQuestionnairesApi->questionnaire_engagement_questionnaires_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Engagement Survey. | 

### Return type

[**QuestionnaireEngagementSurvey**](QuestionnaireEngagementSurvey.md)

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

