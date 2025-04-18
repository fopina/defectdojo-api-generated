# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.jira_project_request import JIRAProjectRequest


class TestJIRAProjectRequest(unittest.TestCase):
    """JIRAProjectRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JIRAProjectRequest:
        """Test JIRAProjectRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `JIRAProjectRequest`
        """
        model = JIRAProjectRequest()
        if include_optional:
            return JIRAProjectRequest(
                project_key = '',
                issue_template_dir = '',
                component = '',
                custom_fields = None,
                default_assignee = '',
                jira_labels = '',
                add_vulnerability_id_to_jira_label = True,
                push_all_issues = True,
                enable_engagement_epic_mapping = True,
                epic_issue_type_name = '',
                push_notes = True,
                product_jira_sla_notification = True,
                risk_acceptance_expiration_notification = True,
                enabled = True,
                jira_instance = 56,
                product = 56,
                engagement = 56
            )
        else:
            return JIRAProjectRequest(
        )
        """

    def testJIRAProjectRequest(self):
        """Test JIRAProjectRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
