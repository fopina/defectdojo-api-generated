# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.paginated_user_list import PaginatedUserList


class TestPaginatedUserList(unittest.TestCase):
    """PaginatedUserList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedUserList:
        """Test PaginatedUserList
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PaginatedUserList`
        """
        model = PaginatedUserList()
        if include_optional:
            return PaginatedUserList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    defectdojo_api_generated.models.user.User(
                        id = 56, 
                        username = 'A', 
                        first_name = '', 
                        last_name = '', 
                        email = '', 
                        date_joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_active = True, 
                        is_superuser = True, 
                        configuration_permissions = [
                            56
                            ], )
                    ]
            )
        else:
            return PaginatedUserList(
                count = 123,
                results = [
                    defectdojo_api_generated.models.user.User(
                        id = 56, 
                        username = 'A', 
                        first_name = '', 
                        last_name = '', 
                        email = '', 
                        date_joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_active = True, 
                        is_superuser = True, 
                        configuration_permissions = [
                            56
                            ], )
                    ],
        )
        """

    def testPaginatedUserList(self):
        """Test PaginatedUserList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
