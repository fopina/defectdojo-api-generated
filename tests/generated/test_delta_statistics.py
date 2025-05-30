# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.delta_statistics import DeltaStatistics


class TestDeltaStatistics(unittest.TestCase):
    """DeltaStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeltaStatistics:
        """Test DeltaStatistics
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `DeltaStatistics`
        """
        model = DeltaStatistics()
        if include_optional:
            return DeltaStatistics(
                created = defectdojo_api_generated.models.severity_status_statistics.SeverityStatusStatistics(
                    info = defectdojo_api_generated.models.status_statistics.StatusStatistics(
                        active = 56, 
                        verified = 56, 
                        duplicate = 56, 
                        false_p = 56, 
                        out_of_scope = 56, 
                        is_mitigated = 56, 
                        risk_accepted = 56, 
                        total = 56, ), 
                    low = defectdojo_api_generated.models.status_statistics.StatusStatistics(
                        active = 56, 
                        verified = 56, 
                        duplicate = 56, 
                        false_p = 56, 
                        out_of_scope = 56, 
                        is_mitigated = 56, 
                        risk_accepted = 56, 
                        total = 56, ), 
                    medium = , 
                    high = , 
                    critical = , 
                    total = , ),
                closed = defectdojo_api_generated.models.severity_status_statistics.SeverityStatusStatistics(
                    info = defectdojo_api_generated.models.status_statistics.StatusStatistics(
                        active = 56, 
                        verified = 56, 
                        duplicate = 56, 
                        false_p = 56, 
                        out_of_scope = 56, 
                        is_mitigated = 56, 
                        risk_accepted = 56, 
                        total = 56, ), 
                    low = defectdojo_api_generated.models.status_statistics.StatusStatistics(
                        active = 56, 
                        verified = 56, 
                        duplicate = 56, 
                        false_p = 56, 
                        out_of_scope = 56, 
                        is_mitigated = 56, 
                        risk_accepted = 56, 
                        total = 56, ), 
                    medium = , 
                    high = , 
                    critical = , 
                    total = , ),
                reactivated = defectdojo_api_generated.models.severity_status_statistics.SeverityStatusStatistics(
                    info = defectdojo_api_generated.models.status_statistics.StatusStatistics(
                        active = 56, 
                        verified = 56, 
                        duplicate = 56, 
                        false_p = 56, 
                        out_of_scope = 56, 
                        is_mitigated = 56, 
                        risk_accepted = 56, 
                        total = 56, ), 
                    low = defectdojo_api_generated.models.status_statistics.StatusStatistics(
                        active = 56, 
                        verified = 56, 
                        duplicate = 56, 
                        false_p = 56, 
                        out_of_scope = 56, 
                        is_mitigated = 56, 
                        risk_accepted = 56, 
                        total = 56, ), 
                    medium = , 
                    high = , 
                    critical = , 
                    total = , ),
                untouched = defectdojo_api_generated.models.severity_status_statistics.SeverityStatusStatistics(
                    info = defectdojo_api_generated.models.status_statistics.StatusStatistics(
                        active = 56, 
                        verified = 56, 
                        duplicate = 56, 
                        false_p = 56, 
                        out_of_scope = 56, 
                        is_mitigated = 56, 
                        risk_accepted = 56, 
                        total = 56, ), 
                    low = defectdojo_api_generated.models.status_statistics.StatusStatistics(
                        active = 56, 
                        verified = 56, 
                        duplicate = 56, 
                        false_p = 56, 
                        out_of_scope = 56, 
                        is_mitigated = 56, 
                        risk_accepted = 56, 
                        total = 56, ), 
                    medium = , 
                    high = , 
                    critical = , 
                    total = , )
            )
        else:
            return DeltaStatistics(
                created = defectdojo_api_generated.models.severity_status_statistics.SeverityStatusStatistics(
                    info = defectdojo_api_generated.models.status_statistics.StatusStatistics(
                        active = 56, 
                        verified = 56, 
                        duplicate = 56, 
                        false_p = 56, 
                        out_of_scope = 56, 
                        is_mitigated = 56, 
                        risk_accepted = 56, 
                        total = 56, ), 
                    low = defectdojo_api_generated.models.status_statistics.StatusStatistics(
                        active = 56, 
                        verified = 56, 
                        duplicate = 56, 
                        false_p = 56, 
                        out_of_scope = 56, 
                        is_mitigated = 56, 
                        risk_accepted = 56, 
                        total = 56, ), 
                    medium = , 
                    high = , 
                    critical = , 
                    total = , ),
                closed = defectdojo_api_generated.models.severity_status_statistics.SeverityStatusStatistics(
                    info = defectdojo_api_generated.models.status_statistics.StatusStatistics(
                        active = 56, 
                        verified = 56, 
                        duplicate = 56, 
                        false_p = 56, 
                        out_of_scope = 56, 
                        is_mitigated = 56, 
                        risk_accepted = 56, 
                        total = 56, ), 
                    low = defectdojo_api_generated.models.status_statistics.StatusStatistics(
                        active = 56, 
                        verified = 56, 
                        duplicate = 56, 
                        false_p = 56, 
                        out_of_scope = 56, 
                        is_mitigated = 56, 
                        risk_accepted = 56, 
                        total = 56, ), 
                    medium = , 
                    high = , 
                    critical = , 
                    total = , ),
                reactivated = defectdojo_api_generated.models.severity_status_statistics.SeverityStatusStatistics(
                    info = defectdojo_api_generated.models.status_statistics.StatusStatistics(
                        active = 56, 
                        verified = 56, 
                        duplicate = 56, 
                        false_p = 56, 
                        out_of_scope = 56, 
                        is_mitigated = 56, 
                        risk_accepted = 56, 
                        total = 56, ), 
                    low = defectdojo_api_generated.models.status_statistics.StatusStatistics(
                        active = 56, 
                        verified = 56, 
                        duplicate = 56, 
                        false_p = 56, 
                        out_of_scope = 56, 
                        is_mitigated = 56, 
                        risk_accepted = 56, 
                        total = 56, ), 
                    medium = , 
                    high = , 
                    critical = , 
                    total = , ),
                untouched = defectdojo_api_generated.models.severity_status_statistics.SeverityStatusStatistics(
                    info = defectdojo_api_generated.models.status_statistics.StatusStatistics(
                        active = 56, 
                        verified = 56, 
                        duplicate = 56, 
                        false_p = 56, 
                        out_of_scope = 56, 
                        is_mitigated = 56, 
                        risk_accepted = 56, 
                        total = 56, ), 
                    low = defectdojo_api_generated.models.status_statistics.StatusStatistics(
                        active = 56, 
                        verified = 56, 
                        duplicate = 56, 
                        false_p = 56, 
                        out_of_scope = 56, 
                        is_mitigated = 56, 
                        risk_accepted = 56, 
                        total = 56, ), 
                    medium = , 
                    high = , 
                    critical = , 
                    total = , ),
        )
        """

    def testDeltaStatistics(self):
        """Test DeltaStatistics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
