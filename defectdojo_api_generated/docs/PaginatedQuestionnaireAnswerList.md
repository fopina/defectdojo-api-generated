# PaginatedQuestionnaireAnswerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[QuestionnaireAnswer]**](QuestionnaireAnswer.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_questionnaire_answer_list import PaginatedQuestionnaireAnswerList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedQuestionnaireAnswerList from a JSON string
paginated_questionnaire_answer_list_instance = PaginatedQuestionnaireAnswerList.from_json(json)
# print the JSON string representation of the object
print(PaginatedQuestionnaireAnswerList.to_json())

# convert the object into a dict
paginated_questionnaire_answer_list_dict = paginated_questionnaire_answer_list_instance.to_dict()
# create an instance of PaginatedQuestionnaireAnswerList from a dict
paginated_questionnaire_answer_list_from_dict = PaginatedQuestionnaireAnswerList.from_dict(paginated_questionnaire_answer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


