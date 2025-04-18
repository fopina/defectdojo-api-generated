# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.finding_engagement import FindingEngagement


class TestFindingEngagement(unittest.TestCase):
    """FindingEngagement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FindingEngagement:
        """Test FindingEngagement
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `FindingEngagement`
        """
        model = FindingEngagement()
        if include_optional:
            return FindingEngagement(
                id = 56,
                name = '',
                description = '',
                product = defectdojo_api_generated.models.finding_product.FindingProduct(
                    id = 56, 
                    name = '', 
                    prod_type = defectdojo_api_generated.models.finding_prod_type.FindingProdType(
                        id = 56, 
                        name = '', ), ),
                target_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                target_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                branch_tag = '',
                engagement_type = 'Interactive',
                build_id = '',
                commit_hash = '',
                version = '',
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return FindingEngagement(
                id = 56,
                target_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                target_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testFindingEngagement(self):
        """Test FindingEngagement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
