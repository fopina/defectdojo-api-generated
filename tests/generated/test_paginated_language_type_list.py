# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.paginated_language_type_list import PaginatedLanguageTypeList


class TestPaginatedLanguageTypeList(unittest.TestCase):
    """PaginatedLanguageTypeList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedLanguageTypeList:
        """Test PaginatedLanguageTypeList
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PaginatedLanguageTypeList`
        """
        model = PaginatedLanguageTypeList()
        if include_optional:
            return PaginatedLanguageTypeList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    defectdojo_api_generated.models.language_type.LanguageType(
                        id = 56, 
                        language = '', 
                        color = '', )
                    ]
            )
        else:
            return PaginatedLanguageTypeList(
                count = 123,
                results = [
                    defectdojo_api_generated.models.language_type.LanguageType(
                        id = 56, 
                        language = '', 
                        color = '', )
                    ],
        )
        """

    def testPaginatedLanguageTypeList(self):
        """Test PaginatedLanguageTypeList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
