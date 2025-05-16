# custom-templates/my_client.mustache
"""DefectDojo Client"""

from typing import Optional, Tuple, overload
from urllib.parse import urlparse
from urllib.request import getproxies, proxy_bypass

from defectdojo_api_generated.api_client import ApiClient as _ApiClient
from defectdojo_api_generated.configuration import Configuration


class DefectDojo:
    """API client for DefectDojo.

    :param base_url: Base URL of the DefectDojo instance.
    :param token: API token to use with DefectDojo.
        Use this OR auth, not both.
    :param auth: Tuple with username and password for basic authentication with DefectDojo.
        Use this OR token, not both.
    :param verify_ssl: Set this to false to skip verifying SSL server certificate.
    :param config: Configuration object to use. If provided, all other parameters are ignored.
    """

    @overload
    def __init__(
        self,
        *,
        base_url: Optional[str] = None,
        token: Optional[str] = None,
        auth: Optional[Tuple[str, str]] = None,
        verify_ssl: bool = True,
    ): ...

    @overload
    def __init__(
        self,
        *,
        config: Configuration,
    ): ...

    def __init__(
        self,
        *,
        base_url: Optional[str] = None,
        token: Optional[str] = None,
        auth: Optional[Tuple[str, str]] = None,
        verify_ssl: bool = True,
        config: Optional[Configuration] = None,
    ):
        if token is not None and auth is not None:
            raise ValueError('Provide `token` OR `auth`, not both.')
        if auth is not None and (not isinstance(auth, tuple) or len(auth) != 2):
            raise ValueError('`auth` needs to be a tuple with 2 elements, username and password')

        if config is None:
            kwargs = {}
            if base_url is not None:
                kwargs['host'] = base_url

            if token is not None:
                kwargs.update({'api_key': {'tokenAuth': token}, 'api_key_prefix': {'tokenAuth': 'Token'}})
            elif auth is not None:
                kwargs.update({'username': auth[0], 'password': auth[1]})

            self.config = Configuration(**kwargs)
            self.config.verify_ssl = verify_ssl
        else:
            self.config = config

        if self.config.proxy is None and self.config.host:
            scheme, host, *_ = urlparse(self.config.host)
            if not proxy_bypass(host):
                self.config.proxy = getproxies().get(scheme)

        self.api_client = _ApiClient(configuration=self.config)

    @property
    def announcements_api(self):
        from defectdojo_api_generated.api.announcements_api import AnnouncementsApi

        return AnnouncementsApi(self.api_client)

    @property
    def api_token_auth_api(self):
        from defectdojo_api_generated.api.api_token_auth_api import ApiTokenAuthApi

        return ApiTokenAuthApi(self.api_client)

    @property
    def configuration_permissions_api(self):
        from defectdojo_api_generated.api.configuration_permissions_api import ConfigurationPermissionsApi

        return ConfigurationPermissionsApi(self.api_client)

    @property
    def credential_mappings_api(self):
        from defectdojo_api_generated.api.credential_mappings_api import CredentialMappingsApi

        return CredentialMappingsApi(self.api_client)

    @property
    def credentials_api(self):
        from defectdojo_api_generated.api.credentials_api import CredentialsApi

        return CredentialsApi(self.api_client)

    @property
    def development_environments_api(self):
        from defectdojo_api_generated.api.development_environments_api import DevelopmentEnvironmentsApi

        return DevelopmentEnvironmentsApi(self.api_client)

    @property
    def dojo_group_members_api(self):
        from defectdojo_api_generated.api.dojo_group_members_api import DojoGroupMembersApi

        return DojoGroupMembersApi(self.api_client)

    @property
    def dojo_groups_api(self):
        from defectdojo_api_generated.api.dojo_groups_api import DojoGroupsApi

        return DojoGroupsApi(self.api_client)

    @property
    def endpoint_meta_import_api(self):
        from defectdojo_api_generated.api.endpoint_meta_import_api import EndpointMetaImportApi

        return EndpointMetaImportApi(self.api_client)

    @property
    def endpoint_status_api(self):
        from defectdojo_api_generated.api.endpoint_status_api import EndpointStatusApi

        return EndpointStatusApi(self.api_client)

    @property
    def endpoints_api(self):
        from defectdojo_api_generated.api.endpoints_api import EndpointsApi

        return EndpointsApi(self.api_client)

    @property
    def engagement_presets_api(self):
        from defectdojo_api_generated.api.engagement_presets_api import EngagementPresetsApi

        return EngagementPresetsApi(self.api_client)

    @property
    def engagements_api(self):
        from defectdojo_api_generated.api.engagements_api import EngagementsApi

        return EngagementsApi(self.api_client)

    @property
    def finding_templates_api(self):
        from defectdojo_api_generated.api.finding_templates_api import FindingTemplatesApi

        return FindingTemplatesApi(self.api_client)

    @property
    def findings_api(self):
        from defectdojo_api_generated.api.findings_api import FindingsApi

        return FindingsApi(self.api_client)

    @property
    def global_roles_api(self):
        from defectdojo_api_generated.api.global_roles_api import GlobalRolesApi

        return GlobalRolesApi(self.api_client)

    @property
    def import_languages_api(self):
        from defectdojo_api_generated.api.import_languages_api import ImportLanguagesApi

        return ImportLanguagesApi(self.api_client)

    @property
    def import_scan_api(self):
        from defectdojo_api_generated.api.import_scan_api import ImportScanApi

        return ImportScanApi(self.api_client)

    @property
    def jira_configurations_api(self):
        from defectdojo_api_generated.api.jira_configurations_api import JiraConfigurationsApi

        return JiraConfigurationsApi(self.api_client)

    @property
    def jira_finding_mappings_api(self):
        from defectdojo_api_generated.api.jira_finding_mappings_api import JiraFindingMappingsApi

        return JiraFindingMappingsApi(self.api_client)

    @property
    def jira_instances_api(self):
        from defectdojo_api_generated.api.jira_instances_api import JiraInstancesApi

        return JiraInstancesApi(self.api_client)

    @property
    def jira_product_configurations_api(self):
        from defectdojo_api_generated.api.jira_product_configurations_api import JiraProductConfigurationsApi

        return JiraProductConfigurationsApi(self.api_client)

    @property
    def jira_projects_api(self):
        from defectdojo_api_generated.api.jira_projects_api import JiraProjectsApi

        return JiraProjectsApi(self.api_client)

    @property
    def language_types_api(self):
        from defectdojo_api_generated.api.language_types_api import LanguageTypesApi

        return LanguageTypesApi(self.api_client)

    @property
    def languages_api(self):
        from defectdojo_api_generated.api.languages_api import LanguagesApi

        return LanguagesApi(self.api_client)

    @property
    def metadata_api(self):
        from defectdojo_api_generated.api.metadata_api import MetadataApi

        return MetadataApi(self.api_client)

    @property
    def network_locations_api(self):
        from defectdojo_api_generated.api.network_locations_api import NetworkLocationsApi

        return NetworkLocationsApi(self.api_client)

    @property
    def note_type_api(self):
        from defectdojo_api_generated.api.note_type_api import NoteTypeApi

        return NoteTypeApi(self.api_client)

    @property
    def notes_api(self):
        from defectdojo_api_generated.api.notes_api import NotesApi

        return NotesApi(self.api_client)

    @property
    def notification_webhooks_api(self):
        from defectdojo_api_generated.api.notification_webhooks_api import NotificationWebhooksApi

        return NotificationWebhooksApi(self.api_client)

    @property
    def notifications_api(self):
        from defectdojo_api_generated.api.notifications_api import NotificationsApi

        return NotificationsApi(self.api_client)

    @property
    def oa3_api(self):
        from defectdojo_api_generated.api.oa3_api import Oa3Api

        return Oa3Api(self.api_client)

    @property
    def product_api_scan_configurations_api(self):
        from defectdojo_api_generated.api.product_api_scan_configurations_api import ProductApiScanConfigurationsApi

        return ProductApiScanConfigurationsApi(self.api_client)

    @property
    def product_groups_api(self):
        from defectdojo_api_generated.api.product_groups_api import ProductGroupsApi

        return ProductGroupsApi(self.api_client)

    @property
    def product_members_api(self):
        from defectdojo_api_generated.api.product_members_api import ProductMembersApi

        return ProductMembersApi(self.api_client)

    @property
    def product_type_groups_api(self):
        from defectdojo_api_generated.api.product_type_groups_api import ProductTypeGroupsApi

        return ProductTypeGroupsApi(self.api_client)

    @property
    def product_type_members_api(self):
        from defectdojo_api_generated.api.product_type_members_api import ProductTypeMembersApi

        return ProductTypeMembersApi(self.api_client)

    @property
    def product_types_api(self):
        from defectdojo_api_generated.api.product_types_api import ProductTypesApi

        return ProductTypesApi(self.api_client)

    @property
    def products_api(self):
        from defectdojo_api_generated.api.products_api import ProductsApi

        return ProductsApi(self.api_client)

    @property
    def questionnaire_answered_questionnaires_api(self):
        from defectdojo_api_generated.api.questionnaire_answered_questionnaires_api import (
            QuestionnaireAnsweredQuestionnairesApi,
        )

        return QuestionnaireAnsweredQuestionnairesApi(self.api_client)

    @property
    def questionnaire_answers_api(self):
        from defectdojo_api_generated.api.questionnaire_answers_api import QuestionnaireAnswersApi

        return QuestionnaireAnswersApi(self.api_client)

    @property
    def questionnaire_engagement_questionnaires_api(self):
        from defectdojo_api_generated.api.questionnaire_engagement_questionnaires_api import (
            QuestionnaireEngagementQuestionnairesApi,
        )

        return QuestionnaireEngagementQuestionnairesApi(self.api_client)

    @property
    def questionnaire_general_questionnaires_api(self):
        from defectdojo_api_generated.api.questionnaire_general_questionnaires_api import (
            QuestionnaireGeneralQuestionnairesApi,
        )

        return QuestionnaireGeneralQuestionnairesApi(self.api_client)

    @property
    def questionnaire_questions_api(self):
        from defectdojo_api_generated.api.questionnaire_questions_api import QuestionnaireQuestionsApi

        return QuestionnaireQuestionsApi(self.api_client)

    @property
    def regulations_api(self):
        from defectdojo_api_generated.api.regulations_api import RegulationsApi

        return RegulationsApi(self.api_client)

    @property
    def reimport_scan_api(self):
        from defectdojo_api_generated.api.reimport_scan_api import ReimportScanApi

        return ReimportScanApi(self.api_client)

    @property
    def request_response_pairs_api(self):
        from defectdojo_api_generated.api.request_response_pairs_api import RequestResponsePairsApi

        return RequestResponsePairsApi(self.api_client)

    @property
    def risk_acceptance_api(self):
        from defectdojo_api_generated.api.risk_acceptance_api import RiskAcceptanceApi

        return RiskAcceptanceApi(self.api_client)

    @property
    def roles_api(self):
        from defectdojo_api_generated.api.roles_api import RolesApi

        return RolesApi(self.api_client)

    @property
    def sla_configurations_api(self):
        from defectdojo_api_generated.api.sla_configurations_api import SlaConfigurationsApi

        return SlaConfigurationsApi(self.api_client)

    @property
    def sonarqube_issues_api(self):
        from defectdojo_api_generated.api.sonarqube_issues_api import SonarqubeIssuesApi

        return SonarqubeIssuesApi(self.api_client)

    @property
    def sonarqube_transitions_api(self):
        from defectdojo_api_generated.api.sonarqube_transitions_api import SonarqubeTransitionsApi

        return SonarqubeTransitionsApi(self.api_client)

    @property
    def stub_findings_api(self):
        from defectdojo_api_generated.api.stub_findings_api import StubFindingsApi

        return StubFindingsApi(self.api_client)

    @property
    def system_settings_api(self):
        from defectdojo_api_generated.api.system_settings_api import SystemSettingsApi

        return SystemSettingsApi(self.api_client)

    @property
    def technologies_api(self):
        from defectdojo_api_generated.api.technologies_api import TechnologiesApi

        return TechnologiesApi(self.api_client)

    @property
    def test_imports_api(self):
        from defectdojo_api_generated.api.test_imports_api import TestImportsApi

        return TestImportsApi(self.api_client)

    @property
    def test_types_api(self):
        from defectdojo_api_generated.api.test_types_api import TestTypesApi

        return TestTypesApi(self.api_client)

    @property
    def tests_api(self):
        from defectdojo_api_generated.api.tests_api import TestsApi

        return TestsApi(self.api_client)

    @property
    def tool_configurations_api(self):
        from defectdojo_api_generated.api.tool_configurations_api import ToolConfigurationsApi

        return ToolConfigurationsApi(self.api_client)

    @property
    def tool_product_settings_api(self):
        from defectdojo_api_generated.api.tool_product_settings_api import ToolProductSettingsApi

        return ToolProductSettingsApi(self.api_client)

    @property
    def tool_types_api(self):
        from defectdojo_api_generated.api.tool_types_api import ToolTypesApi

        return ToolTypesApi(self.api_client)

    @property
    def user_contact_infos_api(self):
        from defectdojo_api_generated.api.user_contact_infos_api import UserContactInfosApi

        return UserContactInfosApi(self.api_client)

    @property
    def user_profile_api(self):
        from defectdojo_api_generated.api.user_profile_api import UserProfileApi

        return UserProfileApi(self.api_client)

    @property
    def users_api(self):
        from defectdojo_api_generated.api.users_api import UsersApi

        return UsersApi(self.api_client)
