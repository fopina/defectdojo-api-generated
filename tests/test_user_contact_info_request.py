# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

The version of the OpenAPI document: 2.44.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.user_contact_info_request import UserContactInfoRequest


class TestUserContactInfoRequest(unittest.TestCase):
    """UserContactInfoRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserContactInfoRequest:
        """Test UserContactInfoRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `UserContactInfoRequest`
        """
        model = UserContactInfoRequest()
        if include_optional:
            return UserContactInfoRequest(
                title = '',
                phone_number = '+10728880015280',
                cell_number = '+10728880015280',
                twitter_username = '',
                github_username = '',
                slack_username = '',
                slack_user_id = '',
                block_execution = True,
                force_password_reset = True,
                user = 56
            )
        else:
            return UserContactInfoRequest(
                user = 56,
        )
        """

    def testUserContactInfoRequest(self):
        """Test UserContactInfoRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
