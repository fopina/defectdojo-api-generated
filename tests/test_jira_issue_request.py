# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.jira_issue_request import JIRAIssueRequest


class TestJIRAIssueRequest(unittest.TestCase):
    """JIRAIssueRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JIRAIssueRequest:
        """Test JIRAIssueRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `JIRAIssueRequest`
        """
        model = JIRAIssueRequest()
        if include_optional:
            return JIRAIssueRequest(
                jira_id = '0',
                jira_key = '0',
                jira_creation = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                jira_change = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                jira_project = 56,
                finding = 56,
                engagement = 56,
                finding_group = 56
            )
        else:
            return JIRAIssueRequest(
                jira_id = '0',
                jira_key = '0',
        )
        """

    def testJIRAIssueRequest(self):
        """Test JIRAIssueRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
