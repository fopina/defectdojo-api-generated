# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from defectdojo_api_generated.models.import_statistics import ImportStatistics
from typing import Optional, Set
from typing_extensions import Self

class ReImportScan(BaseModel):
    """
    ReImportScan
    """ # noqa: E501
    scan_date: Optional[date] = Field(default=None, description="Scan completion date will be used on all findings.")
    minimum_severity: Optional[StrictStr] = Field(default='Info', description="Minimum severity level to be imported  * `Info` - Info * `Low` - Low * `Medium` - Medium * `High` - High * `Critical` - Critical")
    active: Optional[StrictBool] = Field(default=None, description="Force findings to be active/inactive or default to the original tool (None)")
    verified: Optional[StrictBool] = Field(default=None, description="Force findings to be verified/not verified or default to the original tool (None)")
    endpoint_to_add: Optional[StrictInt] = Field(default=None, description="Enter the ID of an Endpoint that is associated with the target Product. New Findings will be added to that Endpoint.")
    file: Optional[StrictStr] = None
    product_type_name: Optional[StrictStr] = None
    product_name: Optional[StrictStr] = None
    engagement_name: Optional[StrictStr] = None
    engagement_end_date: Optional[date] = Field(default=None, description="End Date for Engagement. Default is current time + 365 days. Required format year-month-day")
    source_code_management_uri: Optional[Annotated[str, Field(strict=True, max_length=600)]] = Field(default=None, description="Resource link to source code")
    test_title: Optional[StrictStr] = None
    auto_create_context: Optional[StrictBool] = None
    deduplication_on_engagement: Optional[StrictBool] = None
    lead: Optional[StrictInt] = None
    push_to_jira: Optional[StrictBool] = False
    environment: Optional[StrictStr] = None
    build_id: Optional[StrictStr] = Field(default=None, description="ID of the build that was scanned.")
    branch_tag: Optional[StrictStr] = Field(default=None, description="Branch or Tag that was scanned.")
    commit_hash: Optional[StrictStr] = Field(default=None, description="Commit that was scanned.")
    api_scan_configuration: Optional[StrictInt] = None
    service: Optional[StrictStr] = Field(default=None, description="A service is a self-contained piece of functionality within a Product. This is an optional field which is used in deduplication and closing of old findings when set. This affects the whole engagement/product depending on your deduplication scope.")
    group_by: Optional[StrictStr] = Field(default=None, description="Choose an option to automatically group new findings by the chosen option.  * `component_name` - Component Name * `component_name+component_version` - Component Name + Version * `file_path` - File path * `finding_title` - Finding Title")
    create_finding_groups_for_all_findings: Optional[StrictBool] = Field(default=True, description="If set to false, finding groups will only be created when there is more than one grouped finding")
    test_id: StrictInt
    engagement_id: StrictInt
    product_id: StrictInt
    product_type_id: StrictInt
    statistics: ImportStatistics
    apply_tags_to_findings: Optional[StrictBool] = Field(default=None, description="If set to True, the tags will be applied to the findings")
    apply_tags_to_endpoints: Optional[StrictBool] = Field(default=None, description="If set to True, the tags will be applied to the endpoints")
    do_not_reactivate: Optional[StrictBool] = Field(default=False, description="Select if the import should ignore active findings from the report, useful for triage-less scanners. Will keep existing findings closed, without reactivating them. For more information check the docs.")
    scan_type: StrictStr = Field(description="* `Acunetix Scan` - Acunetix Scan * `Anchore Engine Scan` - Anchore Engine Scan * `Anchore Enterprise Policy Check` - Anchore Enterprise Policy Check * `Anchore Grype` - Anchore Grype * `AnchoreCTL Policies Report` - AnchoreCTL Policies Report * `AnchoreCTL Vuln Report` - AnchoreCTL Vuln Report * `AppCheck Web Application Scanner` - AppCheck Web Application Scanner * `AppSpider Scan` - AppSpider Scan * `Aqua Scan` - Aqua Scan * `Arachni Scan` - Arachni Scan * `AuditJS Scan` - AuditJS Scan * `AWS Inspector2 Scan` - AWS Inspector2 Scan * `AWS Prowler Scan` - AWS Prowler Scan * `AWS Prowler V3` - AWS Prowler V3 * `AWS Security Finding Format (ASFF) Scan` - AWS Security Finding Format (ASFF) Scan * `AWS Security Hub Scan` - AWS Security Hub Scan * `Azure Security Center Recommendations Scan` - Azure Security Center Recommendations Scan * `Bandit Scan` - Bandit Scan * `Bearer CLI` - Bearer CLI * `BlackDuck API` - BlackDuck API * `Blackduck Binary Analysis` - Blackduck Binary Analysis * `Blackduck Component Risk` - Blackduck Component Risk * `Blackduck Hub Scan` - Blackduck Hub Scan * `Brakeman Scan` - Brakeman Scan * `Bugcrowd API Import` - Bugcrowd API Import * `BugCrowd Scan` - BugCrowd Scan * `Bundler-Audit Scan` - Bundler-Audit Scan * `Burp Dastardly Scan` - Burp Dastardly Scan * `Burp Enterprise Scan` - Burp Enterprise Scan * `Burp GraphQL API` - Burp GraphQL API * `Burp REST API` - Burp REST API * `Burp Scan` - Burp Scan * `CargoAudit Scan` - CargoAudit Scan * `Checkmarx CxFlow SAST` - Checkmarx CxFlow SAST * `Checkmarx One Scan` - Checkmarx One Scan * `Checkmarx OSA` - Checkmarx OSA * `Checkmarx Scan` - Checkmarx Scan * `Checkmarx Scan detailed` - Checkmarx Scan detailed * `Checkov Scan` - Checkov Scan * `Chef Inspect Log` - Chef Inspect Log * `Clair Scan` - Clair Scan * `Cloudsploit Scan` - Cloudsploit Scan * `Cobalt.io API Import` - Cobalt.io API Import * `Cobalt.io Scan` - Cobalt.io Scan * `Codechecker Report native` - Codechecker Report native * `Contrast Scan` - Contrast Scan * `Coverity API` - Coverity API * `Coverity Scan JSON Report` - Coverity Scan JSON Report * `Crashtest Security JSON File` - Crashtest Security JSON File * `Crashtest Security XML File` - Crashtest Security XML File * `CredScan Scan` - CredScan Scan * `Crunch42 Scan` - Crunch42 Scan * `CycloneDX Scan` - CycloneDX Scan * `DawnScanner Scan` - DawnScanner Scan * `Deepfence Threatmapper Report` - Deepfence Threatmapper Report * `Dependency Check Scan` - Dependency Check Scan * `Dependency Track Finding Packaging Format (FPF) Export` - Dependency Track Finding Packaging Format (FPF) Export * `Detect-secrets Scan` - Detect-secrets Scan * `docker-bench-security Scan` - docker-bench-security Scan * `Dockle Scan` - Dockle Scan * `DrHeader JSON Importer` - DrHeader JSON Importer * `DSOP Scan` - DSOP Scan * `Edgescan Scan` - Edgescan Scan * `ESLint Scan` - ESLint Scan * `Fortify Scan` - Fortify Scan * `Generic Findings Import` - Generic Findings Import * `Ggshield Scan` - Ggshield Scan * `Github Vulnerability Scan` - Github Vulnerability Scan * `GitLab API Fuzzing Report Scan` - GitLab API Fuzzing Report Scan * `GitLab Container Scan` - GitLab Container Scan * `GitLab DAST Report` - GitLab DAST Report * `GitLab Dependency Scanning Report` - GitLab Dependency Scanning Report * `GitLab SAST Report` - GitLab SAST Report * `GitLab Secret Detection Report` - GitLab Secret Detection Report * `Gitleaks Scan` - Gitleaks Scan * `Google Cloud Artifact Vulnerability Scan` - Google Cloud Artifact Vulnerability Scan * `Gosec Scanner` - Gosec Scanner * `Govulncheck Scanner` - Govulncheck Scanner * `HackerOne Cases` - HackerOne Cases * `Hadolint Dockerfile check` - Hadolint Dockerfile check * `Harbor Vulnerability Scan` - Harbor Vulnerability Scan * `HCL AppScan on Cloud SAST XML` - HCL AppScan on Cloud SAST XML * `HCLAppScan XML` - HCLAppScan XML * `Horusec Scan` - Horusec Scan * `Humble Json Importer` - Humble Json Importer * `HuskyCI Report` - HuskyCI Report * `Hydra Scan` - Hydra Scan * `IBM AppScan DAST` - IBM AppScan DAST * `Immuniweb Scan` - Immuniweb Scan * `IntSights Report` - IntSights Report * `Invicti Scan` - Invicti Scan * `JFrog Xray API Summary Artifact Scan` - JFrog Xray API Summary Artifact Scan * `JFrog Xray On Demand Binary Scan` - JFrog Xray On Demand Binary Scan * `JFrog Xray Scan` - JFrog Xray Scan * `JFrog Xray Unified Scan` - JFrog Xray Unified Scan * `KICS Scan` - KICS Scan * `Kiuwan SCA Scan` - Kiuwan SCA Scan * `Kiuwan Scan` - Kiuwan Scan * `KrakenD Audit Scan` - KrakenD Audit Scan * `kube-bench Scan` - kube-bench Scan * `Kubeaudit Scan` - Kubeaudit Scan * `KubeHunter Scan` - KubeHunter Scan * `Kubescape JSON Importer` - Kubescape JSON Importer * `Legitify Scan` - Legitify Scan * `Mend Scan` - Mend Scan * `Meterian Scan` - Meterian Scan * `Microfocus Webinspect Scan` - Microfocus Webinspect Scan * `MobSF Scan` - MobSF Scan * `MobSF Scorecard Scan` - MobSF Scorecard Scan * `Mobsfscan Scan` - Mobsfscan Scan * `Mozilla Observatory Scan` - Mozilla Observatory Scan * `MSDefender Parser` - MSDefender Parser * `Nancy Scan` - Nancy Scan * `Netsparker Scan` - Netsparker Scan * `NeuVector (compliance)` - NeuVector (compliance) * `NeuVector (REST)` - NeuVector (REST) * `Nexpose Scan` - Nexpose Scan * `Nikto Scan` - Nikto Scan * `Nmap Scan` - Nmap Scan * `Node Security Platform Scan` - Node Security Platform Scan * `Nosey Parker Scan` - Nosey Parker Scan * `NPM Audit Scan` - NPM Audit Scan * `NPM Audit v7+ Scan` - NPM Audit v7+ Scan * `Nuclei Scan` - Nuclei Scan * `Openscap Vulnerability Scan` - Openscap Vulnerability Scan * `OpenVAS Parser` - OpenVAS Parser * `ORT evaluated model Importer` - ORT evaluated model Importer * `OssIndex Devaudit SCA Scan Importer` - OssIndex Devaudit SCA Scan Importer * `OSV Scan` - OSV Scan * `Outpost24 Scan` - Outpost24 Scan * `PHP Security Audit v2` - PHP Security Audit v2 * `PHP Symfony Security Check` - PHP Symfony Security Check * `pip-audit Scan` - pip-audit Scan * `PMD Scan` - PMD Scan * `Popeye Scan` - Popeye Scan * `Progpilot Scan` - Progpilot Scan * `PTART Report` - PTART Report * `PWN SAST` - PWN SAST * `Qualys Hacker Guardian Scan` - Qualys Hacker Guardian Scan * `Qualys Infrastructure Scan (WebGUI XML)` - Qualys Infrastructure Scan (WebGUI XML) * `Qualys Scan` - Qualys Scan * `Qualys Webapp Scan` - Qualys Webapp Scan * `Rapplex Scan` - Rapplex Scan * `Red Hat Satellite` - Red Hat Satellite * `Retire.js Scan` - Retire.js Scan * `Risk Recon API Importer` - Risk Recon API Importer * `Rubocop Scan` - Rubocop Scan * `Rusty Hog Scan` - Rusty Hog Scan * `SARIF` - SARIF * `Scantist Scan` - Scantist Scan * `Scout Suite Scan` - Scout Suite Scan * `Semgrep JSON Report` - Semgrep JSON Report * `SKF Scan` - SKF Scan * `Snyk Code Scan` - Snyk Code Scan * `Snyk Scan` - Snyk Scan * `Solar Appscreener Scan` - Solar Appscreener Scan * `SonarQube API Import` - SonarQube API Import * `SonarQube Scan` - SonarQube Scan * `SonarQube Scan detailed` - SonarQube Scan detailed * `Sonatype Application Scan` - Sonatype Application Scan * `SpotBugs Scan` - SpotBugs Scan * `SSH Audit Importer` - SSH Audit Importer * `SSL Labs Scan` - SSL Labs Scan * `Sslscan` - Sslscan * `Sslyze Scan` - Sslyze Scan * `SSLyze Scan (JSON)` - SSLyze Scan (JSON) * `StackHawk HawkScan` - StackHawk HawkScan * `Sysdig Vulnerability Report` - Sysdig Vulnerability Report * `Talisman Scan` - Talisman Scan * `Tenable Scan` - Tenable Scan * `Terrascan Scan` - Terrascan Scan * `Testssl Scan` - Testssl Scan * `TFSec Scan` - TFSec Scan * `Threagile risks report` - Threagile risks report * `ThreatComposer Scan` - ThreatComposer Scan * `Trivy Operator Scan` - Trivy Operator Scan * `Trivy Scan` - Trivy Scan * `Trufflehog Scan` - Trufflehog Scan * `Trufflehog3 Scan` - Trufflehog3 Scan * `Trustwave Fusion API Scan` - Trustwave Fusion API Scan * `Trustwave Scan (CSV)` - Trustwave Scan (CSV) * `Twistlock Image Scan` - Twistlock Image Scan * `VCG Scan` - VCG Scan * `Veracode Scan` - Veracode Scan * `Veracode SourceClear Scan` - Veracode SourceClear Scan * `Vulners` - Vulners * `Wapiti Scan` - Wapiti Scan * `Wazuh` - Wazuh * `WFuzz JSON report` - WFuzz JSON report * `Whispers Scan` - Whispers Scan * `WhiteHat Sentinel` - WhiteHat Sentinel * `Wiz Scan` - Wiz Scan * `Wizcli Dir Scan` - Wizcli Dir Scan * `Wizcli IaC Scan` - Wizcli IaC Scan * `Wizcli Img Scan` - Wizcli Img Scan * `Wpscan` - Wpscan * `Xanitizer Scan` - Xanitizer Scan * `Yarn Audit Scan` - Yarn Audit Scan * `ZAP Scan` - ZAP Scan")
    test: Optional[StrictInt] = None
    close_old_findings: Optional[StrictBool] = Field(default=True, description="Select if old findings no longer present in the report get closed as mitigated when importing.")
    close_old_findings_product_scope: Optional[StrictBool] = Field(default=False, description="Select if close_old_findings applies to all findings of the same type in the product. By default, it is false meaning that only old findings of the same type in the engagement are in scope. Note that this only applies on the first call to reimport-scan.")
    version: Optional[StrictStr] = Field(default=None, description="Version that will be set on existing Test object. Leave empty to leave existing value in place.")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Modify existing tags that help describe this scan. (Existing test tags will be overwritten)")
    __properties: ClassVar[List[str]] = ["scan_date", "minimum_severity", "active", "verified", "endpoint_to_add", "file", "product_type_name", "product_name", "engagement_name", "engagement_end_date", "source_code_management_uri", "test_title", "auto_create_context", "deduplication_on_engagement", "lead", "push_to_jira", "environment", "build_id", "branch_tag", "commit_hash", "api_scan_configuration", "service", "group_by", "create_finding_groups_for_all_findings", "test_id", "engagement_id", "product_id", "product_type_id", "statistics", "apply_tags_to_findings", "apply_tags_to_endpoints", "do_not_reactivate", "scan_type", "test", "close_old_findings", "close_old_findings_product_scope", "version", "tags"]

    @field_validator('minimum_severity')
    def minimum_severity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Info', 'Low', 'Medium', 'High', 'Critical']):
            raise ValueError("must be one of enum values ('Info', 'Low', 'Medium', 'High', 'Critical')")
        return value

    @field_validator('group_by')
    def group_by_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['component_name', 'component_name+component_version', 'file_path', 'finding_title']):
            raise ValueError("must be one of enum values ('component_name', 'component_name+component_version', 'file_path', 'finding_title')")
        return value

    @field_validator('scan_type')
    def scan_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Acunetix Scan', 'Anchore Engine Scan', 'Anchore Enterprise Policy Check', 'Anchore Grype', 'AnchoreCTL Policies Report', 'AnchoreCTL Vuln Report', 'AppCheck Web Application Scanner', 'AppSpider Scan', 'Aqua Scan', 'Arachni Scan', 'AuditJS Scan', 'AWS Inspector2 Scan', 'AWS Prowler Scan', 'AWS Prowler V3', 'AWS Security Finding Format (ASFF) Scan', 'AWS Security Hub Scan', 'Azure Security Center Recommendations Scan', 'Bandit Scan', 'Bearer CLI', 'BlackDuck API', 'Blackduck Binary Analysis', 'Blackduck Component Risk', 'Blackduck Hub Scan', 'Brakeman Scan', 'Bugcrowd API Import', 'BugCrowd Scan', 'Bundler-Audit Scan', 'Burp Dastardly Scan', 'Burp Enterprise Scan', 'Burp GraphQL API', 'Burp REST API', 'Burp Scan', 'CargoAudit Scan', 'Checkmarx CxFlow SAST', 'Checkmarx One Scan', 'Checkmarx OSA', 'Checkmarx Scan', 'Checkmarx Scan detailed', 'Checkov Scan', 'Chef Inspect Log', 'Clair Scan', 'Cloudsploit Scan', 'Cobalt.io API Import', 'Cobalt.io Scan', 'Codechecker Report native', 'Contrast Scan', 'Coverity API', 'Coverity Scan JSON Report', 'Crashtest Security JSON File', 'Crashtest Security XML File', 'CredScan Scan', 'Crunch42 Scan', 'CycloneDX Scan', 'DawnScanner Scan', 'Deepfence Threatmapper Report', 'Dependency Check Scan', 'Dependency Track Finding Packaging Format (FPF) Export', 'Detect-secrets Scan', 'docker-bench-security Scan', 'Dockle Scan', 'DrHeader JSON Importer', 'DSOP Scan', 'Edgescan Scan', 'ESLint Scan', 'Fortify Scan', 'Generic Findings Import', 'Ggshield Scan', 'Github Vulnerability Scan', 'GitLab API Fuzzing Report Scan', 'GitLab Container Scan', 'GitLab DAST Report', 'GitLab Dependency Scanning Report', 'GitLab SAST Report', 'GitLab Secret Detection Report', 'Gitleaks Scan', 'Google Cloud Artifact Vulnerability Scan', 'Gosec Scanner', 'Govulncheck Scanner', 'HackerOne Cases', 'Hadolint Dockerfile check', 'Harbor Vulnerability Scan', 'HCL AppScan on Cloud SAST XML', 'HCLAppScan XML', 'Horusec Scan', 'Humble Json Importer', 'HuskyCI Report', 'Hydra Scan', 'IBM AppScan DAST', 'Immuniweb Scan', 'IntSights Report', 'Invicti Scan', 'JFrog Xray API Summary Artifact Scan', 'JFrog Xray On Demand Binary Scan', 'JFrog Xray Scan', 'JFrog Xray Unified Scan', 'KICS Scan', 'Kiuwan SCA Scan', 'Kiuwan Scan', 'KrakenD Audit Scan', 'kube-bench Scan', 'Kubeaudit Scan', 'KubeHunter Scan', 'Kubescape JSON Importer', 'Legitify Scan', 'Mend Scan', 'Meterian Scan', 'Microfocus Webinspect Scan', 'MobSF Scan', 'MobSF Scorecard Scan', 'Mobsfscan Scan', 'Mozilla Observatory Scan', 'MSDefender Parser', 'Nancy Scan', 'Netsparker Scan', 'NeuVector (compliance)', 'NeuVector (REST)', 'Nexpose Scan', 'Nikto Scan', 'Nmap Scan', 'Node Security Platform Scan', 'Nosey Parker Scan', 'NPM Audit Scan', 'NPM Audit v7+ Scan', 'Nuclei Scan', 'Openscap Vulnerability Scan', 'OpenVAS Parser', 'ORT evaluated model Importer', 'OssIndex Devaudit SCA Scan Importer', 'OSV Scan', 'Outpost24 Scan', 'PHP Security Audit v2', 'PHP Symfony Security Check', 'pip-audit Scan', 'PMD Scan', 'Popeye Scan', 'Progpilot Scan', 'PTART Report', 'PWN SAST', 'Qualys Hacker Guardian Scan', 'Qualys Infrastructure Scan (WebGUI XML)', 'Qualys Scan', 'Qualys Webapp Scan', 'Rapplex Scan', 'Red Hat Satellite', 'Retire.js Scan', 'Risk Recon API Importer', 'Rubocop Scan', 'Rusty Hog Scan', 'SARIF', 'Scantist Scan', 'Scout Suite Scan', 'Semgrep JSON Report', 'SKF Scan', 'Snyk Code Scan', 'Snyk Scan', 'Solar Appscreener Scan', 'SonarQube API Import', 'SonarQube Scan', 'SonarQube Scan detailed', 'Sonatype Application Scan', 'SpotBugs Scan', 'SSH Audit Importer', 'SSL Labs Scan', 'Sslscan', 'Sslyze Scan', 'SSLyze Scan (JSON)', 'StackHawk HawkScan', 'Sysdig Vulnerability Report', 'Talisman Scan', 'Tenable Scan', 'Terrascan Scan', 'Testssl Scan', 'TFSec Scan', 'Threagile risks report', 'ThreatComposer Scan', 'Trivy Operator Scan', 'Trivy Scan', 'Trufflehog Scan', 'Trufflehog3 Scan', 'Trustwave Fusion API Scan', 'Trustwave Scan (CSV)', 'Twistlock Image Scan', 'VCG Scan', 'Veracode Scan', 'Veracode SourceClear Scan', 'Vulners', 'Wapiti Scan', 'Wazuh', 'WFuzz JSON report', 'Whispers Scan', 'WhiteHat Sentinel', 'Wiz Scan', 'Wizcli Dir Scan', 'Wizcli IaC Scan', 'Wizcli Img Scan', 'Wpscan', 'Xanitizer Scan', 'Yarn Audit Scan', 'ZAP Scan']):
            raise ValueError("must be one of enum values ('Acunetix Scan', 'Anchore Engine Scan', 'Anchore Enterprise Policy Check', 'Anchore Grype', 'AnchoreCTL Policies Report', 'AnchoreCTL Vuln Report', 'AppCheck Web Application Scanner', 'AppSpider Scan', 'Aqua Scan', 'Arachni Scan', 'AuditJS Scan', 'AWS Inspector2 Scan', 'AWS Prowler Scan', 'AWS Prowler V3', 'AWS Security Finding Format (ASFF) Scan', 'AWS Security Hub Scan', 'Azure Security Center Recommendations Scan', 'Bandit Scan', 'Bearer CLI', 'BlackDuck API', 'Blackduck Binary Analysis', 'Blackduck Component Risk', 'Blackduck Hub Scan', 'Brakeman Scan', 'Bugcrowd API Import', 'BugCrowd Scan', 'Bundler-Audit Scan', 'Burp Dastardly Scan', 'Burp Enterprise Scan', 'Burp GraphQL API', 'Burp REST API', 'Burp Scan', 'CargoAudit Scan', 'Checkmarx CxFlow SAST', 'Checkmarx One Scan', 'Checkmarx OSA', 'Checkmarx Scan', 'Checkmarx Scan detailed', 'Checkov Scan', 'Chef Inspect Log', 'Clair Scan', 'Cloudsploit Scan', 'Cobalt.io API Import', 'Cobalt.io Scan', 'Codechecker Report native', 'Contrast Scan', 'Coverity API', 'Coverity Scan JSON Report', 'Crashtest Security JSON File', 'Crashtest Security XML File', 'CredScan Scan', 'Crunch42 Scan', 'CycloneDX Scan', 'DawnScanner Scan', 'Deepfence Threatmapper Report', 'Dependency Check Scan', 'Dependency Track Finding Packaging Format (FPF) Export', 'Detect-secrets Scan', 'docker-bench-security Scan', 'Dockle Scan', 'DrHeader JSON Importer', 'DSOP Scan', 'Edgescan Scan', 'ESLint Scan', 'Fortify Scan', 'Generic Findings Import', 'Ggshield Scan', 'Github Vulnerability Scan', 'GitLab API Fuzzing Report Scan', 'GitLab Container Scan', 'GitLab DAST Report', 'GitLab Dependency Scanning Report', 'GitLab SAST Report', 'GitLab Secret Detection Report', 'Gitleaks Scan', 'Google Cloud Artifact Vulnerability Scan', 'Gosec Scanner', 'Govulncheck Scanner', 'HackerOne Cases', 'Hadolint Dockerfile check', 'Harbor Vulnerability Scan', 'HCL AppScan on Cloud SAST XML', 'HCLAppScan XML', 'Horusec Scan', 'Humble Json Importer', 'HuskyCI Report', 'Hydra Scan', 'IBM AppScan DAST', 'Immuniweb Scan', 'IntSights Report', 'Invicti Scan', 'JFrog Xray API Summary Artifact Scan', 'JFrog Xray On Demand Binary Scan', 'JFrog Xray Scan', 'JFrog Xray Unified Scan', 'KICS Scan', 'Kiuwan SCA Scan', 'Kiuwan Scan', 'KrakenD Audit Scan', 'kube-bench Scan', 'Kubeaudit Scan', 'KubeHunter Scan', 'Kubescape JSON Importer', 'Legitify Scan', 'Mend Scan', 'Meterian Scan', 'Microfocus Webinspect Scan', 'MobSF Scan', 'MobSF Scorecard Scan', 'Mobsfscan Scan', 'Mozilla Observatory Scan', 'MSDefender Parser', 'Nancy Scan', 'Netsparker Scan', 'NeuVector (compliance)', 'NeuVector (REST)', 'Nexpose Scan', 'Nikto Scan', 'Nmap Scan', 'Node Security Platform Scan', 'Nosey Parker Scan', 'NPM Audit Scan', 'NPM Audit v7+ Scan', 'Nuclei Scan', 'Openscap Vulnerability Scan', 'OpenVAS Parser', 'ORT evaluated model Importer', 'OssIndex Devaudit SCA Scan Importer', 'OSV Scan', 'Outpost24 Scan', 'PHP Security Audit v2', 'PHP Symfony Security Check', 'pip-audit Scan', 'PMD Scan', 'Popeye Scan', 'Progpilot Scan', 'PTART Report', 'PWN SAST', 'Qualys Hacker Guardian Scan', 'Qualys Infrastructure Scan (WebGUI XML)', 'Qualys Scan', 'Qualys Webapp Scan', 'Rapplex Scan', 'Red Hat Satellite', 'Retire.js Scan', 'Risk Recon API Importer', 'Rubocop Scan', 'Rusty Hog Scan', 'SARIF', 'Scantist Scan', 'Scout Suite Scan', 'Semgrep JSON Report', 'SKF Scan', 'Snyk Code Scan', 'Snyk Scan', 'Solar Appscreener Scan', 'SonarQube API Import', 'SonarQube Scan', 'SonarQube Scan detailed', 'Sonatype Application Scan', 'SpotBugs Scan', 'SSH Audit Importer', 'SSL Labs Scan', 'Sslscan', 'Sslyze Scan', 'SSLyze Scan (JSON)', 'StackHawk HawkScan', 'Sysdig Vulnerability Report', 'Talisman Scan', 'Tenable Scan', 'Terrascan Scan', 'Testssl Scan', 'TFSec Scan', 'Threagile risks report', 'ThreatComposer Scan', 'Trivy Operator Scan', 'Trivy Scan', 'Trufflehog Scan', 'Trufflehog3 Scan', 'Trustwave Fusion API Scan', 'Trustwave Scan (CSV)', 'Twistlock Image Scan', 'VCG Scan', 'Veracode Scan', 'Veracode SourceClear Scan', 'Vulners', 'Wapiti Scan', 'Wazuh', 'WFuzz JSON report', 'Whispers Scan', 'WhiteHat Sentinel', 'Wiz Scan', 'Wizcli Dir Scan', 'Wizcli IaC Scan', 'Wizcli Img Scan', 'Wpscan', 'Xanitizer Scan', 'Yarn Audit Scan', 'ZAP Scan')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ReImportScan from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "test_id",
            "engagement_id",
            "product_id",
            "product_type_id",
            "statistics",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        # set to None if lead (nullable) is None
        # and model_fields_set contains the field
        if self.lead is None and "lead" in self.model_fields_set:
            _dict['lead'] = None

        # set to None if api_scan_configuration (nullable) is None
        # and model_fields_set contains the field
        if self.api_scan_configuration is None and "api_scan_configuration" in self.model_fields_set:
            _dict['api_scan_configuration'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReImportScan from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "scan_date": obj.get("scan_date"),
            "minimum_severity": obj.get("minimum_severity") if obj.get("minimum_severity") is not None else 'Info',
            "active": obj.get("active"),
            "verified": obj.get("verified"),
            "endpoint_to_add": obj.get("endpoint_to_add"),
            "file": obj.get("file"),
            "product_type_name": obj.get("product_type_name"),
            "product_name": obj.get("product_name"),
            "engagement_name": obj.get("engagement_name"),
            "engagement_end_date": obj.get("engagement_end_date"),
            "source_code_management_uri": obj.get("source_code_management_uri"),
            "test_title": obj.get("test_title"),
            "auto_create_context": obj.get("auto_create_context"),
            "deduplication_on_engagement": obj.get("deduplication_on_engagement"),
            "lead": obj.get("lead"),
            "push_to_jira": obj.get("push_to_jira") if obj.get("push_to_jira") is not None else False,
            "environment": obj.get("environment"),
            "build_id": obj.get("build_id"),
            "branch_tag": obj.get("branch_tag"),
            "commit_hash": obj.get("commit_hash"),
            "api_scan_configuration": obj.get("api_scan_configuration"),
            "service": obj.get("service"),
            "group_by": obj.get("group_by"),
            "create_finding_groups_for_all_findings": obj.get("create_finding_groups_for_all_findings") if obj.get("create_finding_groups_for_all_findings") is not None else True,
            "test_id": obj.get("test_id"),
            "engagement_id": obj.get("engagement_id"),
            "product_id": obj.get("product_id"),
            "product_type_id": obj.get("product_type_id"),
            "statistics": ImportStatistics.from_dict(obj["statistics"]) if obj.get("statistics") is not None else None,
            "apply_tags_to_findings": obj.get("apply_tags_to_findings"),
            "apply_tags_to_endpoints": obj.get("apply_tags_to_endpoints"),
            "do_not_reactivate": obj.get("do_not_reactivate") if obj.get("do_not_reactivate") is not None else False,
            "scan_type": obj.get("scan_type"),
            "test": obj.get("test"),
            "close_old_findings": obj.get("close_old_findings") if obj.get("close_old_findings") is not None else True,
            "close_old_findings_product_scope": obj.get("close_old_findings_product_scope") if obj.get("close_old_findings_product_scope") is not None else False,
            "version": obj.get("version"),
            "tags": obj.get("tags")
        })
        return _obj


