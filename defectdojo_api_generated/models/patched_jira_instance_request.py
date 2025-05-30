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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing_extensions import Annotated, Self


class PatchedJIRAInstanceRequest(BaseModel):
    """
    PatchedJIRAInstanceRequest
    """  # noqa: E501

    configuration_name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=2000)]] = Field(
        default=None, description='Enter a name to give to this configuration'
    )
    url: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=2000)]] = Field(
        default=None, description='For more information how to configure Jira, read the DefectDojo documentation.'
    )
    username: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=2000)]] = Field(
        default=None, description='Username or Email Address, see DefectDojo documentation for more information.'
    )
    password: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=2000)]] = Field(
        default=None,
        description='Password, API Token, or Personal Access Token, see DefectDojo documentation for more information.',
    )
    default_issue_type: Optional[StrictStr] = Field(
        default=None,
        description='You can define extra issue types in settings.py  * `Task` - Task * `Story` - Story * `Epic` - Epic * `Spike` - Spike * `Bug` - Bug * `Security` - Security',
    )
    issue_template_dir: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(
        default=None,
        description='Choose the folder containing the Django templates used to render the JIRA issue description. These are stored in dojo/templates/issue-trackers. Leave empty to use the default jira_full templates.',
    )
    epic_name_id: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(
        default=None,
        description="To obtain the 'Epic name id' visit https://<YOUR JIRA URL>/rest/api/2/field and search for Epic Name. Copy the number out of cf[number] and paste it here.",
    )
    open_status_key: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(
        default=None,
        description='Transition ID to Re-Open JIRA issues, visit https://<YOUR JIRA URL>/rest/api/latest/issue/<ANY VALID ISSUE KEY>/transitions?expand=transitions.fields to find the ID for your JIRA instance',
    )
    close_status_key: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(
        default=None,
        description='Transition ID to Close JIRA issues, visit https://<YOUR JIRA URL>/rest/api/latest/issue/<ANY VALID ISSUE KEY>/transitions?expand=transitions.fields to find the ID for your JIRA instance',
    )
    info_mapping_severity: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=200)]] = Field(
        default=None, description="Maps to the 'Priority' field in Jira. For example: Info"
    )
    low_mapping_severity: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=200)]] = Field(
        default=None, description="Maps to the 'Priority' field in Jira. For example: Low"
    )
    medium_mapping_severity: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=200)]] = Field(
        default=None, description="Maps to the 'Priority' field in Jira. For example: Medium"
    )
    high_mapping_severity: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=200)]] = Field(
        default=None, description="Maps to the 'Priority' field in Jira. For example: High"
    )
    critical_mapping_severity: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=200)]] = Field(
        default=None, description="Maps to the 'Priority' field in Jira. For example: Critical"
    )
    finding_text: Optional[StrictStr] = Field(
        default=None,
        description='Additional text that will be added to the finding in Jira. For example including how the finding was created or who to contact for more information.',
    )
    accepted_mapping_resolution: Optional[Annotated[str, Field(strict=True, max_length=300)]] = Field(
        default=None, description='JIRA resolution names (comma-separated values) that maps to an Accepted Finding'
    )
    false_positive_mapping_resolution: Optional[Annotated[str, Field(strict=True, max_length=300)]] = Field(
        default=None, description='JIRA resolution names (comma-separated values) that maps to a False Positive Finding'
    )
    global_jira_sla_notification: Optional[StrictBool] = Field(
        default=None, description='This setting can be overidden at the Product level'
    )
    finding_jira_sync: Optional[StrictBool] = Field(
        default=None, description='If enabled, this will sync changes to a Finding automatically to JIRA'
    )
    __properties: ClassVar[List[str]] = [
        'configuration_name',
        'url',
        'username',
        'password',
        'default_issue_type',
        'issue_template_dir',
        'epic_name_id',
        'open_status_key',
        'close_status_key',
        'info_mapping_severity',
        'low_mapping_severity',
        'medium_mapping_severity',
        'high_mapping_severity',
        'critical_mapping_severity',
        'finding_text',
        'accepted_mapping_resolution',
        'false_positive_mapping_resolution',
        'global_jira_sla_notification',
        'finding_jira_sync',
    ]

    @field_validator('default_issue_type')
    def default_issue_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Task', 'Story', 'Epic', 'Spike', 'Bug', 'Security']):
            raise ValueError("must be one of enum values ('Task', 'Story', 'Epic', 'Spike', 'Bug', 'Security')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        defer_build=True,
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
        """Create an instance of PatchedJIRAInstanceRequest from a JSON string"""
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

        # set to None if finding_text (nullable) is None
        # and model_fields_set contains the field
        if self.finding_text is None and 'finding_text' in self.model_fields_set:
            _dict['finding_text'] = None

        # set to None if accepted_mapping_resolution (nullable) is None
        # and model_fields_set contains the field
        if self.accepted_mapping_resolution is None and 'accepted_mapping_resolution' in self.model_fields_set:
            _dict['accepted_mapping_resolution'] = None

        # set to None if false_positive_mapping_resolution (nullable) is None
        # and model_fields_set contains the field
        if (
            self.false_positive_mapping_resolution is None
            and 'false_positive_mapping_resolution' in self.model_fields_set
        ):
            _dict['false_positive_mapping_resolution'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedJIRAInstanceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'configuration_name': obj.get('configuration_name'),
                'url': obj.get('url'),
                'username': obj.get('username'),
                'password': obj.get('password'),
                'default_issue_type': obj.get('default_issue_type'),
                'issue_template_dir': obj.get('issue_template_dir'),
                'epic_name_id': obj.get('epic_name_id'),
                'open_status_key': obj.get('open_status_key'),
                'close_status_key': obj.get('close_status_key'),
                'info_mapping_severity': obj.get('info_mapping_severity'),
                'low_mapping_severity': obj.get('low_mapping_severity'),
                'medium_mapping_severity': obj.get('medium_mapping_severity'),
                'high_mapping_severity': obj.get('high_mapping_severity'),
                'critical_mapping_severity': obj.get('critical_mapping_severity'),
                'finding_text': obj.get('finding_text'),
                'accepted_mapping_resolution': obj.get('accepted_mapping_resolution'),
                'false_positive_mapping_resolution': obj.get('false_positive_mapping_resolution'),
                'global_jira_sla_notification': obj.get('global_jira_sla_notification'),
                'finding_jira_sync': obj.get('finding_jira_sync'),
            }
        )
        return _obj
