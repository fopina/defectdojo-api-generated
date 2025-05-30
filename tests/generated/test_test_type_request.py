# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.test_type_request import TestTypeRequest


class TestTestTypeRequest(unittest.TestCase):
    """TestTypeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TestTypeRequest:
        """Test TestTypeRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TestTypeRequest`
        """
        model = TestTypeRequest()
        if include_optional:
            return TestTypeRequest(
                tags = [
                    '0'
                    ],
                name = '0',
                static_tool = True,
                dynamic_tool = True,
                active = True
            )
        else:
            return TestTypeRequest(
                name = '0',
        )
        """

    def testTestTypeRequest(self):
        """Test TestTypeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
