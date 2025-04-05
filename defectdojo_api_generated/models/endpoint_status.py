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
from datetime import date, datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing_extensions import Self


class EndpointStatus(BaseModel):
    """
    EndpointStatus
    """  # noqa: E501

    id: StrictInt
    var_date: Optional[date] = Field(default=None, alias='date')
    last_modified: Optional[datetime]
    mitigated: Optional[StrictBool] = None
    mitigated_time: Optional[datetime]
    false_positive: Optional[StrictBool] = None
    out_of_scope: Optional[StrictBool] = None
    risk_accepted: Optional[StrictBool] = None
    mitigated_by: Optional[StrictInt] = None
    endpoint: StrictInt
    finding: StrictInt
    __properties: ClassVar[List[str]] = [
        'id',
        'date',
        'last_modified',
        'mitigated',
        'mitigated_time',
        'false_positive',
        'out_of_scope',
        'risk_accepted',
        'mitigated_by',
        'endpoint',
        'finding',
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
        """Create an instance of EndpointStatus from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                'id',
                'last_modified',
                'mitigated_time',
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if last_modified (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified is None and 'last_modified' in self.model_fields_set:
            _dict['last_modified'] = None

        # set to None if mitigated_time (nullable) is None
        # and model_fields_set contains the field
        if self.mitigated_time is None and 'mitigated_time' in self.model_fields_set:
            _dict['mitigated_time'] = None

        # set to None if mitigated_by (nullable) is None
        # and model_fields_set contains the field
        if self.mitigated_by is None and 'mitigated_by' in self.model_fields_set:
            _dict['mitigated_by'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EndpointStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'id': obj.get('id'),
                'date': obj.get('date'),
                'last_modified': obj.get('last_modified'),
                'mitigated': obj.get('mitigated'),
                'mitigated_time': obj.get('mitigated_time'),
                'false_positive': obj.get('false_positive'),
                'out_of_scope': obj.get('out_of_scope'),
                'risk_accepted': obj.get('risk_accepted'),
                'mitigated_by': obj.get('mitigated_by'),
                'endpoint': obj.get('endpoint'),
                'finding': obj.get('finding'),
            }
        )
        return _obj
