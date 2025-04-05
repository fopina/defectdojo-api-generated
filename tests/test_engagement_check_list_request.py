# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.engagement_check_list_request import EngagementCheckListRequest


class TestEngagementCheckListRequest(unittest.TestCase):
    """EngagementCheckListRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EngagementCheckListRequest:
        """Test EngagementCheckListRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EngagementCheckListRequest`
        """
        model = EngagementCheckListRequest()
        if include_optional:
            return EngagementCheckListRequest(
                session_management = '0',
                encryption_crypto = '0',
                configuration_management = '0',
                authentication = '0',
                authorization_and_access_control = '0',
                data_input_sanitization_validation = '0',
                sensitive_data = '0',
                other = '0',
                session_issues = [
                    56
                    ],
                crypto_issues = [
                    56
                    ],
                config_issues = [
                    56
                    ],
                auth_issues = [
                    56
                    ],
                author_issues = [
                    56
                    ],
                data_issues = [
                    56
                    ],
                sensitive_issues = [
                    56
                    ],
                other_issues = [
                    56
                    ]
            )
        else:
            return EngagementCheckListRequest(
        )
        """

    def testEngagementCheckListRequest(self):
        """Test EngagementCheckListRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
