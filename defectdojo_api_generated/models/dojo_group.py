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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing_extensions import Annotated, Self


class DojoGroup(BaseModel):
    """
    DojoGroup
    """  # noqa: E501

    id: StrictInt
    configuration_permissions: Optional[List[Optional[StrictInt]]] = None
    name: Annotated[str, Field(strict=True, max_length=255)]
    description: Optional[Annotated[str, Field(strict=True, max_length=4000)]] = None
    social_provider: Optional[StrictStr] = Field(
        default=None, description='Group imported from a social provider.  * `AzureAD` - AzureAD * `Remote` - Remote'
    )
    users: List[StrictInt]
    prefetch: Optional[DojoGroupPrefetch] = None
    __properties: ClassVar[List[str]] = [
        'id',
        'configuration_permissions',
        'name',
        'description',
        'social_provider',
        'users',
        'prefetch',
    ]

    @field_validator('social_provider')
    def social_provider_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AzureAD', 'Remote', '']):
            raise ValueError("must be one of enum values ('AzureAD', 'Remote', '')")
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
        """Create an instance of DojoGroup from a JSON string"""
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
                'id',
                'users',
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of prefetch
        if self.prefetch:
            _dict['prefetch'] = self.prefetch.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and 'description' in self.model_fields_set:
            _dict['description'] = None

        # set to None if social_provider (nullable) is None
        # and model_fields_set contains the field
        if self.social_provider is None and 'social_provider' in self.model_fields_set:
            _dict['social_provider'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DojoGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'id': obj.get('id'),
                'configuration_permissions': obj.get('configuration_permissions'),
                'name': obj.get('name'),
                'description': obj.get('description'),
                'social_provider': obj.get('social_provider'),
                'users': obj.get('users'),
                'prefetch': DojoGroupPrefetch.from_dict(obj['prefetch']) if obj.get('prefetch') is not None else None,
            }
        )
        return _obj


from defectdojo_api_generated.models.dojo_group_prefetch import DojoGroupPrefetch

# TODO: Rewrite to not use raise_errors
DojoGroup.model_rebuild(raise_errors=False)
