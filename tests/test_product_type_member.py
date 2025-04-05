# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.product_type_member import ProductTypeMember


class TestProductTypeMember(unittest.TestCase):
    """ProductTypeMember unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductTypeMember:
        """Test ProductTypeMember
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ProductTypeMember`
        """
        model = ProductTypeMember()
        if include_optional:
            return ProductTypeMember(
                id = 56,
                product_type = 56,
                user = 56,
                role = 56,
                prefetch = defectdojo_api_generated.models.paginated_product_type_member_list_prefetch.PaginatedProductTypeMemberList_prefetch(
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
                                ], )
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
                        }, )
            )
        else:
            return ProductTypeMember(
                id = 56,
                product_type = 56,
                user = 56,
                role = 56,
        )
        """

    def testProductTypeMember(self):
        """Test ProductTypeMember"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
