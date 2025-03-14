# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.patched_engagement_request import PatchedEngagementRequest

class TestPatchedEngagementRequest(unittest.TestCase):
    """PatchedEngagementRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedEngagementRequest:
        """Test PatchedEngagementRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedEngagementRequest`
        """
        model = PatchedEngagementRequest()
        if include_optional:
            return PatchedEngagementRequest(
                tags = [
                    '0'
                    ],
                name = '',
                description = '',
                version = '',
                first_contacted = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                target_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                target_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                reason = '',
                tracker = '',
                test_strategy = '',
                threat_model = True,
                api_test = True,
                pen_test = True,
                check_list = True,
                status = 'Not Started',
                engagement_type = 'Interactive',
                build_id = '',
                commit_hash = '',
                branch_tag = '',
                source_code_management_uri = '',
                deduplication_on_engagement = True,
                lead = 56,
                requester = 56,
                preset = 56,
                report_type = 56,
                product = 56,
                build_server = 56,
                source_code_management_server = 56,
                orchestration_engine = 56
            )
        else:
            return PatchedEngagementRequest(
        )
        """

    def testPatchedEngagementRequest(self):
        """Test PatchedEngagementRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
