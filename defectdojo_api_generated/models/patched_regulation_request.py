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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Annotated, Self


class PatchedRegulationRequest(BaseModel):
    """
    PatchedRegulationRequest
    """  # noqa: E501

    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=128)]] = Field(
        default=None, description='The name of the regulation.'
    )
    acronym: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=20)]] = Field(
        default=None, description='A shortened representation of the name.'
    )
    category: Optional[StrictStr] = Field(
        default=None,
        description='The subject of the regulation.  * `privacy` - Privacy * `finance` - Finance * `education` - Education * `medical` - Medical * `corporate` - Corporate * `security` - Security * `government` - Government * `other` - Other',
    )
    jurisdiction: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=64)]] = Field(
        default=None, description='The territory over which the regulation applies.'
    )
    description: Optional[StrictStr] = Field(default=None, description="Information about the regulation's purpose.")
    reference: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(
        default=None, description='An external URL for more information.'
    )
    __properties: ClassVar[List[str]] = ['name', 'acronym', 'category', 'jurisdiction', 'description', 'reference']

    @field_validator('category')
    def category_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(
            ['privacy', 'finance', 'education', 'medical', 'corporate', 'security', 'government', 'other']
        ):
            raise ValueError(
                "must be one of enum values ('privacy', 'finance', 'education', 'medical', 'corporate', 'security', 'government', 'other')"
            )
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
        """Create an instance of PatchedRegulationRequest from a JSON string"""
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
        """Create an instance of PatchedRegulationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'name': obj.get('name'),
                'acronym': obj.get('acronym'),
                'category': obj.get('category'),
                'jurisdiction': obj.get('jurisdiction'),
                'description': obj.get('description'),
                'reference': obj.get('reference'),
            }
        )
        return _obj
