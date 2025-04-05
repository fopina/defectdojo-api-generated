# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.paginated_questionnaire_general_survey_list import (
    PaginatedQuestionnaireGeneralSurveyList,
)


class TestPaginatedQuestionnaireGeneralSurveyList(unittest.TestCase):
    """PaginatedQuestionnaireGeneralSurveyList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedQuestionnaireGeneralSurveyList:
        """Test PaginatedQuestionnaireGeneralSurveyList
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PaginatedQuestionnaireGeneralSurveyList`
        """
        model = PaginatedQuestionnaireGeneralSurveyList()
        if include_optional:
            return PaginatedQuestionnaireGeneralSurveyList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    defectdojo_api_generated.models.questionnaire_general_survey.QuestionnaireGeneralSurvey(
                        id = 56, 
                        survey = defectdojo_api_generated.models.questionnaire_engagement_survey.QuestionnaireEngagementSurvey(
                            id = 56, 
                            questions = [
                                ''
                                ], 
                            name = '', 
                            description = '', 
                            active = True, ), 
                        num_responses = -2147483648, 
                        generated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return PaginatedQuestionnaireGeneralSurveyList(
                count = 123,
                results = [
                    defectdojo_api_generated.models.questionnaire_general_survey.QuestionnaireGeneralSurvey(
                        id = 56, 
                        survey = defectdojo_api_generated.models.questionnaire_engagement_survey.QuestionnaireEngagementSurvey(
                            id = 56, 
                            questions = [
                                ''
                                ], 
                            name = '', 
                            description = '', 
                            active = True, ), 
                        num_responses = -2147483648, 
                        generated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testPaginatedQuestionnaireGeneralSurveyList(self):
        """Test PaginatedQuestionnaireGeneralSurveyList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
