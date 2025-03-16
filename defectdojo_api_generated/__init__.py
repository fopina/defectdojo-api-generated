# coding: utf-8

# flake8: noqa

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

The version of the OpenAPI document: 2.44.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

__version__ = '1.0.0'
__openapi_version__ = '2.44.1'

# import apis into sdk package
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

# import ApiClient
from defectdojo_api_generated.api_response import ApiResponse
from defectdojo_api_generated.api_client import ApiClient
from defectdojo_api_generated.client import DefectDojo
from defectdojo_api_generated.configuration import Configuration
from defectdojo_api_generated.exceptions import OpenApiException
from defectdojo_api_generated.exceptions import ApiTypeError
from defectdojo_api_generated.exceptions import ApiValueError
from defectdojo_api_generated.exceptions import ApiKeyError
from defectdojo_api_generated.exceptions import ApiAttributeError
from defectdojo_api_generated.exceptions import ApiException

# import models into sdk package
from defectdojo_api_generated.models.accepted_risk_request import AcceptedRiskRequest
from defectdojo_api_generated.models.add_new_note_option_request import AddNewNoteOptionRequest
from defectdojo_api_generated.models.announcement import Announcement
from defectdojo_api_generated.models.announcement_request import AnnouncementRequest
from defectdojo_api_generated.models.app_analysis import AppAnalysis
from defectdojo_api_generated.models.app_analysis_prefetch import AppAnalysisPrefetch
from defectdojo_api_generated.models.app_analysis_request import AppAnalysisRequest
from defectdojo_api_generated.models.auth_token import AuthToken
from defectdojo_api_generated.models.auth_token_request import AuthTokenRequest
from defectdojo_api_generated.models.burp_raw_request_response import BurpRawRequestResponse
from defectdojo_api_generated.models.burp_raw_request_response_multi import BurpRawRequestResponseMulti
from defectdojo_api_generated.models.burp_raw_request_response_multi_request import BurpRawRequestResponseMultiRequest
from defectdojo_api_generated.models.burp_raw_request_response_request import BurpRawRequestResponseRequest
from defectdojo_api_generated.models.configuration_permission import ConfigurationPermission
from defectdojo_api_generated.models.credential import Credential
from defectdojo_api_generated.models.credential_mapping import CredentialMapping
from defectdojo_api_generated.models.credential_mapping_request import CredentialMappingRequest
from defectdojo_api_generated.models.credential_prefetch import CredentialPrefetch
from defectdojo_api_generated.models.credential_request import CredentialRequest
from defectdojo_api_generated.models.delete_preview import DeletePreview
from defectdojo_api_generated.models.delta_statistics import DeltaStatistics
from defectdojo_api_generated.models.delta_statistics_request import DeltaStatisticsRequest
from defectdojo_api_generated.models.development_environment import DevelopmentEnvironment
from defectdojo_api_generated.models.development_environment_request import DevelopmentEnvironmentRequest
from defectdojo_api_generated.models.dojo_group import DojoGroup
from defectdojo_api_generated.models.dojo_group_member import DojoGroupMember
from defectdojo_api_generated.models.dojo_group_member_prefetch import DojoGroupMemberPrefetch
from defectdojo_api_generated.models.dojo_group_member_request import DojoGroupMemberRequest
from defectdojo_api_generated.models.dojo_group_prefetch import DojoGroupPrefetch
from defectdojo_api_generated.models.dojo_group_request import DojoGroupRequest
from defectdojo_api_generated.models.endpoint import Endpoint
from defectdojo_api_generated.models.endpoint_meta_importer import EndpointMetaImporter
from defectdojo_api_generated.models.endpoint_request import EndpointRequest
from defectdojo_api_generated.models.endpoint_status import EndpointStatus
from defectdojo_api_generated.models.endpoint_status_request import EndpointStatusRequest
from defectdojo_api_generated.models.engagement import Engagement
from defectdojo_api_generated.models.engagement_check_list import EngagementCheckList
from defectdojo_api_generated.models.engagement_check_list_request import EngagementCheckListRequest
from defectdojo_api_generated.models.engagement_presets import EngagementPresets
from defectdojo_api_generated.models.engagement_presets_prefetch import EngagementPresetsPrefetch
from defectdojo_api_generated.models.engagement_presets_request import EngagementPresetsRequest
from defectdojo_api_generated.models.engagement_request import EngagementRequest
from defectdojo_api_generated.models.engagement_to_files import EngagementToFiles
from defectdojo_api_generated.models.engagement_to_notes import EngagementToNotes
from defectdojo_api_generated.models.engagement_update_jira_epic import EngagementUpdateJiraEpic
from defectdojo_api_generated.models.engagement_update_jira_epic_request import EngagementUpdateJiraEpicRequest
from defectdojo_api_generated.models.executive_summary import ExecutiveSummary
from defectdojo_api_generated.models.file import File
from defectdojo_api_generated.models.file_request import FileRequest
from defectdojo_api_generated.models.finding import Finding
from defectdojo_api_generated.models.finding_close import FindingClose
from defectdojo_api_generated.models.finding_close_request import FindingCloseRequest
from defectdojo_api_generated.models.finding_create import FindingCreate
from defectdojo_api_generated.models.finding_create_request import FindingCreateRequest
from defectdojo_api_generated.models.finding_engagement import FindingEngagement
from defectdojo_api_generated.models.finding_environment import FindingEnvironment
from defectdojo_api_generated.models.finding_group import FindingGroup
from defectdojo_api_generated.models.finding_group_request import FindingGroupRequest
from defectdojo_api_generated.models.finding_meta import FindingMeta
from defectdojo_api_generated.models.finding_meta_request import FindingMetaRequest
from defectdojo_api_generated.models.finding_prefetch import FindingPrefetch
from defectdojo_api_generated.models.finding_prod_type import FindingProdType
from defectdojo_api_generated.models.finding_product import FindingProduct
from defectdojo_api_generated.models.finding_related_fields import FindingRelatedFields
from defectdojo_api_generated.models.finding_request import FindingRequest
from defectdojo_api_generated.models.finding_template import FindingTemplate
from defectdojo_api_generated.models.finding_template_request import FindingTemplateRequest
from defectdojo_api_generated.models.finding_test import FindingTest
from defectdojo_api_generated.models.finding_test_type import FindingTestType
from defectdojo_api_generated.models.finding_to_files import FindingToFiles
from defectdojo_api_generated.models.finding_to_notes import FindingToNotes
from defectdojo_api_generated.models.global_role import GlobalRole
from defectdojo_api_generated.models.global_role_request import GlobalRoleRequest
from defectdojo_api_generated.models.import_languages import ImportLanguages
from defectdojo_api_generated.models.import_scan import ImportScan
from defectdojo_api_generated.models.import_statistics import ImportStatistics
from defectdojo_api_generated.models.import_statistics_request import ImportStatisticsRequest
from defectdojo_api_generated.models.jira_instance import JIRAInstance
from defectdojo_api_generated.models.jira_instance_request import JIRAInstanceRequest
from defectdojo_api_generated.models.jira_issue import JIRAIssue
from defectdojo_api_generated.models.jira_issue_request import JIRAIssueRequest
from defectdojo_api_generated.models.jira_project import JIRAProject
from defectdojo_api_generated.models.jira_project_prefetch import JIRAProjectPrefetch
from defectdojo_api_generated.models.jira_project_request import JIRAProjectRequest
from defectdojo_api_generated.models.language import Language
from defectdojo_api_generated.models.language_prefetch import LanguagePrefetch
from defectdojo_api_generated.models.language_request import LanguageRequest
from defectdojo_api_generated.models.language_type import LanguageType
from defectdojo_api_generated.models.language_type_request import LanguageTypeRequest
from defectdojo_api_generated.models.meta import Meta
from defectdojo_api_generated.models.meta_main import MetaMain
from defectdojo_api_generated.models.meta_main_request import MetaMainRequest
from defectdojo_api_generated.models.meta_request import MetaRequest
from defectdojo_api_generated.models.metadata import Metadata
from defectdojo_api_generated.models.metadata_request import MetadataRequest
from defectdojo_api_generated.models.network_locations import NetworkLocations
from defectdojo_api_generated.models.network_locations_request import NetworkLocationsRequest
from defectdojo_api_generated.models.note import Note
from defectdojo_api_generated.models.note_history import NoteHistory
from defectdojo_api_generated.models.note_history_request import NoteHistoryRequest
from defectdojo_api_generated.models.note_request import NoteRequest
from defectdojo_api_generated.models.note_type import NoteType
from defectdojo_api_generated.models.note_type_request import NoteTypeRequest
from defectdojo_api_generated.models.notification_webhooks import NotificationWebhooks
from defectdojo_api_generated.models.notification_webhooks_request import NotificationWebhooksRequest
from defectdojo_api_generated.models.notifications import Notifications
from defectdojo_api_generated.models.notifications_request import NotificationsRequest
from defectdojo_api_generated.models.paginated_announcement_list import PaginatedAnnouncementList
from defectdojo_api_generated.models.paginated_app_analysis_list import PaginatedAppAnalysisList
from defectdojo_api_generated.models.paginated_burp_raw_request_response_multi_list import (
    PaginatedBurpRawRequestResponseMultiList,
)
from defectdojo_api_generated.models.paginated_configuration_permission_list import PaginatedConfigurationPermissionList
from defectdojo_api_generated.models.paginated_credential_list import PaginatedCredentialList
from defectdojo_api_generated.models.paginated_credential_mapping_list import PaginatedCredentialMappingList
from defectdojo_api_generated.models.paginated_delete_preview_list import PaginatedDeletePreviewList
from defectdojo_api_generated.models.paginated_development_environment_list import PaginatedDevelopmentEnvironmentList
from defectdojo_api_generated.models.paginated_dojo_group_list import PaginatedDojoGroupList
from defectdojo_api_generated.models.paginated_dojo_group_member_list import PaginatedDojoGroupMemberList
from defectdojo_api_generated.models.paginated_endpoint_list import PaginatedEndpointList
from defectdojo_api_generated.models.paginated_endpoint_status_list import PaginatedEndpointStatusList
from defectdojo_api_generated.models.paginated_engagement_list import PaginatedEngagementList
from defectdojo_api_generated.models.paginated_engagement_presets_list import PaginatedEngagementPresetsList
from defectdojo_api_generated.models.paginated_finding_list import PaginatedFindingList
from defectdojo_api_generated.models.paginated_finding_template_list import PaginatedFindingTemplateList
from defectdojo_api_generated.models.paginated_global_role_list import PaginatedGlobalRoleList
from defectdojo_api_generated.models.paginated_jira_instance_list import PaginatedJIRAInstanceList
from defectdojo_api_generated.models.paginated_jira_issue_list import PaginatedJIRAIssueList
from defectdojo_api_generated.models.paginated_jira_project_list import PaginatedJIRAProjectList
from defectdojo_api_generated.models.paginated_language_list import PaginatedLanguageList
from defectdojo_api_generated.models.paginated_language_type_list import PaginatedLanguageTypeList
from defectdojo_api_generated.models.paginated_meta_list import PaginatedMetaList
from defectdojo_api_generated.models.paginated_network_locations_list import PaginatedNetworkLocationsList
from defectdojo_api_generated.models.paginated_note_list import PaginatedNoteList
from defectdojo_api_generated.models.paginated_note_type_list import PaginatedNoteTypeList
from defectdojo_api_generated.models.paginated_notification_webhooks_list import PaginatedNotificationWebhooksList
from defectdojo_api_generated.models.paginated_notifications_list import PaginatedNotificationsList
from defectdojo_api_generated.models.paginated_product_api_scan_configuration_list import (
    PaginatedProductAPIScanConfigurationList,
)
from defectdojo_api_generated.models.paginated_product_api_scan_configuration_list_prefetch import (
    PaginatedProductAPIScanConfigurationListPrefetch,
)
from defectdojo_api_generated.models.paginated_product_group_list import PaginatedProductGroupList
from defectdojo_api_generated.models.paginated_product_group_list_prefetch import PaginatedProductGroupListPrefetch
from defectdojo_api_generated.models.paginated_product_list import PaginatedProductList
from defectdojo_api_generated.models.paginated_product_list_prefetch import PaginatedProductListPrefetch
from defectdojo_api_generated.models.paginated_product_member_list import PaginatedProductMemberList
from defectdojo_api_generated.models.paginated_product_member_list_prefetch import PaginatedProductMemberListPrefetch
from defectdojo_api_generated.models.paginated_product_type_group_list import PaginatedProductTypeGroupList
from defectdojo_api_generated.models.paginated_product_type_group_list_prefetch import (
    PaginatedProductTypeGroupListPrefetch,
)
from defectdojo_api_generated.models.paginated_product_type_list import PaginatedProductTypeList
from defectdojo_api_generated.models.paginated_product_type_list_prefetch import PaginatedProductTypeListPrefetch
from defectdojo_api_generated.models.paginated_product_type_member_list import PaginatedProductTypeMemberList
from defectdojo_api_generated.models.paginated_product_type_member_list_prefetch import (
    PaginatedProductTypeMemberListPrefetch,
)
from defectdojo_api_generated.models.paginated_questionnaire_answer_list import PaginatedQuestionnaireAnswerList
from defectdojo_api_generated.models.paginated_questionnaire_answered_survey_list import (
    PaginatedQuestionnaireAnsweredSurveyList,
)
from defectdojo_api_generated.models.paginated_questionnaire_answered_survey_list_prefetch import (
    PaginatedQuestionnaireAnsweredSurveyListPrefetch,
)
from defectdojo_api_generated.models.paginated_questionnaire_engagement_survey_list import (
    PaginatedQuestionnaireEngagementSurveyList,
)
from defectdojo_api_generated.models.paginated_questionnaire_general_survey_list import (
    PaginatedQuestionnaireGeneralSurveyList,
)
from defectdojo_api_generated.models.paginated_questionnaire_question_list import PaginatedQuestionnaireQuestionList
from defectdojo_api_generated.models.paginated_regulation_list import PaginatedRegulationList
from defectdojo_api_generated.models.paginated_risk_acceptance_list import PaginatedRiskAcceptanceList
from defectdojo_api_generated.models.paginated_role_list import PaginatedRoleList
from defectdojo_api_generated.models.paginated_sla_configuration_list import PaginatedSLAConfigurationList
from defectdojo_api_generated.models.paginated_sonarqube_issue_list import PaginatedSonarqubeIssueList
from defectdojo_api_generated.models.paginated_sonarqube_issue_transition_list import (
    PaginatedSonarqubeIssueTransitionList,
)
from defectdojo_api_generated.models.paginated_stub_finding_list import PaginatedStubFindingList
from defectdojo_api_generated.models.paginated_system_settings_list import PaginatedSystemSettingsList
from defectdojo_api_generated.models.paginated_test_import_list import PaginatedTestImportList
from defectdojo_api_generated.models.paginated_test_list import PaginatedTestList
from defectdojo_api_generated.models.paginated_test_type_list import PaginatedTestTypeList
from defectdojo_api_generated.models.paginated_tool_configuration_list import PaginatedToolConfigurationList
from defectdojo_api_generated.models.paginated_tool_configuration_list_prefetch import (
    PaginatedToolConfigurationListPrefetch,
)
from defectdojo_api_generated.models.paginated_tool_product_settings_list import PaginatedToolProductSettingsList
from defectdojo_api_generated.models.paginated_tool_product_settings_list_prefetch import (
    PaginatedToolProductSettingsListPrefetch,
)
from defectdojo_api_generated.models.paginated_tool_type_list import PaginatedToolTypeList
from defectdojo_api_generated.models.paginated_user_contact_info_list import PaginatedUserContactInfoList
from defectdojo_api_generated.models.paginated_user_contact_info_list_prefetch import (
    PaginatedUserContactInfoListPrefetch,
)
from defectdojo_api_generated.models.paginated_user_list import PaginatedUserList
from defectdojo_api_generated.models.patched_announcement_request import PatchedAnnouncementRequest
from defectdojo_api_generated.models.patched_app_analysis_request import PatchedAppAnalysisRequest
from defectdojo_api_generated.models.patched_burp_raw_request_response_multi_request import (
    PatchedBurpRawRequestResponseMultiRequest,
)
from defectdojo_api_generated.models.patched_credential_mapping_request import PatchedCredentialMappingRequest
from defectdojo_api_generated.models.patched_credential_request import PatchedCredentialRequest
from defectdojo_api_generated.models.patched_development_environment_request import PatchedDevelopmentEnvironmentRequest
from defectdojo_api_generated.models.patched_dojo_group_request import PatchedDojoGroupRequest
from defectdojo_api_generated.models.patched_endpoint_request import PatchedEndpointRequest
from defectdojo_api_generated.models.patched_endpoint_status_request import PatchedEndpointStatusRequest
from defectdojo_api_generated.models.patched_engagement_presets_request import PatchedEngagementPresetsRequest
from defectdojo_api_generated.models.patched_engagement_request import PatchedEngagementRequest
from defectdojo_api_generated.models.patched_finding_note_request import PatchedFindingNoteRequest
from defectdojo_api_generated.models.patched_finding_request import PatchedFindingRequest
from defectdojo_api_generated.models.patched_finding_template_request import PatchedFindingTemplateRequest
from defectdojo_api_generated.models.patched_global_role_request import PatchedGlobalRoleRequest
from defectdojo_api_generated.models.patched_jira_instance_request import PatchedJIRAInstanceRequest
from defectdojo_api_generated.models.patched_jira_issue_request import PatchedJIRAIssueRequest
from defectdojo_api_generated.models.patched_jira_project_request import PatchedJIRAProjectRequest
from defectdojo_api_generated.models.patched_language_request import PatchedLanguageRequest
from defectdojo_api_generated.models.patched_language_type_request import PatchedLanguageTypeRequest
from defectdojo_api_generated.models.patched_meta_main_request import PatchedMetaMainRequest
from defectdojo_api_generated.models.patched_meta_request import PatchedMetaRequest
from defectdojo_api_generated.models.patched_network_locations_request import PatchedNetworkLocationsRequest
from defectdojo_api_generated.models.patched_note_request import PatchedNoteRequest
from defectdojo_api_generated.models.patched_note_type_request import PatchedNoteTypeRequest
from defectdojo_api_generated.models.patched_notification_webhooks_request import PatchedNotificationWebhooksRequest
from defectdojo_api_generated.models.patched_notifications_request import PatchedNotificationsRequest
from defectdojo_api_generated.models.patched_product_api_scan_configuration_request import (
    PatchedProductAPIScanConfigurationRequest,
)
from defectdojo_api_generated.models.patched_product_request import PatchedProductRequest
from defectdojo_api_generated.models.patched_product_type_request import PatchedProductTypeRequest
from defectdojo_api_generated.models.patched_regulation_request import PatchedRegulationRequest
from defectdojo_api_generated.models.patched_risk_acceptance_request import PatchedRiskAcceptanceRequest
from defectdojo_api_generated.models.patched_sla_configuration_request import PatchedSLAConfigurationRequest
from defectdojo_api_generated.models.patched_sonarqube_issue_request import PatchedSonarqubeIssueRequest
from defectdojo_api_generated.models.patched_sonarqube_issue_transition_request import (
    PatchedSonarqubeIssueTransitionRequest,
)
from defectdojo_api_generated.models.patched_stub_finding_request import PatchedStubFindingRequest
from defectdojo_api_generated.models.patched_system_settings_request import PatchedSystemSettingsRequest
from defectdojo_api_generated.models.patched_tag_request import PatchedTagRequest
from defectdojo_api_generated.models.patched_test_import_request import PatchedTestImportRequest
from defectdojo_api_generated.models.patched_test_request import PatchedTestRequest
from defectdojo_api_generated.models.patched_test_type_request import PatchedTestTypeRequest
from defectdojo_api_generated.models.patched_tool_configuration_request import PatchedToolConfigurationRequest
from defectdojo_api_generated.models.patched_tool_product_settings_request import PatchedToolProductSettingsRequest
from defectdojo_api_generated.models.patched_tool_type_request import PatchedToolTypeRequest
from defectdojo_api_generated.models.patched_user_contact_info_request import PatchedUserContactInfoRequest
from defectdojo_api_generated.models.patched_user_request import PatchedUserRequest
from defectdojo_api_generated.models.product import Product
from defectdojo_api_generated.models.product_api_scan_configuration import ProductAPIScanConfiguration
from defectdojo_api_generated.models.product_api_scan_configuration_request import ProductAPIScanConfigurationRequest
from defectdojo_api_generated.models.product_group import ProductGroup
from defectdojo_api_generated.models.product_group_request import ProductGroupRequest
from defectdojo_api_generated.models.product_member import ProductMember
from defectdojo_api_generated.models.product_member_request import ProductMemberRequest
from defectdojo_api_generated.models.product_meta import ProductMeta
from defectdojo_api_generated.models.product_meta_request import ProductMetaRequest
from defectdojo_api_generated.models.product_request import ProductRequest
from defectdojo_api_generated.models.product_type import ProductType
from defectdojo_api_generated.models.product_type_group import ProductTypeGroup
from defectdojo_api_generated.models.product_type_group_request import ProductTypeGroupRequest
from defectdojo_api_generated.models.product_type_member import ProductTypeMember
from defectdojo_api_generated.models.product_type_member_request import ProductTypeMemberRequest
from defectdojo_api_generated.models.product_type_request import ProductTypeRequest
from defectdojo_api_generated.models.questionnaire_answer import QuestionnaireAnswer
from defectdojo_api_generated.models.questionnaire_answered_survey import QuestionnaireAnsweredSurvey
from defectdojo_api_generated.models.questionnaire_engagement_survey import QuestionnaireEngagementSurvey
from defectdojo_api_generated.models.questionnaire_general_survey import QuestionnaireGeneralSurvey
from defectdojo_api_generated.models.questionnaire_question import QuestionnaireQuestion
from defectdojo_api_generated.models.raw_file import RawFile
from defectdojo_api_generated.models.re_import_scan import ReImportScan
from defectdojo_api_generated.models.regulation import Regulation
from defectdojo_api_generated.models.regulation_request import RegulationRequest
from defectdojo_api_generated.models.report_generate import ReportGenerate
from defectdojo_api_generated.models.report_generate_option_request import ReportGenerateOptionRequest
from defectdojo_api_generated.models.risk_acceptance import RiskAcceptance
from defectdojo_api_generated.models.risk_acceptance_proof import RiskAcceptanceProof
from defectdojo_api_generated.models.risk_acceptance_request import RiskAcceptanceRequest
from defectdojo_api_generated.models.role import Role
from defectdojo_api_generated.models.sla_configuration import SLAConfiguration
from defectdojo_api_generated.models.sla_configuration_request import SLAConfigurationRequest
from defectdojo_api_generated.models.severity_status_statistics import SeverityStatusStatistics
from defectdojo_api_generated.models.severity_status_statistics_request import SeverityStatusStatisticsRequest
from defectdojo_api_generated.models.sonarqube_issue import SonarqubeIssue
from defectdojo_api_generated.models.sonarqube_issue_request import SonarqubeIssueRequest
from defectdojo_api_generated.models.sonarqube_issue_transition import SonarqubeIssueTransition
from defectdojo_api_generated.models.sonarqube_issue_transition_request import SonarqubeIssueTransitionRequest
from defectdojo_api_generated.models.status_statistics import StatusStatistics
from defectdojo_api_generated.models.status_statistics_request import StatusStatisticsRequest
from defectdojo_api_generated.models.stub_finding import StubFinding
from defectdojo_api_generated.models.stub_finding_create import StubFindingCreate
from defectdojo_api_generated.models.stub_finding_create_request import StubFindingCreateRequest
from defectdojo_api_generated.models.stub_finding_request import StubFindingRequest
from defectdojo_api_generated.models.system_settings import SystemSettings
from defectdojo_api_generated.models.system_settings_request import SystemSettingsRequest
from defectdojo_api_generated.models.tag import Tag
from defectdojo_api_generated.models.tag_request import TagRequest
from defectdojo_api_generated.models.test import Test
from defectdojo_api_generated.models.test_create import TestCreate
from defectdojo_api_generated.models.test_create_request import TestCreateRequest
from defectdojo_api_generated.models.test_import import TestImport
from defectdojo_api_generated.models.test_import_finding_action import TestImportFindingAction
from defectdojo_api_generated.models.test_import_finding_action_request import TestImportFindingActionRequest
from defectdojo_api_generated.models.test_import_request import TestImportRequest
from defectdojo_api_generated.models.test_request import TestRequest
from defectdojo_api_generated.models.test_to_files import TestToFiles
from defectdojo_api_generated.models.test_to_notes import TestToNotes
from defectdojo_api_generated.models.test_type import TestType
from defectdojo_api_generated.models.test_type_request import TestTypeRequest
from defectdojo_api_generated.models.tool_configuration import ToolConfiguration
from defectdojo_api_generated.models.tool_configuration_request import ToolConfigurationRequest
from defectdojo_api_generated.models.tool_product_settings import ToolProductSettings
from defectdojo_api_generated.models.tool_product_settings_request import ToolProductSettingsRequest
from defectdojo_api_generated.models.tool_type import ToolType
from defectdojo_api_generated.models.tool_type_request import ToolTypeRequest
from defectdojo_api_generated.models.user import User
from defectdojo_api_generated.models.user_contact_info import UserContactInfo
from defectdojo_api_generated.models.user_contact_info_request import UserContactInfoRequest
from defectdojo_api_generated.models.user_profile import UserProfile
from defectdojo_api_generated.models.user_request import UserRequest
from defectdojo_api_generated.models.user_stub import UserStub
from defectdojo_api_generated.models.user_stub_request import UserStubRequest
from defectdojo_api_generated.models.vulnerability_id import VulnerabilityId
from defectdojo_api_generated.models.vulnerability_id_request import VulnerabilityIdRequest
from defectdojo_api_generated.models.vulnerability_id_template import VulnerabilityIdTemplate
from defectdojo_api_generated.models.vulnerability_id_template_request import VulnerabilityIdTemplateRequest
