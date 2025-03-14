# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

The version of the OpenAPI document: 2.44.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from datetime import date, datetime
from typing import Any, ClassVar, Dict, List, Optional, Set, Union

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing_extensions import Annotated, Self

from defectdojo_api_generated.models.vulnerability_id import VulnerabilityId


class FindingCreate(BaseModel):
    """
    FindingCreate
    """  # noqa: E501

    id: StrictInt
    notes: List[Optional[StrictInt]]
    test: StrictInt
    thread_id: Optional[StrictInt] = 0
    found_by: List[StrictInt]
    url: Optional[StrictStr] = None
    tags: Optional[List[StrictStr]] = None
    push_to_jira: Optional[StrictBool] = False
    vulnerability_ids: Optional[List[VulnerabilityId]] = None
    reporter: Optional[StrictInt] = None
    title: Annotated[str, Field(strict=True, max_length=511)] = Field(description='A short description of the flaw.')
    var_date: Optional[date] = Field(default=None, description='The date the flaw was discovered.', alias='date')
    sla_start_date: Optional[date] = Field(
        default=None,
        description="(readonly)The date used as start date for SLA calculation. Set by expiring risk acceptances. Empty by default, causing a fallback to 'date'.",
    )
    sla_expiration_date: Optional[date] = Field(
        default=None,
        description="(readonly)The date SLA expires for this finding. Empty by default, causing a fallback to 'date'.",
    )
    cwe: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(
        default=None, description='The CWE number associated with this flaw.'
    )
    epss_score: Optional[
        Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]
    ] = Field(
        default=None,
        description='EPSS score for the CVE. Describes how likely it is the vulnerability will be exploited in the next 30 days.',
    )
    epss_percentile: Optional[
        Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]
    ] = Field(
        default=None,
        description='EPSS percentile for the CVE. Describes how many CVEs are scored at or below this one.',
    )
    cvssv3: Optional[Annotated[str, Field(strict=True, max_length=117)]] = Field(
        default=None,
        description='Common Vulnerability Scoring System version 3 (CVSSv3) score associated with this flaw.',
    )
    cvssv3_score: Optional[
        Union[Annotated[float, Field(le=10.0, strict=True, ge=0.0)], Annotated[int, Field(le=10, strict=True, ge=0)]]
    ] = Field(
        default=None,
        description='Numerical CVSSv3 score for the vulnerability. If the vector is given, the score is updated while saving the finding. The value must be between 0-10.',
    )
    severity: Annotated[str, Field(strict=True, max_length=200)] = Field(
        description='The severity level of this flaw (Critical, High, Medium, Low, Info).'
    )
    description: StrictStr = Field(description='Longer more descriptive information about the flaw.')
    mitigation: Optional[StrictStr] = Field(default=None, description='Text describing how to best fix the flaw.')
    impact: Optional[StrictStr] = Field(
        default=None, description='Text describing the impact this flaw has on systems, products, enterprise, etc.'
    )
    steps_to_reproduce: Optional[StrictStr] = Field(
        default=None,
        description='Text describing the steps that must be followed in order to reproduce the flaw / bug.',
    )
    severity_justification: Optional[StrictStr] = Field(
        default=None, description='Text describing why a certain severity was associated with this flaw.'
    )
    references: Optional[StrictStr] = Field(
        default=None, description='The external documentation available for this flaw.'
    )
    active: StrictBool = Field(description='Denotes if this flaw is active or not.')
    verified: StrictBool = Field(description='Denotes if this flaw has been manually verified by the tester.')
    false_p: Optional[StrictBool] = Field(
        default=None, description='Denotes if this flaw has been deemed a false positive by the tester.'
    )
    duplicate: Optional[StrictBool] = Field(
        default=None, description='Denotes if this flaw is a duplicate of other flaws reported.'
    )
    out_of_scope: Optional[StrictBool] = Field(
        default=None, description='Denotes if this flaw falls outside the scope of the test and/or engagement.'
    )
    risk_accepted: Optional[StrictBool] = Field(
        default=None, description='Denotes if this finding has been marked as an accepted risk.'
    )
    under_review: Optional[StrictBool] = Field(
        default=None, description='Denotes is this flaw is currently being reviewed.'
    )
    last_status_update: Optional[datetime] = Field(
        description='Timestamp of latest status update (change in status related fields).'
    )
    under_defect_review: Optional[StrictBool] = Field(
        default=None, description='Denotes if this finding is under defect review.'
    )
    is_mitigated: Optional[StrictBool] = Field(default=None, description='Denotes if this flaw has been fixed.')
    mitigated: Optional[datetime] = Field(
        description='Denotes if this flaw has been fixed by storing the date it was fixed.'
    )
    numerical_severity: Annotated[str, Field(strict=True, max_length=4)] = Field(
        description='The numerical representation of the severity (S0, S1, S2, S3, S4).'
    )
    last_reviewed: Optional[datetime] = Field(description="Provides the date the flaw was last 'touched' by a tester.")
    param: Optional[StrictStr] = Field(description='Parameter used to trigger the issue (DAST).')
    payload: Optional[StrictStr] = Field(
        description='Payload used to attack the service / application and trigger the bug / problem.'
    )
    hash_code: Optional[StrictStr] = Field(
        description='A hash over a configurable set of fields that is used for findings deduplication.'
    )
    line: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(
        default=None, description='Source line number of the attack vector.'
    )
    file_path: Optional[Annotated[str, Field(strict=True, max_length=4000)]] = Field(
        default=None, description='Identified file(s) containing the flaw.'
    )
    component_name: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(
        default=None, description='Name of the affected component (library name, part of a system, ...).'
    )
    component_version: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(
        default=None, description='Version of the affected component.'
    )
    static_finding: Optional[StrictBool] = Field(
        default=None, description='Flaw has been detected from a Static Application Security Testing tool (SAST).'
    )
    dynamic_finding: Optional[StrictBool] = Field(
        default=None, description='Flaw has been detected from a Dynamic Application Security Testing tool (DAST).'
    )
    created: Optional[datetime] = Field(description='The date the finding was created inside DefectDojo.')
    scanner_confidence: Optional[StrictInt] = Field(
        description='Confidence level of vulnerability which is supplied by the scanner.'
    )
    unique_id_from_tool: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(
        default=None,
        description='Vulnerability technical id from the source tool. Allows to track unique vulnerabilities.',
    )
    vuln_id_from_tool: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(
        default=None, description='Non-unique technical id from the source tool associated with the vulnerability type.'
    )
    sast_source_object: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(
        default=None, description='Source object (variable, function...) of the attack vector.'
    )
    sast_sink_object: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(
        default=None, description='Sink object (variable, function...) of the attack vector.'
    )
    sast_source_line: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(
        default=None, description='Source line number of the attack vector.'
    )
    sast_source_file_path: Optional[Annotated[str, Field(strict=True, max_length=4000)]] = Field(
        default=None, description='Source file path of the attack vector.'
    )
    nb_occurences: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(
        default=None,
        description='Number of occurences in the source tool when several vulnerabilites were found and aggregated by the scanner.',
    )
    publish_date: Optional[date] = Field(
        default=None, description='Date when this vulnerability was made publicly available.'
    )
    service: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(
        default=None,
        description='A service is a self-contained piece of functionality within a Product. This is an optional field which is used in deduplication of findings when set.',
    )
    planned_remediation_date: Optional[date] = Field(
        default=None, description='The date the flaw is expected to be remediated.'
    )
    planned_remediation_version: Optional[Annotated[str, Field(strict=True, max_length=99)]] = Field(
        default=None, description='The target version when the vulnerability should be fixed / remediated'
    )
    effort_for_fixing: Optional[Annotated[str, Field(strict=True, max_length=99)]] = Field(
        default=None, description='Effort for fixing / remediating the vulnerability (Low, Medium, High)'
    )
    duplicate_finding: Optional[StrictInt] = Field(
        description='Link to the original finding if this finding is a duplicate.'
    )
    review_requested_by: Optional[StrictInt] = Field(
        default=None, description='Documents who requested a review for this finding.'
    )
    defect_review_requested_by: Optional[StrictInt] = Field(
        default=None, description='Documents who requested a defect review for this flaw.'
    )
    mitigated_by: Optional[StrictInt] = Field(description='Documents who has marked this flaw as fixed.')
    last_reviewed_by: Optional[StrictInt] = Field(description='Provides the person who last reviewed the flaw.')
    sonarqube_issue: Optional[StrictInt] = Field(
        default=None, description='The SonarQube issue associated with this finding.'
    )
    endpoints: List[StrictInt] = Field(
        description='The hosts within the product that are susceptible to this flaw. + The status of the endpoint associated with this flaw (Vulnerable, Mitigated, ...).'
    )
    reviewers: Optional[List[StrictInt]] = Field(default=None, description='Documents who reviewed the flaw.')
    files: List[StrictInt] = Field(description='Files(s) related to the flaw.')
    __properties: ClassVar[List[str]] = [
        'id',
        'notes',
        'test',
        'thread_id',
        'found_by',
        'url',
        'tags',
        'push_to_jira',
        'vulnerability_ids',
        'reporter',
        'title',
        'date',
        'sla_start_date',
        'sla_expiration_date',
        'cwe',
        'epss_score',
        'epss_percentile',
        'cvssv3',
        'cvssv3_score',
        'severity',
        'description',
        'mitigation',
        'impact',
        'steps_to_reproduce',
        'severity_justification',
        'references',
        'active',
        'verified',
        'false_p',
        'duplicate',
        'out_of_scope',
        'risk_accepted',
        'under_review',
        'last_status_update',
        'under_defect_review',
        'is_mitigated',
        'mitigated',
        'numerical_severity',
        'last_reviewed',
        'param',
        'payload',
        'hash_code',
        'line',
        'file_path',
        'component_name',
        'component_version',
        'static_finding',
        'dynamic_finding',
        'created',
        'scanner_confidence',
        'unique_id_from_tool',
        'vuln_id_from_tool',
        'sast_source_object',
        'sast_sink_object',
        'sast_source_line',
        'sast_source_file_path',
        'nb_occurences',
        'publish_date',
        'service',
        'planned_remediation_date',
        'planned_remediation_version',
        'effort_for_fixing',
        'duplicate_finding',
        'review_requested_by',
        'defect_review_requested_by',
        'mitigated_by',
        'last_reviewed_by',
        'sonarqube_issue',
        'endpoints',
        'reviewers',
        'files',
    ]

    @field_validator('cvssv3')
    def cvssv3_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r'^AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]', value):
            raise ValueError(
                r'must validate the regular expression /^AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]/'
            )
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
        """Create an instance of FindingCreate from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                'id',
                'notes',
                'last_status_update',
                'mitigated',
                'last_reviewed',
                'param',
                'payload',
                'hash_code',
                'created',
                'scanner_confidence',
                'duplicate_finding',
                'mitigated_by',
                'last_reviewed_by',
                'endpoints',
                'files',
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in vulnerability_ids (list)
        _items = []
        if self.vulnerability_ids:
            for _item_vulnerability_ids in self.vulnerability_ids:
                if _item_vulnerability_ids:
                    _items.append(_item_vulnerability_ids.to_dict())
            _dict['vulnerability_ids'] = _items
        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and 'url' in self.model_fields_set:
            _dict['url'] = None

        # set to None if sla_start_date (nullable) is None
        # and model_fields_set contains the field
        if self.sla_start_date is None and 'sla_start_date' in self.model_fields_set:
            _dict['sla_start_date'] = None

        # set to None if sla_expiration_date (nullable) is None
        # and model_fields_set contains the field
        if self.sla_expiration_date is None and 'sla_expiration_date' in self.model_fields_set:
            _dict['sla_expiration_date'] = None

        # set to None if cwe (nullable) is None
        # and model_fields_set contains the field
        if self.cwe is None and 'cwe' in self.model_fields_set:
            _dict['cwe'] = None

        # set to None if epss_score (nullable) is None
        # and model_fields_set contains the field
        if self.epss_score is None and 'epss_score' in self.model_fields_set:
            _dict['epss_score'] = None

        # set to None if epss_percentile (nullable) is None
        # and model_fields_set contains the field
        if self.epss_percentile is None and 'epss_percentile' in self.model_fields_set:
            _dict['epss_percentile'] = None

        # set to None if cvssv3 (nullable) is None
        # and model_fields_set contains the field
        if self.cvssv3 is None and 'cvssv3' in self.model_fields_set:
            _dict['cvssv3'] = None

        # set to None if cvssv3_score (nullable) is None
        # and model_fields_set contains the field
        if self.cvssv3_score is None and 'cvssv3_score' in self.model_fields_set:
            _dict['cvssv3_score'] = None

        # set to None if mitigation (nullable) is None
        # and model_fields_set contains the field
        if self.mitigation is None and 'mitigation' in self.model_fields_set:
            _dict['mitigation'] = None

        # set to None if impact (nullable) is None
        # and model_fields_set contains the field
        if self.impact is None and 'impact' in self.model_fields_set:
            _dict['impact'] = None

        # set to None if steps_to_reproduce (nullable) is None
        # and model_fields_set contains the field
        if self.steps_to_reproduce is None and 'steps_to_reproduce' in self.model_fields_set:
            _dict['steps_to_reproduce'] = None

        # set to None if severity_justification (nullable) is None
        # and model_fields_set contains the field
        if self.severity_justification is None and 'severity_justification' in self.model_fields_set:
            _dict['severity_justification'] = None

        # set to None if references (nullable) is None
        # and model_fields_set contains the field
        if self.references is None and 'references' in self.model_fields_set:
            _dict['references'] = None

        # set to None if last_status_update (nullable) is None
        # and model_fields_set contains the field
        if self.last_status_update is None and 'last_status_update' in self.model_fields_set:
            _dict['last_status_update'] = None

        # set to None if mitigated (nullable) is None
        # and model_fields_set contains the field
        if self.mitigated is None and 'mitigated' in self.model_fields_set:
            _dict['mitigated'] = None

        # set to None if last_reviewed (nullable) is None
        # and model_fields_set contains the field
        if self.last_reviewed is None and 'last_reviewed' in self.model_fields_set:
            _dict['last_reviewed'] = None

        # set to None if param (nullable) is None
        # and model_fields_set contains the field
        if self.param is None and 'param' in self.model_fields_set:
            _dict['param'] = None

        # set to None if payload (nullable) is None
        # and model_fields_set contains the field
        if self.payload is None and 'payload' in self.model_fields_set:
            _dict['payload'] = None

        # set to None if hash_code (nullable) is None
        # and model_fields_set contains the field
        if self.hash_code is None and 'hash_code' in self.model_fields_set:
            _dict['hash_code'] = None

        # set to None if line (nullable) is None
        # and model_fields_set contains the field
        if self.line is None and 'line' in self.model_fields_set:
            _dict['line'] = None

        # set to None if file_path (nullable) is None
        # and model_fields_set contains the field
        if self.file_path is None and 'file_path' in self.model_fields_set:
            _dict['file_path'] = None

        # set to None if component_name (nullable) is None
        # and model_fields_set contains the field
        if self.component_name is None and 'component_name' in self.model_fields_set:
            _dict['component_name'] = None

        # set to None if component_version (nullable) is None
        # and model_fields_set contains the field
        if self.component_version is None and 'component_version' in self.model_fields_set:
            _dict['component_version'] = None

        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and 'created' in self.model_fields_set:
            _dict['created'] = None

        # set to None if scanner_confidence (nullable) is None
        # and model_fields_set contains the field
        if self.scanner_confidence is None and 'scanner_confidence' in self.model_fields_set:
            _dict['scanner_confidence'] = None

        # set to None if unique_id_from_tool (nullable) is None
        # and model_fields_set contains the field
        if self.unique_id_from_tool is None and 'unique_id_from_tool' in self.model_fields_set:
            _dict['unique_id_from_tool'] = None

        # set to None if vuln_id_from_tool (nullable) is None
        # and model_fields_set contains the field
        if self.vuln_id_from_tool is None and 'vuln_id_from_tool' in self.model_fields_set:
            _dict['vuln_id_from_tool'] = None

        # set to None if sast_source_object (nullable) is None
        # and model_fields_set contains the field
        if self.sast_source_object is None and 'sast_source_object' in self.model_fields_set:
            _dict['sast_source_object'] = None

        # set to None if sast_sink_object (nullable) is None
        # and model_fields_set contains the field
        if self.sast_sink_object is None and 'sast_sink_object' in self.model_fields_set:
            _dict['sast_sink_object'] = None

        # set to None if sast_source_line (nullable) is None
        # and model_fields_set contains the field
        if self.sast_source_line is None and 'sast_source_line' in self.model_fields_set:
            _dict['sast_source_line'] = None

        # set to None if sast_source_file_path (nullable) is None
        # and model_fields_set contains the field
        if self.sast_source_file_path is None and 'sast_source_file_path' in self.model_fields_set:
            _dict['sast_source_file_path'] = None

        # set to None if nb_occurences (nullable) is None
        # and model_fields_set contains the field
        if self.nb_occurences is None and 'nb_occurences' in self.model_fields_set:
            _dict['nb_occurences'] = None

        # set to None if publish_date (nullable) is None
        # and model_fields_set contains the field
        if self.publish_date is None and 'publish_date' in self.model_fields_set:
            _dict['publish_date'] = None

        # set to None if service (nullable) is None
        # and model_fields_set contains the field
        if self.service is None and 'service' in self.model_fields_set:
            _dict['service'] = None

        # set to None if planned_remediation_date (nullable) is None
        # and model_fields_set contains the field
        if self.planned_remediation_date is None and 'planned_remediation_date' in self.model_fields_set:
            _dict['planned_remediation_date'] = None

        # set to None if planned_remediation_version (nullable) is None
        # and model_fields_set contains the field
        if self.planned_remediation_version is None and 'planned_remediation_version' in self.model_fields_set:
            _dict['planned_remediation_version'] = None

        # set to None if effort_for_fixing (nullable) is None
        # and model_fields_set contains the field
        if self.effort_for_fixing is None and 'effort_for_fixing' in self.model_fields_set:
            _dict['effort_for_fixing'] = None

        # set to None if duplicate_finding (nullable) is None
        # and model_fields_set contains the field
        if self.duplicate_finding is None and 'duplicate_finding' in self.model_fields_set:
            _dict['duplicate_finding'] = None

        # set to None if review_requested_by (nullable) is None
        # and model_fields_set contains the field
        if self.review_requested_by is None and 'review_requested_by' in self.model_fields_set:
            _dict['review_requested_by'] = None

        # set to None if defect_review_requested_by (nullable) is None
        # and model_fields_set contains the field
        if self.defect_review_requested_by is None and 'defect_review_requested_by' in self.model_fields_set:
            _dict['defect_review_requested_by'] = None

        # set to None if mitigated_by (nullable) is None
        # and model_fields_set contains the field
        if self.mitigated_by is None and 'mitigated_by' in self.model_fields_set:
            _dict['mitigated_by'] = None

        # set to None if last_reviewed_by (nullable) is None
        # and model_fields_set contains the field
        if self.last_reviewed_by is None and 'last_reviewed_by' in self.model_fields_set:
            _dict['last_reviewed_by'] = None

        # set to None if sonarqube_issue (nullable) is None
        # and model_fields_set contains the field
        if self.sonarqube_issue is None and 'sonarqube_issue' in self.model_fields_set:
            _dict['sonarqube_issue'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FindingCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'id': obj.get('id'),
                'notes': obj.get('notes'),
                'test': obj.get('test'),
                'thread_id': obj.get('thread_id') if obj.get('thread_id') is not None else 0,
                'found_by': obj.get('found_by'),
                'url': obj.get('url'),
                'tags': obj.get('tags'),
                'push_to_jira': obj.get('push_to_jira') if obj.get('push_to_jira') is not None else False,
                'vulnerability_ids': [VulnerabilityId.from_dict(_item) for _item in obj['vulnerability_ids']]
                if obj.get('vulnerability_ids') is not None
                else None,
                'reporter': obj.get('reporter'),
                'title': obj.get('title'),
                'date': obj.get('date'),
                'sla_start_date': obj.get('sla_start_date'),
                'sla_expiration_date': obj.get('sla_expiration_date'),
                'cwe': obj.get('cwe'),
                'epss_score': obj.get('epss_score'),
                'epss_percentile': obj.get('epss_percentile'),
                'cvssv3': obj.get('cvssv3'),
                'cvssv3_score': obj.get('cvssv3_score'),
                'severity': obj.get('severity'),
                'description': obj.get('description'),
                'mitigation': obj.get('mitigation'),
                'impact': obj.get('impact'),
                'steps_to_reproduce': obj.get('steps_to_reproduce'),
                'severity_justification': obj.get('severity_justification'),
                'references': obj.get('references'),
                'active': obj.get('active'),
                'verified': obj.get('verified'),
                'false_p': obj.get('false_p'),
                'duplicate': obj.get('duplicate'),
                'out_of_scope': obj.get('out_of_scope'),
                'risk_accepted': obj.get('risk_accepted'),
                'under_review': obj.get('under_review'),
                'last_status_update': obj.get('last_status_update'),
                'under_defect_review': obj.get('under_defect_review'),
                'is_mitigated': obj.get('is_mitigated'),
                'mitigated': obj.get('mitigated'),
                'numerical_severity': obj.get('numerical_severity'),
                'last_reviewed': obj.get('last_reviewed'),
                'param': obj.get('param'),
                'payload': obj.get('payload'),
                'hash_code': obj.get('hash_code'),
                'line': obj.get('line'),
                'file_path': obj.get('file_path'),
                'component_name': obj.get('component_name'),
                'component_version': obj.get('component_version'),
                'static_finding': obj.get('static_finding'),
                'dynamic_finding': obj.get('dynamic_finding'),
                'created': obj.get('created'),
                'scanner_confidence': obj.get('scanner_confidence'),
                'unique_id_from_tool': obj.get('unique_id_from_tool'),
                'vuln_id_from_tool': obj.get('vuln_id_from_tool'),
                'sast_source_object': obj.get('sast_source_object'),
                'sast_sink_object': obj.get('sast_sink_object'),
                'sast_source_line': obj.get('sast_source_line'),
                'sast_source_file_path': obj.get('sast_source_file_path'),
                'nb_occurences': obj.get('nb_occurences'),
                'publish_date': obj.get('publish_date'),
                'service': obj.get('service'),
                'planned_remediation_date': obj.get('planned_remediation_date'),
                'planned_remediation_version': obj.get('planned_remediation_version'),
                'effort_for_fixing': obj.get('effort_for_fixing'),
                'duplicate_finding': obj.get('duplicate_finding'),
                'review_requested_by': obj.get('review_requested_by'),
                'defect_review_requested_by': obj.get('defect_review_requested_by'),
                'mitigated_by': obj.get('mitigated_by'),
                'last_reviewed_by': obj.get('last_reviewed_by'),
                'sonarqube_issue': obj.get('sonarqube_issue'),
                'endpoints': obj.get('endpoints'),
                'reviewers': obj.get('reviewers'),
                'files': obj.get('files'),
            }
        )
        return _obj
