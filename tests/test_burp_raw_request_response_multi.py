# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

The version of the OpenAPI document: 2.44.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.burp_raw_request_response_multi import BurpRawRequestResponseMulti


class TestBurpRawRequestResponseMulti(unittest.TestCase):
    """BurpRawRequestResponseMulti unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BurpRawRequestResponseMulti:
        """Test BurpRawRequestResponseMulti
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `BurpRawRequestResponseMulti`
        """
        model = BurpRawRequestResponseMulti()
        if include_optional:
            return BurpRawRequestResponseMulti(
                id = 56,
                burp_request_base64 = '',
                burp_response_base64 = '',
                finding = 56
            )
        else:
            return BurpRawRequestResponseMulti(
                id = 56,
                burp_request_base64 = '',
                burp_response_base64 = '',
        )
        """

    def testBurpRawRequestResponseMulti(self):
        """Test BurpRawRequestResponseMulti"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
