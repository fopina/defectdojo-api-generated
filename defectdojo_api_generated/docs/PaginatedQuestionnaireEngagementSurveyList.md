# PaginatedQuestionnaireEngagementSurveyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[QuestionnaireEngagementSurvey]**](QuestionnaireEngagementSurvey.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_questionnaire_engagement_survey_list import PaginatedQuestionnaireEngagementSurveyList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedQuestionnaireEngagementSurveyList from a JSON string
paginated_questionnaire_engagement_survey_list_instance = PaginatedQuestionnaireEngagementSurveyList.from_json(json)
# print the JSON string representation of the object
print(PaginatedQuestionnaireEngagementSurveyList.to_json())

# convert the object into a dict
paginated_questionnaire_engagement_survey_list_dict = paginated_questionnaire_engagement_survey_list_instance.to_dict()
# create an instance of PaginatedQuestionnaireEngagementSurveyList from a dict
paginated_questionnaire_engagement_survey_list_from_dict = PaginatedQuestionnaireEngagementSurveyList.from_dict(paginated_questionnaire_engagement_survey_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


