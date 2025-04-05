# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.patched_tool_product_settings_request import PatchedToolProductSettingsRequest


class TestPatchedToolProductSettingsRequest(unittest.TestCase):
    """PatchedToolProductSettingsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedToolProductSettingsRequest:
        """Test PatchedToolProductSettingsRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PatchedToolProductSettingsRequest`
        """
        model = PatchedToolProductSettingsRequest()
        if include_optional:
            return PatchedToolProductSettingsRequest(
                setting_url = '0',
                product = 56,
                name = '0',
                description = '',
                url = '',
                tool_project_id = '',
                tool_configuration = 56
            )
        else:
            return PatchedToolProductSettingsRequest(
        )
        """

    def testPatchedToolProductSettingsRequest(self):
        """Test PatchedToolProductSettingsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
