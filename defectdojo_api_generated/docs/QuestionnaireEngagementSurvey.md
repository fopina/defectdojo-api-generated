# QuestionnaireEngagementSurvey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**questions** | **List[str]** |  | [readonly] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.questionnaire_engagement_survey import QuestionnaireEngagementSurvey

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionnaireEngagementSurvey from a JSON string
questionnaire_engagement_survey_instance = QuestionnaireEngagementSurvey.from_json(json)
# print the JSON string representation of the object
print(QuestionnaireEngagementSurvey.to_json())

# convert the object into a dict
questionnaire_engagement_survey_dict = questionnaire_engagement_survey_instance.to_dict()
# create an instance of QuestionnaireEngagementSurvey from a dict
questionnaire_engagement_survey_from_dict = QuestionnaireEngagementSurvey.from_dict(questionnaire_engagement_survey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


