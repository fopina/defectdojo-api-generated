# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.patched_test_request import PatchedTestRequest

class TestPatchedTestRequest(unittest.TestCase):
    """PatchedTestRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedTestRequest:
        """Test PatchedTestRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedTestRequest`
        """
        model = PatchedTestRequest()
        if include_optional:
            return PatchedTestRequest(
                tags = [
                    '0'
                    ],
                scan_type = '0',
                title = '',
                description = '',
                target_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                target_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                percent_complete = -2147483648,
                version = '',
                build_id = '',
                commit_hash = '',
                branch_tag = '',
                lead = 56,
                test_type = 56,
                environment = 56,
                api_scan_configuration = 56
            )
        else:
            return PatchedTestRequest(
        )
        """

    def testPatchedTestRequest(self):
        """Test PatchedTestRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
