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


class PatchedUserContactInfoRequest(BaseModel):
    """
    PatchedUserContactInfoRequest
    """  # noqa: E501

    title: Optional[Annotated[str, Field(strict=True, max_length=150)]] = None
    phone_number: Optional[Annotated[str, Field(strict=True, max_length=15)]] = Field(
        default=None, description="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    cell_number: Optional[Annotated[str, Field(strict=True, max_length=15)]] = Field(
        default=None, description="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    twitter_username: Optional[Annotated[str, Field(strict=True, max_length=150)]] = None
    github_username: Optional[Annotated[str, Field(strict=True, max_length=150)]] = None
    slack_username: Optional[Annotated[str, Field(strict=True, max_length=150)]] = Field(
        default=None, description='Email address associated with your slack account'
    )
    slack_user_id: Optional[Annotated[str, Field(strict=True, max_length=25)]] = None
    block_execution: Optional[StrictBool] = Field(
        default=None,
        description="Instead of async deduping a finding the findings will be deduped synchronously and will 'block' the user until completion.",
    )
    force_password_reset: Optional[StrictBool] = Field(
        default=None, description='Forces this user to reset their password on next login.'
    )
    user: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = [
        'title',
        'phone_number',
        'cell_number',
        'twitter_username',
        'github_username',
        'slack_username',
        'slack_user_id',
        'block_execution',
        'force_password_reset',
        'user',
    ]

    @field_validator('phone_number')
    def phone_number_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r'^\+?1?\d{9,15}$', value):
            raise ValueError(r'must validate the regular expression /^\+?1?\d{9,15}$/')
        return value

    @field_validator('cell_number')
    def cell_number_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r'^\+?1?\d{9,15}$', value):
            raise ValueError(r'must validate the regular expression /^\+?1?\d{9,15}$/')
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
        """Create an instance of PatchedUserContactInfoRequest from a JSON string"""
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
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and 'title' in self.model_fields_set:
            _dict['title'] = None

        # set to None if twitter_username (nullable) is None
        # and model_fields_set contains the field
        if self.twitter_username is None and 'twitter_username' in self.model_fields_set:
            _dict['twitter_username'] = None

        # set to None if github_username (nullable) is None
        # and model_fields_set contains the field
        if self.github_username is None and 'github_username' in self.model_fields_set:
            _dict['github_username'] = None

        # set to None if slack_username (nullable) is None
        # and model_fields_set contains the field
        if self.slack_username is None and 'slack_username' in self.model_fields_set:
            _dict['slack_username'] = None

        # set to None if slack_user_id (nullable) is None
        # and model_fields_set contains the field
        if self.slack_user_id is None and 'slack_user_id' in self.model_fields_set:
            _dict['slack_user_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedUserContactInfoRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'title': obj.get('title'),
                'phone_number': obj.get('phone_number'),
                'cell_number': obj.get('cell_number'),
                'twitter_username': obj.get('twitter_username'),
                'github_username': obj.get('github_username'),
                'slack_username': obj.get('slack_username'),
                'slack_user_id': obj.get('slack_user_id'),
                'block_execution': obj.get('block_execution'),
                'force_password_reset': obj.get('force_password_reset'),
                'user': obj.get('user'),
            }
        )
        return _obj
