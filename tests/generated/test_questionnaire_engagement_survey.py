# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.questionnaire_engagement_survey import QuestionnaireEngagementSurvey


class TestQuestionnaireEngagementSurvey(unittest.TestCase):
    """QuestionnaireEngagementSurvey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuestionnaireEngagementSurvey:
        """Test QuestionnaireEngagementSurvey
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `QuestionnaireEngagementSurvey`
        """
        model = QuestionnaireEngagementSurvey()
        if include_optional:
            return QuestionnaireEngagementSurvey(
                id = 56,
                questions = [
                    ''
                    ],
                name = '',
                description = '',
                active = True
            )
        else:
            return QuestionnaireEngagementSurvey(
                id = 56,
                questions = [
                    ''
                    ],
        )
        """

    def testQuestionnaireEngagementSurvey(self):
        """Test QuestionnaireEngagementSurvey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
