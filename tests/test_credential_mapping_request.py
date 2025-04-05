# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.credential_mapping_request import CredentialMappingRequest


class TestCredentialMappingRequest(unittest.TestCase):
    """CredentialMappingRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CredentialMappingRequest:
        """Test CredentialMappingRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CredentialMappingRequest`
        """
        model = CredentialMappingRequest()
        if include_optional:
            return CredentialMappingRequest(
                is_authn_provider = True,
                url = '',
                cred_id = 56,
                product = 56,
                finding = 56,
                engagement = 56,
                test = 56
            )
        else:
            return CredentialMappingRequest(
                cred_id = 56,
        )
        """

    def testCredentialMappingRequest(self):
        """Test CredentialMappingRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
