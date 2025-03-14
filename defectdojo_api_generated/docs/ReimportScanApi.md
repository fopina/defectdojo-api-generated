# defectdojo_api_generated.ReimportScanApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reimport_scan_create**](ReimportScanApi.md#reimport_scan_create) | **POST** /api/v2/reimport-scan/ | 


# **reimport_scan_create**
> ReImportScan reimport_scan_create(scan_type, scan_date=scan_date, minimum_severity=minimum_severity, active=active, verified=verified, endpoint_to_add=endpoint_to_add, file=file, product_type_name=product_type_name, product_name=product_name, engagement_name=engagement_name, engagement_end_date=engagement_end_date, source_code_management_uri=source_code_management_uri, test_title=test_title, auto_create_context=auto_create_context, deduplication_on_engagement=deduplication_on_engagement, lead=lead, push_to_jira=push_to_jira, environment=environment, build_id=build_id, branch_tag=branch_tag, commit_hash=commit_hash, api_scan_configuration=api_scan_configuration, service=service, group_by=group_by, create_finding_groups_for_all_findings=create_finding_groups_for_all_findings, apply_tags_to_findings=apply_tags_to_findings, apply_tags_to_endpoints=apply_tags_to_endpoints, do_not_reactivate=do_not_reactivate, test=test, close_old_findings=close_old_findings, close_old_findings_product_scope=close_old_findings_product_scope, version=version, tags=tags)

Reimports a scan report into an existing test.

By ID:
- Create a Product (or use an existing product)
- Create an Engagement inside the product
- Import a scan report and find the id of the Test
- Provide this in the `test` parameter

By Names:
- Create a Product (or use an existing product)
- Create an Engagement inside the product
- Import a report which will create a Test
- Provide `product_name`
- Provide `engagement_name`
- Optional: Provide `test_title`

In this scenario Defect Dojo will look up the Test by the provided details.
If no `test_title` is provided, the latest test inside the engagement will be chosen based on scan_type.

When using names you can let the importer automatically create Engagements, Products and Product_Types
by using `auto_create_context=True`.

