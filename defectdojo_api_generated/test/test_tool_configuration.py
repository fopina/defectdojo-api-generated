# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.tool_configuration import ToolConfiguration

class TestToolConfiguration(unittest.TestCase):
    """ToolConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ToolConfiguration:
        """Test ToolConfiguration
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ToolConfiguration`
        """
        model = ToolConfiguration()
        if include_optional:
            return ToolConfiguration(
                id = 56,
                name = '',
                description = '',
                url = '',
                authentication_type = 'API',
                extras = '',
                username = '',
                auth_title = '',
                tool_type = 56,
                prefetch = defectdojo_api_generated.models.paginated_tool_configuration_list_prefetch.PaginatedToolConfigurationList_prefetch(
                    tool_type = {
                        'key' : defectdojo_api_generated.models.tool_type.ToolType(
                            id = 56, 
                            name = '', 
                            description = '', )
                        }, )
            )
        else:
            return ToolConfiguration(
                id = 56,
                name = '',
                tool_type = 56,
        )
        """

    def testToolConfiguration(self):
        """Test ToolConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
