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
from datetime import date, datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing_extensions import Annotated, Self

from defectdojo_api_generated.models.file import File
from defectdojo_api_generated.models.note import Note


class Engagement(BaseModel):
    """
    Engagement
    """  # noqa: E501

    id: StrictInt
    tags: Optional[List[StrictStr]] = None
    name: Optional[Annotated[str, Field(strict=True, max_length=300)]] = None
    description: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = None
    version: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(
        default=None, description='Version of the product the engagement tested.'
    )
    first_contacted: Optional[date] = None
    target_start: date
    target_end: date
    reason: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = None
    updated: Optional[datetime]
    created: Optional[datetime]
    active: StrictBool
    tracker: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(
        default=None, description='Link to epic or ticket system with changes to version.'
    )
    test_strategy: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    threat_model: Optional[StrictBool] = None
    api_test: Optional[StrictBool] = None
    pen_test: Optional[StrictBool] = None
    check_list: Optional[StrictBool] = None
    status: Optional[StrictStr] = Field(
        default=None,
        description='* `Not Started` - Not Started * `Blocked` - Blocked * `Cancelled` - Cancelled * `Completed` - Completed * `In Progress` - In Progress * `On Hold` - On Hold * `Waiting for Resource` - Waiting for Resource',
    )
    progress: StrictStr
    tmodel_path: Optional[StrictStr]
    done_testing: StrictBool
    engagement_type: Optional[StrictStr] = Field(
        default=None, description='* `Interactive` - Interactive * `CI/CD` - CI/CD'
    )
    build_id: Optional[Annotated[str, Field(strict=True, max_length=150)]] = Field(
        default=None, description='Build ID of the product the engagement tested.'
    )
    commit_hash: Optional[Annotated[str, Field(strict=True, max_length=150)]] = Field(
        default=None, description='Commit hash from repo'
    )
    branch_tag: Optional[Annotated[str, Field(strict=True, max_length=150)]] = Field(
        default=None, description='Tag or branch of the product the engagement tested.'
    )
    source_code_management_uri: Optional[Annotated[str, Field(strict=True, max_length=600)]] = Field(
        default=None, description='Resource link to source code'
    )
    deduplication_on_engagement: Optional[StrictBool] = Field(
        default=None,
        description='If enabled deduplication will only mark a finding in this engagement as duplicate of another finding if both findings are in this engagement. If disabled, deduplication is on the product level.',
    )
    lead: Optional[StrictInt] = None
    requester: Optional[StrictInt] = None
    preset: Optional[StrictInt] = Field(default=None, description='Settings and notes for performing this engagement.')
    report_type: Optional[StrictInt] = None
    product: StrictInt
    build_server: Optional[StrictInt] = Field(default=None, description='Build server responsible for CI/CD test')
    source_code_management_server: Optional[StrictInt] = Field(
        default=None, description='Source code server for CI/CD test'
    )
    orchestration_engine: Optional[StrictInt] = Field(
        default=None, description='Orchestration service responsible for CI/CD test'
    )
    notes: List[Note]
    files: List[File]
    risk_acceptance: List[StrictInt]
    __properties: ClassVar[List[str]] = [
        'id',
        'tags',
        'name',
        'description',
        'version',
        'first_contacted',
        'target_start',
        'target_end',
        'reason',
        'updated',
        'created',
        'active',
        'tracker',
        'test_strategy',
        'threat_model',
        'api_test',
        'pen_test',
        'check_list',
        'status',
        'progress',
        'tmodel_path',
        'done_testing',
        'engagement_type',
        'build_id',
        'commit_hash',
        'branch_tag',
        'source_code_management_uri',
        'deduplication_on_engagement',
        'lead',
        'requester',
        'preset',
        'report_type',
        'product',
        'build_server',
        'source_code_management_server',
        'orchestration_engine',
        'notes',
        'files',
        'risk_acceptance',
    ]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(
            ['Not Started', 'Blocked', 'Cancelled', 'Completed', 'In Progress', 'On Hold', 'Waiting for Resource']
        ):
            raise ValueError(
                "must be one of enum values ('Not Started', 'Blocked', 'Cancelled', 'Completed', 'In Progress', 'On Hold', 'Waiting for Resource')"
            )
        return value

    @field_validator('engagement_type')
    def engagement_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Interactive', 'CI/CD']):
            raise ValueError("must be one of enum values ('Interactive', 'CI/CD')")
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
        """Create an instance of Engagement from a JSON string"""
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
        """
        excluded_fields: Set[str] = set(
            [
                'id',
                'updated',
                'created',
                'active',
                'progress',
                'tmodel_path',
                'done_testing',
                'notes',
                'files',
                'risk_acceptance',
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item_notes in self.notes:
                if _item_notes:
                    _items.append(_item_notes.to_dict())
            _dict['notes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item_files in self.files:
                if _item_files:
                    _items.append(_item_files.to_dict())
            _dict['files'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and 'name' in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and 'description' in self.model_fields_set:
            _dict['description'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and 'version' in self.model_fields_set:
            _dict['version'] = None

        # set to None if first_contacted (nullable) is None
        # and model_fields_set contains the field
        if self.first_contacted is None and 'first_contacted' in self.model_fields_set:
            _dict['first_contacted'] = None

        # set to None if reason (nullable) is None
        # and model_fields_set contains the field
        if self.reason is None and 'reason' in self.model_fields_set:
            _dict['reason'] = None

        # set to None if updated (nullable) is None
        # and model_fields_set contains the field
        if self.updated is None and 'updated' in self.model_fields_set:
            _dict['updated'] = None

        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and 'created' in self.model_fields_set:
            _dict['created'] = None

        # set to None if tracker (nullable) is None
        # and model_fields_set contains the field
        if self.tracker is None and 'tracker' in self.model_fields_set:
            _dict['tracker'] = None

        # set to None if test_strategy (nullable) is None
        # and model_fields_set contains the field
        if self.test_strategy is None and 'test_strategy' in self.model_fields_set:
            _dict['test_strategy'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and 'status' in self.model_fields_set:
            _dict['status'] = None

        # set to None if tmodel_path (nullable) is None
        # and model_fields_set contains the field
        if self.tmodel_path is None and 'tmodel_path' in self.model_fields_set:
            _dict['tmodel_path'] = None

        # set to None if engagement_type (nullable) is None
        # and model_fields_set contains the field
        if self.engagement_type is None and 'engagement_type' in self.model_fields_set:
            _dict['engagement_type'] = None

        # set to None if build_id (nullable) is None
        # and model_fields_set contains the field
        if self.build_id is None and 'build_id' in self.model_fields_set:
            _dict['build_id'] = None

        # set to None if commit_hash (nullable) is None
        # and model_fields_set contains the field
        if self.commit_hash is None and 'commit_hash' in self.model_fields_set:
            _dict['commit_hash'] = None

        # set to None if branch_tag (nullable) is None
        # and model_fields_set contains the field
        if self.branch_tag is None and 'branch_tag' in self.model_fields_set:
            _dict['branch_tag'] = None

        # set to None if source_code_management_uri (nullable) is None
        # and model_fields_set contains the field
        if self.source_code_management_uri is None and 'source_code_management_uri' in self.model_fields_set:
            _dict['source_code_management_uri'] = None

        # set to None if lead (nullable) is None
        # and model_fields_set contains the field
        if self.lead is None and 'lead' in self.model_fields_set:
            _dict['lead'] = None

        # set to None if requester (nullable) is None
        # and model_fields_set contains the field
        if self.requester is None and 'requester' in self.model_fields_set:
            _dict['requester'] = None

        # set to None if preset (nullable) is None
        # and model_fields_set contains the field
        if self.preset is None and 'preset' in self.model_fields_set:
            _dict['preset'] = None

        # set to None if report_type (nullable) is None
        # and model_fields_set contains the field
        if self.report_type is None and 'report_type' in self.model_fields_set:
            _dict['report_type'] = None

        # set to None if build_server (nullable) is None
        # and model_fields_set contains the field
        if self.build_server is None and 'build_server' in self.model_fields_set:
            _dict['build_server'] = None

        # set to None if source_code_management_server (nullable) is None
        # and model_fields_set contains the field
        if self.source_code_management_server is None and 'source_code_management_server' in self.model_fields_set:
            _dict['source_code_management_server'] = None

        # set to None if orchestration_engine (nullable) is None
        # and model_fields_set contains the field
        if self.orchestration_engine is None and 'orchestration_engine' in self.model_fields_set:
            _dict['orchestration_engine'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Engagement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'id': obj.get('id'),
                'tags': obj.get('tags'),
                'name': obj.get('name'),
                'description': obj.get('description'),
                'version': obj.get('version'),
                'first_contacted': obj.get('first_contacted'),
                'target_start': obj.get('target_start'),
                'target_end': obj.get('target_end'),
                'reason': obj.get('reason'),
                'updated': obj.get('updated'),
                'created': obj.get('created'),
                'active': obj.get('active'),
                'tracker': obj.get('tracker'),
                'test_strategy': obj.get('test_strategy'),
                'threat_model': obj.get('threat_model'),
                'api_test': obj.get('api_test'),
                'pen_test': obj.get('pen_test'),
                'check_list': obj.get('check_list'),
                'status': obj.get('status'),
                'progress': obj.get('progress'),
                'tmodel_path': obj.get('tmodel_path'),
                'done_testing': obj.get('done_testing'),
                'engagement_type': obj.get('engagement_type'),
                'build_id': obj.get('build_id'),
                'commit_hash': obj.get('commit_hash'),
                'branch_tag': obj.get('branch_tag'),
                'source_code_management_uri': obj.get('source_code_management_uri'),
                'deduplication_on_engagement': obj.get('deduplication_on_engagement'),
                'lead': obj.get('lead'),
                'requester': obj.get('requester'),
                'preset': obj.get('preset'),
                'report_type': obj.get('report_type'),
                'product': obj.get('product'),
                'build_server': obj.get('build_server'),
                'source_code_management_server': obj.get('source_code_management_server'),
                'orchestration_engine': obj.get('orchestration_engine'),
                'notes': [Note.from_dict(_item) for _item in obj['notes']] if obj.get('notes') is not None else None,
                'files': [File.from_dict(_item) for _item in obj['files']] if obj.get('files') is not None else None,
                'risk_acceptance': obj.get('risk_acceptance'),
            }
        )
        return _obj
