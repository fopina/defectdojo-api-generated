# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.regulation_request import RegulationRequest

class TestRegulationRequest(unittest.TestCase):
    """RegulationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RegulationRequest:
        """Test RegulationRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RegulationRequest`
        """
        model = RegulationRequest()
        if include_optional:
            return RegulationRequest(
                name = '0',
                acronym = '0',
                category = 'privacy',
                jurisdiction = '0',
                description = '',
                reference = ''
            )
        else:
            return RegulationRequest(
                name = '0',
                acronym = '0',
                category = 'privacy',
                jurisdiction = '0',
        )
        """

    def testRegulationRequest(self):
        """Test RegulationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
