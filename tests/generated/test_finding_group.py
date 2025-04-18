# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.finding_group import FindingGroup


class TestFindingGroup(unittest.TestCase):
    """FindingGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FindingGroup:
        """Test FindingGroup
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `FindingGroup`
        """
        model = FindingGroup()
        if include_optional:
            return FindingGroup(
                id = 56,
                name = '',
                test = 56,
                jira_issue = defectdojo_api_generated.models.jira_issue.JIRAIssue(
                    id = 56, 
                    url = '', 
                    jira_id = '', 
                    jira_key = '', 
                    jira_creation = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    jira_change = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    jira_project = 56, 
                    finding = 56, 
                    engagement = 56, 
                    finding_group = 56, )
            )
        else:
            return FindingGroup(
                id = 56,
                name = '',
                test = 56,
                jira_issue = defectdojo_api_generated.models.jira_issue.JIRAIssue(
                    id = 56, 
                    url = '', 
                    jira_id = '', 
                    jira_key = '', 
                    jira_creation = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    jira_change = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    jira_project = 56, 
                    finding = 56, 
                    engagement = 56, 
                    finding_group = 56, ),
        )
        """

    def testFindingGroup(self):
        """Test FindingGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
