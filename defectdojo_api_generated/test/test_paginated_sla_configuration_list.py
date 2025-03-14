# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.paginated_sla_configuration_list import PaginatedSLAConfigurationList

class TestPaginatedSLAConfigurationList(unittest.TestCase):
    """PaginatedSLAConfigurationList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedSLAConfigurationList:
        """Test PaginatedSLAConfigurationList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedSLAConfigurationList`
        """
        model = PaginatedSLAConfigurationList()
        if include_optional:
            return PaginatedSLAConfigurationList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    defectdojo_api_generated.models.sla_configuration.SLAConfiguration(
                        id = 56, 
                        name = '', 
                        description = '', 
                        critical = -2147483648, 
                        enforce_critical = True, 
                        high = -2147483648, 
                        enforce_high = True, 
                        medium = -2147483648, 
                        enforce_medium = True, 
                        low = -2147483648, 
                        enforce_low = True, )
                    ]
            )
        else:
            return PaginatedSLAConfigurationList(
                count = 123,
                results = [
                    defectdojo_api_generated.models.sla_configuration.SLAConfiguration(
                        id = 56, 
                        name = '', 
                        description = '', 
                        critical = -2147483648, 
                        enforce_critical = True, 
                        high = -2147483648, 
                        enforce_high = True, 
                        medium = -2147483648, 
                        enforce_medium = True, 
                        low = -2147483648, 
                        enforce_low = True, )
                    ],
        )
        """

    def testPaginatedSLAConfigurationList(self):
        """Test PaginatedSLAConfigurationList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
