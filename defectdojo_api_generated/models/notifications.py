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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing_extensions import Self

from defectdojo_api_generated.models.app_analysis_prefetch import AppAnalysisPrefetch


class Notifications(BaseModel):
    """
    Notifications
    """  # noqa: E501

    id: StrictInt
    product: Optional[StrictInt] = None
    user: Optional[StrictInt] = None
    product_type_added: Optional[List[StrictStr]] = None
    product_added: Optional[List[StrictStr]] = None
    engagement_added: Optional[List[StrictStr]] = None
    test_added: Optional[List[StrictStr]] = None
    scan_added: Optional[List[StrictStr]] = None
    jira_update: Optional[List[StrictStr]] = None
    upcoming_engagement: Optional[List[StrictStr]] = None
    stale_engagement: Optional[List[StrictStr]] = None
    auto_close_engagement: Optional[List[StrictStr]] = None
    close_engagement: Optional[List[StrictStr]] = None
    user_mentioned: Optional[List[StrictStr]] = None
    code_review: Optional[List[StrictStr]] = None
    review_requested: Optional[List[StrictStr]] = None
    other: Optional[List[StrictStr]] = None
    sla_breach: Optional[List[StrictStr]] = None
    sla_breach_combined: Optional[List[StrictStr]] = None
    risk_acceptance_expiration: Optional[List[StrictStr]] = None
    template: Optional[StrictBool] = False
    scan_added_empty: Optional[StrictStr] = Field(
        default=None,
        description='Triggered whenever an (re-)import has been done (even if that created/updated/closed no findings).  * `slack` - slack * `msteams` - msteams * `mail` - mail * `webhooks` - webhooks * `alert` - alert',
    )
    prefetch: Optional[AppAnalysisPrefetch] = None
    __properties: ClassVar[List[str]] = [
        'id',
        'product',
        'user',
        'product_type_added',
        'product_added',
        'engagement_added',
        'test_added',
        'scan_added',
        'jira_update',
        'upcoming_engagement',
        'stale_engagement',
        'auto_close_engagement',
        'close_engagement',
        'user_mentioned',
        'code_review',
        'review_requested',
        'other',
        'sla_breach',
        'sla_breach_combined',
        'risk_acceptance_expiration',
        'template',
        'scan_added_empty',
        'prefetch',
    ]

    @field_validator('product_type_added')
    def product_type_added_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('product_added')
    def product_added_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('engagement_added')
    def engagement_added_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('test_added')
    def test_added_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('scan_added')
    def scan_added_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('jira_update')
    def jira_update_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('upcoming_engagement')
    def upcoming_engagement_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('stale_engagement')
    def stale_engagement_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('auto_close_engagement')
    def auto_close_engagement_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('close_engagement')
    def close_engagement_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('user_mentioned')
    def user_mentioned_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('code_review')
    def code_review_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('review_requested')
    def review_requested_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('other')
    def other_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('sla_breach')
    def sla_breach_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('sla_breach_combined')
    def sla_breach_combined_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('risk_acceptance_expiration')
    def risk_acceptance_expiration_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert']):
                raise ValueError("each list item must be one of ('slack', 'msteams', 'mail', 'webhooks', 'alert')")
        return value

    @field_validator('scan_added_empty')
    def scan_added_empty_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['slack', 'msteams', 'mail', 'webhooks', 'alert', '']):
            raise ValueError("must be one of enum values ('slack', 'msteams', 'mail', 'webhooks', 'alert', '')")
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
        """Create an instance of Notifications from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                'id',
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
        # set to None if product (nullable) is None
        # and model_fields_set contains the field
        if self.product is None and 'product' in self.model_fields_set:
            _dict['product'] = None

        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and 'user' in self.model_fields_set:
            _dict['user'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Notifications from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'id': obj.get('id'),
                'product': obj.get('product'),
                'user': obj.get('user'),
                'product_type_added': obj.get('product_type_added'),
                'product_added': obj.get('product_added'),
                'engagement_added': obj.get('engagement_added'),
                'test_added': obj.get('test_added'),
                'scan_added': obj.get('scan_added'),
                'jira_update': obj.get('jira_update'),
                'upcoming_engagement': obj.get('upcoming_engagement'),
                'stale_engagement': obj.get('stale_engagement'),
                'auto_close_engagement': obj.get('auto_close_engagement'),
                'close_engagement': obj.get('close_engagement'),
                'user_mentioned': obj.get('user_mentioned'),
                'code_review': obj.get('code_review'),
                'review_requested': obj.get('review_requested'),
                'other': obj.get('other'),
                'sla_breach': obj.get('sla_breach'),
                'sla_breach_combined': obj.get('sla_breach_combined'),
                'risk_acceptance_expiration': obj.get('risk_acceptance_expiration'),
                'template': obj.get('template') if obj.get('template') is not None else False,
                'scan_added_empty': obj.get('scan_added_empty'),
                'prefetch': AppAnalysisPrefetch.from_dict(obj['prefetch']) if obj.get('prefetch') is not None else None,
            }
        )
        return _obj
