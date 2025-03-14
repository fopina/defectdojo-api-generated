# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

The version of the OpenAPI document: 2.44.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing_extensions import Annotated, Self


class RiskAcceptance(BaseModel):
    """
    RiskAcceptance
    """  # noqa: E501

    id: StrictInt
    recommendation: StrictStr
    decision: StrictStr
    path: StrictStr
    name: Annotated[str, Field(strict=True, max_length=300)] = Field(
        description='Descriptive name which in the future may also be used to group risk acceptances together across engagements and products'
    )
    recommendation_details: Optional[StrictStr] = Field(
        default=None, description='Explanation of security recommendation'
    )
    decision_details: Optional[StrictStr] = Field(
        default=None,
        description='If a compensating control exists to mitigate the finding or reduce risk, then list the compensating control(s).',
    )
    accepted_by: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(
        default=None, description='The person that accepts the risk, can be outside of DefectDojo.'
    )
    expiration_date: Optional[datetime] = Field(
        default=None,
        description='When the risk acceptance expires, the findings will be reactivated (unless disabled below).',
    )
    expiration_date_warned: Optional[datetime] = Field(
        default=None, description='(readonly) Date at which notice about the risk acceptance expiration was sent.'
    )
    expiration_date_handled: Optional[datetime] = Field(
        default=None,
        description='(readonly) When the risk acceptance expiration was handled (manually or by the daily job).',
    )
    reactivate_expired: Optional[StrictBool] = Field(
        default=None, description='Reactivate findings when risk acceptance expires?'
    )
    restart_sla_expired: Optional[StrictBool] = Field(
        default=None, description='When enabled, the SLA for findings is restarted when the risk acceptance expires.'
    )
    created: datetime
    updated: datetime
    owner: StrictInt = Field(
        description='User in DefectDojo owning this acceptance. Only the owner and staff users can edit the risk acceptance.'
    )
    accepted_findings: List[StrictInt]
    notes: List[StrictInt]
    __properties: ClassVar[List[str]] = [
        'id',
        'recommendation',
        'decision',
        'path',
        'name',
        'recommendation_details',
        'decision_details',
        'accepted_by',
        'expiration_date',
        'expiration_date_warned',
        'expiration_date_handled',
        'reactivate_expired',
        'restart_sla_expired',
        'created',
        'updated',
        'owner',
        'accepted_findings',
        'notes',
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
        """Create an instance of RiskAcceptance from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                'id',
                'recommendation',
                'decision',
                'path',
                'created',
                'updated',
                'notes',
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if recommendation_details (nullable) is None
        # and model_fields_set contains the field
        if self.recommendation_details is None and 'recommendation_details' in self.model_fields_set:
            _dict['recommendation_details'] = None

        # set to None if decision_details (nullable) is None
        # and model_fields_set contains the field
        if self.decision_details is None and 'decision_details' in self.model_fields_set:
            _dict['decision_details'] = None

        # set to None if accepted_by (nullable) is None
        # and model_fields_set contains the field
        if self.accepted_by is None and 'accepted_by' in self.model_fields_set:
            _dict['accepted_by'] = None

        # set to None if expiration_date (nullable) is None
        # and model_fields_set contains the field
        if self.expiration_date is None and 'expiration_date' in self.model_fields_set:
            _dict['expiration_date'] = None

        # set to None if expiration_date_warned (nullable) is None
        # and model_fields_set contains the field
        if self.expiration_date_warned is None and 'expiration_date_warned' in self.model_fields_set:
            _dict['expiration_date_warned'] = None

        # set to None if expiration_date_handled (nullable) is None
        # and model_fields_set contains the field
        if self.expiration_date_handled is None and 'expiration_date_handled' in self.model_fields_set:
            _dict['expiration_date_handled'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RiskAcceptance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'id': obj.get('id'),
                'recommendation': obj.get('recommendation'),
                'decision': obj.get('decision'),
                'path': obj.get('path'),
                'name': obj.get('name'),
                'recommendation_details': obj.get('recommendation_details'),
                'decision_details': obj.get('decision_details'),
                'accepted_by': obj.get('accepted_by'),
                'expiration_date': obj.get('expiration_date'),
                'expiration_date_warned': obj.get('expiration_date_warned'),
                'expiration_date_handled': obj.get('expiration_date_handled'),
                'reactivate_expired': obj.get('reactivate_expired'),
                'restart_sla_expired': obj.get('restart_sla_expired'),
                'created': obj.get('created'),
                'updated': obj.get('updated'),
                'owner': obj.get('owner'),
                'accepted_findings': obj.get('accepted_findings'),
                'notes': obj.get('notes'),
            }
        )
        return _obj
