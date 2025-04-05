# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.patched_language_type_request import PatchedLanguageTypeRequest


class TestPatchedLanguageTypeRequest(unittest.TestCase):
    """PatchedLanguageTypeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedLanguageTypeRequest:
        """Test PatchedLanguageTypeRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PatchedLanguageTypeRequest`
        """
        model = PatchedLanguageTypeRequest()
        if include_optional:
            return PatchedLanguageTypeRequest(
                language = '0',
                color = ''
            )
        else:
            return PatchedLanguageTypeRequest(
        )
        """

    def testPatchedLanguageTypeRequest(self):
        """Test PatchedLanguageTypeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
