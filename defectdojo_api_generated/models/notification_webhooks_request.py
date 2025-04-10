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


class NotificationWebhooksRequest(BaseModel):
    """
    NotificationWebhooksRequest
    """  # noqa: E501

    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = Field(
        default=None, description='Name of the incoming webhook'
    )
    url: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=200)]] = Field(
        default=None, description='The full URL of the incoming webhook'
    )
    header_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(
        default=None, description='Name of the header required for interacting with Webhook endpoint'
    )
    header_value: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(
        default=None, description='Content of the header required for interacting with Webhook endpoint'
    )
    owner: Optional[StrictInt] = Field(
        default=None, description='Owner/receiver of notification, if empty processed as system notification'
    )
    __properties: ClassVar[List[str]] = ['name', 'url', 'header_name', 'header_value', 'owner']

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
        """Create an instance of NotificationWebhooksRequest from a JSON string"""
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
        # set to None if header_name (nullable) is None
        # and model_fields_set contains the field
        if self.header_name is None and 'header_name' in self.model_fields_set:
            _dict['header_name'] = None

        # set to None if header_value (nullable) is None
        # and model_fields_set contains the field
        if self.header_value is None and 'header_value' in self.model_fields_set:
            _dict['header_value'] = None

        # set to None if owner (nullable) is None
        # and model_fields_set contains the field
        if self.owner is None and 'owner' in self.model_fields_set:
            _dict['owner'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationWebhooksRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'name': obj.get('name'),
                'url': obj.get('url'),
                'header_name': obj.get('header_name'),
                'header_value': obj.get('header_value'),
                'owner': obj.get('owner'),
            }
        )
        return _obj
