# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.jira_instance import JIRAInstance

class TestJIRAInstance(unittest.TestCase):
    """JIRAInstance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JIRAInstance:
        """Test JIRAInstance
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JIRAInstance`
        """
        model = JIRAInstance()
        if include_optional:
            return JIRAInstance(
                id = 56,
                configuration_name = '',
                url = '',
                username = '',
                default_issue_type = 'Task',
                issue_template_dir = '',
                epic_name_id = -2147483648,
                open_status_key = -2147483648,
                close_status_key = -2147483648,
                info_mapping_severity = '',
                low_mapping_severity = '',
                medium_mapping_severity = '',
                high_mapping_severity = '',
                critical_mapping_severity = '',
                finding_text = '',
                accepted_mapping_resolution = '',
                false_positive_mapping_resolution = '',
                global_jira_sla_notification = True,
                finding_jira_sync = True
            )
        else:
            return JIRAInstance(
                id = 56,
                url = '',
                username = '',
                epic_name_id = -2147483648,
                open_status_key = -2147483648,
                close_status_key = -2147483648,
                info_mapping_severity = '',
                low_mapping_severity = '',
                medium_mapping_severity = '',
                high_mapping_severity = '',
                critical_mapping_severity = '',
        )
        """

    def testJIRAInstance(self):
        """Test JIRAInstance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
