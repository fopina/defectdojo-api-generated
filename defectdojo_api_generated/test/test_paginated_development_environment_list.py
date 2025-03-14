# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.paginated_development_environment_list import PaginatedDevelopmentEnvironmentList

class TestPaginatedDevelopmentEnvironmentList(unittest.TestCase):
    """PaginatedDevelopmentEnvironmentList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedDevelopmentEnvironmentList:
        """Test PaginatedDevelopmentEnvironmentList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedDevelopmentEnvironmentList`
        """
        model = PaginatedDevelopmentEnvironmentList()
        if include_optional:
            return PaginatedDevelopmentEnvironmentList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    defectdojo_api_generated.models.development_environment.DevelopmentEnvironment(
                        id = 56, 
                        name = '', )
                    ]
            )
        else:
            return PaginatedDevelopmentEnvironmentList(
                count = 123,
                results = [
                    defectdojo_api_generated.models.development_environment.DevelopmentEnvironment(
                        id = 56, 
                        name = '', )
                    ],
        )
        """

    def testPaginatedDevelopmentEnvironmentList(self):
        """Test PaginatedDevelopmentEnvironmentList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
