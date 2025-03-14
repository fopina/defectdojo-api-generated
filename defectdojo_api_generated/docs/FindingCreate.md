# FindingCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**notes** | **List[Optional[int]]** |  | [readonly] 
**test** | **int** |  | 
**thread_id** | **int** |  | [optional] [default to 0]
**found_by** | **List[int]** |  | 
**url** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**push_to_jira** | **bool** |  | [optional] [default to False]
**vulnerability_ids** | [**List[VulnerabilityId]**](VulnerabilityId.md) |  | [optional] 
**reporter** | **int** |  | [optional] 
**title** | **str** | A short description of the flaw. | 
**var_date** | **date** | The date the flaw was discovered. | [optional] 
**sla_start_date** | **date** | (readonly)The date used as start date for SLA calculation. Set by expiring risk acceptances. Empty by default, causing a fallback to &#39;date&#39;. | [optional] 
**sla_expiration_date** | **date** | (readonly)The date SLA expires for this finding. Empty by default, causing a fallback to &#39;date&#39;. | [optional] 
**cwe** | **int** | The CWE number associated with this flaw. | [optional] 
**epss_score** | **float** | EPSS score for the CVE. Describes how likely it is the vulnerability will be exploited in the next 30 days. | [optional] 
**epss_percentile** | **float** | EPSS percentile for the CVE. Describes how many CVEs are scored at or below this one. | [optional] 
**cvssv3** | **str** | Common Vulnerability Scoring System version 3 (CVSSv3) score associated with this flaw. | [optional] 
**cvssv3_score** | **float** | Numerical CVSSv3 score for the vulnerability. If the vector is given, the score is updated while saving the finding. The value must be between 0-10. | [optional] 
**severity** | **str** | The severity level of this flaw (Critical, High, Medium, Low, Info). | 
**description** | **str** | Longer more descriptive information about the flaw. | 
**mitigation** | **str** | Text describing how to best fix the flaw. | [optional] 
**impact** | **str** | Text describing the impact this flaw has on systems, products, enterprise, etc. | [optional] 
**steps_to_reproduce** | **str** | Text describing the steps that must be followed in order to reproduce the flaw / bug. | [optional] 
**severity_justification** | **str** | Text describing why a certain severity was associated with this flaw. | [optional] 
**references** | **str** | The external documentation available for this flaw. | [optional] 
**active** | **bool** | Denotes if this flaw is active or not. | 
**verified** | **bool** | Denotes if this flaw has been manually verified by the tester. | 
**false_p** | **bool** | Denotes if this flaw has been deemed a false positive by the tester. | [optional] 
**duplicate** | **bool** | Denotes if this flaw is a duplicate of other flaws reported. | [optional] 
**out_of_scope** | **bool** | Denotes if this flaw falls outside the scope of the test and/or engagement. | [optional] 
**risk_accepted** | **bool** | Denotes if this finding has been marked as an accepted risk. | [optional] 
**under_review** | **bool** | Denotes is this flaw is currently being reviewed. | [optional] 
**last_status_update** | **datetime** | Timestamp of latest status update (change in status related fields). | [readonly] 
**under_defect_review** | **bool** | Denotes if this finding is under defect review. | [optional] 
**is_mitigated** | **bool** | Denotes if this flaw has been fixed. | [optional] 
**mitigated** | **datetime** | Denotes if this flaw has been fixed by storing the date it was fixed. | [readonly] 
**numerical_severity** | **str** | The numerical representation of the severity (S0, S1, S2, S3, S4). | 
**last_reviewed** | **datetime** | Provides the date the flaw was last &#39;touched&#39; by a tester. | [readonly] 
**param** | **str** | Parameter used to trigger the issue (DAST). | [readonly] 
**payload** | **str** | Payload used to attack the service / application and trigger the bug / problem. | [readonly] 
**hash_code** | **str** | A hash over a configurable set of fields that is used for findings deduplication. | [readonly] 
**line** | **int** | Source line number of the attack vector. | [optional] 
**file_path** | **str** | Identified file(s) containing the flaw. | [optional] 
**component_name** | **str** | Name of the affected component (library name, part of a system, ...). | [optional] 
**component_version** | **str** | Version of the affected component. | [optional] 
**static_finding** | **bool** | Flaw has been detected from a Static Application Security Testing tool (SAST). | [optional] 
**dynamic_finding** | **bool** | Flaw has been detected from a Dynamic Application Security Testing tool (DAST). | [optional] 
**created** | **datetime** | The date the finding was created inside DefectDojo. | [readonly] 
**scanner_confidence** | **int** | Confidence level of vulnerability which is supplied by the scanner. | [readonly] 
**unique_id_from_tool** | **str** | Vulnerability technical id from the source tool. Allows to track unique vulnerabilities. | [optional] 
**vuln_id_from_tool** | **str** | Non-unique technical id from the source tool associated with the vulnerability type. | [optional] 
**sast_source_object** | **str** | Source object (variable, function...) of the attack vector. | [optional] 
**sast_sink_object** | **str** | Sink object (variable, function...) of the attack vector. | [optional] 
**sast_source_line** | **int** | Source line number of the attack vector. | [optional] 
**sast_source_file_path** | **str** | Source file path of the attack vector. | [optional] 
**nb_occurences** | **int** | Number of occurences in the source tool when several vulnerabilites were found and aggregated by the scanner. | [optional] 
**publish_date** | **date** | Date when this vulnerability was made publicly available. | [optional] 
**service** | **str** | A service is a self-contained piece of functionality within a Product. This is an optional field which is used in deduplication of findings when set. | [optional] 
**planned_remediation_date** | **date** | The date the flaw is expected to be remediated. | [optional] 
**planned_remediation_version** | **str** | The target version when the vulnerability should be fixed / remediated | [optional] 
**effort_for_fixing** | **str** | Effort for fixing / remediating the vulnerability (Low, Medium, High) | [optional] 
**duplicate_finding** | **int** | Link to the original finding if this finding is a duplicate. | [readonly] 
**review_requested_by** | **int** | Documents who requested a review for this finding. | [optional] 
**defect_review_requested_by** | **int** | Documents who requested a defect review for this flaw. | [optional] 
**mitigated_by** | **int** | Documents who has marked this flaw as fixed. | [readonly] 
**last_reviewed_by** | **int** | Provides the person who last reviewed the flaw. | [readonly] 
**sonarqube_issue** | **int** | The SonarQube issue associated with this finding. | [optional] 
**endpoints** | **List[int]** | The hosts within the product that are susceptible to this flaw. + The status of the endpoint associated with this flaw (Vulnerable, Mitigated, ...). | [readonly] 
**reviewers** | **List[int]** | Documents who reviewed the flaw. | [optional] 
**files** | **List[int]** | Files(s) related to the flaw. | [readonly] 

## Example

```python
from defectdojo_api_generated.models.finding_create import FindingCreate

# TODO update the JSON string below
json = "{}"
# create an instance of FindingCreate from a JSON string
finding_create_instance = FindingCreate.from_json(json)
# print the JSON string representation of the object
print(FindingCreate.to_json())

# convert the object into a dict
finding_create_dict = finding_create_instance.to_dict()
# create an instance of FindingCreate from a dict
finding_create_from_dict = FindingCreate.from_dict(finding_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


