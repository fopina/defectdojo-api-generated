# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

The version of the OpenAPI document: 2.44.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.patched_endpoint_request import PatchedEndpointRequest


class TestPatchedEndpointRequest(unittest.TestCase):
    """PatchedEndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedEndpointRequest:
        """Test PatchedEndpointRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PatchedEndpointRequest`
        """
        model = PatchedEndpointRequest()
        if include_optional:
            return PatchedEndpointRequest(
                tags = [
                    '0'
                    ],
                protocol = '',
                userinfo = '',
                host = '',
                port = -2147483648,
                path = '',
                query = '',
                fragment = '',
                product = 56
            )
        else:
            return PatchedEndpointRequest(
        )
        """

    def testPatchedEndpointRequest(self):
        """Test PatchedEndpointRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
