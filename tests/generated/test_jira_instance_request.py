# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.jira_instance_request import JIRAInstanceRequest


class TestJIRAInstanceRequest(unittest.TestCase):
    """JIRAInstanceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JIRAInstanceRequest:
        """Test JIRAInstanceRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `JIRAInstanceRequest`
        """
        model = JIRAInstanceRequest()
        if include_optional:
            return JIRAInstanceRequest(
                configuration_name = '0',
                url = '0',
                username = '0',
                password = '0',
                default_issue_type = 'Task',
                issue_template_dir = '',
                epic_name_id = -2147483648,
                open_status_key = -2147483648,
                close_status_key = -2147483648,
                info_mapping_severity = '0',
                low_mapping_severity = '0',
                medium_mapping_severity = '0',
                high_mapping_severity = '0',
                critical_mapping_severity = '0',
                finding_text = '',
                accepted_mapping_resolution = '',
                false_positive_mapping_resolution = '',
                global_jira_sla_notification = True,
                finding_jira_sync = True
            )
        else:
            return JIRAInstanceRequest(
                url = '0',
                username = '0',
                password = '0',
                epic_name_id = -2147483648,
                open_status_key = -2147483648,
                close_status_key = -2147483648,
                info_mapping_severity = '0',
                low_mapping_severity = '0',
                medium_mapping_severity = '0',
                high_mapping_severity = '0',
                critical_mapping_severity = '0',
        )
        """

    def testJIRAInstanceRequest(self):
        """Test JIRAInstanceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
