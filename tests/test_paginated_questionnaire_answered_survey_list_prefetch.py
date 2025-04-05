# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.paginated_questionnaire_answered_survey_list_prefetch import (
    PaginatedQuestionnaireAnsweredSurveyListPrefetch,
)


class TestPaginatedQuestionnaireAnsweredSurveyListPrefetch(unittest.TestCase):
    """PaginatedQuestionnaireAnsweredSurveyListPrefetch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedQuestionnaireAnsweredSurveyListPrefetch:
        """Test PaginatedQuestionnaireAnsweredSurveyListPrefetch
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PaginatedQuestionnaireAnsweredSurveyListPrefetch`
        """
        model = PaginatedQuestionnaireAnsweredSurveyListPrefetch()
        if include_optional:
            return PaginatedQuestionnaireAnsweredSurveyListPrefetch(
                assignee = {
                    'key' : defectdojo_api_generated.models.user_stub.UserStub(
                        id = 56, 
                        username = 'A', 
                        first_name = '', 
                        last_name = '', )
                    },
                engagement = {
                    'key' : defectdojo_api_generated.models.finding_engagement.FindingEngagement(
                        id = 56, 
                        name = '', 
                        description = '', 
                        product = defectdojo_api_generated.models.finding_product.FindingProduct(
                            id = 56, 
                            name = '', 
                            prod_type = defectdojo_api_generated.models.finding_prod_type.FindingProdType(
                                id = 56, 
                                name = '', ), ), 
                        target_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        target_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        branch_tag = '', 
                        engagement_type = 'Interactive', 
                        build_id = '', 
                        commit_hash = '', 
                        version = '', 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    },
                responder = {
                    'key' : defectdojo_api_generated.models.user_stub.UserStub(
                        id = 56, 
                        username = 'A', 
                        first_name = '', 
                        last_name = '', )
                    },
                survey = {
                    'key' : defectdojo_api_generated.models.questionnaire_engagement_survey.QuestionnaireEngagementSurvey(
                        id = 56, 
                        questions = [
                            ''
                            ], 
                        name = '', 
                        description = '', 
                        active = True, )
                    }
            )
        else:
            return PaginatedQuestionnaireAnsweredSurveyListPrefetch(
        )
        """

    def testPaginatedQuestionnaireAnsweredSurveyListPrefetch(self):
        """Test PaginatedQuestionnaireAnsweredSurveyListPrefetch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
