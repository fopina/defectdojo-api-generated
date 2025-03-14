# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.patched_endpoint_status_request import PatchedEndpointStatusRequest

class TestPatchedEndpointStatusRequest(unittest.TestCase):
    """PatchedEndpointStatusRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedEndpointStatusRequest:
        """Test PatchedEndpointStatusRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedEndpointStatusRequest`
        """
        model = PatchedEndpointStatusRequest()
        if include_optional:
            return PatchedEndpointStatusRequest(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                mitigated = True,
                false_positive = True,
                out_of_scope = True,
                risk_accepted = True,
                mitigated_by = 56,
                endpoint = 56,
                finding = 56
            )
        else:
            return PatchedEndpointStatusRequest(
        )
        """

    def testPatchedEndpointStatusRequest(self):
        """Test PatchedEndpointStatusRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
