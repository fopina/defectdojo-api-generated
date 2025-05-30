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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing_extensions import Annotated, Self


class CredentialRequest(BaseModel):
    """
    CredentialRequest
    """  # noqa: E501

    name: Annotated[str, Field(min_length=1, strict=True, max_length=200)]
    username: Annotated[str, Field(min_length=1, strict=True, max_length=200)]
    role: Annotated[str, Field(min_length=1, strict=True, max_length=200)]
    authentication: Optional[StrictStr] = Field(
        default=None, description='* `Form` - Form Authentication * `SSO` - SSO Redirect'
    )
    http_authentication: Optional[StrictStr] = Field(default=None, description='* `Basic` - Basic * `NTLM` - NTLM')
    description: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = None
    url: Annotated[str, Field(min_length=1, strict=True, max_length=2000)]
    login_regex: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    logout_regex: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    is_valid: Optional[StrictBool] = None
    environment: StrictInt
    __properties: ClassVar[List[str]] = [
        'name',
        'username',
        'role',
        'authentication',
        'http_authentication',
        'description',
        'url',
        'login_regex',
        'logout_regex',
        'is_valid',
        'environment',
    ]

    @field_validator('authentication')
    def authentication_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Form', 'SSO']):
            raise ValueError("must be one of enum values ('Form', 'SSO')")
        return value

    @field_validator('http_authentication')
    def http_authentication_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Basic', 'NTLM', '']):
            raise ValueError("must be one of enum values ('Basic', 'NTLM', '')")
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
        """Create an instance of CredentialRequest from a JSON string"""
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
        # set to None if http_authentication (nullable) is None
        # and model_fields_set contains the field
        if self.http_authentication is None and 'http_authentication' in self.model_fields_set:
            _dict['http_authentication'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and 'description' in self.model_fields_set:
            _dict['description'] = None

        # set to None if login_regex (nullable) is None
        # and model_fields_set contains the field
        if self.login_regex is None and 'login_regex' in self.model_fields_set:
            _dict['login_regex'] = None

        # set to None if logout_regex (nullable) is None
        # and model_fields_set contains the field
        if self.logout_regex is None and 'logout_regex' in self.model_fields_set:
            _dict['logout_regex'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CredentialRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'name': obj.get('name'),
                'username': obj.get('username'),
                'role': obj.get('role'),
                'authentication': obj.get('authentication'),
                'http_authentication': obj.get('http_authentication'),
                'description': obj.get('description'),
                'url': obj.get('url'),
                'login_regex': obj.get('login_regex'),
                'logout_regex': obj.get('logout_regex'),
                'is_valid': obj.get('is_valid'),
                'environment': obj.get('environment'),
            }
        )
        return _obj
