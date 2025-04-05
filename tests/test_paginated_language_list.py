# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.paginated_language_list import PaginatedLanguageList


class TestPaginatedLanguageList(unittest.TestCase):
    """PaginatedLanguageList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedLanguageList:
        """Test PaginatedLanguageList
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PaginatedLanguageList`
        """
        model = PaginatedLanguageList()
        if include_optional:
            return PaginatedLanguageList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    defectdojo_api_generated.models.language.Language(
                        id = 56, 
                        files = -2147483648, 
                        blank = -2147483648, 
                        comment = -2147483648, 
                        code = -2147483648, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        language = 56, 
                        product = 56, 
                        user = 56, 
                        prefetch = defectdojo_api_generated.models.language_prefetch.Language_prefetch(
                            language = {
                                'key' : defectdojo_api_generated.models.language_type.LanguageType(
                                    id = 56, 
                                    language = '', 
                                    color = '', )
                                }, 
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
                            user = {
                                'key' : defectdojo_api_generated.models.user_stub.UserStub(
                                    id = 56, 
                                    username = 'A', 
                                    first_name = '', 
                                    last_name = '', )
                                }, ), )
                    ],
                prefetch = defectdojo_api_generated.models.language_prefetch.Language_prefetch(
                    language = {
                        'key' : defectdojo_api_generated.models.language_type.LanguageType(
                            id = 56, 
                            language = '', 
                            color = '', )
                        }, 
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
                                ], 
                            prefetch = defectdojo_api_generated.models.paginated_product_list_prefetch.PaginatedProductList_prefetch(
                                prod_type = {
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
                                product_manager = {
                                    'key' : defectdojo_api_generated.models.user_stub.UserStub(
                                        id = 56, 
                                        username = 'A', 
                                        first_name = '', 
                                        last_name = '', )
                                    }, 
                                sla_configuration = {
                                    'key' : defectdojo_api_generated.models.sla_configuration.SLAConfiguration(
                                        id = 56, 
                                        name = '', 
                                        description = '', 
                                        critical = -2147483648, 
                                        enforce_critical = True, 
                                        high = -2147483648, 
                                        enforce_high = True, 
                                        medium = -2147483648, 
                                        enforce_medium = True, 
                                        low = -2147483648, 
                                        enforce_low = True, )
                                    }, 
                                team_manager = {
                                    'key' : defectdojo_api_generated.models.user_stub.UserStub(
                                        id = 56, 
                                        username = 'A', 
                                        first_name = '', 
                                        last_name = '', )
                                    }, 
                                technical_contact = {
                                    'key' : 
                                    }, ), )
                        }, 
                    user = {
                        'key' : 
                        }, )
            )
        else:
            return PaginatedLanguageList(
                count = 123,
                results = [
                    defectdojo_api_generated.models.language.Language(
                        id = 56, 
                        files = -2147483648, 
                        blank = -2147483648, 
                        comment = -2147483648, 
                        code = -2147483648, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        language = 56, 
                        product = 56, 
                        user = 56, 
                        prefetch = defectdojo_api_generated.models.language_prefetch.Language_prefetch(
                            language = {
                                'key' : defectdojo_api_generated.models.language_type.LanguageType(
                                    id = 56, 
                                    language = '', 
                                    color = '', )
                                }, 
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
                            user = {
                                'key' : defectdojo_api_generated.models.user_stub.UserStub(
                                    id = 56, 
                                    username = 'A', 
                                    first_name = '', 
                                    last_name = '', )
                                }, ), )
                    ],
        )
        """

    def testPaginatedLanguageList(self):
        """Test PaginatedLanguageList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
