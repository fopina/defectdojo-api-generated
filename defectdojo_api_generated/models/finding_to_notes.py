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

from pydantic import BaseModel, ConfigDict, StrictInt
from typing_extensions import Self

from defectdojo_api_generated.models.note import Note


class FindingToNotes(BaseModel):
    """
    FindingToNotes
    """  # noqa: E501

    finding_id: Optional[StrictInt]
    notes: List[Note]
    __properties: ClassVar[List[str]] = ['finding_id', 'notes']

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
        """Create an instance of FindingToNotes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item_notes in self.notes:
                if _item_notes:
                    _items.append(_item_notes.to_dict())
            _dict['notes'] = _items
        # set to None if finding_id (nullable) is None
        # and model_fields_set contains the field
        if self.finding_id is None and 'finding_id' in self.model_fields_set:
            _dict['finding_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FindingToNotes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'finding_id': obj.get('finding_id'),
                'notes': [Note.from_dict(_item) for _item in obj['notes']] if obj.get('notes') is not None else None,
            }
        )
        return _obj
