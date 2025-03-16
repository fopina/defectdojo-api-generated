# custom-templates/my_client.mustache
"""DefectDojo Client"""

from urllib.parse import urlparse
from urllib.request import getproxies, proxy_bypass

from defectdojo_api_generated.api.announcements_api import AnnouncementsApi
from defectdojo_api_generated.api.api_token_auth_api import ApiTokenAuthApi
from defectdojo_api_generated.api.configuration_permissions_api import ConfigurationPermissionsApi
from defectdojo_api_generated.api.credential_mappings_api import CredentialMappingsApi
from defectdojo_api_generated.api.credentials_api import CredentialsApi
from defectdojo_api_generated.api.development_environments_api import DevelopmentEnvironmentsApi
from defectdojo_api_generated.api.dojo_group_members_api import DojoGroupMembersApi
from defectdojo_api_generated.api.dojo_groups_api import DojoGroupsApi
from defectdojo_api_generated.api.endpoint_meta_import_api import EndpointMetaImportApi
from defectdojo_api_generated.api.endpoint_status_api import EndpointStatusApi
from defectdojo_api_generated.api.endpoints_api import EndpointsApi
from defectdojo_api_generated.api.engagement_presets_api import EngagementPresetsApi
from defectdojo_api_generated.api.engagements_api import EngagementsApi
from defectdojo_api_generated.api.finding_templates_api import FindingTemplatesApi
from defectdojo_api_generated.api.findings_api import FindingsApi
from defectdojo_api_generated.api.global_roles_api import GlobalRolesApi
from defectdojo_api_generated.api.import_languages_api import ImportLanguagesApi
from defectdojo_api_generated.api.import_scan_api import ImportScanApi
from defectdojo_api_generated.api.jira_configurations_api import JiraConfigurationsApi
from defectdojo_api_generated.api.jira_finding_mappings_api import JiraFindingMappingsApi
from defectdojo_api_generated.api.jira_instances_api import JiraInstancesApi
from defectdojo_api_generated.api.jira_product_configurations_api import JiraProductConfigurationsApi
from defectdojo_api_generated.api.jira_projects_api import JiraProjectsApi
from defectdojo_api_generated.api.language_types_api import LanguageTypesApi
from defectdojo_api_generated.api.languages_api import LanguagesApi
from defectdojo_api_generated.api.metadata_api import MetadataApi
from defectdojo_api_generated.api.network_locations_api import NetworkLocationsApi
from defectdojo_api_generated.api.note_type_api import NoteTypeApi
from defectdojo_api_generated.api.notes_api import NotesApi
from defectdojo_api_generated.api.notification_webhooks_api import NotificationWebhooksApi
from defectdojo_api_generated.api.notifications_api import NotificationsApi
from defectdojo_api_generated.api.oa3_api import Oa3Api
from defectdojo_api_generated.api.product_api_scan_configurations_api import ProductApiScanConfigurationsApi
from defectdojo_api_generated.api.product_groups_api import ProductGroupsApi
from defectdojo_api_generated.api.product_members_api import ProductMembersApi
from defectdojo_api_generated.api.product_type_groups_api import ProductTypeGroupsApi
from defectdojo_api_generated.api.product_type_members_api import ProductTypeMembersApi
from defectdojo_api_generated.api.product_types_api import ProductTypesApi
from defectdojo_api_generated.api.products_api import ProductsApi
from defectdojo_api_generated.api.questionnaire_answered_questionnaires_api import (
    QuestionnaireAnsweredQuestionnairesApi,
)
from defectdojo_api_generated.api.questionnaire_answers_api import QuestionnaireAnswersApi
from defectdojo_api_generated.api.questionnaire_engagement_questionnaires_api import (
    QuestionnaireEngagementQuestionnairesApi,
)
from defectdojo_api_generated.api.questionnaire_general_questionnaires_api import QuestionnaireGeneralQuestionnairesApi
from defectdojo_api_generated.api.questionnaire_questions_api import QuestionnaireQuestionsApi
from defectdojo_api_generated.api.regulations_api import RegulationsApi
from defectdojo_api_generated.api.reimport_scan_api import ReimportScanApi
from defectdojo_api_generated.api.request_response_pairs_api import RequestResponsePairsApi
from defectdojo_api_generated.api.risk_acceptance_api import RiskAcceptanceApi
from defectdojo_api_generated.api.roles_api import RolesApi
from defectdojo_api_generated.api.sla_configurations_api import SlaConfigurationsApi
from defectdojo_api_generated.api.sonarqube_issues_api import SonarqubeIssuesApi
from defectdojo_api_generated.api.sonarqube_transitions_api import SonarqubeTransitionsApi
from defectdojo_api_generated.api.stub_findings_api import StubFindingsApi
from defectdojo_api_generated.api.system_settings_api import SystemSettingsApi
from defectdojo_api_generated.api.technologies_api import TechnologiesApi
from defectdojo_api_generated.api.test_imports_api import TestImportsApi
from defectdojo_api_generated.api.test_types_api import TestTypesApi
from defectdojo_api_generated.api.tests_api import TestsApi
from defectdojo_api_generated.api.tool_configurations_api import ToolConfigurationsApi
from defectdojo_api_generated.api.tool_product_settings_api import ToolProductSettingsApi
from defectdojo_api_generated.api.tool_types_api import ToolTypesApi
from defectdojo_api_generated.api.user_contact_infos_api import UserContactInfosApi
from defectdojo_api_generated.api.user_profile_api import UserProfileApi
from defectdojo_api_generated.api.users_api import UsersApi
from defectdojo_api_generated.api_client import ApiClient as _ApiClient
from defectdojo_api_generated.configuration import Configuration


