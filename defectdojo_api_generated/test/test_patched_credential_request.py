# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.patched_credential_request import PatchedCredentialRequest

class TestPatchedCredentialRequest(unittest.TestCase):
    """PatchedCredentialRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedCredentialRequest:
        """Test PatchedCredentialRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedCredentialRequest`
        """
        model = PatchedCredentialRequest()
        if include_optional:
            return PatchedCredentialRequest(
                name = '0',
                username = '0',
                role = '0',
                authentication = 'Form',
                http_authentication = 'Basic',
                description = '',
                url = '0',
                login_regex = '',
                logout_regex = '',
                is_valid = True,
                environment = 56
            )
        else:
            return PatchedCredentialRequest(
        )
        """

    def testPatchedCredentialRequest(self):
        """Test PatchedCredentialRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
