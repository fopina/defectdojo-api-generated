# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.finding_template import FindingTemplate


class TestFindingTemplate(unittest.TestCase):
    """FindingTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FindingTemplate:
        """Test FindingTemplate
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `FindingTemplate`
        """
        model = FindingTemplate()
        if include_optional:
            return FindingTemplate(
                id = 56,
                tags = [
                    ''
                    ],
                vulnerability_ids = [
                    defectdojo_api_generated.models.vulnerability_id_template.VulnerabilityIdTemplate(
                        vulnerability_id = '', )
                    ],
                title = '',
                cwe = -2147483648,
                cvssv3 = 'PR:U',
                severity = '',
                description = '',
                mitigation = '',
                impact = '',
                references = '',
                last_used = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                numerical_severity = '',
                template_match = True,
                template_match_title = True
            )
        else:
            return FindingTemplate(
                id = 56,
                title = '',
                last_used = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                numerical_severity = '',
        )
        """

    def testFindingTemplate(self):
        """Test FindingTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
