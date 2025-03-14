# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.product_api_scan_configuration import ProductAPIScanConfiguration

class TestProductAPIScanConfiguration(unittest.TestCase):
    """ProductAPIScanConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductAPIScanConfiguration:
        """Test ProductAPIScanConfiguration
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductAPIScanConfiguration`
        """
        model = ProductAPIScanConfiguration()
        if include_optional:
            return ProductAPIScanConfiguration(
                id = 56,
                service_key_1 = '',
                service_key_2 = '',
                service_key_3 = '',
                product = 56,
                tool_configuration = 56,
                prefetch = defectdojo_api_generated.models.paginated_product_api_scan_configuration_list_prefetch.PaginatedProductAPIScanConfigurationList_prefetch(
                    product = {
                        'key' : defectdojo_api_generated.models.product.Product(
                            id = 56, 
                            findings_count = 56, 
                            findings_list = [
                                56
                                ], 
                            tags = [
                                ''
                                ], 
                            product_meta = [
                                defectdojo_api_generated.models.product_meta.ProductMeta(
                                    name = '', 
                                    value = '', )
                                ], 
                            name = '', 
                            description = '', 
                            created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
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
                            members = [
                                56
                                ], 
                            authorization_groups = [
                                56
                                ], 
                            regulations = [
                                56
                                ], )
                        }, 
                    tool_configuration = {
                        'key' : defectdojo_api_generated.models.tool_configuration.ToolConfiguration(
                            id = 56, 
                            name = '', 
                            description = '', 
                            url = '', 
                            authentication_type = 'API', 
                            extras = '', 
                            username = '', 
                            auth_title = '', 
                            tool_type = 56, )
                        }, )
            )
        else:
            return ProductAPIScanConfiguration(
                id = 56,
                product = 56,
                tool_configuration = 56,
        )
        """

    def testProductAPIScanConfiguration(self):
        """Test ProductAPIScanConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
