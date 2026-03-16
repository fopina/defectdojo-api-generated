## v 2.56.1 (from v 2.46.2)

### New

#### Endpoints
- `DELETE /api/v2/asset_api_scan_configurations/{id}/`
- `DELETE /api/v2/asset_groups/{id}/`
- `DELETE /api/v2/asset_members/{id}/`
- `DELETE /api/v2/assets/{id}/`
- `DELETE /api/v2/organization_groups/{id}/`
- `DELETE /api/v2/organization_members/{id}/`
- `DELETE /api/v2/organizations/{id}/`
- `GET /api/v2/asset_api_scan_configurations/`
- `GET /api/v2/asset_api_scan_configurations/{id}/`
- `GET /api/v2/asset_api_scan_configurations/{id}/delete_preview/`
- `GET /api/v2/asset_groups/`
- `GET /api/v2/asset_groups/{id}/`
- `GET /api/v2/asset_groups/{id}/delete_preview/`
- `GET /api/v2/asset_members/`
- `GET /api/v2/asset_members/{id}/`
- `GET /api/v2/asset_members/{id}/delete_preview/`
- `GET /api/v2/assets/`
- `GET /api/v2/assets/{id}/`
- `GET /api/v2/assets/{id}/delete_preview/`
- `GET /api/v2/organization_groups/`
- `GET /api/v2/organization_groups/{id}/`
- `GET /api/v2/organization_groups/{id}/delete_preview/`
- `GET /api/v2/organization_members/`
- `GET /api/v2/organization_members/{id}/`
- `GET /api/v2/organization_members/{id}/delete_preview/`
- `GET /api/v2/organizations/`
- `GET /api/v2/organizations/{id}/`
- `GET /api/v2/organizations/{id}/delete_preview/`
- `PATCH /api/v2/asset_api_scan_configurations/{id}/`
- `PATCH /api/v2/assets/{id}/`
- `PATCH /api/v2/organizations/{id}/`
- `POST /api/v2/asset_api_scan_configurations/`
- `POST /api/v2/asset_groups/`
- `POST /api/v2/asset_members/`
- `POST /api/v2/assets/`
- `POST /api/v2/assets/{id}/generate_report/`
- `POST /api/v2/organization_groups/`
- `POST /api/v2/organization_members/`
- `POST /api/v2/organizations/`
- `POST /api/v2/organizations/{id}/generate_report/`
- `POST /api/v2/users/{id}/reset_api_token/`
- `PUT /api/v2/asset_api_scan_configurations/{id}/`
- `PUT /api/v2/asset_groups/{id}/`
- `PUT /api/v2/asset_members/{id}/`
- `PUT /api/v2/assets/{id}/`
- `PUT /api/v2/organization_groups/{id}/`
- `PUT /api/v2/organization_members/{id}/`
- `PUT /api/v2/organizations/{id}/`

#### Models
- `Asset`
- `AssetAPIScanConfiguration`
- `AssetAPIScanConfigurationRequest`
- `AssetGroup`
- `AssetGroupRequest`
- `AssetMember`
- `AssetMemberRequest`
- `AssetRequest`
- `Organization`
- `OrganizationGroup`
- `OrganizationGroupRequest`
- `OrganizationMember`
- `OrganizationMemberRequest`
- `OrganizationRequest`
- `PaginatedAssetAPIScanConfigurationList`
- `PaginatedAssetGroupList`
- `PaginatedAssetList`
- `PaginatedAssetMemberList`
- `PaginatedOrganizationGroupList`
- `PaginatedOrganizationList`
- `PaginatedOrganizationMemberList`
- `PatchedAssetAPIScanConfigurationRequest`
- `PatchedAssetRequest`
- `PatchedOrganizationRequest`
- `TestTypeCreate`
- `TestTypeCreateRequest`

### Removed

#### Models
- `VulnerabilityIdTemplate`
- `VulnerabilityIdTemplateRequest`

### Changed

