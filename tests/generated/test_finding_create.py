# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.finding_create import FindingCreate


class TestFindingCreate(unittest.TestCase):
    """FindingCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FindingCreate:
        """Test FindingCreate
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `FindingCreate`
        """
        model = FindingCreate()
        if include_optional:
            return FindingCreate(
                id = 56,
                notes = [
                    56
                    ],
                test = 56,
                thread_id = 56,
                found_by = [
                    56
                    ],
                url = '',
                tags = [
                    ''
                    ],
                push_to_jira = True,
                vulnerability_ids = [
                    defectdojo_api_generated.models.vulnerability_id.VulnerabilityId(
                        vulnerability_id = '', )
                    ],
                reporter = 56,
                title = '',
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                sla_start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                sla_expiration_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                cwe = -2147483648,
                epss_score = 0.0,
                epss_percentile = 0.0,
                cvssv3 = 'PR:U',
                cvssv3_score = 0.0,
                severity = '',
                description = '',
                mitigation = '',
                impact = '',
                steps_to_reproduce = '',
                severity_justification = '',
                references = '',
                active = True,
                verified = True,
                false_p = True,
                duplicate = True,
                out_of_scope = True,
                risk_accepted = True,
                under_review = True,
                last_status_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                under_defect_review = True,
                is_mitigated = True,
                mitigated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                numerical_severity = '',
                last_reviewed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                param = '',
                payload = '',
                hash_code = '',
                line = -2147483648,
                file_path = '',
                component_name = '',
                component_version = '',
                static_finding = True,
                dynamic_finding = True,
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                scanner_confidence = 56,
                unique_id_from_tool = '',
                vuln_id_from_tool = '',
                sast_source_object = '',
                sast_sink_object = '',
                sast_source_line = -2147483648,
                sast_source_file_path = '',
                nb_occurences = -2147483648,
                publish_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                service = '',
                planned_remediation_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                planned_remediation_version = '',
                effort_for_fixing = '',
                duplicate_finding = 56,
                review_requested_by = 56,
                defect_review_requested_by = 56,
                mitigated_by = 56,
                last_reviewed_by = 56,
                sonarqube_issue = 56,
                endpoints = [
                    56
                    ],
                reviewers = [
                    56
                    ],
                files = [
                    56
                    ]
            )
        else:
            return FindingCreate(
                id = 56,
                notes = [
                    56
                    ],
                test = 56,
                found_by = [
                    56
                    ],
                title = '',
                severity = '',
                description = '',
                active = True,
                verified = True,
                last_status_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                mitigated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                numerical_severity = '',
                last_reviewed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                param = '',
                payload = '',
                hash_code = '',
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                scanner_confidence = 56,
                duplicate_finding = 56,
                mitigated_by = 56,
                last_reviewed_by = 56,
                endpoints = [
                    56
                    ],
                files = [
                    56
                    ],
        )
        """

    def testFindingCreate(self):
        """Test FindingCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
