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

from pydantic import BaseModel, ConfigDict
from typing_extensions import Self

from defectdojo_api_generated.models.user_stub import UserStub


class PaginatedProductTypeListPrefetch(BaseModel):
    """
    PaginatedProductTypeListPrefetch
    """  # noqa: E501

    authorization_groups: Optional[Dict[str, DojoGroup]] = None
    members: Optional[Dict[str, UserStub]] = None
    __properties: ClassVar[List[str]] = ['authorization_groups', 'members']

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
        """Create an instance of PaginatedProductTypeListPrefetch from a JSON string"""
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
                'authorization_groups',
                'members',
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each value in authorization_groups (dict)
        _field_dict = {}
        if self.authorization_groups:
            for _key_authorization_groups in self.authorization_groups:
                if self.authorization_groups[_key_authorization_groups]:
                    _field_dict[_key_authorization_groups] = self.authorization_groups[
                        _key_authorization_groups
                    ].to_dict()
            _dict['authorization_groups'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in members (dict)
        _field_dict = {}
        if self.members:
            for _key_members in self.members:
                if self.members[_key_members]:
                    _field_dict[_key_members] = self.members[_key_members].to_dict()
            _dict['members'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaginatedProductTypeListPrefetch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'authorization_groups': dict(
                    (_k, DojoGroup.from_dict(_v)) for _k, _v in obj['authorization_groups'].items()
                )
                if obj.get('authorization_groups') is not None
                else None,
                'members': dict((_k, UserStub.from_dict(_v)) for _k, _v in obj['members'].items())
                if obj.get('members') is not None
                else None,
            }
        )
        return _obj


from defectdojo_api_generated.models.dojo_group import DojoGroup

# TODO: Rewrite to not use raise_errors
PaginatedProductTypeListPrefetch.model_rebuild(raise_errors=False)
