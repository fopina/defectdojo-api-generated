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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing_extensions import Annotated, Self

from defectdojo_api_generated.models.app_analysis_prefetch import AppAnalysisPrefetch


class AppAnalysis(BaseModel):
    """
    AppAnalysis
    """  # noqa: E501

    id: StrictInt
    tags: Optional[List[StrictStr]] = None
    name: Annotated[str, Field(strict=True, max_length=200)]
    confidence: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    version: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    icon: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    website: Optional[Annotated[str, Field(strict=True, max_length=400)]] = None
    website_found: Optional[Annotated[str, Field(strict=True, max_length=400)]] = None
    created: datetime
    product: StrictInt
    user: StrictInt
    prefetch: Optional[AppAnalysisPrefetch] = None
    __properties: ClassVar[List[str]] = [
        'id',
        'tags',
        'name',
        'confidence',
        'version',
        'icon',
        'website',
        'website_found',
        'created',
        'product',
        'user',
        'prefetch',
    ]

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
        """Create an instance of AppAnalysis from a JSON string"""
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
        # set to None if confidence (nullable) is None
        # and model_fields_set contains the field
        if self.confidence is None and 'confidence' in self.model_fields_set:
            _dict['confidence'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and 'version' in self.model_fields_set:
            _dict['version'] = None

        # set to None if icon (nullable) is None
        # and model_fields_set contains the field
        if self.icon is None and 'icon' in self.model_fields_set:
            _dict['icon'] = None

        # set to None if website (nullable) is None
        # and model_fields_set contains the field
        if self.website is None and 'website' in self.model_fields_set:
            _dict['website'] = None

        # set to None if website_found (nullable) is None
        # and model_fields_set contains the field
        if self.website_found is None and 'website_found' in self.model_fields_set:
            _dict['website_found'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppAnalysis from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'id': obj.get('id'),
                'tags': obj.get('tags'),
                'name': obj.get('name'),
                'confidence': obj.get('confidence'),
                'version': obj.get('version'),
                'icon': obj.get('icon'),
                'website': obj.get('website'),
                'website_found': obj.get('website_found'),
                'created': obj.get('created'),
                'product': obj.get('product'),
                'user': obj.get('user'),
                'prefetch': AppAnalysisPrefetch.from_dict(obj['prefetch']) if obj.get('prefetch') is not None else None,
            }
        )
        return _obj
