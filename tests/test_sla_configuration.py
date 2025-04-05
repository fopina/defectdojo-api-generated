# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.sla_configuration import SLAConfiguration


class TestSLAConfiguration(unittest.TestCase):
    """SLAConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SLAConfiguration:
        """Test SLAConfiguration
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SLAConfiguration`
        """
        model = SLAConfiguration()
        if include_optional:
            return SLAConfiguration(
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
                enforce_low = True
            )
        else:
            return SLAConfiguration(
                id = 56,
                name = '',
        )
        """

    def testSLAConfiguration(self):
        """Test SLAConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
