# defectdojo_api_generated.FindingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findings_accept_risks_create**](FindingsApi.md#findings_accept_risks_create) | **POST** /api/v2/findings/accept_risks/ | 
[**findings_close_create**](FindingsApi.md#findings_close_create) | **POST** /api/v2/findings/{id}/close/ | 
[**findings_create**](FindingsApi.md#findings_create) | **POST** /api/v2/findings/ | 
[**findings_delete_preview_list**](FindingsApi.md#findings_delete_preview_list) | **GET** /api/v2/findings/{id}/delete_preview/ | 
[**findings_destroy**](FindingsApi.md#findings_destroy) | **DELETE** /api/v2/findings/{id}/ | 
[**findings_duplicate_list**](FindingsApi.md#findings_duplicate_list) | **GET** /api/v2/findings/{id}/duplicate/ | 
[**findings_duplicate_reset_create**](FindingsApi.md#findings_duplicate_reset_create) | **POST** /api/v2/findings/{id}/duplicate/reset/ | 
[**findings_files_create**](FindingsApi.md#findings_files_create) | **POST** /api/v2/findings/{id}/files/ | 
[**findings_files_download_retrieve**](FindingsApi.md#findings_files_download_retrieve) | **GET** /api/v2/findings/{id}/files/download/{file_id}/ | 
[**findings_files_retrieve**](FindingsApi.md#findings_files_retrieve) | **GET** /api/v2/findings/{id}/files/ | 
[**findings_generate_report_create**](FindingsApi.md#findings_generate_report_create) | **POST** /api/v2/findings/generate_report/ | 
[**findings_list**](FindingsApi.md#findings_list) | **GET** /api/v2/findings/ | 
[**findings_metadata_create**](FindingsApi.md#findings_metadata_create) | **POST** /api/v2/findings/{id}/metadata/ | 
[**findings_metadata_destroy**](FindingsApi.md#findings_metadata_destroy) | **DELETE** /api/v2/findings/{id}/metadata/ | 
[**findings_metadata_list**](FindingsApi.md#findings_metadata_list) | **GET** /api/v2/findings/{id}/metadata/ | 
[**findings_metadata_update**](FindingsApi.md#findings_metadata_update) | **PUT** /api/v2/findings/{id}/metadata/ | 
[**findings_notes_create**](FindingsApi.md#findings_notes_create) | **POST** /api/v2/findings/{id}/notes/ | 
[**findings_notes_retrieve**](FindingsApi.md#findings_notes_retrieve) | **GET** /api/v2/findings/{id}/notes/ | 
[**findings_original_create**](FindingsApi.md#findings_original_create) | **POST** /api/v2/findings/{id}/original/{new_fid}/ | 
[**findings_partial_update**](FindingsApi.md#findings_partial_update) | **PATCH** /api/v2/findings/{id}/ | 
[**findings_remove_note_partial_update**](FindingsApi.md#findings_remove_note_partial_update) | **PATCH** /api/v2/findings/{id}/remove_note/ | 
[**findings_remove_tags_partial_update**](FindingsApi.md#findings_remove_tags_partial_update) | **PATCH** /api/v2/findings/{id}/remove_tags/ | 
[**findings_remove_tags_update**](FindingsApi.md#findings_remove_tags_update) | **PUT** /api/v2/findings/{id}/remove_tags/ | 
[**findings_request_response_create**](FindingsApi.md#findings_request_response_create) | **POST** /api/v2/findings/{id}/request_response/ | 
[**findings_request_response_retrieve**](FindingsApi.md#findings_request_response_retrieve) | **GET** /api/v2/findings/{id}/request_response/ | 
[**findings_retrieve**](FindingsApi.md#findings_retrieve) | **GET** /api/v2/findings/{id}/ | 
[**findings_tags_create**](FindingsApi.md#findings_tags_create) | **POST** /api/v2/findings/{id}/tags/ | 
[**findings_tags_retrieve**](FindingsApi.md#findings_tags_retrieve) | **GET** /api/v2/findings/{id}/tags/ | 
[**findings_update**](FindingsApi.md#findings_update) | **PUT** /api/v2/findings/{id}/ | 


# **findings_accept_risks_create**
> PaginatedRiskAcceptanceList findings_accept_risks_create(accepted_risk_request, active=active, component_name=component_name, component_version=component_version, created=created, cvssv3=cvssv3, cvssv3_score=cvssv3_score, cwe=cwe, var_date=var_date, defect_review_requested_by=defect_review_requested_by, description=description, discovered_after=discovered_after, discovered_before=discovered_before, discovered_on=discovered_on, duplicate=duplicate, duplicate_finding=duplicate_finding, dynamic_finding=dynamic_finding, effort_for_fixing=effort_for_fixing, endpoints=endpoints, epss_percentile_max=epss_percentile_max, epss_percentile_min=epss_percentile_min, epss_score_max=epss_score_max, epss_score_min=epss_score_min, false_p=false_p, file_path=file_path, finding_group=finding_group, found_by=found_by, has_jira=has_jira, has_tags=has_tags, hash_code=hash_code, id=id, impact=impact, inherited_tags=inherited_tags, is_mitigated=is_mitigated, jira_change=jira_change, jira_creation=jira_creation, last_reviewed=last_reviewed, last_reviewed_by=last_reviewed_by, last_status_update=last_status_update, limit=limit, mitigated=mitigated, mitigated_after=mitigated_after, mitigated_before=mitigated_before, mitigated_by=mitigated_by, mitigated_on=mitigated_on, mitigation=mitigation, nb_occurences=nb_occurences, not_tag=not_tag, not_tags=not_tags, not_test__engagement__product__tags=not_test__engagement__product__tags, not_test__engagement__tags=not_test__engagement__tags, not_test__tags=not_test__tags, numerical_severity=numerical_severity, o=o, offset=offset, out_of_scope=out_of_scope, outside_of_sla=outside_of_sla, param=param, payload=payload, planned_remediation_date=planned_remediation_date, planned_remediation_version=planned_remediation_version, product_lifecycle=product_lifecycle, product_name=product_name, product_name_contains=product_name_contains, publish_date=publish_date, references=references, reporter=reporter, review_requested_by=review_requested_by, reviewers=reviewers, risk_acceptance=risk_acceptance, risk_accepted=risk_accepted, sast_sink_object=sast_sink_object, sast_source_file_path=sast_source_file_path, sast_source_line=sast_source_line, sast_source_object=sast_source_object, scanner_confidence=scanner_confidence, service=service, severity=severity, severity_justification=severity_justification, sla_expiration_date=sla_expiration_date, sla_start_date=sla_start_date, sonarqube_issue=sonarqube_issue, static_finding=static_finding, steps_to_reproduce=steps_to_reproduce, tag=tag, tags=tags, tags__and=tags__and, test=test, test__engagement=test__engagement, test__engagement__product=test__engagement__product, test__engagement__product__prod_type=test__engagement__product__prod_type, test__engagement__product__tags=test__engagement__product__tags, test__engagement__product__tags__and=test__engagement__product__tags__and, test__engagement__tags=test__engagement__tags, test__engagement__tags__and=test__engagement__tags__and, test__tags=test__tags, test__tags__and=test__tags__and, test__test_type=test__test_type, title=title, under_defect_review=under_defect_review, under_review=under_review, unique_id_from_tool=unique_id_from_tool, verified=verified, vuln_id_from_tool=vuln_id_from_tool, vulnerability_id=vulnerability_id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.accepted_risk_request import AcceptedRiskRequest
from defectdojo_api_generated.models.paginated_risk_acceptance_list import PaginatedRiskAcceptanceList
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    accepted_risk_request = [defectdojo_api_generated.AcceptedRiskRequest()] # List[AcceptedRiskRequest] | 
    active = True # bool |  (optional)
    component_name = 'component_name_example' # str |  (optional)
    component_version = 'component_version_example' # str |  (optional)
    created = '2013-10-20T19:20:30+01:00' # datetime | The date the finding was created inside DefectDojo.  * `None` - Any date * `1` - Today * `2` - Past 7 days * `3` - Past 30 days * `4` - Past 90 days * `5` - Current month * `6` - Current year * `7` - Past year (optional)
    cvssv3 = 'cvssv3_example' # str |  (optional)
    cvssv3_score = 3.4 # float |  (optional)
    cwe = [56] # List[int] | Multiple values may be separated by commas. (optional)
    var_date = '2013-10-20' # date | The date the flaw was discovered.  * `None` - Any date * `1` - Today * `2` - Past 7 days * `3` - Past 30 days * `4` - Past 90 days * `5` - Current month * `6` - Current year * `7` - Past year (optional)
    defect_review_requested_by = [56] # List[int] | Multiple values may be separated by commas. (optional)
    description = 'description_example' # str |  (optional)
    discovered_after = '2013-10-20' # date |  (optional)
    discovered_before = '2013-10-20' # date |  (optional)
    discovered_on = '2013-10-20' # date |  (optional)
    duplicate = True # bool |  (optional)
    duplicate_finding = 56 # int |  (optional)
    dynamic_finding = True # bool |  (optional)
    effort_for_fixing = 'effort_for_fixing_example' # str |  (optional)
    endpoints = [56] # List[int] | Multiple values may be separated by commas. (optional)
    epss_percentile_max = 3.4 # float | The range of EPSS percentiles to filter on; the min input is a lower bound, the max is an upper bound. Leaving one empty will skip that bound (e.g., leaving the min bound input empty will filter only on the max bound -- filtering on \"less than or equal\"). Leading 0 required. (optional)
    epss_percentile_min = 3.4 # float | The range of EPSS percentiles to filter on; the min input is a lower bound, the max is an upper bound. Leaving one empty will skip that bound (e.g., leaving the min bound input empty will filter only on the max bound -- filtering on \"less than or equal\"). Leading 0 required. (optional)
    epss_score_max = 3.4 # float | The range of EPSS score percentages to filter on; the min input is a lower bound, the max is an upper bound. Leaving one empty will skip that bound (e.g., leaving the min bound input empty will filter only on the max bound -- filtering on \"less than or equal\"). Leading 0 required. (optional)
    epss_score_min = 3.4 # float | The range of EPSS score percentages to filter on; the min input is a lower bound, the max is an upper bound. Leaving one empty will skip that bound (e.g., leaving the min bound input empty will filter only on the max bound -- filtering on \"less than or equal\"). Leading 0 required. (optional)
    false_p = True # bool |  (optional)
    file_path = 'file_path_example' # str |  (optional)
    finding_group = [3.4] # List[float] | Multiple values may be separated by commas. (optional)
    found_by = [56] # List[int] | Multiple values may be separated by commas. (optional)
    has_jira = True # bool |  (optional)
    has_tags = True # bool | Has tags (optional)
    hash_code = 'hash_code_example' # str |  (optional)
    id = [56] # List[int] | Multiple values may be separated by commas. (optional)
    impact = 'impact_example' # str |  (optional)
    inherited_tags = [defectdojo_api_generated.List[int]()] # List[List[int]] | Internal use tags sepcifically for maintaining parity with product. This field will be present as a subset in the tags field (optional)
    is_mitigated = True # bool |  (optional)
    jira_change = '2013-10-20T19:20:30+01:00' # datetime | The date the linked Jira issue was last modified.  * `None` - Any date * `1` - Today * `2` - Past 7 days * `3` - Past 30 days * `4` - Past 90 days * `5` - Current month * `6` - Current year * `7` - Past year (optional)
    jira_creation = '2013-10-20T19:20:30+01:00' # datetime | The date a Jira issue was created from this finding.  * `None` - Any date * `1` - Today * `2` - Past 7 days * `3` - Past 30 days * `4` - Past 90 days * `5` - Current month * `6` - Current year * `7` - Past year (optional)
    last_reviewed = '2013-10-20T19:20:30+01:00' # datetime | Provides the date the flaw was last 'touched' by a tester.  * `None` - Any date * `1` - Today * `2` - Past 7 days * `3` - Past 30 days * `4` - Past 90 days * `5` - Current month * `6` - Current year * `7` - Past year (optional)
    last_reviewed_by = [56] # List[int] | Multiple values may be separated by commas. (optional)
    last_status_update = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    mitigated = '2013-10-20T19:20:30+01:00' # datetime | Denotes if this flaw has been fixed by storing the date it was fixed.  * `None` - Any date * `1` - Today * `2` - Past 7 days * `3` - Past 30 days * `4` - Past 90 days * `5` - Current month * `6` - Current year * `7` - Past year (optional)
    mitigated_after = '2013-10-20T19:20:30+01:00' # datetime | Mitigated After (optional)
    mitigated_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    mitigated_by = [56] # List[int] | Multiple values may be separated by commas. (optional)
    mitigated_on = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    mitigation = 'mitigation_example' # str |  (optional)
    nb_occurences = [56] # List[int] | Multiple values may be separated by commas. (optional)
    not_tag = 'not_tag_example' # str | Not Tag name contains (optional)
    not_tags = ['not_tags_example'] # List[str] | Comma separated list of exact tags not present on model (optional)
    not_test__engagement__product__tags = ['not_test__engagement__product__tags_example'] # List[str] | Comma separated list of exact tags not present on product (optional)
    not_test__engagement__tags = ['not_test__engagement__tags_example'] # List[str] | Comma separated list of exact tags not present on engagement (optional)
    not_test__tags = ['not_test__tags_example'] # List[str] | Comma separated list of exact tags present on test (optional)
    numerical_severity = 'numerical_severity_example' # str |  (optional)
    o = ['o_example'] # List[str] | Ordering  * `active` - Active * `-active` - Active (descending) * `component_name` - Component name * `-component_name` - Component name (descending) * `component_version` - Component version * `-component_version` - Component version (descending) * `created` - Created * `-created` - Created (descending) * `last_status_update` - Last status update * `-last_status_update` - Last status update (descending) * `last_reviewed` - Last reviewed * `-last_reviewed` - Last reviewed (descending) * `cwe` - Cwe * `-cwe` - Cwe (descending) * `date` - Date * `-date` - Date (descending) * `duplicate` - Duplicate * `-duplicate` - Duplicate (descending) * `dynamic_finding` - Dynamic finding * `-dynamic_finding` - Dynamic finding (descending) * `false_p` - False p * `-false_p` - False p (descending) * `found_by` - Found by * `-found_by` - Found by (descending) * `id` - Id * `-id` - Id (descending) * `is_mitigated` - Is mitigated * `-is_mitigated` - Is mitigated (descending) * `numerical_severity` - Numerical severity * `-numerical_severity` - Numerical severity (descending) * `out_of_scope` - Out of scope * `-out_of_scope` - Out of scope (descending) * `severity` - Severity * `-severity` - Severity (descending) * `reviewers` - Reviewers * `-reviewers` - Reviewers (descending) * `static_finding` - Static finding * `-static_finding` - Static finding (descending) * `test__engagement__product__name` - Test  engagement  product  name * `-test__engagement__product__name` - Test  engagement  product  name (descending) * `title` - Title * `-title` - Title (descending) * `under_defect_review` - Under defect review * `-under_defect_review` - Under defect review (descending) * `under_review` - Under review * `-under_review` - Under review (descending) * `verified` - Verified * `-verified` - Verified (descending) (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    out_of_scope = True # bool |  (optional)
    outside_of_sla = 3.4 # float |  (optional)
    param = 'param_example' # str |  (optional)
    payload = 'payload_example' # str |  (optional)
    planned_remediation_date = '2013-10-20' # date |  (optional)
    planned_remediation_version = 'planned_remediation_version_example' # str |  (optional)
    product_lifecycle = 'product_lifecycle_example' # str | Comma separated list of exact product lifecycles (optional)
    product_name = 'product_name_example' # str | exact product name (optional)
    product_name_contains = 'product_name_contains_example' # str | exact product name (optional)
    publish_date = '2013-10-20' # date |  (optional)
    references = 'references_example' # str |  (optional)
    reporter = [56] # List[int] | Multiple values may be separated by commas. (optional)
    review_requested_by = [56] # List[int] | Multiple values may be separated by commas. (optional)
    reviewers = [56] # List[int] | Multiple values may be separated by commas. (optional)
    risk_acceptance = 3.4 # float |  (optional)
    risk_accepted = True # bool |  (optional)
    sast_sink_object = 'sast_sink_object_example' # str |  (optional)
    sast_source_file_path = 'sast_source_file_path_example' # str |  (optional)
    sast_source_line = [56] # List[int] | Multiple values may be separated by commas. (optional)
    sast_source_object = 'sast_source_object_example' # str |  (optional)
    scanner_confidence = [56] # List[int] | Multiple values may be separated by commas. (optional)
    service = 'service_example' # str |  (optional)
    severity = 'severity_example' # str |  (optional)
    severity_justification = 'severity_justification_example' # str |  (optional)
    sla_expiration_date = '2013-10-20' # date |  (optional)
    sla_start_date = '2013-10-20' # date |  (optional)
    sonarqube_issue = [56] # List[int] | Multiple values may be separated by commas. (optional)
    static_finding = True # bool |  (optional)
    steps_to_reproduce = 'steps_to_reproduce_example' # str |  (optional)
    tag = 'tag_example' # str | Tag name contains (optional)
    tags = ['tags_example'] # List[str] | Comma separated list of exact tags (uses OR for multiple values) (optional)
    tags__and = ['tags__and_example'] # List[str] | Comma separated list of exact tags to match with an AND expression (optional)
    test = 56 # int |  (optional)
    test__engagement = [56] # List[int] | Multiple values may be separated by commas. (optional)
    test__engagement__product = [56] # List[int] | Multiple values may be separated by commas. (optional)
    test__engagement__product__prod_type = [56] # List[int] | Multiple values may be separated by commas. (optional)
    test__engagement__product__tags = ['test__engagement__product__tags_example'] # List[str] | Comma separated list of exact tags present on product (uses OR for multiple values) (optional)
    test__engagement__product__tags__and = ['test__engagement__product__tags__and_example'] # List[str] | Comma separated list of exact tags to match with an AND expression present on product (optional)
    test__engagement__tags = ['test__engagement__tags_example'] # List[str] | Comma separated list of exact tags present on engagement (uses OR for multiple values) (optional)
    test__engagement__tags__and = ['test__engagement__tags__and_example'] # List[str] | Comma separated list of exact tags to match with an AND expression present on engagement (optional)
    test__tags = ['test__tags_example'] # List[str] | Comma separated list of exact tags present on test (uses OR for multiple values) (optional)
    test__tags__and = ['test__tags__and_example'] # List[str] | Comma separated list of exact tags to match with an AND expression present on test (optional)
    test__test_type = [56] # List[int] | Multiple values may be separated by commas. (optional)
    title = 'title_example' # str |  (optional)
    under_defect_review = True # bool |  (optional)
    under_review = True # bool |  (optional)
    unique_id_from_tool = 'unique_id_from_tool_example' # str |  (optional)
    verified = True # bool |  (optional)
    vuln_id_from_tool = 'vuln_id_from_tool_example' # str |  (optional)
    vulnerability_id = 'vulnerability_id_example' # str |  (optional)

    try:
        api_response = api_instance.findings_accept_risks_create(accepted_risk_request, active=active, component_name=component_name, component_version=component_version, created=created, cvssv3=cvssv3, cvssv3_score=cvssv3_score, cwe=cwe, var_date=var_date, defect_review_requested_by=defect_review_requested_by, description=description, discovered_after=discovered_after, discovered_before=discovered_before, discovered_on=discovered_on, duplicate=duplicate, duplicate_finding=duplicate_finding, dynamic_finding=dynamic_finding, effort_for_fixing=effort_for_fixing, endpoints=endpoints, epss_percentile_max=epss_percentile_max, epss_percentile_min=epss_percentile_min, epss_score_max=epss_score_max, epss_score_min=epss_score_min, false_p=false_p, file_path=file_path, finding_group=finding_group, found_by=found_by, has_jira=has_jira, has_tags=has_tags, hash_code=hash_code, id=id, impact=impact, inherited_tags=inherited_tags, is_mitigated=is_mitigated, jira_change=jira_change, jira_creation=jira_creation, last_reviewed=last_reviewed, last_reviewed_by=last_reviewed_by, last_status_update=last_status_update, limit=limit, mitigated=mitigated, mitigated_after=mitigated_after, mitigated_before=mitigated_before, mitigated_by=mitigated_by, mitigated_on=mitigated_on, mitigation=mitigation, nb_occurences=nb_occurences, not_tag=not_tag, not_tags=not_tags, not_test__engagement__product__tags=not_test__engagement__product__tags, not_test__engagement__tags=not_test__engagement__tags, not_test__tags=not_test__tags, numerical_severity=numerical_severity, o=o, offset=offset, out_of_scope=out_of_scope, outside_of_sla=outside_of_sla, param=param, payload=payload, planned_remediation_date=planned_remediation_date, planned_remediation_version=planned_remediation_version, product_lifecycle=product_lifecycle, product_name=product_name, product_name_contains=product_name_contains, publish_date=publish_date, references=references, reporter=reporter, review_requested_by=review_requested_by, reviewers=reviewers, risk_acceptance=risk_acceptance, risk_accepted=risk_accepted, sast_sink_object=sast_sink_object, sast_source_file_path=sast_source_file_path, sast_source_line=sast_source_line, sast_source_object=sast_source_object, scanner_confidence=scanner_confidence, service=service, severity=severity, severity_justification=severity_justification, sla_expiration_date=sla_expiration_date, sla_start_date=sla_start_date, sonarqube_issue=sonarqube_issue, static_finding=static_finding, steps_to_reproduce=steps_to_reproduce, tag=tag, tags=tags, tags__and=tags__and, test=test, test__engagement=test__engagement, test__engagement__product=test__engagement__product, test__engagement__product__prod_type=test__engagement__product__prod_type, test__engagement__product__tags=test__engagement__product__tags, test__engagement__product__tags__and=test__engagement__product__tags__and, test__engagement__tags=test__engagement__tags, test__engagement__tags__and=test__engagement__tags__and, test__tags=test__tags, test__tags__and=test__tags__and, test__test_type=test__test_type, title=title, under_defect_review=under_defect_review, under_review=under_review, unique_id_from_tool=unique_id_from_tool, verified=verified, vuln_id_from_tool=vuln_id_from_tool, vulnerability_id=vulnerability_id)
        print("The response of FindingsApi->findings_accept_risks_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_accept_risks_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accepted_risk_request** | [**List[AcceptedRiskRequest]**](AcceptedRiskRequest.md)|  | 
 **active** | **bool**|  | [optional] 
 **component_name** | **str**|  | [optional] 
 **component_version** | **str**|  | [optional] 
 **created** | **datetime**| The date the finding was created inside DefectDojo.  * &#x60;None&#x60; - Any date * &#x60;1&#x60; - Today * &#x60;2&#x60; - Past 7 days * &#x60;3&#x60; - Past 30 days * &#x60;4&#x60; - Past 90 days * &#x60;5&#x60; - Current month * &#x60;6&#x60; - Current year * &#x60;7&#x60; - Past year | [optional] 
 **cvssv3** | **str**|  | [optional] 
 **cvssv3_score** | **float**|  | [optional] 
 **cwe** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **var_date** | **date**| The date the flaw was discovered.  * &#x60;None&#x60; - Any date * &#x60;1&#x60; - Today * &#x60;2&#x60; - Past 7 days * &#x60;3&#x60; - Past 30 days * &#x60;4&#x60; - Past 90 days * &#x60;5&#x60; - Current month * &#x60;6&#x60; - Current year * &#x60;7&#x60; - Past year | [optional] 
 **defect_review_requested_by** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **description** | **str**|  | [optional] 
 **discovered_after** | **date**|  | [optional] 
 **discovered_before** | **date**|  | [optional] 
 **discovered_on** | **date**|  | [optional] 
 **duplicate** | **bool**|  | [optional] 
 **duplicate_finding** | **int**|  | [optional] 
 **dynamic_finding** | **bool**|  | [optional] 
 **effort_for_fixing** | **str**|  | [optional] 
 **endpoints** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **epss_percentile_max** | **float**| The range of EPSS percentiles to filter on; the min input is a lower bound, the max is an upper bound. Leaving one empty will skip that bound (e.g., leaving the min bound input empty will filter only on the max bound -- filtering on \&quot;less than or equal\&quot;). Leading 0 required. | [optional] 
 **epss_percentile_min** | **float**| The range of EPSS percentiles to filter on; the min input is a lower bound, the max is an upper bound. Leaving one empty will skip that bound (e.g., leaving the min bound input empty will filter only on the max bound -- filtering on \&quot;less than or equal\&quot;). Leading 0 required. | [optional] 
 **epss_score_max** | **float**| The range of EPSS score percentages to filter on; the min input is a lower bound, the max is an upper bound. Leaving one empty will skip that bound (e.g., leaving the min bound input empty will filter only on the max bound -- filtering on \&quot;less than or equal\&quot;). Leading 0 required. | [optional] 
 **epss_score_min** | **float**| The range of EPSS score percentages to filter on; the min input is a lower bound, the max is an upper bound. Leaving one empty will skip that bound (e.g., leaving the min bound input empty will filter only on the max bound -- filtering on \&quot;less than or equal\&quot;). Leading 0 required. | [optional] 
 **false_p** | **bool**|  | [optional] 
 **file_path** | **str**|  | [optional] 
 **finding_group** | [**List[float]**](float.md)| Multiple values may be separated by commas. | [optional] 
 **found_by** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **has_jira** | **bool**|  | [optional] 
 **has_tags** | **bool**| Has tags | [optional] 
 **hash_code** | **str**|  | [optional] 
 **id** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **impact** | **str**|  | [optional] 
 **inherited_tags** | [**List[List[int]]**](List[int].md)| Internal use tags sepcifically for maintaining parity with product. This field will be present as a subset in the tags field | [optional] 
 **is_mitigated** | **bool**|  | [optional] 
 **jira_change** | **datetime**| The date the linked Jira issue was last modified.  * &#x60;None&#x60; - Any date * &#x60;1&#x60; - Today * &#x60;2&#x60; - Past 7 days * &#x60;3&#x60; - Past 30 days * &#x60;4&#x60; - Past 90 days * &#x60;5&#x60; - Current month * &#x60;6&#x60; - Current year * &#x60;7&#x60; - Past year | [optional] 
 **jira_creation** | **datetime**| The date a Jira issue was created from this finding.  * &#x60;None&#x60; - Any date * &#x60;1&#x60; - Today * &#x60;2&#x60; - Past 7 days * &#x60;3&#x60; - Past 30 days * &#x60;4&#x60; - Past 90 days * &#x60;5&#x60; - Current month * &#x60;6&#x60; - Current year * &#x60;7&#x60; - Past year | [optional] 
 **last_reviewed** | **datetime**| Provides the date the flaw was last &#39;touched&#39; by a tester.  * &#x60;None&#x60; - Any date * &#x60;1&#x60; - Today * &#x60;2&#x60; - Past 7 days * &#x60;3&#x60; - Past 30 days * &#x60;4&#x60; - Past 90 days * &#x60;5&#x60; - Current month * &#x60;6&#x60; - Current year * &#x60;7&#x60; - Past year | [optional] 
 **last_reviewed_by** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **last_status_update** | **datetime**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **mitigated** | **datetime**| Denotes if this flaw has been fixed by storing the date it was fixed.  * &#x60;None&#x60; - Any date * &#x60;1&#x60; - Today * &#x60;2&#x60; - Past 7 days * &#x60;3&#x60; - Past 30 days * &#x60;4&#x60; - Past 90 days * &#x60;5&#x60; - Current month * &#x60;6&#x60; - Current year * &#x60;7&#x60; - Past year | [optional] 
 **mitigated_after** | **datetime**| Mitigated After | [optional] 
 **mitigated_before** | **datetime**|  | [optional] 
 **mitigated_by** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **mitigated_on** | **datetime**|  | [optional] 
 **mitigation** | **str**|  | [optional] 
 **nb_occurences** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **not_tag** | **str**| Not Tag name contains | [optional] 
 **not_tags** | [**List[str]**](str.md)| Comma separated list of exact tags not present on model | [optional] 
 **not_test__engagement__product__tags** | [**List[str]**](str.md)| Comma separated list of exact tags not present on product | [optional] 
 **not_test__engagement__tags** | [**List[str]**](str.md)| Comma separated list of exact tags not present on engagement | [optional] 
 **not_test__tags** | [**List[str]**](str.md)| Comma separated list of exact tags present on test | [optional] 
 **numerical_severity** | **str**|  | [optional] 
 **o** | [**List[str]**](str.md)| Ordering  * &#x60;active&#x60; - Active * &#x60;-active&#x60; - Active (descending) * &#x60;component_name&#x60; - Component name * &#x60;-component_name&#x60; - Component name (descending) * &#x60;component_version&#x60; - Component version * &#x60;-component_version&#x60; - Component version (descending) * &#x60;created&#x60; - Created * &#x60;-created&#x60; - Created (descending) * &#x60;last_status_update&#x60; - Last status update * &#x60;-last_status_update&#x60; - Last status update (descending) * &#x60;last_reviewed&#x60; - Last reviewed * &#x60;-last_reviewed&#x60; - Last reviewed (descending) * &#x60;cwe&#x60; - Cwe * &#x60;-cwe&#x60; - Cwe (descending) * &#x60;date&#x60; - Date * &#x60;-date&#x60; - Date (descending) * &#x60;duplicate&#x60; - Duplicate * &#x60;-duplicate&#x60; - Duplicate (descending) * &#x60;dynamic_finding&#x60; - Dynamic finding * &#x60;-dynamic_finding&#x60; - Dynamic finding (descending) * &#x60;false_p&#x60; - False p * &#x60;-false_p&#x60; - False p (descending) * &#x60;found_by&#x60; - Found by * &#x60;-found_by&#x60; - Found by (descending) * &#x60;id&#x60; - Id * &#x60;-id&#x60; - Id (descending) * &#x60;is_mitigated&#x60; - Is mitigated * &#x60;-is_mitigated&#x60; - Is mitigated (descending) * &#x60;numerical_severity&#x60; - Numerical severity * &#x60;-numerical_severity&#x60; - Numerical severity (descending) * &#x60;out_of_scope&#x60; - Out of scope * &#x60;-out_of_scope&#x60; - Out of scope (descending) * &#x60;severity&#x60; - Severity * &#x60;-severity&#x60; - Severity (descending) * &#x60;reviewers&#x60; - Reviewers * &#x60;-reviewers&#x60; - Reviewers (descending) * &#x60;static_finding&#x60; - Static finding * &#x60;-static_finding&#x60; - Static finding (descending) * &#x60;test__engagement__product__name&#x60; - Test  engagement  product  name * &#x60;-test__engagement__product__name&#x60; - Test  engagement  product  name (descending) * &#x60;title&#x60; - Title * &#x60;-title&#x60; - Title (descending) * &#x60;under_defect_review&#x60; - Under defect review * &#x60;-under_defect_review&#x60; - Under defect review (descending) * &#x60;under_review&#x60; - Under review * &#x60;-under_review&#x60; - Under review (descending) * &#x60;verified&#x60; - Verified * &#x60;-verified&#x60; - Verified (descending) | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **out_of_scope** | **bool**|  | [optional] 
 **outside_of_sla** | **float**|  | [optional] 
 **param** | **str**|  | [optional] 
 **payload** | **str**|  | [optional] 
 **planned_remediation_date** | **date**|  | [optional] 
 **planned_remediation_version** | **str**|  | [optional] 
 **product_lifecycle** | **str**| Comma separated list of exact product lifecycles | [optional] 
 **product_name** | **str**| exact product name | [optional] 
 **product_name_contains** | **str**| exact product name | [optional] 
 **publish_date** | **date**|  | [optional] 
 **references** | **str**|  | [optional] 
 **reporter** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **review_requested_by** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **reviewers** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **risk_acceptance** | **float**|  | [optional] 
 **risk_accepted** | **bool**|  | [optional] 
 **sast_sink_object** | **str**|  | [optional] 
 **sast_source_file_path** | **str**|  | [optional] 
 **sast_source_line** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **sast_source_object** | **str**|  | [optional] 
 **scanner_confidence** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **service** | **str**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **severity_justification** | **str**|  | [optional] 
 **sla_expiration_date** | **date**|  | [optional] 
 **sla_start_date** | **date**|  | [optional] 
 **sonarqube_issue** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **static_finding** | **bool**|  | [optional] 
 **steps_to_reproduce** | **str**|  | [optional] 
 **tag** | **str**| Tag name contains | [optional] 
 **tags** | [**List[str]**](str.md)| Comma separated list of exact tags (uses OR for multiple values) | [optional] 
 **tags__and** | [**List[str]**](str.md)| Comma separated list of exact tags to match with an AND expression | [optional] 
 **test** | **int**|  | [optional] 
 **test__engagement** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **test__engagement__product** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **test__engagement__product__prod_type** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **test__engagement__product__tags** | [**List[str]**](str.md)| Comma separated list of exact tags present on product (uses OR for multiple values) | [optional] 
 **test__engagement__product__tags__and** | [**List[str]**](str.md)| Comma separated list of exact tags to match with an AND expression present on product | [optional] 
 **test__engagement__tags** | [**List[str]**](str.md)| Comma separated list of exact tags present on engagement (uses OR for multiple values) | [optional] 
 **test__engagement__tags__and** | [**List[str]**](str.md)| Comma separated list of exact tags to match with an AND expression present on engagement | [optional] 
 **test__tags** | [**List[str]**](str.md)| Comma separated list of exact tags present on test (uses OR for multiple values) | [optional] 
 **test__tags__and** | [**List[str]**](str.md)| Comma separated list of exact tags to match with an AND expression present on test | [optional] 
 **test__test_type** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **title** | **str**|  | [optional] 
 **under_defect_review** | **bool**|  | [optional] 
 **under_review** | **bool**|  | [optional] 
 **unique_id_from_tool** | **str**|  | [optional] 
 **verified** | **bool**|  | [optional] 
 **vuln_id_from_tool** | **str**|  | [optional] 
 **vulnerability_id** | **str**|  | [optional] 

### Return type

[**PaginatedRiskAcceptanceList**](PaginatedRiskAcceptanceList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_close_create**
> FindingClose findings_close_create(id, finding_close_request=finding_close_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.finding_close import FindingClose
from defectdojo_api_generated.models.finding_close_request import FindingCloseRequest
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
    finding_close_request = defectdojo_api_generated.FindingCloseRequest() # FindingCloseRequest |  (optional)

    try:
        api_response = api_instance.findings_close_create(id, finding_close_request=finding_close_request)
        print("The response of FindingsApi->findings_close_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_close_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **finding_close_request** | [**FindingCloseRequest**](FindingCloseRequest.md)|  | [optional] 

### Return type

[**FindingClose**](FindingClose.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_create**
> FindingCreate findings_create(finding_create_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.finding_create import FindingCreate
from defectdojo_api_generated.models.finding_create_request import FindingCreateRequest
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    finding_create_request = defectdojo_api_generated.FindingCreateRequest() # FindingCreateRequest | 

    try:
        api_response = api_instance.findings_create(finding_create_request)
        print("The response of FindingsApi->findings_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finding_create_request** | [**FindingCreateRequest**](FindingCreateRequest.md)|  | 

### Return type

[**FindingCreate**](FindingCreate.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_delete_preview_list**
> PaginatedDeletePreviewList findings_delete_preview_list(id, limit=limit, offset=offset)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_delete_preview_list import PaginatedDeletePreviewList
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.findings_delete_preview_list(id, limit=limit, offset=offset)
        print("The response of FindingsApi->findings_delete_preview_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_delete_preview_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedDeletePreviewList**](PaginatedDeletePreviewList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_destroy**
> findings_destroy(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_instance.findings_destroy(id)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_duplicate_list**
> List[Finding] findings_duplicate_list(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.finding import Finding
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_response = api_instance.findings_duplicate_list(id)
        print("The response of FindingsApi->findings_duplicate_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_duplicate_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

[**List[Finding]**](Finding.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_duplicate_reset_create**
> findings_duplicate_reset_create(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_instance.findings_duplicate_reset_create(id)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_duplicate_reset_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_files_create**
> File findings_files_create(id, title, file)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.file import File
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
    title = 'title_example' # str | 
    file = None # bytearray | 

    try:
        api_response = api_instance.findings_files_create(id, title, file)
        print("The response of FindingsApi->findings_files_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_files_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **title** | **str**|  | 
 **file** | **bytearray**|  | 

### Return type

[**File**](File.md)

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

# **findings_files_download_retrieve**
> RawFile findings_files_download_retrieve(file_id, id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.raw_file import RawFile
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    file_id = 'file_id_example' # str | 
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_response = api_instance.findings_files_download_retrieve(file_id, id)
        print("The response of FindingsApi->findings_files_download_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_files_download_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

[**RawFile**](RawFile.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_files_retrieve**
> FindingToFiles findings_files_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.finding_to_files import FindingToFiles
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_response = api_instance.findings_files_retrieve(id)
        print("The response of FindingsApi->findings_files_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_files_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

[**FindingToFiles**](FindingToFiles.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_generate_report_create**
> ReportGenerate findings_generate_report_create(report_generate_option_request=report_generate_option_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.report_generate import ReportGenerate
from defectdojo_api_generated.models.report_generate_option_request import ReportGenerateOptionRequest
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    report_generate_option_request = defectdojo_api_generated.ReportGenerateOptionRequest() # ReportGenerateOptionRequest |  (optional)

    try:
        api_response = api_instance.findings_generate_report_create(report_generate_option_request=report_generate_option_request)
        print("The response of FindingsApi->findings_generate_report_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_generate_report_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_generate_option_request** | [**ReportGenerateOptionRequest**](ReportGenerateOptionRequest.md)|  | [optional] 

### Return type

[**ReportGenerate**](ReportGenerate.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_list**
> PaginatedFindingList findings_list(active=active, component_name=component_name, component_version=component_version, created=created, cvssv3=cvssv3, cvssv3_score=cvssv3_score, cwe=cwe, var_date=var_date, defect_review_requested_by=defect_review_requested_by, description=description, discovered_after=discovered_after, discovered_before=discovered_before, discovered_on=discovered_on, duplicate=duplicate, duplicate_finding=duplicate_finding, dynamic_finding=dynamic_finding, effort_for_fixing=effort_for_fixing, endpoints=endpoints, epss_percentile_max=epss_percentile_max, epss_percentile_min=epss_percentile_min, epss_score_max=epss_score_max, epss_score_min=epss_score_min, false_p=false_p, file_path=file_path, finding_group=finding_group, found_by=found_by, has_jira=has_jira, has_tags=has_tags, hash_code=hash_code, id=id, impact=impact, inherited_tags=inherited_tags, is_mitigated=is_mitigated, jira_change=jira_change, jira_creation=jira_creation, last_reviewed=last_reviewed, last_reviewed_by=last_reviewed_by, last_status_update=last_status_update, limit=limit, mitigated=mitigated, mitigated_after=mitigated_after, mitigated_before=mitigated_before, mitigated_by=mitigated_by, mitigated_on=mitigated_on, mitigation=mitigation, nb_occurences=nb_occurences, not_tag=not_tag, not_tags=not_tags, not_test__engagement__product__tags=not_test__engagement__product__tags, not_test__engagement__tags=not_test__engagement__tags, not_test__tags=not_test__tags, numerical_severity=numerical_severity, o=o, offset=offset, out_of_scope=out_of_scope, outside_of_sla=outside_of_sla, param=param, payload=payload, planned_remediation_date=planned_remediation_date, planned_remediation_version=planned_remediation_version, prefetch=prefetch, product_lifecycle=product_lifecycle, product_name=product_name, product_name_contains=product_name_contains, publish_date=publish_date, references=references, related_fields=related_fields, reporter=reporter, review_requested_by=review_requested_by, reviewers=reviewers, risk_acceptance=risk_acceptance, risk_accepted=risk_accepted, sast_sink_object=sast_sink_object, sast_source_file_path=sast_source_file_path, sast_source_line=sast_source_line, sast_source_object=sast_source_object, scanner_confidence=scanner_confidence, service=service, severity=severity, severity_justification=severity_justification, sla_expiration_date=sla_expiration_date, sla_start_date=sla_start_date, sonarqube_issue=sonarqube_issue, static_finding=static_finding, steps_to_reproduce=steps_to_reproduce, tag=tag, tags=tags, tags__and=tags__and, test=test, test__engagement=test__engagement, test__engagement__product=test__engagement__product, test__engagement__product__prod_type=test__engagement__product__prod_type, test__engagement__product__tags=test__engagement__product__tags, test__engagement__product__tags__and=test__engagement__product__tags__and, test__engagement__tags=test__engagement__tags, test__engagement__tags__and=test__engagement__tags__and, test__tags=test__tags, test__tags__and=test__tags__and, test__test_type=test__test_type, title=title, under_defect_review=under_defect_review, under_review=under_review, unique_id_from_tool=unique_id_from_tool, verified=verified, vuln_id_from_tool=vuln_id_from_tool, vulnerability_id=vulnerability_id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.paginated_finding_list import PaginatedFindingList
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    active = True # bool |  (optional)
    component_name = 'component_name_example' # str |  (optional)
    component_version = 'component_version_example' # str |  (optional)
    created = '2013-10-20T19:20:30+01:00' # datetime | The date the finding was created inside DefectDojo.  * `None` - Any date * `1` - Today * `2` - Past 7 days * `3` - Past 30 days * `4` - Past 90 days * `5` - Current month * `6` - Current year * `7` - Past year (optional)
    cvssv3 = 'cvssv3_example' # str |  (optional)
    cvssv3_score = 3.4 # float |  (optional)
    cwe = [56] # List[int] | Multiple values may be separated by commas. (optional)
    var_date = '2013-10-20' # date | The date the flaw was discovered.  * `None` - Any date * `1` - Today * `2` - Past 7 days * `3` - Past 30 days * `4` - Past 90 days * `5` - Current month * `6` - Current year * `7` - Past year (optional)
    defect_review_requested_by = [56] # List[int] | Multiple values may be separated by commas. (optional)
    description = 'description_example' # str |  (optional)
    discovered_after = '2013-10-20' # date |  (optional)
    discovered_before = '2013-10-20' # date |  (optional)
    discovered_on = '2013-10-20' # date |  (optional)
    duplicate = True # bool |  (optional)
    duplicate_finding = 56 # int |  (optional)
    dynamic_finding = True # bool |  (optional)
    effort_for_fixing = 'effort_for_fixing_example' # str |  (optional)
    endpoints = [56] # List[int] | Multiple values may be separated by commas. (optional)
    epss_percentile_max = 3.4 # float | The range of EPSS percentiles to filter on; the min input is a lower bound, the max is an upper bound. Leaving one empty will skip that bound (e.g., leaving the min bound input empty will filter only on the max bound -- filtering on \"less than or equal\"). Leading 0 required. (optional)
    epss_percentile_min = 3.4 # float | The range of EPSS percentiles to filter on; the min input is a lower bound, the max is an upper bound. Leaving one empty will skip that bound (e.g., leaving the min bound input empty will filter only on the max bound -- filtering on \"less than or equal\"). Leading 0 required. (optional)
    epss_score_max = 3.4 # float | The range of EPSS score percentages to filter on; the min input is a lower bound, the max is an upper bound. Leaving one empty will skip that bound (e.g., leaving the min bound input empty will filter only on the max bound -- filtering on \"less than or equal\"). Leading 0 required. (optional)
    epss_score_min = 3.4 # float | The range of EPSS score percentages to filter on; the min input is a lower bound, the max is an upper bound. Leaving one empty will skip that bound (e.g., leaving the min bound input empty will filter only on the max bound -- filtering on \"less than or equal\"). Leading 0 required. (optional)
    false_p = True # bool |  (optional)
    file_path = 'file_path_example' # str |  (optional)
    finding_group = [3.4] # List[float] | Multiple values may be separated by commas. (optional)
    found_by = [56] # List[int] | Multiple values may be separated by commas. (optional)
    has_jira = True # bool |  (optional)
    has_tags = True # bool | Has tags (optional)
    hash_code = 'hash_code_example' # str |  (optional)
    id = [56] # List[int] | Multiple values may be separated by commas. (optional)
    impact = 'impact_example' # str |  (optional)
    inherited_tags = [defectdojo_api_generated.List[int]()] # List[List[int]] | Internal use tags sepcifically for maintaining parity with product. This field will be present as a subset in the tags field (optional)
    is_mitigated = True # bool |  (optional)
    jira_change = '2013-10-20T19:20:30+01:00' # datetime | The date the linked Jira issue was last modified.  * `None` - Any date * `1` - Today * `2` - Past 7 days * `3` - Past 30 days * `4` - Past 90 days * `5` - Current month * `6` - Current year * `7` - Past year (optional)
    jira_creation = '2013-10-20T19:20:30+01:00' # datetime | The date a Jira issue was created from this finding.  * `None` - Any date * `1` - Today * `2` - Past 7 days * `3` - Past 30 days * `4` - Past 90 days * `5` - Current month * `6` - Current year * `7` - Past year (optional)
    last_reviewed = '2013-10-20T19:20:30+01:00' # datetime | Provides the date the flaw was last 'touched' by a tester.  * `None` - Any date * `1` - Today * `2` - Past 7 days * `3` - Past 30 days * `4` - Past 90 days * `5` - Current month * `6` - Current year * `7` - Past year (optional)
    last_reviewed_by = [56] # List[int] | Multiple values may be separated by commas. (optional)
    last_status_update = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    mitigated = '2013-10-20T19:20:30+01:00' # datetime | Denotes if this flaw has been fixed by storing the date it was fixed.  * `None` - Any date * `1` - Today * `2` - Past 7 days * `3` - Past 30 days * `4` - Past 90 days * `5` - Current month * `6` - Current year * `7` - Past year (optional)
    mitigated_after = '2013-10-20T19:20:30+01:00' # datetime | Mitigated After (optional)
    mitigated_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    mitigated_by = [56] # List[int] | Multiple values may be separated by commas. (optional)
    mitigated_on = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    mitigation = 'mitigation_example' # str |  (optional)
    nb_occurences = [56] # List[int] | Multiple values may be separated by commas. (optional)
    not_tag = 'not_tag_example' # str | Not Tag name contains (optional)
    not_tags = ['not_tags_example'] # List[str] | Comma separated list of exact tags not present on model (optional)
    not_test__engagement__product__tags = ['not_test__engagement__product__tags_example'] # List[str] | Comma separated list of exact tags not present on product (optional)
    not_test__engagement__tags = ['not_test__engagement__tags_example'] # List[str] | Comma separated list of exact tags not present on engagement (optional)
    not_test__tags = ['not_test__tags_example'] # List[str] | Comma separated list of exact tags present on test (optional)
    numerical_severity = 'numerical_severity_example' # str |  (optional)
    o = ['o_example'] # List[str] | Ordering  * `active` - Active * `-active` - Active (descending) * `component_name` - Component name * `-component_name` - Component name (descending) * `component_version` - Component version * `-component_version` - Component version (descending) * `created` - Created * `-created` - Created (descending) * `last_status_update` - Last status update * `-last_status_update` - Last status update (descending) * `last_reviewed` - Last reviewed * `-last_reviewed` - Last reviewed (descending) * `cwe` - Cwe * `-cwe` - Cwe (descending) * `date` - Date * `-date` - Date (descending) * `duplicate` - Duplicate * `-duplicate` - Duplicate (descending) * `dynamic_finding` - Dynamic finding * `-dynamic_finding` - Dynamic finding (descending) * `false_p` - False p * `-false_p` - False p (descending) * `found_by` - Found by * `-found_by` - Found by (descending) * `id` - Id * `-id` - Id (descending) * `is_mitigated` - Is mitigated * `-is_mitigated` - Is mitigated (descending) * `numerical_severity` - Numerical severity * `-numerical_severity` - Numerical severity (descending) * `out_of_scope` - Out of scope * `-out_of_scope` - Out of scope (descending) * `severity` - Severity * `-severity` - Severity (descending) * `reviewers` - Reviewers * `-reviewers` - Reviewers (descending) * `static_finding` - Static finding * `-static_finding` - Static finding (descending) * `test__engagement__product__name` - Test  engagement  product  name * `-test__engagement__product__name` - Test  engagement  product  name (descending) * `title` - Title * `-title` - Title (descending) * `under_defect_review` - Under defect review * `-under_defect_review` - Under defect review (descending) * `under_review` - Under review * `-under_review` - Under review (descending) * `verified` - Verified * `-verified` - Verified (descending) (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    out_of_scope = True # bool |  (optional)
    outside_of_sla = 3.4 # float |  (optional)
    param = 'param_example' # str |  (optional)
    payload = 'payload_example' # str |  (optional)
    planned_remediation_date = '2013-10-20' # date |  (optional)
    planned_remediation_version = 'planned_remediation_version_example' # str |  (optional)
    prefetch = ['prefetch_example'] # List[str] | List of fields for which to prefetch model instances and add those to the response (optional)
    product_lifecycle = 'product_lifecycle_example' # str | Comma separated list of exact product lifecycles (optional)
    product_name = 'product_name_example' # str | exact product name (optional)
    product_name_contains = 'product_name_contains_example' # str | exact product name (optional)
    publish_date = '2013-10-20' # date |  (optional)
    references = 'references_example' # str |  (optional)
    related_fields = True # bool | Expand finding external relations (engagement, environment, product,                                             product_type, test, test_type) (optional)
    reporter = [56] # List[int] | Multiple values may be separated by commas. (optional)
    review_requested_by = [56] # List[int] | Multiple values may be separated by commas. (optional)
    reviewers = [56] # List[int] | Multiple values may be separated by commas. (optional)
    risk_acceptance = 3.4 # float |  (optional)
    risk_accepted = True # bool |  (optional)
    sast_sink_object = 'sast_sink_object_example' # str |  (optional)
    sast_source_file_path = 'sast_source_file_path_example' # str |  (optional)
    sast_source_line = [56] # List[int] | Multiple values may be separated by commas. (optional)
    sast_source_object = 'sast_source_object_example' # str |  (optional)
    scanner_confidence = [56] # List[int] | Multiple values may be separated by commas. (optional)
    service = 'service_example' # str |  (optional)
    severity = 'severity_example' # str |  (optional)
    severity_justification = 'severity_justification_example' # str |  (optional)
    sla_expiration_date = '2013-10-20' # date |  (optional)
    sla_start_date = '2013-10-20' # date |  (optional)
    sonarqube_issue = [56] # List[int] | Multiple values may be separated by commas. (optional)
    static_finding = True # bool |  (optional)
    steps_to_reproduce = 'steps_to_reproduce_example' # str |  (optional)
    tag = 'tag_example' # str | Tag name contains (optional)
    tags = ['tags_example'] # List[str] | Comma separated list of exact tags (uses OR for multiple values) (optional)
    tags__and = ['tags__and_example'] # List[str] | Comma separated list of exact tags to match with an AND expression (optional)
    test = 56 # int |  (optional)
    test__engagement = [56] # List[int] | Multiple values may be separated by commas. (optional)
    test__engagement__product = [56] # List[int] | Multiple values may be separated by commas. (optional)
    test__engagement__product__prod_type = [56] # List[int] | Multiple values may be separated by commas. (optional)
    test__engagement__product__tags = ['test__engagement__product__tags_example'] # List[str] | Comma separated list of exact tags present on product (uses OR for multiple values) (optional)
    test__engagement__product__tags__and = ['test__engagement__product__tags__and_example'] # List[str] | Comma separated list of exact tags to match with an AND expression present on product (optional)
    test__engagement__tags = ['test__engagement__tags_example'] # List[str] | Comma separated list of exact tags present on engagement (uses OR for multiple values) (optional)
    test__engagement__tags__and = ['test__engagement__tags__and_example'] # List[str] | Comma separated list of exact tags to match with an AND expression present on engagement (optional)
    test__tags = ['test__tags_example'] # List[str] | Comma separated list of exact tags present on test (uses OR for multiple values) (optional)
    test__tags__and = ['test__tags__and_example'] # List[str] | Comma separated list of exact tags to match with an AND expression present on test (optional)
    test__test_type = [56] # List[int] | Multiple values may be separated by commas. (optional)
    title = 'title_example' # str |  (optional)
    under_defect_review = True # bool |  (optional)
    under_review = True # bool |  (optional)
    unique_id_from_tool = 'unique_id_from_tool_example' # str |  (optional)
    verified = True # bool |  (optional)
    vuln_id_from_tool = 'vuln_id_from_tool_example' # str |  (optional)
    vulnerability_id = 'vulnerability_id_example' # str |  (optional)

    try:
        api_response = api_instance.findings_list(active=active, component_name=component_name, component_version=component_version, created=created, cvssv3=cvssv3, cvssv3_score=cvssv3_score, cwe=cwe, var_date=var_date, defect_review_requested_by=defect_review_requested_by, description=description, discovered_after=discovered_after, discovered_before=discovered_before, discovered_on=discovered_on, duplicate=duplicate, duplicate_finding=duplicate_finding, dynamic_finding=dynamic_finding, effort_for_fixing=effort_for_fixing, endpoints=endpoints, epss_percentile_max=epss_percentile_max, epss_percentile_min=epss_percentile_min, epss_score_max=epss_score_max, epss_score_min=epss_score_min, false_p=false_p, file_path=file_path, finding_group=finding_group, found_by=found_by, has_jira=has_jira, has_tags=has_tags, hash_code=hash_code, id=id, impact=impact, inherited_tags=inherited_tags, is_mitigated=is_mitigated, jira_change=jira_change, jira_creation=jira_creation, last_reviewed=last_reviewed, last_reviewed_by=last_reviewed_by, last_status_update=last_status_update, limit=limit, mitigated=mitigated, mitigated_after=mitigated_after, mitigated_before=mitigated_before, mitigated_by=mitigated_by, mitigated_on=mitigated_on, mitigation=mitigation, nb_occurences=nb_occurences, not_tag=not_tag, not_tags=not_tags, not_test__engagement__product__tags=not_test__engagement__product__tags, not_test__engagement__tags=not_test__engagement__tags, not_test__tags=not_test__tags, numerical_severity=numerical_severity, o=o, offset=offset, out_of_scope=out_of_scope, outside_of_sla=outside_of_sla, param=param, payload=payload, planned_remediation_date=planned_remediation_date, planned_remediation_version=planned_remediation_version, prefetch=prefetch, product_lifecycle=product_lifecycle, product_name=product_name, product_name_contains=product_name_contains, publish_date=publish_date, references=references, related_fields=related_fields, reporter=reporter, review_requested_by=review_requested_by, reviewers=reviewers, risk_acceptance=risk_acceptance, risk_accepted=risk_accepted, sast_sink_object=sast_sink_object, sast_source_file_path=sast_source_file_path, sast_source_line=sast_source_line, sast_source_object=sast_source_object, scanner_confidence=scanner_confidence, service=service, severity=severity, severity_justification=severity_justification, sla_expiration_date=sla_expiration_date, sla_start_date=sla_start_date, sonarqube_issue=sonarqube_issue, static_finding=static_finding, steps_to_reproduce=steps_to_reproduce, tag=tag, tags=tags, tags__and=tags__and, test=test, test__engagement=test__engagement, test__engagement__product=test__engagement__product, test__engagement__product__prod_type=test__engagement__product__prod_type, test__engagement__product__tags=test__engagement__product__tags, test__engagement__product__tags__and=test__engagement__product__tags__and, test__engagement__tags=test__engagement__tags, test__engagement__tags__and=test__engagement__tags__and, test__tags=test__tags, test__tags__and=test__tags__and, test__test_type=test__test_type, title=title, under_defect_review=under_defect_review, under_review=under_review, unique_id_from_tool=unique_id_from_tool, verified=verified, vuln_id_from_tool=vuln_id_from_tool, vulnerability_id=vulnerability_id)
        print("The response of FindingsApi->findings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **bool**|  | [optional] 
 **component_name** | **str**|  | [optional] 
 **component_version** | **str**|  | [optional] 
 **created** | **datetime**| The date the finding was created inside DefectDojo.  * &#x60;None&#x60; - Any date * &#x60;1&#x60; - Today * &#x60;2&#x60; - Past 7 days * &#x60;3&#x60; - Past 30 days * &#x60;4&#x60; - Past 90 days * &#x60;5&#x60; - Current month * &#x60;6&#x60; - Current year * &#x60;7&#x60; - Past year | [optional] 
 **cvssv3** | **str**|  | [optional] 
 **cvssv3_score** | **float**|  | [optional] 
 **cwe** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **var_date** | **date**| The date the flaw was discovered.  * &#x60;None&#x60; - Any date * &#x60;1&#x60; - Today * &#x60;2&#x60; - Past 7 days * &#x60;3&#x60; - Past 30 days * &#x60;4&#x60; - Past 90 days * &#x60;5&#x60; - Current month * &#x60;6&#x60; - Current year * &#x60;7&#x60; - Past year | [optional] 
 **defect_review_requested_by** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **description** | **str**|  | [optional] 
 **discovered_after** | **date**|  | [optional] 
 **discovered_before** | **date**|  | [optional] 
 **discovered_on** | **date**|  | [optional] 
 **duplicate** | **bool**|  | [optional] 
 **duplicate_finding** | **int**|  | [optional] 
 **dynamic_finding** | **bool**|  | [optional] 
 **effort_for_fixing** | **str**|  | [optional] 
 **endpoints** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **epss_percentile_max** | **float**| The range of EPSS percentiles to filter on; the min input is a lower bound, the max is an upper bound. Leaving one empty will skip that bound (e.g., leaving the min bound input empty will filter only on the max bound -- filtering on \&quot;less than or equal\&quot;). Leading 0 required. | [optional] 
 **epss_percentile_min** | **float**| The range of EPSS percentiles to filter on; the min input is a lower bound, the max is an upper bound. Leaving one empty will skip that bound (e.g., leaving the min bound input empty will filter only on the max bound -- filtering on \&quot;less than or equal\&quot;). Leading 0 required. | [optional] 
 **epss_score_max** | **float**| The range of EPSS score percentages to filter on; the min input is a lower bound, the max is an upper bound. Leaving one empty will skip that bound (e.g., leaving the min bound input empty will filter only on the max bound -- filtering on \&quot;less than or equal\&quot;). Leading 0 required. | [optional] 
 **epss_score_min** | **float**| The range of EPSS score percentages to filter on; the min input is a lower bound, the max is an upper bound. Leaving one empty will skip that bound (e.g., leaving the min bound input empty will filter only on the max bound -- filtering on \&quot;less than or equal\&quot;). Leading 0 required. | [optional] 
 **false_p** | **bool**|  | [optional] 
 **file_path** | **str**|  | [optional] 
 **finding_group** | [**List[float]**](float.md)| Multiple values may be separated by commas. | [optional] 
 **found_by** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **has_jira** | **bool**|  | [optional] 
 **has_tags** | **bool**| Has tags | [optional] 
 **hash_code** | **str**|  | [optional] 
 **id** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **impact** | **str**|  | [optional] 
 **inherited_tags** | [**List[List[int]]**](List[int].md)| Internal use tags sepcifically for maintaining parity with product. This field will be present as a subset in the tags field | [optional] 
 **is_mitigated** | **bool**|  | [optional] 
 **jira_change** | **datetime**| The date the linked Jira issue was last modified.  * &#x60;None&#x60; - Any date * &#x60;1&#x60; - Today * &#x60;2&#x60; - Past 7 days * &#x60;3&#x60; - Past 30 days * &#x60;4&#x60; - Past 90 days * &#x60;5&#x60; - Current month * &#x60;6&#x60; - Current year * &#x60;7&#x60; - Past year | [optional] 
 **jira_creation** | **datetime**| The date a Jira issue was created from this finding.  * &#x60;None&#x60; - Any date * &#x60;1&#x60; - Today * &#x60;2&#x60; - Past 7 days * &#x60;3&#x60; - Past 30 days * &#x60;4&#x60; - Past 90 days * &#x60;5&#x60; - Current month * &#x60;6&#x60; - Current year * &#x60;7&#x60; - Past year | [optional] 
 **last_reviewed** | **datetime**| Provides the date the flaw was last &#39;touched&#39; by a tester.  * &#x60;None&#x60; - Any date * &#x60;1&#x60; - Today * &#x60;2&#x60; - Past 7 days * &#x60;3&#x60; - Past 30 days * &#x60;4&#x60; - Past 90 days * &#x60;5&#x60; - Current month * &#x60;6&#x60; - Current year * &#x60;7&#x60; - Past year | [optional] 
 **last_reviewed_by** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **last_status_update** | **datetime**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **mitigated** | **datetime**| Denotes if this flaw has been fixed by storing the date it was fixed.  * &#x60;None&#x60; - Any date * &#x60;1&#x60; - Today * &#x60;2&#x60; - Past 7 days * &#x60;3&#x60; - Past 30 days * &#x60;4&#x60; - Past 90 days * &#x60;5&#x60; - Current month * &#x60;6&#x60; - Current year * &#x60;7&#x60; - Past year | [optional] 
 **mitigated_after** | **datetime**| Mitigated After | [optional] 
 **mitigated_before** | **datetime**|  | [optional] 
 **mitigated_by** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **mitigated_on** | **datetime**|  | [optional] 
 **mitigation** | **str**|  | [optional] 
 **nb_occurences** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **not_tag** | **str**| Not Tag name contains | [optional] 
 **not_tags** | [**List[str]**](str.md)| Comma separated list of exact tags not present on model | [optional] 
 **not_test__engagement__product__tags** | [**List[str]**](str.md)| Comma separated list of exact tags not present on product | [optional] 
 **not_test__engagement__tags** | [**List[str]**](str.md)| Comma separated list of exact tags not present on engagement | [optional] 
 **not_test__tags** | [**List[str]**](str.md)| Comma separated list of exact tags present on test | [optional] 
 **numerical_severity** | **str**|  | [optional] 
 **o** | [**List[str]**](str.md)| Ordering  * &#x60;active&#x60; - Active * &#x60;-active&#x60; - Active (descending) * &#x60;component_name&#x60; - Component name * &#x60;-component_name&#x60; - Component name (descending) * &#x60;component_version&#x60; - Component version * &#x60;-component_version&#x60; - Component version (descending) * &#x60;created&#x60; - Created * &#x60;-created&#x60; - Created (descending) * &#x60;last_status_update&#x60; - Last status update * &#x60;-last_status_update&#x60; - Last status update (descending) * &#x60;last_reviewed&#x60; - Last reviewed * &#x60;-last_reviewed&#x60; - Last reviewed (descending) * &#x60;cwe&#x60; - Cwe * &#x60;-cwe&#x60; - Cwe (descending) * &#x60;date&#x60; - Date * &#x60;-date&#x60; - Date (descending) * &#x60;duplicate&#x60; - Duplicate * &#x60;-duplicate&#x60; - Duplicate (descending) * &#x60;dynamic_finding&#x60; - Dynamic finding * &#x60;-dynamic_finding&#x60; - Dynamic finding (descending) * &#x60;false_p&#x60; - False p * &#x60;-false_p&#x60; - False p (descending) * &#x60;found_by&#x60; - Found by * &#x60;-found_by&#x60; - Found by (descending) * &#x60;id&#x60; - Id * &#x60;-id&#x60; - Id (descending) * &#x60;is_mitigated&#x60; - Is mitigated * &#x60;-is_mitigated&#x60; - Is mitigated (descending) * &#x60;numerical_severity&#x60; - Numerical severity * &#x60;-numerical_severity&#x60; - Numerical severity (descending) * &#x60;out_of_scope&#x60; - Out of scope * &#x60;-out_of_scope&#x60; - Out of scope (descending) * &#x60;severity&#x60; - Severity * &#x60;-severity&#x60; - Severity (descending) * &#x60;reviewers&#x60; - Reviewers * &#x60;-reviewers&#x60; - Reviewers (descending) * &#x60;static_finding&#x60; - Static finding * &#x60;-static_finding&#x60; - Static finding (descending) * &#x60;test__engagement__product__name&#x60; - Test  engagement  product  name * &#x60;-test__engagement__product__name&#x60; - Test  engagement  product  name (descending) * &#x60;title&#x60; - Title * &#x60;-title&#x60; - Title (descending) * &#x60;under_defect_review&#x60; - Under defect review * &#x60;-under_defect_review&#x60; - Under defect review (descending) * &#x60;under_review&#x60; - Under review * &#x60;-under_review&#x60; - Under review (descending) * &#x60;verified&#x60; - Verified * &#x60;-verified&#x60; - Verified (descending) | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **out_of_scope** | **bool**|  | [optional] 
 **outside_of_sla** | **float**|  | [optional] 
 **param** | **str**|  | [optional] 
 **payload** | **str**|  | [optional] 
 **planned_remediation_date** | **date**|  | [optional] 
 **planned_remediation_version** | **str**|  | [optional] 
 **prefetch** | [**List[str]**](str.md)| List of fields for which to prefetch model instances and add those to the response | [optional] 
 **product_lifecycle** | **str**| Comma separated list of exact product lifecycles | [optional] 
 **product_name** | **str**| exact product name | [optional] 
 **product_name_contains** | **str**| exact product name | [optional] 
 **publish_date** | **date**|  | [optional] 
 **references** | **str**|  | [optional] 
 **related_fields** | **bool**| Expand finding external relations (engagement, environment, product,                                             product_type, test, test_type) | [optional] 
 **reporter** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **review_requested_by** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **reviewers** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **risk_acceptance** | **float**|  | [optional] 
 **risk_accepted** | **bool**|  | [optional] 
 **sast_sink_object** | **str**|  | [optional] 
 **sast_source_file_path** | **str**|  | [optional] 
 **sast_source_line** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **sast_source_object** | **str**|  | [optional] 
 **scanner_confidence** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **service** | **str**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **severity_justification** | **str**|  | [optional] 
 **sla_expiration_date** | **date**|  | [optional] 
 **sla_start_date** | **date**|  | [optional] 
 **sonarqube_issue** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **static_finding** | **bool**|  | [optional] 
 **steps_to_reproduce** | **str**|  | [optional] 
 **tag** | **str**| Tag name contains | [optional] 
 **tags** | [**List[str]**](str.md)| Comma separated list of exact tags (uses OR for multiple values) | [optional] 
 **tags__and** | [**List[str]**](str.md)| Comma separated list of exact tags to match with an AND expression | [optional] 
 **test** | **int**|  | [optional] 
 **test__engagement** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **test__engagement__product** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **test__engagement__product__prod_type** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **test__engagement__product__tags** | [**List[str]**](str.md)| Comma separated list of exact tags present on product (uses OR for multiple values) | [optional] 
 **test__engagement__product__tags__and** | [**List[str]**](str.md)| Comma separated list of exact tags to match with an AND expression present on product | [optional] 
 **test__engagement__tags** | [**List[str]**](str.md)| Comma separated list of exact tags present on engagement (uses OR for multiple values) | [optional] 
 **test__engagement__tags__and** | [**List[str]**](str.md)| Comma separated list of exact tags to match with an AND expression present on engagement | [optional] 
 **test__tags** | [**List[str]**](str.md)| Comma separated list of exact tags present on test (uses OR for multiple values) | [optional] 
 **test__tags__and** | [**List[str]**](str.md)| Comma separated list of exact tags to match with an AND expression present on test | [optional] 
 **test__test_type** | [**List[int]**](int.md)| Multiple values may be separated by commas. | [optional] 
 **title** | **str**|  | [optional] 
 **under_defect_review** | **bool**|  | [optional] 
 **under_review** | **bool**|  | [optional] 
 **unique_id_from_tool** | **str**|  | [optional] 
 **verified** | **bool**|  | [optional] 
 **vuln_id_from_tool** | **str**|  | [optional] 
 **vulnerability_id** | **str**|  | [optional] 

### Return type

[**PaginatedFindingList**](PaginatedFindingList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_metadata_create**
> FindingMeta findings_metadata_create(id, finding_meta_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.finding_meta import FindingMeta
from defectdojo_api_generated.models.finding_meta_request import FindingMetaRequest
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
    finding_meta_request = defectdojo_api_generated.FindingMetaRequest() # FindingMetaRequest | 

    try:
        api_response = api_instance.findings_metadata_create(id, finding_meta_request)
        print("The response of FindingsApi->findings_metadata_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_metadata_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **finding_meta_request** | [**FindingMetaRequest**](FindingMetaRequest.md)|  | 

### Return type

[**FindingMeta**](FindingMeta.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Returned if finding does not exist |  -  |
**400** | Returned if there was a problem with the metadata information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_metadata_destroy**
> findings_metadata_destroy(id, name)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
    name = 56 # int | name of the metadata to retrieve. If name is empty, return all the                                     metadata associated with the finding

    try:
        api_instance.findings_metadata_destroy(id, name)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_metadata_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **name** | **int**| name of the metadata to retrieve. If name is empty, return all the                                     metadata associated with the finding | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned if the metadata was correctly deleted |  -  |
**404** | Returned if finding does not exist |  -  |
**400** | Returned if there was a problem with the metadata information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_metadata_list**
> List[FindingMeta] findings_metadata_list(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.finding_meta import FindingMeta
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_response = api_instance.findings_metadata_list(id)
        print("The response of FindingsApi->findings_metadata_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_metadata_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

[**List[FindingMeta]**](FindingMeta.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Returned if finding does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_metadata_update**
> FindingMeta findings_metadata_update(id, finding_meta_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.finding_meta import FindingMeta
from defectdojo_api_generated.models.finding_meta_request import FindingMetaRequest
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
    finding_meta_request = defectdojo_api_generated.FindingMetaRequest() # FindingMetaRequest | 

    try:
        api_response = api_instance.findings_metadata_update(id, finding_meta_request)
        print("The response of FindingsApi->findings_metadata_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_metadata_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **finding_meta_request** | [**FindingMetaRequest**](FindingMetaRequest.md)|  | 

### Return type

[**FindingMeta**](FindingMeta.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Returned if finding does not exist |  -  |
**400** | Returned if there was a problem with the metadata information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_notes_create**
> Note findings_notes_create(id, add_new_note_option_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.add_new_note_option_request import AddNewNoteOptionRequest
from defectdojo_api_generated.models.note import Note
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
    add_new_note_option_request = defectdojo_api_generated.AddNewNoteOptionRequest() # AddNewNoteOptionRequest | 

    try:
        api_response = api_instance.findings_notes_create(id, add_new_note_option_request)
        print("The response of FindingsApi->findings_notes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_notes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **add_new_note_option_request** | [**AddNewNoteOptionRequest**](AddNewNoteOptionRequest.md)|  | 

### Return type

[**Note**](Note.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_notes_retrieve**
> FindingToNotes findings_notes_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.finding_to_notes import FindingToNotes
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_response = api_instance.findings_notes_retrieve(id)
        print("The response of FindingsApi->findings_notes_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_notes_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

[**FindingToNotes**](FindingToNotes.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_original_create**
> findings_original_create(id, new_fid)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
    new_fid = 56 # int | 

    try:
        api_instance.findings_original_create(id, new_fid)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_original_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **new_fid** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_partial_update**
> Finding findings_partial_update(id, patched_finding_request=patched_finding_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.finding import Finding
from defectdojo_api_generated.models.patched_finding_request import PatchedFindingRequest
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
    patched_finding_request = defectdojo_api_generated.PatchedFindingRequest() # PatchedFindingRequest |  (optional)

    try:
        api_response = api_instance.findings_partial_update(id, patched_finding_request=patched_finding_request)
        print("The response of FindingsApi->findings_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **patched_finding_request** | [**PatchedFindingRequest**](PatchedFindingRequest.md)|  | [optional] 

### Return type

[**Finding**](Finding.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_remove_note_partial_update**
> findings_remove_note_partial_update(id, patched_finding_note_request=patched_finding_note_request)

Remove Note From Finding Note

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.patched_finding_note_request import PatchedFindingNoteRequest
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
    patched_finding_note_request = defectdojo_api_generated.PatchedFindingNoteRequest() # PatchedFindingNoteRequest |  (optional)

    try:
        api_instance.findings_remove_note_partial_update(id, patched_finding_note_request=patched_finding_note_request)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_remove_note_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **patched_finding_note_request** | [**PatchedFindingNoteRequest**](PatchedFindingNoteRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_remove_tags_partial_update**
> findings_remove_tags_partial_update(id, patched_tag_request=patched_tag_request)

Remove Tag(s) from finding list of tags

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.patched_tag_request import PatchedTagRequest
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
    patched_tag_request = defectdojo_api_generated.PatchedTagRequest() # PatchedTagRequest |  (optional)

    try:
        api_instance.findings_remove_tags_partial_update(id, patched_tag_request=patched_tag_request)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_remove_tags_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **patched_tag_request** | [**PatchedTagRequest**](PatchedTagRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_remove_tags_update**
> findings_remove_tags_update(id, tag_request)

Remove Tag(s) from finding list of tags

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.tag_request import TagRequest
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
    tag_request = defectdojo_api_generated.TagRequest() # TagRequest | 

    try:
        api_instance.findings_remove_tags_update(id, tag_request)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_remove_tags_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **tag_request** | [**TagRequest**](TagRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_request_response_create**
> BurpRawRequestResponse findings_request_response_create(id, burp_raw_request_response_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.burp_raw_request_response import BurpRawRequestResponse
from defectdojo_api_generated.models.burp_raw_request_response_request import BurpRawRequestResponseRequest
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
    burp_raw_request_response_request = defectdojo_api_generated.BurpRawRequestResponseRequest() # BurpRawRequestResponseRequest | 

    try:
        api_response = api_instance.findings_request_response_create(id, burp_raw_request_response_request)
        print("The response of FindingsApi->findings_request_response_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_request_response_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **burp_raw_request_response_request** | [**BurpRawRequestResponseRequest**](BurpRawRequestResponseRequest.md)|  | 

### Return type

[**BurpRawRequestResponse**](BurpRawRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_request_response_retrieve**
> BurpRawRequestResponse findings_request_response_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.burp_raw_request_response import BurpRawRequestResponse
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_response = api_instance.findings_request_response_retrieve(id)
        print("The response of FindingsApi->findings_request_response_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_request_response_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

[**BurpRawRequestResponse**](BurpRawRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_retrieve**
> Finding findings_retrieve(id, prefetch=prefetch, related_fields=related_fields)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.finding import Finding
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
    prefetch = ['prefetch_example'] # List[str] | List of fields for which to prefetch model instances and add those to the response (optional)
    related_fields = True # bool | Expand finding external relations (engagement, environment, product,                                             product_type, test, test_type) (optional)

    try:
        api_response = api_instance.findings_retrieve(id, prefetch=prefetch, related_fields=related_fields)
        print("The response of FindingsApi->findings_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **prefetch** | [**List[str]**](str.md)| List of fields for which to prefetch model instances and add those to the response | [optional] 
 **related_fields** | **bool**| Expand finding external relations (engagement, environment, product,                                             product_type, test, test_type) | [optional] 

### Return type

[**Finding**](Finding.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_tags_create**
> Tag findings_tags_create(id, tag_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.tag import Tag
from defectdojo_api_generated.models.tag_request import TagRequest
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
    tag_request = defectdojo_api_generated.TagRequest() # TagRequest | 

    try:
        api_response = api_instance.findings_tags_create(id, tag_request)
        print("The response of FindingsApi->findings_tags_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_tags_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **tag_request** | [**TagRequest**](TagRequest.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_tags_retrieve**
> Tag findings_tags_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.tag import Tag
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_response = api_instance.findings_tags_retrieve(id)
        print("The response of FindingsApi->findings_tags_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_tags_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_update**
> Finding findings_update(id, finding_request)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import defectdojo_api_generated
from defectdojo_api_generated.models.finding import Finding
from defectdojo_api_generated.models.finding_request import FindingRequest
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
    api_instance = defectdojo_api_generated.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
    finding_request = defectdojo_api_generated.FindingRequest() # FindingRequest | 

    try:
        api_response = api_instance.findings_update(id, finding_request)
        print("The response of FindingsApi->findings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->findings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **finding_request** | [**FindingRequest**](FindingRequest.md)|  | 

### Return type

[**Finding**](Finding.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

