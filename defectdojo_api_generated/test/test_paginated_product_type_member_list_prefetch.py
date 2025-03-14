# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.paginated_product_type_member_list_prefetch import PaginatedProductTypeMemberListPrefetch

class TestPaginatedProductTypeMemberListPrefetch(unittest.TestCase):
    """PaginatedProductTypeMemberListPrefetch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedProductTypeMemberListPrefetch:
        """Test PaginatedProductTypeMemberListPrefetch
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedProductTypeMemberListPrefetch`
        """
        model = PaginatedProductTypeMemberListPrefetch()
        if include_optional:
            return PaginatedProductTypeMemberListPrefetch(
                product_type = {
                    'key' : defectdojo_api_generated.models.product_type.ProductType(
                        id = 56, 
                        name = '', 
                        description = '', 
                        critical_product = True, 
                        key_product = True, 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        members = [
                            56
                            ], 
                        authorization_groups = [
                            56
                            ], 
                        prefetch = defectdojo_api_generated.models.paginated_product_type_list_prefetch.PaginatedProductTypeList_prefetch(), )
                    },
                role = {
                    'key' : defectdojo_api_generated.models.role.Role(
                        id = 56, 
                        name = '', 
                        is_owner = True, )
                    },
                user = {
                    'key' : defectdojo_api_generated.models.user_stub.UserStub(
                        id = 56, 
                        username = 'A', 
                        first_name = '', 
                        last_name = '', )
                    }
            )
        else:
            return PaginatedProductTypeMemberListPrefetch(
        )
        """

    def testPaginatedProductTypeMemberListPrefetch(self):
        """Test PaginatedProductTypeMemberListPrefetch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
