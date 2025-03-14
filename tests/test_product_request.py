# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

The version of the OpenAPI document: 2.44.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.product_request import ProductRequest


class TestProductRequest(unittest.TestCase):
    """ProductRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductRequest:
        """Test ProductRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ProductRequest`
        """
        model = ProductRequest()
        if include_optional:
            return ProductRequest(
                tags = [
                    '0'
                    ],
                name = '0',
                description = '0',
                prod_numeric_grade = -2147483648,
                business_criticality = 'very high',
                platform = 'web service',
                lifecycle = 'construction',
                origin = 'third party library',
                user_records = 0,
                revenue = '-8072888001.',
                external_audience = True,
                internet_accessible = True,
                enable_product_tag_inheritance = True,
                enable_simple_risk_acceptance = True,
                enable_full_risk_acceptance = True,
                disable_sla_breach_notifications = True,
                product_manager = 56,
                technical_contact = 56,
                team_manager = 56,
                prod_type = 56,
                sla_configuration = 56,
                regulations = [
                    56
                    ]
            )
        else:
            return ProductRequest(
                name = '0',
                description = '0',
                prod_type = 56,
        )
        """

    def testProductRequest(self):
        """Test ProductRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
