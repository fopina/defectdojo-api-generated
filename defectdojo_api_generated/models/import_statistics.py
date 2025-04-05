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

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Self

from defectdojo_api_generated.models.delta_statistics import DeltaStatistics
from defectdojo_api_generated.models.severity_status_statistics import SeverityStatusStatistics


class ImportStatistics(BaseModel):
    """
    ImportStatistics
    """  # noqa: E501

    before: Optional[SeverityStatusStatistics] = Field(
        default=None, description='Finding statistics as stored in Defect Dojo before the import'
    )
    delta: Optional[DeltaStatistics] = Field(
        default=None,
        description='Finding statistics of modifications made by the reimport. Only available when TRACK_IMPORT_HISTORY has not been disabled.',
    )
    after: SeverityStatusStatistics = Field(description='Finding statistics as stored in Defect Dojo after the import')
    __properties: ClassVar[List[str]] = ['before', 'delta', 'after']

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
        """Create an instance of ImportStatistics from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of before
        if self.before:
            _dict['before'] = self.before.to_dict()
        # override the default output from pydantic by calling `to_dict()` of delta
        if self.delta:
            _dict['delta'] = self.delta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of after
        if self.after:
            _dict['after'] = self.after.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ImportStatistics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'before': SeverityStatusStatistics.from_dict(obj['before']) if obj.get('before') is not None else None,
                'delta': DeltaStatistics.from_dict(obj['delta']) if obj.get('delta') is not None else None,
                'after': SeverityStatusStatistics.from_dict(obj['after']) if obj.get('after') is not None else None,
            }
        )
        return _obj
