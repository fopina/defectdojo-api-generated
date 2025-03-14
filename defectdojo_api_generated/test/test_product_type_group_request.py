# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.product_type_group_request import ProductTypeGroupRequest

class TestProductTypeGroupRequest(unittest.TestCase):
    """ProductTypeGroupRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductTypeGroupRequest:
        """Test ProductTypeGroupRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductTypeGroupRequest`
        """
        model = ProductTypeGroupRequest()
        if include_optional:
            return ProductTypeGroupRequest(
                product_type = 56,
                group = 56,
                role = 56
            )
        else:
            return ProductTypeGroupRequest(
                product_type = 56,
                group = 56,
                role = 56,
        )
        """

    def testProductTypeGroupRequest(self):
        """Test ProductTypeGroupRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
