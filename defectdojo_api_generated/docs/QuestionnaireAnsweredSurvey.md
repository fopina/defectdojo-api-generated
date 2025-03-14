# QuestionnaireAnsweredSurvey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**completed** | **bool** |  | [optional] 
**answered_on** | **date** |  | [optional] 
**engagement** | **int** |  | [optional] 
**survey** | **int** |  | 
**assignee** | **int** |  | [optional] 
**responder** | **int** |  | [optional] 
**prefetch** | [**PaginatedQuestionnaireAnsweredSurveyListPrefetch**](PaginatedQuestionnaireAnsweredSurveyListPrefetch.md) |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.questionnaire_answered_survey import QuestionnaireAnsweredSurvey

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionnaireAnsweredSurvey from a JSON string
questionnaire_answered_survey_instance = QuestionnaireAnsweredSurvey.from_json(json)
# print the JSON string representation of the object
print(QuestionnaireAnsweredSurvey.to_json())

# convert the object into a dict
questionnaire_answered_survey_dict = questionnaire_answered_survey_instance.to_dict()
# create an instance of QuestionnaireAnsweredSurvey from a dict
questionnaire_answered_survey_from_dict = QuestionnaireAnsweredSurvey.from_dict(questionnaire_answered_survey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


