# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.paginated_questionnaire_engagement_survey_list import PaginatedQuestionnaireEngagementSurveyList

class TestPaginatedQuestionnaireEngagementSurveyList(unittest.TestCase):
    """PaginatedQuestionnaireEngagementSurveyList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedQuestionnaireEngagementSurveyList:
        """Test PaginatedQuestionnaireEngagementSurveyList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedQuestionnaireEngagementSurveyList`
        """
        model = PaginatedQuestionnaireEngagementSurveyList()
        if include_optional:
            return PaginatedQuestionnaireEngagementSurveyList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    defectdojo_api_generated.models.questionnaire_engagement_survey.QuestionnaireEngagementSurvey(
                        id = 56, 
                        questions = [
                            ''
                            ], 
                        name = '', 
                        description = '', 
                        active = True, )
                    ]
            )
        else:
            return PaginatedQuestionnaireEngagementSurveyList(
                count = 123,
                results = [
                    defectdojo_api_generated.models.questionnaire_engagement_survey.QuestionnaireEngagementSurvey(
                        id = 56, 
                        questions = [
                            ''
                            ], 
                        name = '', 
                        description = '', 
                        active = True, )
                    ],
        )
        """

    def testPaginatedQuestionnaireEngagementSurveyList(self):
        """Test PaginatedQuestionnaireEngagementSurveyList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
