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
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing_extensions import Annotated, Self

from defectdojo_api_generated.models.engagement_presets_prefetch import EngagementPresetsPrefetch


class EngagementPresets(BaseModel):
    """
    EngagementPresets
    """  # noqa: E501

    id: StrictInt
    title: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(
        default=None, description='Brief description of preset.'
    )
    notes: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = Field(
        default=None, description='Description of what needs to be tested or setting up environment for testing'
    )
    scope: Optional[Annotated[str, Field(strict=True, max_length=800)]] = Field(
        default=None, description="Scope of Engagement testing, IP's/Resources/URL's)"
    )
    created: datetime
    product: StrictInt
    test_type: Optional[List[StrictInt]] = None
    network_locations: Optional[List[StrictInt]] = None
    prefetch: Optional[EngagementPresetsPrefetch] = None
    __properties: ClassVar[List[str]] = [
        'id',
        'title',
        'notes',
        'scope',
        'created',
        'product',
        'test_type',
        'network_locations',
        'prefetch',
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
        """Create an instance of EngagementPresets from a JSON string"""
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
                'created',
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
        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and 'notes' in self.model_fields_set:
            _dict['notes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EngagementPresets from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'id': obj.get('id'),
                'title': obj.get('title'),
                'notes': obj.get('notes'),
                'scope': obj.get('scope'),
                'created': obj.get('created'),
                'product': obj.get('product'),
                'test_type': obj.get('test_type'),
                'network_locations': obj.get('network_locations'),
                'prefetch': EngagementPresetsPrefetch.from_dict(obj['prefetch'])
                if obj.get('prefetch') is not None
                else None,
            }
        )
        return _obj
