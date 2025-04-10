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
from typing_extensions import Self


class GlobalRoleRequest(BaseModel):
    """
    GlobalRoleRequest
    """  # noqa: E501

    user: Optional[StrictInt] = None
    group: Optional[StrictInt] = None
    role: Optional[StrictInt] = Field(
        default=None, description='The global role will be applied to all product types and products.'
    )
    __properties: ClassVar[List[str]] = ['user', 'group', 'role']

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
        """Create an instance of GlobalRoleRequest from a JSON string"""
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
        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and 'user' in self.model_fields_set:
            _dict['user'] = None

        # set to None if group (nullable) is None
        # and model_fields_set contains the field
        if self.group is None and 'group' in self.model_fields_set:
            _dict['group'] = None

        # set to None if role (nullable) is None
        # and model_fields_set contains the field
        if self.role is None and 'role' in self.model_fields_set:
            _dict['role'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GlobalRoleRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({'user': obj.get('user'), 'group': obj.get('group'), 'role': obj.get('role')})
        return _obj
