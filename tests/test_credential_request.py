# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.credential_request import CredentialRequest


class TestCredentialRequest(unittest.TestCase):
    """CredentialRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CredentialRequest:
        """Test CredentialRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CredentialRequest`
        """
        model = CredentialRequest()
        if include_optional:
            return CredentialRequest(
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
            return CredentialRequest(
                name = '0',
                username = '0',
                role = '0',
                url = '0',
                environment = 56,
        )
        """

    def testCredentialRequest(self):
        """Test CredentialRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