#### Endpoints
- `GET /api/v2/announcements/`
- `GET /api/v2/engagements/`
- `GET /api/v2/findings/`
- `GET /api/v2/metadata/`
- `GET /api/v2/products/`
- `GET /api/v2/questionnaire_answered_questionnaires/`
- `GET /api/v2/questionnaire_answered_questionnaires/{id}/`
- `GET /api/v2/questionnaire_answers/`
- `GET /api/v2/questionnaire_answers/{id}/`
- `GET /api/v2/questionnaire_engagement_questionnaires/`
- `GET /api/v2/questionnaire_engagement_questionnaires/{id}/`
- `GET /api/v2/questionnaire_general_questionnaires/`
- `GET /api/v2/questionnaire_general_questionnaires/{id}/`
- `GET /api/v2/questionnaire_questions/`
- `GET /api/v2/questionnaire_questions/{id}/`
- `GET /api/v2/risk_acceptance/`
- `GET /api/v2/test_imports/`
- `GET /api/v2/tests/`
- `GET /api/v2/user_contact_infos/`
- `GET /api/v2/users/`
- `POST /api/v2/findings/accept_risks/`
- `POST /api/v2/questionnaire_engagement_questionnaires/{id}/link_engagement/{engagement_id}/`
- `POST /api/v2/test_types/`
- `PUT /api/v2/test_types/{id}/`

#### Models
- `Announcement`
- `AnnouncementRequest`
- `Engagement`
- `EngagementRequest`
- `Finding`
- `FindingClose`
- `FindingCloseRequest`
- `FindingCreate`
- `FindingCreateRequest`
- `FindingEngagement`
- `FindingRequest`
- `FindingTemplate`
- `FindingTemplateRequest`
- `ImportScan`
- `ImportScanRequest`
- `JIRAInstance`
- `JIRAInstanceRequest`
- `Meta`
- `MetaRequest`
- `Notifications`
- `NotificationsRequest`
- `PatchedAnnouncementRequest`
- `PatchedEngagementRequest`
- `PatchedFindingRequest`
- `PatchedFindingTemplateRequest`
- `PatchedJIRAInstanceRequest`
- `PatchedMetaRequest`
- `PatchedNotificationsRequest`
- `PatchedProductRequest`
- `PatchedRegulationRequest`
- `PatchedRiskAcceptanceRequest`
- `PatchedSLAConfigurationRequest`
- `PatchedSystemSettingsRequest`
- `PatchedTestTypeRequest`
- `PatchedUserContactInfoRequest`
- `Product`
- `ProductRequest`
- `ProductType`
- `QuestionnaireGeneralSurvey`
- `ReImportScan`
- `ReImportScanRequest`
- `Regulation`
- `RegulationRequest`
- `RiskAcceptance`
- `RiskAcceptanceRequest`
- `SLAConfiguration`
- `SLAConfigurationRequest`
- `SystemSettings`
- `SystemSettingsRequest`
- `Test`
- `TestCreate`
- `TestImportFindingAction`
- `TestImportFindingActionRequest`
- `TestType`
- `TestTypeRequest`
- `User`
- `UserContactInfo`
- `UserContactInfoRequest`

## v 2.46.2 (from v 2.45.0)

### Changed

#### Endpoints
- `GET /api/v2/test_imports/`

#### Models
- `DeltaStatistics`
- `DeltaStatisticsRequest`
- `ImportScan`
- `ImportScanRequest`
- `JIRAInstance`
- `JIRAInstanceRequest`
- `PatchedJIRAInstanceRequest`
- `PatchedRiskAcceptanceRequest`
- `ReImportScan`
- `ReImportScanRequest`
- `RiskAcceptance`
- `RiskAcceptanceRequest`
- `TestImportFindingAction`
- `TestImportFindingActionRequest`

## v 2.45.0 (from v 2.44.4)

No changes

## v 2.44.4 (from v 2.44.1)

### Changed

#### Models
- `PatchedRegulationRequest`
- `Regulation`
- `RegulationRequest`

## v 2.44.1

First version - baseline.