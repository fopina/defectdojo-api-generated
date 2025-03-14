# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.paginated_credential_mapping_list import PaginatedCredentialMappingList

class TestPaginatedCredentialMappingList(unittest.TestCase):
    """PaginatedCredentialMappingList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedCredentialMappingList:
        """Test PaginatedCredentialMappingList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedCredentialMappingList`
        """
        model = PaginatedCredentialMappingList()
        if include_optional:
            return PaginatedCredentialMappingList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    defectdojo_api_generated.models.credential_mapping.CredentialMapping(
                        id = 56, 
                        is_authn_provider = True, 
                        url = '', 
                        cred_id = 56, 
                        product = 56, 
                        finding = 56, 
                        engagement = 56, 
                        test = 56, )
                    ]
            )
        else:
            return PaginatedCredentialMappingList(
                count = 123,
                results = [
                    defectdojo_api_generated.models.credential_mapping.CredentialMapping(
                        id = 56, 
                        is_authn_provider = True, 
                        url = '', 
                        cred_id = 56, 
                        product = 56, 
                        finding = 56, 
                        engagement = 56, 
                        test = 56, )
                    ],
        )
        """

    def testPaginatedCredentialMappingList(self):
        """Test PaginatedCredentialMappingList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
