# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.language_type import LanguageType

class TestLanguageType(unittest.TestCase):
    """LanguageType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LanguageType:
        """Test LanguageType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LanguageType`
        """
        model = LanguageType()
        if include_optional:
            return LanguageType(
                id = 56,
                language = '',
                color = ''
            )
        else:
            return LanguageType(
                id = 56,
                language = '',
        )
        """

    def testLanguageType(self):
        """Test LanguageType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
