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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing_extensions import Annotated, Self

from defectdojo_api_generated.models.test_import_finding_action import TestImportFindingAction


class TestImport(BaseModel):
    """
    TestImport
    """  # noqa: E501

    id: StrictInt
    test_import_finding_action_set: List[TestImportFindingAction]
    created: datetime
    modified: datetime
    import_settings: Optional[Any] = None
    type: Optional[Annotated[str, Field(strict=True, max_length=64)]] = None
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
    test: StrictInt
    findings_affected: List[StrictInt]
    __properties: ClassVar[List[str]] = [
        'id',
        'test_import_finding_action_set',
        'created',
        'modified',
        'import_settings',
        'type',
        'version',
        'build_id',
        'commit_hash',
        'branch_tag',
        'test',
        'findings_affected',
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
        """Create an instance of TestImport from a JSON string"""
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
        """
        excluded_fields: Set[str] = set(
            [
                'id',
                'test_import_finding_action_set',
                'created',
                'modified',
                'test',
                'findings_affected',
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in test_import_finding_action_set (list)
        _items = []
        if self.test_import_finding_action_set:
            for _item_test_import_finding_action_set in self.test_import_finding_action_set:
                if _item_test_import_finding_action_set:
                    _items.append(_item_test_import_finding_action_set.to_dict())
            _dict['test_import_finding_action_set'] = _items
        # set to None if import_settings (nullable) is None
        # and model_fields_set contains the field
        if self.import_settings is None and 'import_settings' in self.model_fields_set:
            _dict['import_settings'] = None

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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestImport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'id': obj.get('id'),
                'test_import_finding_action_set': [
                    TestImportFindingAction.from_dict(_item) for _item in obj['test_import_finding_action_set']
                ]
                if obj.get('test_import_finding_action_set') is not None
                else None,
                'created': obj.get('created'),
                'modified': obj.get('modified'),
                'import_settings': obj.get('import_settings'),
                'type': obj.get('type'),
                'version': obj.get('version'),
                'build_id': obj.get('build_id'),
                'commit_hash': obj.get('commit_hash'),
                'branch_tag': obj.get('branch_tag'),
                'test': obj.get('test'),
                'findings_affected': obj.get('findings_affected'),
            }
        )
        return _obj
