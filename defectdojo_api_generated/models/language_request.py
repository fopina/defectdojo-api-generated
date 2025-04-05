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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing_extensions import Annotated, Self


class LanguageRequest(BaseModel):
    """
    LanguageRequest
    """  # noqa: E501

    files: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    blank: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    comment: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    code: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    language: StrictInt
    product: StrictInt
    user: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ['files', 'blank', 'comment', 'code', 'language', 'product', 'user']

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
        """Create an instance of LanguageRequest from a JSON string"""
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
        # set to None if files (nullable) is None
        # and model_fields_set contains the field
        if self.files is None and 'files' in self.model_fields_set:
            _dict['files'] = None

        # set to None if blank (nullable) is None
        # and model_fields_set contains the field
        if self.blank is None and 'blank' in self.model_fields_set:
            _dict['blank'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and 'comment' in self.model_fields_set:
            _dict['comment'] = None

        # set to None if code (nullable) is None
        # and model_fields_set contains the field
        if self.code is None and 'code' in self.model_fields_set:
            _dict['code'] = None

        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and 'user' in self.model_fields_set:
            _dict['user'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LanguageRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'files': obj.get('files'),
                'blank': obj.get('blank'),
                'comment': obj.get('comment'),
                'code': obj.get('code'),
                'language': obj.get('language'),
                'product': obj.get('product'),
                'user': obj.get('user'),
            }
        )
        return _obj
