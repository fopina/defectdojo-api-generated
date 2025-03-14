# QuestionnaireGeneralSurvey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**survey** | [**QuestionnaireEngagementSurvey**](QuestionnaireEngagementSurvey.md) |  | 
**num_responses** | **int** |  | [optional] 
**generated** | **datetime** |  | [readonly] 
**expiration** | **datetime** |  | 

## Example

```python
from defectdojo_api_generated.models.questionnaire_general_survey import QuestionnaireGeneralSurvey

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionnaireGeneralSurvey from a JSON string
questionnaire_general_survey_instance = QuestionnaireGeneralSurvey.from_json(json)
# print the JSON string representation of the object
print(QuestionnaireGeneralSurvey.to_json())

# convert the object into a dict
questionnaire_general_survey_dict = questionnaire_general_survey_instance.to_dict()
# create an instance of QuestionnaireGeneralSurvey from a dict
questionnaire_general_survey_from_dict = QuestionnaireGeneralSurvey.from_dict(questionnaire_general_survey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


