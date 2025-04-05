# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.patched_jira_issue_request import PatchedJIRAIssueRequest


class TestPatchedJIRAIssueRequest(unittest.TestCase):
    """PatchedJIRAIssueRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedJIRAIssueRequest:
        """Test PatchedJIRAIssueRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PatchedJIRAIssueRequest`
        """
        model = PatchedJIRAIssueRequest()
        if include_optional:
            return PatchedJIRAIssueRequest(
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
            return PatchedJIRAIssueRequest(
        )
        """

    def testPatchedJIRAIssueRequest(self):
        """Test PatchedJIRAIssueRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
