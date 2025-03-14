# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.system_settings import SystemSettings

class TestSystemSettings(unittest.TestCase):
    """SystemSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemSettings:
        """Test SystemSettings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemSettings`
        """
        model = SystemSettings()
        if include_optional:
            return SystemSettings(
                id = 56,
                enable_deduplication = True,
                delete_duplicates = True,
                max_dupes = -2147483648,
                email_from = '',
                enable_jira = True,
                enable_jira_web_hook = True,
                disable_jira_webhook_secret = True,
                jira_webhook_secret = '',
                jira_minimum_severity = 'Critical',
                jira_labels = '',
                add_vulnerability_id_to_jira_label = True,
                enable_github = True,
                enable_slack_notifications = True,
                slack_channel = '',
                slack_token = '',
                slack_username = '',
                enable_msteams_notifications = True,
                msteams_url = '',
                enable_mail_notifications = True,
                mail_notifications_to = '',
                enable_webhooks_notifications = True,
                webhooks_notifications_timeout = -2147483648,
                enforce_verified_status = True,
                enforce_verified_status_jira = True,
                enforce_verified_status_product_grading = True,
                enforce_verified_status_metrics = True,
                false_positive_history = True,
                retroactive_false_positive_history = True,
                url_prefix = '',
                team_name = '',
                time_zone = 'Africa/Abidjan',
                enable_product_grade = True,
                product_grade = '',
                product_grade_a = -2147483648,
                product_grade_b = -2147483648,
                product_grade_c = -2147483648,
                product_grade_d = -2147483648,
                product_grade_f = -2147483648,
                enable_product_tag_inheritance = True,
                enable_benchmark = True,
                enable_template_match = True,
                enable_similar_findings = True,
                engagement_auto_close = True,
                engagement_auto_close_days = -2147483648,
                enable_finding_sla = True,
                enable_notify_sla_active = True,
                enable_notify_sla_active_verified = True,
                enable_notify_sla_jira_only = True,
                enable_notify_sla_exponential_backoff = True,
                allow_anonymous_survey_repsonse = True,
                credentials = '',
                disclaimer_notifications = '',
                disclaimer_reports = '',
                disclaimer_reports_forced = True,
                disclaimer_notes = '',
                risk_acceptance_form_default_days = -2147483648,
                risk_acceptance_notify_before_expiration = -2147483648,
                enable_credentials = True,
                enable_questionnaires = True,
                enable_checklists = True,
                enable_endpoint_metadata_import = True,
                enable_user_profile_editable = True,
                enable_product_tracking_files = True,
                enable_finding_groups = True,
                enable_ui_table_based_searching = True,
                enable_calendar = True,
                default_group_email_pattern = '',
                minimum_password_length = -2147483648,
                maximum_password_length = -2147483648,
                number_character_required = True,
                special_character_required = True,
                lowercase_character_required = True,
                uppercase_character_required = True,
                non_common_password_required = True,
                api_expose_error_details = True,
                filter_string_matching = True,
                default_group = 56,
                default_group_role = 56
            )
        else:
            return SystemSettings(
                id = 56,
        )
        """

    def testSystemSettings(self):
        """Test SystemSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
