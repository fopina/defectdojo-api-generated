# QuestionnaireQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**created** | **datetime** |  | [readonly] 
**modified** | **datetime** |  | [readonly] 
**order** | **int** | The render order | [optional] 
**optional** | **bool** | If selected, user doesn&#39;t have to answer this question | [optional] 
**text** | **str** | The question text | [optional] 

## Example

```python
from defectdojo_api_generated.models.questionnaire_question import QuestionnaireQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionnaireQuestion from a JSON string
questionnaire_question_instance = QuestionnaireQuestion.from_json(json)
# print the JSON string representation of the object
print(QuestionnaireQuestion.to_json())

# convert the object into a dict
questionnaire_question_dict = questionnaire_question_instance.to_dict()
# create an instance of QuestionnaireQuestion from a dict
questionnaire_question_from_dict = QuestionnaireQuestion.from_dict(questionnaire_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


