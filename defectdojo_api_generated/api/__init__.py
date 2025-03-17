# flake8: noqa

# import apis into api package
import lazy_import
from typing import TYPE_CHECKING

if TYPE_CHECKING:
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
    from defectdojo_api_generated.api.questionnaire_general_questionnaires_api import (
        QuestionnaireGeneralQuestionnairesApi,
    )
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

else:
    AnnouncementsApi = lazy_import.lazy_class('defectdojo_api_generated.api.announcements_api.AnnouncementsApi')
    ApiTokenAuthApi = lazy_import.lazy_class('defectdojo_api_generated.api.api_token_auth_api.ApiTokenAuthApi')
    ConfigurationPermissionsApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.configuration_permissions_api.ConfigurationPermissionsApi'
    )
    CredentialMappingsApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.credential_mappings_api.CredentialMappingsApi'
    )
    CredentialsApi = lazy_import.lazy_class('defectdojo_api_generated.api.credentials_api.CredentialsApi')
    DevelopmentEnvironmentsApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.development_environments_api.DevelopmentEnvironmentsApi'
    )
    DojoGroupMembersApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.dojo_group_members_api.DojoGroupMembersApi'
    )
    DojoGroupsApi = lazy_import.lazy_class('defectdojo_api_generated.api.dojo_groups_api.DojoGroupsApi')
    EndpointMetaImportApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.endpoint_meta_import_api.EndpointMetaImportApi'
    )
    EndpointStatusApi = lazy_import.lazy_class('defectdojo_api_generated.api.endpoint_status_api.EndpointStatusApi')
    EndpointsApi = lazy_import.lazy_class('defectdojo_api_generated.api.endpoints_api.EndpointsApi')
    EngagementPresetsApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.engagement_presets_api.EngagementPresetsApi'
    )
    EngagementsApi = lazy_import.lazy_class('defectdojo_api_generated.api.engagements_api.EngagementsApi')
    FindingTemplatesApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.finding_templates_api.FindingTemplatesApi'
    )
    FindingsApi = lazy_import.lazy_class('defectdojo_api_generated.api.findings_api.FindingsApi')
    GlobalRolesApi = lazy_import.lazy_class('defectdojo_api_generated.api.global_roles_api.GlobalRolesApi')
    ImportLanguagesApi = lazy_import.lazy_class('defectdojo_api_generated.api.import_languages_api.ImportLanguagesApi')
    ImportScanApi = lazy_import.lazy_class('defectdojo_api_generated.api.import_scan_api.ImportScanApi')
    JiraConfigurationsApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.jira_configurations_api.JiraConfigurationsApi'
    )
    JiraFindingMappingsApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.jira_finding_mappings_api.JiraFindingMappingsApi'
    )
    JiraInstancesApi = lazy_import.lazy_class('defectdojo_api_generated.api.jira_instances_api.JiraInstancesApi')
    JiraProductConfigurationsApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.jira_product_configurations_api.JiraProductConfigurationsApi'
    )
    JiraProjectsApi = lazy_import.lazy_class('defectdojo_api_generated.api.jira_projects_api.JiraProjectsApi')
    LanguageTypesApi = lazy_import.lazy_class('defectdojo_api_generated.api.language_types_api.LanguageTypesApi')
    LanguagesApi = lazy_import.lazy_class('defectdojo_api_generated.api.languages_api.LanguagesApi')
    MetadataApi = lazy_import.lazy_class('defectdojo_api_generated.api.metadata_api.MetadataApi')
    NetworkLocationsApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.network_locations_api.NetworkLocationsApi'
    )
    NoteTypeApi = lazy_import.lazy_class('defectdojo_api_generated.api.note_type_api.NoteTypeApi')
    NotesApi = lazy_import.lazy_class('defectdojo_api_generated.api.notes_api.NotesApi')
    NotificationWebhooksApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.notification_webhooks_api.NotificationWebhooksApi'
    )
    NotificationsApi = lazy_import.lazy_class('defectdojo_api_generated.api.notifications_api.NotificationsApi')
    Oa3Api = lazy_import.lazy_class('defectdojo_api_generated.api.oa3_api.Oa3Api')
    ProductApiScanConfigurationsApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.product_api_scan_configurations_api.ProductApiScanConfigurationsApi'
    )
    ProductGroupsApi = lazy_import.lazy_class('defectdojo_api_generated.api.product_groups_api.ProductGroupsApi')
    ProductMembersApi = lazy_import.lazy_class('defectdojo_api_generated.api.product_members_api.ProductMembersApi')
    ProductTypeGroupsApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.product_type_groups_api.ProductTypeGroupsApi'
    )
    ProductTypeMembersApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.product_type_members_api.ProductTypeMembersApi'
    )
    ProductTypesApi = lazy_import.lazy_class('defectdojo_api_generated.api.product_types_api.ProductTypesApi')
    ProductsApi = lazy_import.lazy_class('defectdojo_api_generated.api.products_api.ProductsApi')
    QuestionnaireAnsweredQuestionnairesApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.questionnaire_answered_questionnaires_api.QuestionnaireAnsweredQuestionnairesApi'
    )
    QuestionnaireAnswersApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.questionnaire_answers_api.QuestionnaireAnswersApi'
    )
    QuestionnaireEngagementQuestionnairesApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.questionnaire_engagement_questionnaires_api.QuestionnaireEngagementQuestionnairesApi'
    )
    QuestionnaireGeneralQuestionnairesApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.questionnaire_general_questionnaires_api.QuestionnaireGeneralQuestionnairesApi'
    )
    QuestionnaireQuestionsApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.questionnaire_questions_api.QuestionnaireQuestionsApi'
    )
    RegulationsApi = lazy_import.lazy_class('defectdojo_api_generated.api.regulations_api.RegulationsApi')
    ReimportScanApi = lazy_import.lazy_class('defectdojo_api_generated.api.reimport_scan_api.ReimportScanApi')
    RequestResponsePairsApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.request_response_pairs_api.RequestResponsePairsApi'
    )
    RiskAcceptanceApi = lazy_import.lazy_class('defectdojo_api_generated.api.risk_acceptance_api.RiskAcceptanceApi')
    RolesApi = lazy_import.lazy_class('defectdojo_api_generated.api.roles_api.RolesApi')
    SlaConfigurationsApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.sla_configurations_api.SlaConfigurationsApi'
    )
    SonarqubeIssuesApi = lazy_import.lazy_class('defectdojo_api_generated.api.sonarqube_issues_api.SonarqubeIssuesApi')
    SonarqubeTransitionsApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.sonarqube_transitions_api.SonarqubeTransitionsApi'
    )
    StubFindingsApi = lazy_import.lazy_class('defectdojo_api_generated.api.stub_findings_api.StubFindingsApi')
    SystemSettingsApi = lazy_import.lazy_class('defectdojo_api_generated.api.system_settings_api.SystemSettingsApi')
    TechnologiesApi = lazy_import.lazy_class('defectdojo_api_generated.api.technologies_api.TechnologiesApi')
    TestImportsApi = lazy_import.lazy_class('defectdojo_api_generated.api.test_imports_api.TestImportsApi')
    TestTypesApi = lazy_import.lazy_class('defectdojo_api_generated.api.test_types_api.TestTypesApi')
    TestsApi = lazy_import.lazy_class('defectdojo_api_generated.api.tests_api.TestsApi')
    ToolConfigurationsApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.tool_configurations_api.ToolConfigurationsApi'
    )
    ToolProductSettingsApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.tool_product_settings_api.ToolProductSettingsApi'
    )
    ToolTypesApi = lazy_import.lazy_class('defectdojo_api_generated.api.tool_types_api.ToolTypesApi')
    UserContactInfosApi = lazy_import.lazy_class(
        'defectdojo_api_generated.api.user_contact_infos_api.UserContactInfosApi'
    )
    UserProfileApi = lazy_import.lazy_class('defectdojo_api_generated.api.user_profile_api.UserProfileApi')
    UsersApi = lazy_import.lazy_class('defectdojo_api_generated.api.users_api.UsersApi')
