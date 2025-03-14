# PaginatedQuestionnaireQuestionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[QuestionnaireQuestion]**](QuestionnaireQuestion.md) |  | 

## Example

```python
from defectdojo_api_generated.models.paginated_questionnaire_question_list import PaginatedQuestionnaireQuestionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedQuestionnaireQuestionList from a JSON string
paginated_questionnaire_question_list_instance = PaginatedQuestionnaireQuestionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedQuestionnaireQuestionList.to_json())

# convert the object into a dict
paginated_questionnaire_question_list_dict = paginated_questionnaire_question_list_instance.to_dict()
# create an instance of PaginatedQuestionnaireQuestionList from a dict
paginated_questionnaire_question_list_from_dict = PaginatedQuestionnaireQuestionList.from_dict(paginated_questionnaire_question_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


