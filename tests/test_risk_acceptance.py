# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.risk_acceptance import RiskAcceptance


class TestRiskAcceptance(unittest.TestCase):
    """RiskAcceptance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RiskAcceptance:
        """Test RiskAcceptance
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `RiskAcceptance`
        """
        model = RiskAcceptance()
        if include_optional:
            return RiskAcceptance(
                id = 56,
                recommendation = '',
                decision = '',
                path = '',
                name = '',
                recommendation_details = '',
                decision_details = '',
                accepted_by = '',
                expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expiration_date_warned = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expiration_date_handled = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                reactivate_expired = True,
                restart_sla_expired = True,
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                owner = 56,
                accepted_findings = [
                    56
                    ],
                notes = [
                    56
                    ]
            )
        else:
            return RiskAcceptance(
                id = 56,
                recommendation = '',
                decision = '',
                path = '',
                name = '',
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                owner = 56,
                accepted_findings = [
                    56
                    ],
                notes = [
                    56
                    ],
        )
        """

    def testRiskAcceptance(self):
        """Test RiskAcceptance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
