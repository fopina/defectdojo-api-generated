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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing_extensions import Annotated, Self


class PatchedAnnouncementRequest(BaseModel):
    """
    PatchedAnnouncementRequest
    """  # noqa: E501

    message: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=500)]] = Field(
        default=None,
        description="This dismissable message will be displayed on all pages for authenticated users. It can contain basic html tags, for example <a href='https://www.fred.com' style='color: #337ab7;' target='_blank'>https://example.com</a>",
    )
    style: Optional[StrictStr] = Field(
        default=None,
        description='The style of banner to display. (info, success, warning, danger)  * `info` - Info * `success` - Success * `warning` - Warning * `danger` - Danger',
    )
    dismissable: Optional[StrictBool] = Field(
        default=None, description='Ticking this box allows users to dismiss the current announcement'
    )
    __properties: ClassVar[List[str]] = ['message', 'style', 'dismissable']

    @field_validator('style')
    def style_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['info', 'success', 'warning', 'danger']):
            raise ValueError("must be one of enum values ('info', 'success', 'warning', 'danger')")
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
        """Create an instance of PatchedAnnouncementRequest from a JSON string"""
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
        """Create an instance of PatchedAnnouncementRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {'message': obj.get('message'), 'style': obj.get('style'), 'dismissable': obj.get('dismissable')}
        )
        return _obj