When `auto_create_context` is set to `True` you can use `deduplication_on_engagement` to restrict deduplication for
imported Findings to the newly created Engagement.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.re_import_scan import ReImportScan
from defectdojo_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = defectdojo_api_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = defectdojo_api_generated.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with defectdojo_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = defectdojo_api_generated.ReimportScanApi(api_client)
    scan_type = 'scan_type_example' # str | * `Acunetix Scan` - Acunetix Scan * `Anchore Engine Scan` - Anchore Engine Scan * `Anchore Enterprise Policy Check` - Anchore Enterprise Policy Check * `Anchore Grype` - Anchore Grype * `AnchoreCTL Policies Report` - AnchoreCTL Policies Report * `AnchoreCTL Vuln Report` - AnchoreCTL Vuln Report * `AppCheck Web Application Scanner` - AppCheck Web Application Scanner * `AppSpider Scan` - AppSpider Scan * `Aqua Scan` - Aqua Scan * `Arachni Scan` - Arachni Scan * `AuditJS Scan` - AuditJS Scan * `AWS Inspector2 Scan` - AWS Inspector2 Scan * `AWS Prowler Scan` - AWS Prowler Scan * `AWS Prowler V3` - AWS Prowler V3 * `AWS Security Finding Format (ASFF) Scan` - AWS Security Finding Format (ASFF) Scan * `AWS Security Hub Scan` - AWS Security Hub Scan * `Azure Security Center Recommendations Scan` - Azure Security Center Recommendations Scan * `Bandit Scan` - Bandit Scan * `Bearer CLI` - Bearer CLI * `BlackDuck API` - BlackDuck API * `Blackduck Binary Analysis` - Blackduck Binary Analysis * `Blackduck Component Risk` - Blackduck Component Risk * `Blackduck Hub Scan` - Blackduck Hub Scan * `Brakeman Scan` - Brakeman Scan * `Bugcrowd API Import` - Bugcrowd API Import * `BugCrowd Scan` - BugCrowd Scan * `Bundler-Audit Scan` - Bundler-Audit Scan * `Burp Dastardly Scan` - Burp Dastardly Scan * `Burp Enterprise Scan` - Burp Enterprise Scan * `Burp GraphQL API` - Burp GraphQL API * `Burp REST API` - Burp REST API * `Burp Scan` - Burp Scan * `CargoAudit Scan` - CargoAudit Scan * `Checkmarx CxFlow SAST` - Checkmarx CxFlow SAST * `Checkmarx One Scan` - Checkmarx One Scan * `Checkmarx OSA` - Checkmarx OSA * `Checkmarx Scan` - Checkmarx Scan * `Checkmarx Scan detailed` - Checkmarx Scan detailed * `Checkov Scan` - Checkov Scan * `Chef Inspect Log` - Chef Inspect Log * `Clair Scan` - Clair Scan * `Cloudsploit Scan` - Cloudsploit Scan * `Cobalt.io API Import` - Cobalt.io API Import * `Cobalt.io Scan` - Cobalt.io Scan * `Codechecker Report native` - Codechecker Report native * `Contrast Scan` - Contrast Scan * `Coverity API` - Coverity API * `Coverity Scan JSON Report` - Coverity Scan JSON Report * `Crashtest Security JSON File` - Crashtest Security JSON File * `Crashtest Security XML File` - Crashtest Security XML File * `CredScan Scan` - CredScan Scan * `Crunch42 Scan` - Crunch42 Scan * `CycloneDX Scan` - CycloneDX Scan * `DawnScanner Scan` - DawnScanner Scan * `Deepfence Threatmapper Report` - Deepfence Threatmapper Report * `Dependency Check Scan` - Dependency Check Scan * `Dependency Track Finding Packaging Format (FPF) Export` - Dependency Track Finding Packaging Format (FPF) Export * `Detect-secrets Scan` - Detect-secrets Scan * `docker-bench-security Scan` - docker-bench-security Scan * `Dockle Scan` - Dockle Scan * `DrHeader JSON Importer` - DrHeader JSON Importer * `DSOP Scan` - DSOP Scan * `Edgescan Scan` - Edgescan Scan * `ESLint Scan` - ESLint Scan * `Fortify Scan` - Fortify Scan * `Generic Findings Import` - Generic Findings Import * `Ggshield Scan` - Ggshield Scan * `Github Vulnerability Scan` - Github Vulnerability Scan * `GitLab API Fuzzing Report Scan` - GitLab API Fuzzing Report Scan * `GitLab Container Scan` - GitLab Container Scan * `GitLab DAST Report` - GitLab DAST Report * `GitLab Dependency Scanning Report` - GitLab Dependency Scanning Report * `GitLab SAST Report` - GitLab SAST Report * `GitLab Secret Detection Report` - GitLab Secret Detection Report * `Gitleaks Scan` - Gitleaks Scan * `Google Cloud Artifact Vulnerability Scan` - Google Cloud Artifact Vulnerability Scan * `Gosec Scanner` - Gosec Scanner * `Govulncheck Scanner` - Govulncheck Scanner * `HackerOne Cases` - HackerOne Cases * `Hadolint Dockerfile check` - Hadolint Dockerfile check * `Harbor Vulnerability Scan` - Harbor Vulnerability Scan * `HCL AppScan on Cloud SAST XML` - HCL AppScan on Cloud SAST XML * `HCLAppScan XML` - HCLAppScan XML * `Horusec Scan` - Horusec Scan * `Humble Json Importer` - Humble Json Importer * `HuskyCI Report` - HuskyCI Report * `Hydra Scan` - Hydra Scan * `IBM AppScan DAST` - IBM AppScan DAST * `Immuniweb Scan` - Immuniweb Scan * `IntSights Report` - IntSights Report * `Invicti Scan` - Invicti Scan * `JFrog Xray API Summary Artifact Scan` - JFrog Xray API Summary Artifact Scan * `JFrog Xray On Demand Binary Scan` - JFrog Xray On Demand Binary Scan * `JFrog Xray Scan` - JFrog Xray Scan * `JFrog Xray Unified Scan` - JFrog Xray Unified Scan * `KICS Scan` - KICS Scan * `Kiuwan SCA Scan` - Kiuwan SCA Scan * `Kiuwan Scan` - Kiuwan Scan * `KrakenD Audit Scan` - KrakenD Audit Scan * `kube-bench Scan` - kube-bench Scan * `Kubeaudit Scan` - Kubeaudit Scan * `KubeHunter Scan` - KubeHunter Scan * `Kubescape JSON Importer` - Kubescape JSON Importer * `Legitify Scan` - Legitify Scan * `Mend Scan` - Mend Scan * `Meterian Scan` - Meterian Scan * `Microfocus Webinspect Scan` - Microfocus Webinspect Scan * `MobSF Scan` - MobSF Scan * `MobSF Scorecard Scan` - MobSF Scorecard Scan * `Mobsfscan Scan` - Mobsfscan Scan * `Mozilla Observatory Scan` - Mozilla Observatory Scan * `MSDefender Parser` - MSDefender Parser * `Nancy Scan` - Nancy Scan * `Netsparker Scan` - Netsparker Scan * `NeuVector (compliance)` - NeuVector (compliance) * `NeuVector (REST)` - NeuVector (REST) * `Nexpose Scan` - Nexpose Scan * `Nikto Scan` - Nikto Scan * `Nmap Scan` - Nmap Scan * `Node Security Platform Scan` - Node Security Platform Scan * `Nosey Parker Scan` - Nosey Parker Scan * `NPM Audit Scan` - NPM Audit Scan * `NPM Audit v7+ Scan` - NPM Audit v7+ Scan * `Nuclei Scan` - Nuclei Scan * `Openscap Vulnerability Scan` - Openscap Vulnerability Scan * `OpenVAS Parser` - OpenVAS Parser * `ORT evaluated model Importer` - ORT evaluated model Importer * `OssIndex Devaudit SCA Scan Importer` - OssIndex Devaudit SCA Scan Importer * `OSV Scan` - OSV Scan * `Outpost24 Scan` - Outpost24 Scan * `PHP Security Audit v2` - PHP Security Audit v2 * `PHP Symfony Security Check` - PHP Symfony Security Check * `pip-audit Scan` - pip-audit Scan * `PMD Scan` - PMD Scan * `Popeye Scan` - Popeye Scan * `Progpilot Scan` - Progpilot Scan * `PTART Report` - PTART Report * `PWN SAST` - PWN SAST * `Qualys Hacker Guardian Scan` - Qualys Hacker Guardian Scan * `Qualys Infrastructure Scan (WebGUI XML)` - Qualys Infrastructure Scan (WebGUI XML) * `Qualys Scan` - Qualys Scan * `Qualys Webapp Scan` - Qualys Webapp Scan * `Rapplex Scan` - Rapplex Scan * `Red Hat Satellite` - Red Hat Satellite * `Retire.js Scan` - Retire.js Scan * `Risk Recon API Importer` - Risk Recon API Importer * `Rubocop Scan` - Rubocop Scan * `Rusty Hog Scan` - Rusty Hog Scan * `SARIF` - SARIF * `Scantist Scan` - Scantist Scan * `Scout Suite Scan` - Scout Suite Scan * `Semgrep JSON Report` - Semgrep JSON Report * `SKF Scan` - SKF Scan * `Snyk Code Scan` - Snyk Code Scan * `Snyk Scan` - Snyk Scan * `Solar Appscreener Scan` - Solar Appscreener Scan * `SonarQube API Import` - SonarQube API Import * `SonarQube Scan` - SonarQube Scan * `SonarQube Scan detailed` - SonarQube Scan detailed * `Sonatype Application Scan` - Sonatype Application Scan * `SpotBugs Scan` - SpotBugs Scan * `SSH Audit Importer` - SSH Audit Importer * `SSL Labs Scan` - SSL Labs Scan * `Sslscan` - Sslscan * `Sslyze Scan` - Sslyze Scan * `SSLyze Scan (JSON)` - SSLyze Scan (JSON) * `StackHawk HawkScan` - StackHawk HawkScan * `Sysdig Vulnerability Report` - Sysdig Vulnerability Report * `Talisman Scan` - Talisman Scan * `Tenable Scan` - Tenable Scan * `Terrascan Scan` - Terrascan Scan * `Testssl Scan` - Testssl Scan * `TFSec Scan` - TFSec Scan * `Threagile risks report` - Threagile risks report * `ThreatComposer Scan` - ThreatComposer Scan * `Trivy Operator Scan` - Trivy Operator Scan * `Trivy Scan` - Trivy Scan * `Trufflehog Scan` - Trufflehog Scan * `Trufflehog3 Scan` - Trufflehog3 Scan * `Trustwave Fusion API Scan` - Trustwave Fusion API Scan * `Trustwave Scan (CSV)` - Trustwave Scan (CSV) * `Twistlock Image Scan` - Twistlock Image Scan * `VCG Scan` - VCG Scan * `Veracode Scan` - Veracode Scan * `Veracode SourceClear Scan` - Veracode SourceClear Scan * `Vulners` - Vulners * `Wapiti Scan` - Wapiti Scan * `Wazuh` - Wazuh * `WFuzz JSON report` - WFuzz JSON report * `Whispers Scan` - Whispers Scan * `WhiteHat Sentinel` - WhiteHat Sentinel * `Wiz Scan` - Wiz Scan * `Wizcli Dir Scan` - Wizcli Dir Scan * `Wizcli IaC Scan` - Wizcli IaC Scan * `Wizcli Img Scan` - Wizcli Img Scan * `Wpscan` - Wpscan * `Xanitizer Scan` - Xanitizer Scan * `Yarn Audit Scan` - Yarn Audit Scan * `ZAP Scan` - ZAP Scan
    scan_date = '2013-10-20' # date | Scan completion date will be used on all findings. (optional)
    minimum_severity = Info # str | Minimum severity level to be imported  * `Info` - Info * `Low` - Low * `Medium` - Medium * `High` - High * `Critical` - Critical (optional) (default to Info)
    active = True # bool | Force findings to be active/inactive or default to the original tool (None) (optional)
    verified = True # bool | Force findings to be verified/not verified or default to the original tool (None) (optional)
    endpoint_to_add = 56 # int | Enter the ID of an Endpoint that is associated with the target Product. New Findings will be added to that Endpoint. (optional)
    file = None # bytearray |  (optional)
    product_type_name = 'product_type_name_example' # str |  (optional)
    product_name = 'product_name_example' # str |  (optional)
    engagement_name = 'engagement_name_example' # str |  (optional)
    engagement_end_date = '2013-10-20' # date | End Date for Engagement. Default is current time + 365 days. Required format year-month-day (optional)
    source_code_management_uri = 'source_code_management_uri_example' # str | Resource link to source code (optional)
    test_title = 'test_title_example' # str |  (optional)
    auto_create_context = True # bool |  (optional)
    deduplication_on_engagement = True # bool |  (optional)
    lead = 56 # int |  (optional)
    push_to_jira = False # bool |  (optional) (default to False)
    environment = 'environment_example' # str |  (optional)
    build_id = 'build_id_example' # str | ID of the build that was scanned. (optional)
    branch_tag = 'branch_tag_example' # str | Branch or Tag that was scanned. (optional)
    commit_hash = 'commit_hash_example' # str | Commit that was scanned. (optional)
    api_scan_configuration = 56 # int |  (optional)
    service = 'service_example' # str | A service is a self-contained piece of functionality within a Product. This is an optional field which is used in deduplication and closing of old findings when set. This affects the whole engagement/product depending on your deduplication scope. (optional)
    group_by = 'group_by_example' # str | Choose an option to automatically group new findings by the chosen option.  * `component_name` - Component Name * `component_name+component_version` - Component Name + Version * `file_path` - File path * `finding_title` - Finding Title (optional)
    create_finding_groups_for_all_findings = True # bool | If set to false, finding groups will only be created when there is more than one grouped finding (optional) (default to True)
    apply_tags_to_findings = True # bool | If set to True, the tags will be applied to the findings (optional)
    apply_tags_to_endpoints = True # bool | If set to True, the tags will be applied to the endpoints (optional)
    do_not_reactivate = False # bool | Select if the import should ignore active findings from the report, useful for triage-less scanners. Will keep existing findings closed, without reactivating them. For more information check the docs. (optional) (default to False)
    test = 56 # int |  (optional)
    close_old_findings = True # bool | Select if old findings no longer present in the report get closed as mitigated when importing. (optional) (default to True)
    close_old_findings_product_scope = False # bool | Select if close_old_findings applies to all findings of the same type in the product. By default, it is false meaning that only old findings of the same type in the engagement are in scope. Note that this only applies on the first call to reimport-scan. (optional) (default to False)
    version = 'version_example' # str | Version that will be set on existing Test object. Leave empty to leave existing value in place. (optional)
    tags = ['tags_example'] # List[str] | Modify existing tags that help describe this scan. (Existing test tags will be overwritten) (optional)

    try:
        api_response = api_instance.reimport_scan_create(scan_type, scan_date=scan_date, minimum_severity=minimum_severity, active=active, verified=verified, endpoint_to_add=endpoint_to_add, file=file, product_type_name=product_type_name, product_name=product_name, engagement_name=engagement_name, engagement_end_date=engagement_end_date, source_code_management_uri=source_code_management_uri, test_title=test_title, auto_create_context=auto_create_context, deduplication_on_engagement=deduplication_on_engagement, lead=lead, push_to_jira=push_to_jira, environment=environment, build_id=build_id, branch_tag=branch_tag, commit_hash=commit_hash, api_scan_configuration=api_scan_configuration, service=service, group_by=group_by, create_finding_groups_for_all_findings=create_finding_groups_for_all_findings, apply_tags_to_findings=apply_tags_to_findings, apply_tags_to_endpoints=apply_tags_to_endpoints, do_not_reactivate=do_not_reactivate, test=test, close_old_findings=close_old_findings, close_old_findings_product_scope=close_old_findings_product_scope, version=version, tags=tags)
        print("The response of ReimportScanApi->reimport_scan_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReimportScanApi->reimport_scan_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_type** | **str**| * &#x60;Acunetix Scan&#x60; - Acunetix Scan * &#x60;Anchore Engine Scan&#x60; - Anchore Engine Scan * &#x60;Anchore Enterprise Policy Check&#x60; - Anchore Enterprise Policy Check * &#x60;Anchore Grype&#x60; - Anchore Grype * &#x60;AnchoreCTL Policies Report&#x60; - AnchoreCTL Policies Report * &#x60;AnchoreCTL Vuln Report&#x60; - AnchoreCTL Vuln Report * &#x60;AppCheck Web Application Scanner&#x60; - AppCheck Web Application Scanner * &#x60;AppSpider Scan&#x60; - AppSpider Scan * &#x60;Aqua Scan&#x60; - Aqua Scan * &#x60;Arachni Scan&#x60; - Arachni Scan * &#x60;AuditJS Scan&#x60; - AuditJS Scan * &#x60;AWS Inspector2 Scan&#x60; - AWS Inspector2 Scan * &#x60;AWS Prowler Scan&#x60; - AWS Prowler Scan * &#x60;AWS Prowler V3&#x60; - AWS Prowler V3 * &#x60;AWS Security Finding Format (ASFF) Scan&#x60; - AWS Security Finding Format (ASFF) Scan * &#x60;AWS Security Hub Scan&#x60; - AWS Security Hub Scan * &#x60;Azure Security Center Recommendations Scan&#x60; - Azure Security Center Recommendations Scan * &#x60;Bandit Scan&#x60; - Bandit Scan * &#x60;Bearer CLI&#x60; - Bearer CLI * &#x60;BlackDuck API&#x60; - BlackDuck API * &#x60;Blackduck Binary Analysis&#x60; - Blackduck Binary Analysis * &#x60;Blackduck Component Risk&#x60; - Blackduck Component Risk * &#x60;Blackduck Hub Scan&#x60; - Blackduck Hub Scan * &#x60;Brakeman Scan&#x60; - Brakeman Scan * &#x60;Bugcrowd API Import&#x60; - Bugcrowd API Import * &#x60;BugCrowd Scan&#x60; - BugCrowd Scan * &#x60;Bundler-Audit Scan&#x60; - Bundler-Audit Scan * &#x60;Burp Dastardly Scan&#x60; - Burp Dastardly Scan * &#x60;Burp Enterprise Scan&#x60; - Burp Enterprise Scan * &#x60;Burp GraphQL API&#x60; - Burp GraphQL API * &#x60;Burp REST API&#x60; - Burp REST API * &#x60;Burp Scan&#x60; - Burp Scan * &#x60;CargoAudit Scan&#x60; - CargoAudit Scan * &#x60;Checkmarx CxFlow SAST&#x60; - Checkmarx CxFlow SAST * &#x60;Checkmarx One Scan&#x60; - Checkmarx One Scan * &#x60;Checkmarx OSA&#x60; - Checkmarx OSA * &#x60;Checkmarx Scan&#x60; - Checkmarx Scan * &#x60;Checkmarx Scan detailed&#x60; - Checkmarx Scan detailed * &#x60;Checkov Scan&#x60; - Checkov Scan * &#x60;Chef Inspect Log&#x60; - Chef Inspect Log * &#x60;Clair Scan&#x60; - Clair Scan * &#x60;Cloudsploit Scan&#x60; - Cloudsploit Scan * &#x60;Cobalt.io API Import&#x60; - Cobalt.io API Import * &#x60;Cobalt.io Scan&#x60; - Cobalt.io Scan * &#x60;Codechecker Report native&#x60; - Codechecker Report native * &#x60;Contrast Scan&#x60; - Contrast Scan * &#x60;Coverity API&#x60; - Coverity API * &#x60;Coverity Scan JSON Report&#x60; - Coverity Scan JSON Report * &#x60;Crashtest Security JSON File&#x60; - Crashtest Security JSON File * &#x60;Crashtest Security XML File&#x60; - Crashtest Security XML File * &#x60;CredScan Scan&#x60; - CredScan Scan * &#x60;Crunch42 Scan&#x60; - Crunch42 Scan * &#x60;CycloneDX Scan&#x60; - CycloneDX Scan * &#x60;DawnScanner Scan&#x60; - DawnScanner Scan * &#x60;Deepfence Threatmapper Report&#x60; - Deepfence Threatmapper Report * &#x60;Dependency Check Scan&#x60; - Dependency Check Scan * &#x60;Dependency Track Finding Packaging Format (FPF) Export&#x60; - Dependency Track Finding Packaging Format (FPF) Export * &#x60;Detect-secrets Scan&#x60; - Detect-secrets Scan * &#x60;docker-bench-security Scan&#x60; - docker-bench-security Scan * &#x60;Dockle Scan&#x60; - Dockle Scan * &#x60;DrHeader JSON Importer&#x60; - DrHeader JSON Importer * &#x60;DSOP Scan&#x60; - DSOP Scan * &#x60;Edgescan Scan&#x60; - Edgescan Scan * &#x60;ESLint Scan&#x60; - ESLint Scan * &#x60;Fortify Scan&#x60; - Fortify Scan * &#x60;Generic Findings Import&#x60; - Generic Findings Import * &#x60;Ggshield Scan&#x60; - Ggshield Scan * &#x60;Github Vulnerability Scan&#x60; - Github Vulnerability Scan * &#x60;GitLab API Fuzzing Report Scan&#x60; - GitLab API Fuzzing Report Scan * &#x60;GitLab Container Scan&#x60; - GitLab Container Scan * &#x60;GitLab DAST Report&#x60; - GitLab DAST Report * &#x60;GitLab Dependency Scanning Report&#x60; - GitLab Dependency Scanning Report * &#x60;GitLab SAST Report&#x60; - GitLab SAST Report * &#x60;GitLab Secret Detection Report&#x60; - GitLab Secret Detection Report * &#x60;Gitleaks Scan&#x60; - Gitleaks Scan * &#x60;Google Cloud Artifact Vulnerability Scan&#x60; - Google Cloud Artifact Vulnerability Scan * &#x60;Gosec Scanner&#x60; - Gosec Scanner * &#x60;Govulncheck Scanner&#x60; - Govulncheck Scanner * &#x60;HackerOne Cases&#x60; - HackerOne Cases * &#x60;Hadolint Dockerfile check&#x60; - Hadolint Dockerfile check * &#x60;Harbor Vulnerability Scan&#x60; - Harbor Vulnerability Scan * &#x60;HCL AppScan on Cloud SAST XML&#x60; - HCL AppScan on Cloud SAST XML * &#x60;HCLAppScan XML&#x60; - HCLAppScan XML * &#x60;Horusec Scan&#x60; - Horusec Scan * &#x60;Humble Json Importer&#x60; - Humble Json Importer * &#x60;HuskyCI Report&#x60; - HuskyCI Report * &#x60;Hydra Scan&#x60; - Hydra Scan * &#x60;IBM AppScan DAST&#x60; - IBM AppScan DAST * &#x60;Immuniweb Scan&#x60; - Immuniweb Scan * &#x60;IntSights Report&#x60; - IntSights Report * &#x60;Invicti Scan&#x60; - Invicti Scan * &#x60;JFrog Xray API Summary Artifact Scan&#x60; - JFrog Xray API Summary Artifact Scan * &#x60;JFrog Xray On Demand Binary Scan&#x60; - JFrog Xray On Demand Binary Scan * &#x60;JFrog Xray Scan&#x60; - JFrog Xray Scan * &#x60;JFrog Xray Unified Scan&#x60; - JFrog Xray Unified Scan * &#x60;KICS Scan&#x60; - KICS Scan * &#x60;Kiuwan SCA Scan&#x60; - Kiuwan SCA Scan * &#x60;Kiuwan Scan&#x60; - Kiuwan Scan * &#x60;KrakenD Audit Scan&#x60; - KrakenD Audit Scan * &#x60;kube-bench Scan&#x60; - kube-bench Scan * &#x60;Kubeaudit Scan&#x60; - Kubeaudit Scan * &#x60;KubeHunter Scan&#x60; - KubeHunter Scan * &#x60;Kubescape JSON Importer&#x60; - Kubescape JSON Importer * &#x60;Legitify Scan&#x60; - Legitify Scan * &#x60;Mend Scan&#x60; - Mend Scan * &#x60;Meterian Scan&#x60; - Meterian Scan * &#x60;Microfocus Webinspect Scan&#x60; - Microfocus Webinspect Scan * &#x60;MobSF Scan&#x60; - MobSF Scan * &#x60;MobSF Scorecard Scan&#x60; - MobSF Scorecard Scan * &#x60;Mobsfscan Scan&#x60; - Mobsfscan Scan * &#x60;Mozilla Observatory Scan&#x60; - Mozilla Observatory Scan * &#x60;MSDefender Parser&#x60; - MSDefender Parser * &#x60;Nancy Scan&#x60; - Nancy Scan * &#x60;Netsparker Scan&#x60; - Netsparker Scan * &#x60;NeuVector (compliance)&#x60; - NeuVector (compliance) * &#x60;NeuVector (REST)&#x60; - NeuVector (REST) * &#x60;Nexpose Scan&#x60; - Nexpose Scan * &#x60;Nikto Scan&#x60; - Nikto Scan * &#x60;Nmap Scan&#x60; - Nmap Scan * &#x60;Node Security Platform Scan&#x60; - Node Security Platform Scan * &#x60;Nosey Parker Scan&#x60; - Nosey Parker Scan * &#x60;NPM Audit Scan&#x60; - NPM Audit Scan * &#x60;NPM Audit v7+ Scan&#x60; - NPM Audit v7+ Scan * &#x60;Nuclei Scan&#x60; - Nuclei Scan * &#x60;Openscap Vulnerability Scan&#x60; - Openscap Vulnerability Scan * &#x60;OpenVAS Parser&#x60; - OpenVAS Parser * &#x60;ORT evaluated model Importer&#x60; - ORT evaluated model Importer * &#x60;OssIndex Devaudit SCA Scan Importer&#x60; - OssIndex Devaudit SCA Scan Importer * &#x60;OSV Scan&#x60; - OSV Scan * &#x60;Outpost24 Scan&#x60; - Outpost24 Scan * &#x60;PHP Security Audit v2&#x60; - PHP Security Audit v2 * &#x60;PHP Symfony Security Check&#x60; - PHP Symfony Security Check * &#x60;pip-audit Scan&#x60; - pip-audit Scan * &#x60;PMD Scan&#x60; - PMD Scan * &#x60;Popeye Scan&#x60; - Popeye Scan * &#x60;Progpilot Scan&#x60; - Progpilot Scan * &#x60;PTART Report&#x60; - PTART Report * &#x60;PWN SAST&#x60; - PWN SAST * &#x60;Qualys Hacker Guardian Scan&#x60; - Qualys Hacker Guardian Scan * &#x60;Qualys Infrastructure Scan (WebGUI XML)&#x60; - Qualys Infrastructure Scan (WebGUI XML) * &#x60;Qualys Scan&#x60; - Qualys Scan * &#x60;Qualys Webapp Scan&#x60; - Qualys Webapp Scan * &#x60;Rapplex Scan&#x60; - Rapplex Scan * &#x60;Red Hat Satellite&#x60; - Red Hat Satellite * &#x60;Retire.js Scan&#x60; - Retire.js Scan * &#x60;Risk Recon API Importer&#x60; - Risk Recon API Importer * &#x60;Rubocop Scan&#x60; - Rubocop Scan * &#x60;Rusty Hog Scan&#x60; - Rusty Hog Scan * &#x60;SARIF&#x60; - SARIF * &#x60;Scantist Scan&#x60; - Scantist Scan * &#x60;Scout Suite Scan&#x60; - Scout Suite Scan * &#x60;Semgrep JSON Report&#x60; - Semgrep JSON Report * &#x60;SKF Scan&#x60; - SKF Scan * &#x60;Snyk Code Scan&#x60; - Snyk Code Scan * &#x60;Snyk Scan&#x60; - Snyk Scan * &#x60;Solar Appscreener Scan&#x60; - Solar Appscreener Scan * &#x60;SonarQube API Import&#x60; - SonarQube API Import * &#x60;SonarQube Scan&#x60; - SonarQube Scan * &#x60;SonarQube Scan detailed&#x60; - SonarQube Scan detailed * &#x60;Sonatype Application Scan&#x60; - Sonatype Application Scan * &#x60;SpotBugs Scan&#x60; - SpotBugs Scan * &#x60;SSH Audit Importer&#x60; - SSH Audit Importer * &#x60;SSL Labs Scan&#x60; - SSL Labs Scan * &#x60;Sslscan&#x60; - Sslscan * &#x60;Sslyze Scan&#x60; - Sslyze Scan * &#x60;SSLyze Scan (JSON)&#x60; - SSLyze Scan (JSON) * &#x60;StackHawk HawkScan&#x60; - StackHawk HawkScan * &#x60;Sysdig Vulnerability Report&#x60; - Sysdig Vulnerability Report * &#x60;Talisman Scan&#x60; - Talisman Scan * &#x60;Tenable Scan&#x60; - Tenable Scan * &#x60;Terrascan Scan&#x60; - Terrascan Scan * &#x60;Testssl Scan&#x60; - Testssl Scan * &#x60;TFSec Scan&#x60; - TFSec Scan * &#x60;Threagile risks report&#x60; - Threagile risks report * &#x60;ThreatComposer Scan&#x60; - ThreatComposer Scan * &#x60;Trivy Operator Scan&#x60; - Trivy Operator Scan * &#x60;Trivy Scan&#x60; - Trivy Scan * &#x60;Trufflehog Scan&#x60; - Trufflehog Scan * &#x60;Trufflehog3 Scan&#x60; - Trufflehog3 Scan * &#x60;Trustwave Fusion API Scan&#x60; - Trustwave Fusion API Scan * &#x60;Trustwave Scan (CSV)&#x60; - Trustwave Scan (CSV) * &#x60;Twistlock Image Scan&#x60; - Twistlock Image Scan * &#x60;VCG Scan&#x60; - VCG Scan * &#x60;Veracode Scan&#x60; - Veracode Scan * &#x60;Veracode SourceClear Scan&#x60; - Veracode SourceClear Scan * &#x60;Vulners&#x60; - Vulners * &#x60;Wapiti Scan&#x60; - Wapiti Scan * &#x60;Wazuh&#x60; - Wazuh * &#x60;WFuzz JSON report&#x60; - WFuzz JSON report * &#x60;Whispers Scan&#x60; - Whispers Scan * &#x60;WhiteHat Sentinel&#x60; - WhiteHat Sentinel * &#x60;Wiz Scan&#x60; - Wiz Scan * &#x60;Wizcli Dir Scan&#x60; - Wizcli Dir Scan * &#x60;Wizcli IaC Scan&#x60; - Wizcli IaC Scan * &#x60;Wizcli Img Scan&#x60; - Wizcli Img Scan * &#x60;Wpscan&#x60; - Wpscan * &#x60;Xanitizer Scan&#x60; - Xanitizer Scan * &#x60;Yarn Audit Scan&#x60; - Yarn Audit Scan * &#x60;ZAP Scan&#x60; - ZAP Scan | 
 **scan_date** | **date**| Scan completion date will be used on all findings. | [optional] 
 **minimum_severity** | **str**| Minimum severity level to be imported  * &#x60;Info&#x60; - Info * &#x60;Low&#x60; - Low * &#x60;Medium&#x60; - Medium * &#x60;High&#x60; - High * &#x60;Critical&#x60; - Critical | [optional] [default to Info]
 **active** | **bool**| Force findings to be active/inactive or default to the original tool (None) | [optional] 
 **verified** | **bool**| Force findings to be verified/not verified or default to the original tool (None) | [optional] 
 **endpoint_to_add** | **int**| Enter the ID of an Endpoint that is associated with the target Product. New Findings will be added to that Endpoint. | [optional] 
 **file** | **bytearray**|  | [optional] 
 **product_type_name** | **str**|  | [optional] 
 **product_name** | **str**|  | [optional] 
 **engagement_name** | **str**|  | [optional] 
 **engagement_end_date** | **date**| End Date for Engagement. Default is current time + 365 days. Required format year-month-day | [optional] 
 **source_code_management_uri** | **str**| Resource link to source code | [optional] 
 **test_title** | **str**|  | [optional] 
 **auto_create_context** | **bool**|  | [optional] 
 **deduplication_on_engagement** | **bool**|  | [optional] 
 **lead** | **int**|  | [optional] 
 **push_to_jira** | **bool**|  | [optional] [default to False]
 **environment** | **str**|  | [optional] 
 **build_id** | **str**| ID of the build that was scanned. | [optional] 
 **branch_tag** | **str**| Branch or Tag that was scanned. | [optional] 
 **commit_hash** | **str**| Commit that was scanned. | [optional] 
 **api_scan_configuration** | **int**|  | [optional] 
 **service** | **str**| A service is a self-contained piece of functionality within a Product. This is an optional field which is used in deduplication and closing of old findings when set. This affects the whole engagement/product depending on your deduplication scope. | [optional] 
 **group_by** | **str**| Choose an option to automatically group new findings by the chosen option.  * &#x60;component_name&#x60; - Component Name * &#x60;component_name+component_version&#x60; - Component Name + Version * &#x60;file_path&#x60; - File path * &#x60;finding_title&#x60; - Finding Title | [optional] 
 **create_finding_groups_for_all_findings** | **bool**| If set to false, finding groups will only be created when there is more than one grouped finding | [optional] [default to True]
 **apply_tags_to_findings** | **bool**| If set to True, the tags will be applied to the findings | [optional] 
 **apply_tags_to_endpoints** | **bool**| If set to True, the tags will be applied to the endpoints | [optional] 
 **do_not_reactivate** | **bool**| Select if the import should ignore active findings from the report, useful for triage-less scanners. Will keep existing findings closed, without reactivating them. For more information check the docs. | [optional] [default to False]
 **test** | **int**|  | [optional] 
 **close_old_findings** | **bool**| Select if old findings no longer present in the report get closed as mitigated when importing. | [optional] [default to True]
 **close_old_findings_product_scope** | **bool**| Select if close_old_findings applies to all findings of the same type in the product. By default, it is false meaning that only old findings of the same type in the engagement are in scope. Note that this only applies on the first call to reimport-scan. | [optional] [default to False]
 **version** | **str**| Version that will be set on existing Test object. Leave empty to leave existing value in place. | [optional] 
 **tags** | [**List[str]**](str.md)| Modify existing tags that help describe this scan. (Existing test tags will be overwritten) | [optional] 

### Return type

[**ReImportScan**](ReImportScan.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

