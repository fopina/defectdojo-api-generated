# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.finding_template_request import FindingTemplateRequest

class TestFindingTemplateRequest(unittest.TestCase):
    """FindingTemplateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FindingTemplateRequest:
        """Test FindingTemplateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FindingTemplateRequest`
        """
        model = FindingTemplateRequest()
        if include_optional:
            return FindingTemplateRequest(
                tags = [
                    '0'
                    ],
                vulnerability_ids = [
                    defectdojo_api_generated.models.vulnerability_id_template_request.VulnerabilityIdTemplateRequest(
                        vulnerability_id = '0', )
                    ],
                title = '0',
                cwe = -2147483648,
                cvssv3 = 'PR:U0',
                severity = '',
                description = '',
                mitigation = '',
                impact = '',
                references = '',
                template_match = True,
                template_match_title = True
            )
        else:
            return FindingTemplateRequest(
                title = '0',
        )
        """

    def testFindingTemplateRequest(self):
        """Test FindingTemplateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
