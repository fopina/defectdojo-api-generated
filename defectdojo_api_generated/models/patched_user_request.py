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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, field_validator
from typing_extensions import Annotated, Self


class PatchedUserRequest(BaseModel):
    """
    PatchedUserRequest
    """  # noqa: E501

    username: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=150)]] = Field(
        default=None, description='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
    )
    first_name: Optional[Annotated[str, Field(strict=True, max_length=150)]] = None
    last_name: Optional[Annotated[str, Field(strict=True, max_length=150)]] = None
    email: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    is_active: Optional[StrictBool] = Field(
        default=None,
        description='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
    )
    is_superuser: Optional[StrictBool] = Field(
        default=None, description='Designates that this user has all permissions without explicitly assigning them.'
    )
    password: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    configuration_permissions: Optional[List[Optional[StrictInt]]] = None
    __properties: ClassVar[List[str]] = [
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'is_superuser',
        'password',
        'configuration_permissions',
    ]

    @field_validator('username')
    def username_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r'^[\w.@+-]+$', value):
            raise ValueError(r'must validate the regular expression /^[\w.@+-]+$/')
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
        """Create an instance of PatchedUserRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedUserRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'username': obj.get('username'),
                'first_name': obj.get('first_name'),
                'last_name': obj.get('last_name'),
                'email': obj.get('email'),
                'is_active': obj.get('is_active'),
                'is_superuser': obj.get('is_superuser'),
                'password': obj.get('password'),
                'configuration_permissions': obj.get('configuration_permissions'),
            }
        )
        return _obj
