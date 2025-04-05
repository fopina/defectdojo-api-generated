# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.dojo_group_member_prefetch import DojoGroupMemberPrefetch


class TestDojoGroupMemberPrefetch(unittest.TestCase):
    """DojoGroupMemberPrefetch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DojoGroupMemberPrefetch:
        """Test DojoGroupMemberPrefetch
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `DojoGroupMemberPrefetch`
        """
        model = DojoGroupMemberPrefetch()
        if include_optional:
            return DojoGroupMemberPrefetch(
                group = {
                    'key' : defectdojo_api_generated.models.dojo_group.DojoGroup(
                        id = 56, 
                        configuration_permissions = [
                            56
                            ], 
                        name = '', 
                        description = '', 
                        social_provider = 'AzureAD', 
                        users = [
                            56
                            ], 
                        prefetch = defectdojo_api_generated.models.dojo_group_prefetch.DojoGroup_prefetch(
                            product_groups = {
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
                            product_type_groups = {
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
                                }, ), )
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
            return DojoGroupMemberPrefetch(
        )
        """

    def testDojoGroupMemberPrefetch(self):
        """Test DojoGroupMemberPrefetch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
