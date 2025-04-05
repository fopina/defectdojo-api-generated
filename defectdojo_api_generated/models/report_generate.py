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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing_extensions import Annotated, Self

from defectdojo_api_generated.models.endpoint import Endpoint
from defectdojo_api_generated.models.engagement import Engagement
from defectdojo_api_generated.models.executive_summary import ExecutiveSummary
from defectdojo_api_generated.models.finding import Finding
from defectdojo_api_generated.models.finding_to_notes import FindingToNotes
from defectdojo_api_generated.models.product import Product
from defectdojo_api_generated.models.product_type import ProductType
from defectdojo_api_generated.models.test import Test
from defectdojo_api_generated.models.user_stub import UserStub


class ReportGenerate(BaseModel):
    """
    ReportGenerate
    """  # noqa: E501

    executive_summary: Optional[ExecutiveSummary]
    product_type: ProductType
    product: Product
    engagement: Engagement
    report_name: Annotated[str, Field(strict=True, max_length=200)]
    report_info: Annotated[str, Field(strict=True, max_length=200)]
    test: Test
    endpoint: Endpoint
    endpoints: List[Endpoint]
    findings: List[Finding]
    user: UserStub
    team_name: Annotated[str, Field(strict=True, max_length=200)]
    title: Annotated[str, Field(strict=True, max_length=200)]
    user_id: StrictInt
    host: Annotated[str, Field(strict=True, max_length=200)]
    finding_notes: Optional[List[FindingToNotes]] = None
    __properties: ClassVar[List[str]] = [
        'executive_summary',
        'product_type',
        'product',
        'engagement',
        'report_name',
        'report_info',
        'test',
        'endpoint',
        'endpoints',
        'findings',
        'user',
        'team_name',
        'title',
        'user_id',
        'host',
        'finding_notes',
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
        """Create an instance of ReportGenerate from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                'product_type',
                'product',
                'engagement',
                'test',
                'endpoint',
                'endpoints',
                'findings',
                'user',
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of executive_summary
        if self.executive_summary:
            _dict['executive_summary'] = self.executive_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product_type
        if self.product_type:
            _dict['product_type'] = self.product_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product
        if self.product:
            _dict['product'] = self.product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of engagement
        if self.engagement:
            _dict['engagement'] = self.engagement.to_dict()
        # override the default output from pydantic by calling `to_dict()` of test
        if self.test:
            _dict['test'] = self.test.to_dict()
        # override the default output from pydantic by calling `to_dict()` of endpoint
        if self.endpoint:
            _dict['endpoint'] = self.endpoint.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in endpoints (list)
        _items = []
        if self.endpoints:
            for _item_endpoints in self.endpoints:
                if _item_endpoints:
                    _items.append(_item_endpoints.to_dict())
            _dict['endpoints'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in findings (list)
        _items = []
        if self.findings:
            for _item_findings in self.findings:
                if _item_findings:
                    _items.append(_item_findings.to_dict())
            _dict['findings'] = _items
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in finding_notes (list)
        _items = []
        if self.finding_notes:
            for _item_finding_notes in self.finding_notes:
                if _item_finding_notes:
                    _items.append(_item_finding_notes.to_dict())
            _dict['finding_notes'] = _items
        # set to None if executive_summary (nullable) is None
        # and model_fields_set contains the field
        if self.executive_summary is None and 'executive_summary' in self.model_fields_set:
            _dict['executive_summary'] = None

        # set to None if finding_notes (nullable) is None
        # and model_fields_set contains the field
        if self.finding_notes is None and 'finding_notes' in self.model_fields_set:
            _dict['finding_notes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReportGenerate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'executive_summary': ExecutiveSummary.from_dict(obj['executive_summary'])
                if obj.get('executive_summary') is not None
                else None,
                'product_type': ProductType.from_dict(obj['product_type'])
                if obj.get('product_type') is not None
                else None,
                'product': Product.from_dict(obj['product']) if obj.get('product') is not None else None,
                'engagement': Engagement.from_dict(obj['engagement']) if obj.get('engagement') is not None else None,
                'report_name': obj.get('report_name'),
                'report_info': obj.get('report_info'),
                'test': Test.from_dict(obj['test']) if obj.get('test') is not None else None,
                'endpoint': Endpoint.from_dict(obj['endpoint']) if obj.get('endpoint') is not None else None,
                'endpoints': [Endpoint.from_dict(_item) for _item in obj['endpoints']]
                if obj.get('endpoints') is not None
                else None,
                'findings': [Finding.from_dict(_item) for _item in obj['findings']]
                if obj.get('findings') is not None
                else None,
                'user': UserStub.from_dict(obj['user']) if obj.get('user') is not None else None,
                'team_name': obj.get('team_name'),
                'title': obj.get('title'),
                'user_id': obj.get('user_id'),
                'host': obj.get('host'),
                'finding_notes': [FindingToNotes.from_dict(_item) for _item in obj['finding_notes']]
                if obj.get('finding_notes') is not None
                else None,
            }
        )
        return _obj
