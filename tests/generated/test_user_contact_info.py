# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.user_contact_info import UserContactInfo


class TestUserContactInfo(unittest.TestCase):
    """UserContactInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserContactInfo:
        """Test UserContactInfo
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `UserContactInfo`
        """
        model = UserContactInfo()
        if include_optional:
            return UserContactInfo(
                id = 56,
                user_profile = defectdojo_api_generated.models.user.User(
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
                        ], ),
                title = '',
                phone_number = '+10728880015280',
                cell_number = '+10728880015280',
                twitter_username = '',
                github_username = '',
                slack_username = '',
                slack_user_id = '',
                block_execution = True,
                force_password_reset = True,
                user = 56,
                prefetch = defectdojo_api_generated.models.paginated_user_contact_info_list_prefetch.PaginatedUserContactInfoList_prefetch(
                    user = {
                        'key' : defectdojo_api_generated.models.user_stub.UserStub(
                            id = 56, 
                            username = 'A', 
                            first_name = '', 
                            last_name = '', )
                        }, )
            )
        else:
            return UserContactInfo(
                id = 56,
                user_profile = defectdojo_api_generated.models.user.User(
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
                        ], ),
                user = 56,
        )
        """

    def testUserContactInfo(self):
        """Test UserContactInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
