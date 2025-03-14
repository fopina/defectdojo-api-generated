# PaginatedQuestionnaireAnsweredSurveyListPrefetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 
**engagement** | [**Dict[str, FindingEngagement]**](FindingEngagement.md) |  | [optional] [readonly] 
**responder** | [**Dict[str, UserStub]**](UserStub.md) |  | [optional] [readonly] 
**survey** | [**Dict[str, QuestionnaireEngagementSurvey]**](QuestionnaireEngagementSurvey.md) |  | [optional] [readonly] 

## Example

```python
from defectdojo_api_generated.models.paginated_questionnaire_answered_survey_list_prefetch import PaginatedQuestionnaireAnsweredSurveyListPrefetch

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedQuestionnaireAnsweredSurveyListPrefetch from a JSON string
paginated_questionnaire_answered_survey_list_prefetch_instance = PaginatedQuestionnaireAnsweredSurveyListPrefetch.from_json(json)
# print the JSON string representation of the object
print(PaginatedQuestionnaireAnsweredSurveyListPrefetch.to_json())

# convert the object into a dict
paginated_questionnaire_answered_survey_list_prefetch_dict = paginated_questionnaire_answered_survey_list_prefetch_instance.to_dict()
# create an instance of PaginatedQuestionnaireAnsweredSurveyListPrefetch from a dict
paginated_questionnaire_answered_survey_list_prefetch_from_dict = PaginatedQuestionnaireAnsweredSurveyListPrefetch.from_dict(paginated_questionnaire_answered_survey_list_prefetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