class DefectDojo:
    """API client for DefectDojo.

    :param base_url: base URL of the DefectDojo instance.
    :param token: API token to use with DefectDojo.
        Use this OR auth, not both.
    :param auth: tuple with username and password for basic authentication with DefectDojo.
        Use this OR token, not both.
    :param config: Configuration object to use. If provided, all other parameters are ignored.
    """

    def __init__(self, base_url: str, token: str = None, auth: tuple[str] = None, config: Configuration = None):
        if token is not None and auth is not None:
            raise ValueError('Provide `token` OR `auth`, not both.')
        if auth is not None and (not isinstance(auth, tuple) or len(auth) != 2):
            raise ValueError('`auth` needs to be a tuple with 2 elements, username and password')

        if config is None:
            # drop last / (if any) as it is already added as part of endpoints
            kwargs = {'host': base_url.rstrip('/')}

            if token is not None:
                kwargs.update({'api_key': {'tokenAuth': token}, 'api_key_prefix': {'tokenAuth': 'Token'}})
            elif auth is not None:
                kwargs.update({'username': auth[0], 'password': auth[1]})

            self.config = Configuration(**kwargs)
        else:
            self.config = config

        # TODO: just python-requests as generator library...
        if self.config.proxy is None:
            scheme, host, *_ = urlparse(base_url)
            if not proxy_bypass(host):
                self.config.proxy = getproxies().get(scheme)

        self.api_client = _ApiClient(configuration=self.config)
        self.announcements_api = AnnouncementsApi(self.api_client)
        self.api_token_auth_api = ApiTokenAuthApi(self.api_client)
        self.configuration_permissions_api = ConfigurationPermissionsApi(self.api_client)
        self.credential_mappings_api = CredentialMappingsApi(self.api_client)
        self.credentials_api = CredentialsApi(self.api_client)
        self.development_environments_api = DevelopmentEnvironmentsApi(self.api_client)
        self.dojo_group_members_api = DojoGroupMembersApi(self.api_client)
        self.dojo_groups_api = DojoGroupsApi(self.api_client)
        self.endpoint_meta_import_api = EndpointMetaImportApi(self.api_client)
        self.endpoint_status_api = EndpointStatusApi(self.api_client)
        self.endpoints_api = EndpointsApi(self.api_client)
        self.engagement_presets_api = EngagementPresetsApi(self.api_client)
        self.engagements_api = EngagementsApi(self.api_client)
        self.finding_templates_api = FindingTemplatesApi(self.api_client)
        self.findings_api = FindingsApi(self.api_client)
        self.global_roles_api = GlobalRolesApi(self.api_client)
        self.import_languages_api = ImportLanguagesApi(self.api_client)
        self.import_scan_api = ImportScanApi(self.api_client)
        self.jira_configurations_api = JiraConfigurationsApi(self.api_client)
        self.jira_finding_mappings_api = JiraFindingMappingsApi(self.api_client)
        self.jira_instances_api = JiraInstancesApi(self.api_client)
        self.jira_product_configurations_api = JiraProductConfigurationsApi(self.api_client)
        self.jira_projects_api = JiraProjectsApi(self.api_client)
        self.language_types_api = LanguageTypesApi(self.api_client)
        self.languages_api = LanguagesApi(self.api_client)
        self.metadata_api = MetadataApi(self.api_client)
        self.network_locations_api = NetworkLocationsApi(self.api_client)
        self.note_type_api = NoteTypeApi(self.api_client)
        self.notes_api = NotesApi(self.api_client)
        self.notification_webhooks_api = NotificationWebhooksApi(self.api_client)
        self.notifications_api = NotificationsApi(self.api_client)
        self.oa3_api = Oa3Api(self.api_client)
        self.product_api_scan_configurations_api = ProductApiScanConfigurationsApi(self.api_client)
        self.product_groups_api = ProductGroupsApi(self.api_client)
        self.product_members_api = ProductMembersApi(self.api_client)
        self.product_type_groups_api = ProductTypeGroupsApi(self.api_client)
        self.product_type_members_api = ProductTypeMembersApi(self.api_client)
        self.product_types_api = ProductTypesApi(self.api_client)
        self.products_api = ProductsApi(self.api_client)
        self.questionnaire_answered_questionnaires_api = QuestionnaireAnsweredQuestionnairesApi(self.api_client)
        self.questionnaire_answers_api = QuestionnaireAnswersApi(self.api_client)
        self.questionnaire_engagement_questionnaires_api = QuestionnaireEngagementQuestionnairesApi(self.api_client)
        self.questionnaire_general_questionnaires_api = QuestionnaireGeneralQuestionnairesApi(self.api_client)
        self.questionnaire_questions_api = QuestionnaireQuestionsApi(self.api_client)
        self.regulations_api = RegulationsApi(self.api_client)
        self.reimport_scan_api = ReimportScanApi(self.api_client)
        self.request_response_pairs_api = RequestResponsePairsApi(self.api_client)
        self.risk_acceptance_api = RiskAcceptanceApi(self.api_client)
        self.roles_api = RolesApi(self.api_client)
        self.sla_configurations_api = SlaConfigurationsApi(self.api_client)
        self.sonarqube_issues_api = SonarqubeIssuesApi(self.api_client)
        self.sonarqube_transitions_api = SonarqubeTransitionsApi(self.api_client)
        self.stub_findings_api = StubFindingsApi(self.api_client)
        self.system_settings_api = SystemSettingsApi(self.api_client)
        self.technologies_api = TechnologiesApi(self.api_client)
        self.test_imports_api = TestImportsApi(self.api_client)
        self.test_types_api = TestTypesApi(self.api_client)
        self.tests_api = TestsApi(self.api_client)
        self.tool_configurations_api = ToolConfigurationsApi(self.api_client)
        self.tool_product_settings_api = ToolProductSettingsApi(self.api_client)
        self.tool_types_api = ToolTypesApi(self.api_client)
        self.user_contact_infos_api = UserContactInfosApi(self.api_client)
        self.user_profile_api = UserProfileApi(self.api_client)
        self.users_api = UsersApi(self.api_client)
