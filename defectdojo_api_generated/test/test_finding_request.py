# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.finding_request import FindingRequest

class TestFindingRequest(unittest.TestCase):
    """FindingRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FindingRequest:
        """Test FindingRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FindingRequest`
        """
        model = FindingRequest()
        if include_optional:
            return FindingRequest(
                tags = [
                    '0'
                    ],
                push_to_jira = True,
                vulnerability_ids = [
                    defectdojo_api_generated.models.vulnerability_id_request.VulnerabilityIdRequest(
                        vulnerability_id = '0', )
                    ],
                reporter = 56,
                title = '0',
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                sla_start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                sla_expiration_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                cwe = -2147483648,
                epss_score = 0.0,
                epss_percentile = 0.0,
                cvssv3 = 'PR:U0',
                cvssv3_score = 0.0,
                severity = '0',
                description = '0',
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
                under_defect_review = True,
                is_mitigated = True,
                numerical_severity = '0',
                line = -2147483648,
                file_path = '',
                component_name = '',
                component_version = '',
                static_finding = True,
                dynamic_finding = True,
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
                review_requested_by = 56,
                defect_review_requested_by = 56,
                sonarqube_issue = 56,
                reviewers = [
                    56
                    ]
            )
        else:
            return FindingRequest(
                title = '0',
                severity = '0',
                description = '0',
                numerical_severity = '0',
        )
        """

    def testFindingRequest(self):
        """Test FindingRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
