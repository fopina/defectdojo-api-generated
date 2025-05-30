# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.patched_sonarqube_issue_transition_request import (
    PatchedSonarqubeIssueTransitionRequest,
)


class TestPatchedSonarqubeIssueTransitionRequest(unittest.TestCase):
    """PatchedSonarqubeIssueTransitionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedSonarqubeIssueTransitionRequest:
        """Test PatchedSonarqubeIssueTransitionRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PatchedSonarqubeIssueTransitionRequest`
        """
        model = PatchedSonarqubeIssueTransitionRequest()
        if include_optional:
            return PatchedSonarqubeIssueTransitionRequest(
                finding_status = '0',
                sonarqube_status = '0',
                transitions = '0',
                sonarqube_issue = 56
            )
        else:
            return PatchedSonarqubeIssueTransitionRequest(
        )
        """

    def testPatchedSonarqubeIssueTransitionRequest(self):
        """Test PatchedSonarqubeIssueTransitionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
