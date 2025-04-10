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


class TestRequest(BaseModel):
    """
    TestRequest
    """  # noqa: E501

    tags: Optional[List[Annotated[str, Field(min_length=1, strict=True)]]] = None
    scan_type: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    title: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    description: Optional[StrictStr] = None
    target_start: datetime
    target_end: datetime
    percent_complete: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    version: Optional[Annotated[str, Field(strict=True, max_length=100)]] = None
    build_id: Optional[Annotated[str, Field(strict=True, max_length=150)]] = Field(
        default=None, description='Build ID that was tested, a reimport may update this field.'
    )
    commit_hash: Optional[Annotated[str, Field(strict=True, max_length=150)]] = Field(
        default=None, description='Commit hash tested, a reimport may update this field.'
    )
    branch_tag: Optional[Annotated[str, Field(strict=True, max_length=150)]] = Field(
        default=None, description='Tag or branch that was tested, a reimport may update this field.'
    )
    lead: Optional[StrictInt] = None
    test_type: StrictInt
    environment: Optional[StrictInt] = None
    api_scan_configuration: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = [
        'tags',
        'scan_type',
        'title',
        'description',
        'target_start',
        'target_end',
        'percent_complete',
        'version',
        'build_id',
        'commit_hash',
        'branch_tag',
        'lead',
        'test_type',
        'environment',
        'api_scan_configuration',
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
        """Create an instance of TestRequest from a JSON string"""
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
        # set to None if scan_type (nullable) is None
        # and model_fields_set contains the field
        if self.scan_type is None and 'scan_type' in self.model_fields_set:
            _dict['scan_type'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and 'title' in self.model_fields_set:
            _dict['title'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and 'description' in self.model_fields_set:
            _dict['description'] = None

        # set to None if percent_complete (nullable) is None
        # and model_fields_set contains the field
        if self.percent_complete is None and 'percent_complete' in self.model_fields_set:
            _dict['percent_complete'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and 'version' in self.model_fields_set:
            _dict['version'] = None

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

        # set to None if lead (nullable) is None
        # and model_fields_set contains the field
        if self.lead is None and 'lead' in self.model_fields_set:
            _dict['lead'] = None

        # set to None if environment (nullable) is None
        # and model_fields_set contains the field
        if self.environment is None and 'environment' in self.model_fields_set:
            _dict['environment'] = None

        # set to None if api_scan_configuration (nullable) is None
        # and model_fields_set contains the field
        if self.api_scan_configuration is None and 'api_scan_configuration' in self.model_fields_set:
            _dict['api_scan_configuration'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'tags': obj.get('tags'),
                'scan_type': obj.get('scan_type'),
                'title': obj.get('title'),
                'description': obj.get('description'),
                'target_start': obj.get('target_start'),
                'target_end': obj.get('target_end'),
                'percent_complete': obj.get('percent_complete'),
                'version': obj.get('version'),
                'build_id': obj.get('build_id'),
                'commit_hash': obj.get('commit_hash'),
                'branch_tag': obj.get('branch_tag'),
                'lead': obj.get('lead'),
                'test_type': obj.get('test_type'),
                'environment': obj.get('environment'),
                'api_scan_configuration': obj.get('api_scan_configuration'),
            }
        )
        return _obj
