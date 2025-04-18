# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.engagement_presets_request import EngagementPresetsRequest


class TestEngagementPresetsRequest(unittest.TestCase):
    """EngagementPresetsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EngagementPresetsRequest:
        """Test EngagementPresetsRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EngagementPresetsRequest`
        """
        model = EngagementPresetsRequest()
        if include_optional:
            return EngagementPresetsRequest(
                title = '0',
                notes = '',
                scope = '',
                product = 56,
                test_type = [
                    56
                    ],
                network_locations = [
                    56
                    ]
            )
        else:
            return EngagementPresetsRequest(
                product = 56,
        )
        """

    def testEngagementPresetsRequest(self):
        """Test EngagementPresetsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
