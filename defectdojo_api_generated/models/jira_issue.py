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
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing_extensions import Annotated, Self


class JIRAIssue(BaseModel):
    """
    JIRAIssue
    """  # noqa: E501

    id: StrictInt
    url: StrictStr
    jira_id: Annotated[str, Field(strict=True, max_length=200)]
    jira_key: Annotated[str, Field(strict=True, max_length=200)]
    jira_creation: Optional[datetime] = Field(
        default=None, description='The date a Jira issue was created from this finding.'
    )
    jira_change: Optional[datetime] = Field(
        default=None, description='The date the linked Jira issue was last modified.'
    )
    jira_project: Optional[StrictInt] = None
    finding: Optional[StrictInt] = None
    engagement: Optional[StrictInt] = None
    finding_group: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = [
        'id',
        'url',
        'jira_id',
        'jira_key',
        'jira_creation',
        'jira_change',
        'jira_project',
        'finding',
        'engagement',
        'finding_group',
    ]

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
        """Create an instance of JIRAIssue from a JSON string"""
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
        """
        excluded_fields: Set[str] = set(
            [
                'id',
                'url',
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if jira_creation (nullable) is None
        # and model_fields_set contains the field
        if self.jira_creation is None and 'jira_creation' in self.model_fields_set:
            _dict['jira_creation'] = None

        # set to None if jira_change (nullable) is None
        # and model_fields_set contains the field
        if self.jira_change is None and 'jira_change' in self.model_fields_set:
            _dict['jira_change'] = None

        # set to None if jira_project (nullable) is None
        # and model_fields_set contains the field
        if self.jira_project is None and 'jira_project' in self.model_fields_set:
            _dict['jira_project'] = None

        # set to None if finding (nullable) is None
        # and model_fields_set contains the field
        if self.finding is None and 'finding' in self.model_fields_set:
            _dict['finding'] = None

        # set to None if engagement (nullable) is None
        # and model_fields_set contains the field
        if self.engagement is None and 'engagement' in self.model_fields_set:
            _dict['engagement'] = None

        # set to None if finding_group (nullable) is None
        # and model_fields_set contains the field
        if self.finding_group is None and 'finding_group' in self.model_fields_set:
            _dict['finding_group'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JIRAIssue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'id': obj.get('id'),
                'url': obj.get('url'),
                'jira_id': obj.get('jira_id'),
                'jira_key': obj.get('jira_key'),
                'jira_creation': obj.get('jira_creation'),
                'jira_change': obj.get('jira_change'),
                'jira_project': obj.get('jira_project'),
                'finding': obj.get('finding'),
                'engagement': obj.get('engagement'),
                'finding_group': obj.get('finding_group'),
            }
        )
        return _obj
