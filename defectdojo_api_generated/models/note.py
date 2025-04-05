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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing_extensions import Self

from defectdojo_api_generated.models.note_history import NoteHistory
from defectdojo_api_generated.models.note_type import NoteType
from defectdojo_api_generated.models.user_stub import UserStub


class Note(BaseModel):
    """
    Note
    """  # noqa: E501

    id: StrictInt
    author: UserStub
    editor: Optional[UserStub]
    history: List[NoteHistory]
    note_type: NoteType
    entry: StrictStr
    var_date: datetime = Field(alias='date')
    private: Optional[StrictBool] = None
    edited: Optional[StrictBool] = None
    edit_time: Optional[datetime]
    __properties: ClassVar[List[str]] = [
        'id',
        'author',
        'editor',
        'history',
        'note_type',
        'entry',
        'date',
        'private',
        'edited',
        'edit_time',
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
        """Create an instance of Note from a JSON string"""
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
        """
        excluded_fields: Set[str] = set(
            [
                'id',
                'author',
                'editor',
                'history',
                'note_type',
                'var_date',
                'edit_time',
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of editor
        if self.editor:
            _dict['editor'] = self.editor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in history (list)
        _items = []
        if self.history:
            for _item_history in self.history:
                if _item_history:
                    _items.append(_item_history.to_dict())
            _dict['history'] = _items
        # override the default output from pydantic by calling `to_dict()` of note_type
        if self.note_type:
            _dict['note_type'] = self.note_type.to_dict()
        # set to None if editor (nullable) is None
        # and model_fields_set contains the field
        if self.editor is None and 'editor' in self.model_fields_set:
            _dict['editor'] = None

        # set to None if edit_time (nullable) is None
        # and model_fields_set contains the field
        if self.edit_time is None and 'edit_time' in self.model_fields_set:
            _dict['edit_time'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Note from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'id': obj.get('id'),
                'author': UserStub.from_dict(obj['author']) if obj.get('author') is not None else None,
                'editor': UserStub.from_dict(obj['editor']) if obj.get('editor') is not None else None,
                'history': [NoteHistory.from_dict(_item) for _item in obj['history']]
                if obj.get('history') is not None
                else None,
                'note_type': NoteType.from_dict(obj['note_type']) if obj.get('note_type') is not None else None,
                'entry': obj.get('entry'),
                'date': obj.get('date'),
                'private': obj.get('private'),
                'edited': obj.get('edited'),
                'edit_time': obj.get('edit_time'),
            }
        )
        return _obj
