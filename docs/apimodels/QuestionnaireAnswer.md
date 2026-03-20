# QuestionnaireAnswer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**created** | **datetime** |  | [optional] [readonly] 
**modified** | **datetime** |  | [optional] [readonly] 
**question** | **int** |  | [optional] 
**answered_survey** | **int** |  | [optional] 

## Example

```python
from defectdojo_api_generated.models.questionnaire_answer import QuestionnaireAnswer

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionnaireAnswer from a JSON string
questionnaire_answer_instance = QuestionnaireAnswer.from_json(json)
# print the JSON string representation of the object
print(QuestionnaireAnswer.to_json())

# convert the object into a dict
questionnaire_answer_dict = questionnaire_answer_instance.to_dict()
# create an instance of QuestionnaireAnswer from a dict
questionnaire_answer_from_dict = QuestionnaireAnswer.from_dict(questionnaire_answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


