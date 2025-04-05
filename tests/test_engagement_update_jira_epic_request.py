# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.engagement_update_jira_epic_request import EngagementUpdateJiraEpicRequest


class TestEngagementUpdateJiraEpicRequest(unittest.TestCase):
    """EngagementUpdateJiraEpicRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EngagementUpdateJiraEpicRequest:
        """Test EngagementUpdateJiraEpicRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EngagementUpdateJiraEpicRequest`
        """
        model = EngagementUpdateJiraEpicRequest()
        if include_optional:
            return EngagementUpdateJiraEpicRequest(
                epic_name = '0',
                epic_priority = '0'
            )
        else:
            return EngagementUpdateJiraEpicRequest(
        )
        """

    def testEngagementUpdateJiraEpicRequest(self):
        """Test EngagementUpdateJiraEpicRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
