# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing_extensions import Annotated, Self


class JIRAProjectRequest(BaseModel):
    """
    JIRAProjectRequest
    """  # noqa: E501

    project_key: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    issue_template_dir: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(
        default=None,
        description='Choose the folder containing the Django templates used to render the JIRA issue description. These are stored in dojo/templates/issue-trackers. Leave empty to use the default jira_full templates.',
    )
    component: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    custom_fields: Optional[Any] = Field(
        default=None,
        description='JIRA custom field JSON mapping of Id to value, e.g. {"customfield_10122": [{"name": "8.0.1"}]}',
    )
    default_assignee: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(
        default=None,
        description='JIRA default assignee (name). If left blank then it defaults to whatever is configured in JIRA.',
    )
    jira_labels: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(
        default=None, description='JIRA issue labels space seperated'
    )
    add_vulnerability_id_to_jira_label: Optional[StrictBool] = None
    push_all_issues: Optional[StrictBool] = Field(
        default=None,
        description='Automatically create JIRA tickets for verified findings, assuming enforce_verified_status is True, or for all findings otherwise. Once linked, the JIRA ticket will continue to sync, regardless of status in DefectDojo.',
    )
    enable_engagement_epic_mapping: Optional[StrictBool] = None
    epic_issue_type_name: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(
        default=None, description='The name of the of structure that represents an Epic'
    )
    push_notes: Optional[StrictBool] = None
    product_jira_sla_notification: Optional[StrictBool] = None
    risk_acceptance_expiration_notification: Optional[StrictBool] = None
    enabled: Optional[StrictBool] = Field(
        default=None,
        description='When disabled, Findings will no longer be pushed to Jira, even if they have already been pushed previously.',
    )
    jira_instance: Optional[StrictInt] = None
    product: Optional[StrictInt] = None
    engagement: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = [
        'project_key',
        'issue_template_dir',
        'component',
        'custom_fields',
        'default_assignee',
        'jira_labels',
        'add_vulnerability_id_to_jira_label',
        'push_all_issues',
        'enable_engagement_epic_mapping',
        'epic_issue_type_name',
        'push_notes',
        'product_jira_sla_notification',
        'risk_acceptance_expiration_notification',
        'enabled',
        'jira_instance',
        'product',
        'engagement',
    ]

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
        """Create an instance of JIRAProjectRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if issue_template_dir (nullable) is None
        # and model_fields_set contains the field
        if self.issue_template_dir is None and 'issue_template_dir' in self.model_fields_set:
            _dict['issue_template_dir'] = None

        # set to None if custom_fields (nullable) is None
        # and model_fields_set contains the field
        if self.custom_fields is None and 'custom_fields' in self.model_fields_set:
            _dict['custom_fields'] = None

        # set to None if default_assignee (nullable) is None
        # and model_fields_set contains the field
        if self.default_assignee is None and 'default_assignee' in self.model_fields_set:
            _dict['default_assignee'] = None

        # set to None if jira_labels (nullable) is None
        # and model_fields_set contains the field
        if self.jira_labels is None and 'jira_labels' in self.model_fields_set:
            _dict['jira_labels'] = None

        # set to None if jira_instance (nullable) is None
        # and model_fields_set contains the field
        if self.jira_instance is None and 'jira_instance' in self.model_fields_set:
            _dict['jira_instance'] = None

        # set to None if product (nullable) is None
        # and model_fields_set contains the field
        if self.product is None and 'product' in self.model_fields_set:
            _dict['product'] = None

        # set to None if engagement (nullable) is None
        # and model_fields_set contains the field
        if self.engagement is None and 'engagement' in self.model_fields_set:
            _dict['engagement'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JIRAProjectRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'project_key': obj.get('project_key'),
                'issue_template_dir': obj.get('issue_template_dir'),
                'component': obj.get('component'),
                'custom_fields': obj.get('custom_fields'),
                'default_assignee': obj.get('default_assignee'),
                'jira_labels': obj.get('jira_labels'),
                'add_vulnerability_id_to_jira_label': obj.get('add_vulnerability_id_to_jira_label'),
                'push_all_issues': obj.get('push_all_issues'),
                'enable_engagement_epic_mapping': obj.get('enable_engagement_epic_mapping'),
                'epic_issue_type_name': obj.get('epic_issue_type_name'),
                'push_notes': obj.get('push_notes'),
                'product_jira_sla_notification': obj.get('product_jira_sla_notification'),
                'risk_acceptance_expiration_notification': obj.get('risk_acceptance_expiration_notification'),
                'enabled': obj.get('enabled'),
                'jira_instance': obj.get('jira_instance'),
                'product': obj.get('product'),
                'engagement': obj.get('engagement'),
            }
        )
        return _obj
