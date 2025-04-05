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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing_extensions import Annotated, Self


class PatchedSLAConfigurationRequest(BaseModel):
    """
    PatchedSLAConfigurationRequest
    """  # noqa: E501

    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=128)]] = Field(
        default=None, description='A unique name for the set of SLAs.'
    )
    description: Optional[Annotated[str, Field(strict=True, max_length=512)]] = None
    critical: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(
        default=None, description='The number of days to remediate a critical finding.'
    )
    enforce_critical: Optional[StrictBool] = Field(
        default=None,
        description='When enabled, critical findings will be assigned an SLA expiration date based on the critical finding SLA days within this SLA configuration.',
    )
    high: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(
        default=None, description='The number of days to remediate a high finding.'
    )
    enforce_high: Optional[StrictBool] = Field(
        default=None,
        description='When enabled, high findings will be assigned an SLA expiration date based on the high finding SLA days within this SLA configuration.',
    )
    medium: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(
        default=None, description='The number of days to remediate a medium finding.'
    )
    enforce_medium: Optional[StrictBool] = Field(
        default=None,
        description='When enabled, medium findings will be assigned an SLA expiration date based on the medium finding SLA days within this SLA configuration.',
    )
    low: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(
        default=None, description='The number of days to remediate a low finding.'
    )
    enforce_low: Optional[StrictBool] = Field(
        default=None,
        description='When enabled, low findings will be assigned an SLA expiration date based on the low finding SLA days within this SLA configuration.',
    )
    __properties: ClassVar[List[str]] = [
        'name',
        'description',
        'critical',
        'enforce_critical',
        'high',
        'enforce_high',
        'medium',
        'enforce_medium',
        'low',
        'enforce_low',
    ]

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
        """Create an instance of PatchedSLAConfigurationRequest from a JSON string"""
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
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and 'description' in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedSLAConfigurationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'name': obj.get('name'),
                'description': obj.get('description'),
                'critical': obj.get('critical'),
                'enforce_critical': obj.get('enforce_critical'),
                'high': obj.get('high'),
                'enforce_high': obj.get('enforce_high'),
                'medium': obj.get('medium'),
                'enforce_medium': obj.get('enforce_medium'),
                'low': obj.get('low'),
                'enforce_low': obj.get('enforce_low'),
            }
        )
        return _obj
