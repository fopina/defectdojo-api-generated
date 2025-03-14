# PaginatedQuestionnaireGeneralSurveyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[QuestionnaireGeneralSurvey]**](QuestionnaireGeneralSurvey.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_questionnaire_general_survey_list import PaginatedQuestionnaireGeneralSurveyList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedQuestionnaireGeneralSurveyList from a JSON string
paginated_questionnaire_general_survey_list_instance = PaginatedQuestionnaireGeneralSurveyList.from_json(json)
# print the JSON string representation of the object
print(PaginatedQuestionnaireGeneralSurveyList.to_json())

# convert the object into a dict
paginated_questionnaire_general_survey_list_dict = paginated_questionnaire_general_survey_list_instance.to_dict()
# create an instance of PaginatedQuestionnaireGeneralSurveyList from a dict
paginated_questionnaire_general_survey_list_from_dict = PaginatedQuestionnaireGeneralSurveyList.from_dict(paginated_questionnaire_general_survey_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


