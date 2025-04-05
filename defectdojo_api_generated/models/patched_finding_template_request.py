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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing_extensions import Annotated, Self

from defectdojo_api_generated.models.vulnerability_id_template_request import VulnerabilityIdTemplateRequest


class PatchedFindingTemplateRequest(BaseModel):
    """
    PatchedFindingTemplateRequest
    """  # noqa: E501

    tags: Optional[List[Annotated[str, Field(min_length=1, strict=True)]]] = None
    vulnerability_ids: Optional[List[VulnerabilityIdTemplateRequest]] = None
    title: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1000)]] = None
    cwe: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    cvssv3: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=117)]] = None
    severity: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    description: Optional[StrictStr] = None
    mitigation: Optional[StrictStr] = None
    impact: Optional[StrictStr] = None
    references: Optional[StrictStr] = None
    template_match: Optional[StrictBool] = Field(
        default=None,
        description='Enables this template for matching remediation advice. Match will be applied to all active, verified findings by CWE.',
    )
    template_match_title: Optional[StrictBool] = Field(
        default=None, description='Matches by title text (contains search) and CWE.'
    )
    __properties: ClassVar[List[str]] = [
        'tags',
        'vulnerability_ids',
        'title',
        'cwe',
        'cvssv3',
        'severity',
        'description',
        'mitigation',
        'impact',
        'references',
        'template_match',
        'template_match_title',
    ]

    @field_validator('cvssv3')
    def cvssv3_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r'^AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]', value):
            raise ValueError(
                r'must validate the regular expression /^AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]/'
            )
        return value

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
        """Create an instance of PatchedFindingTemplateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in vulnerability_ids (list)
        _items = []
        if self.vulnerability_ids:
            for _item_vulnerability_ids in self.vulnerability_ids:
                if _item_vulnerability_ids:
                    _items.append(_item_vulnerability_ids.to_dict())
            _dict['vulnerability_ids'] = _items
        # set to None if cwe (nullable) is None
        # and model_fields_set contains the field
        if self.cwe is None and 'cwe' in self.model_fields_set:
            _dict['cwe'] = None

        # set to None if cvssv3 (nullable) is None
        # and model_fields_set contains the field
        if self.cvssv3 is None and 'cvssv3' in self.model_fields_set:
            _dict['cvssv3'] = None

        # set to None if severity (nullable) is None
        # and model_fields_set contains the field
        if self.severity is None and 'severity' in self.model_fields_set:
            _dict['severity'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and 'description' in self.model_fields_set:
            _dict['description'] = None

        # set to None if mitigation (nullable) is None
        # and model_fields_set contains the field
        if self.mitigation is None and 'mitigation' in self.model_fields_set:
            _dict['mitigation'] = None

        # set to None if impact (nullable) is None
        # and model_fields_set contains the field
        if self.impact is None and 'impact' in self.model_fields_set:
            _dict['impact'] = None

        # set to None if references (nullable) is None
        # and model_fields_set contains the field
        if self.references is None and 'references' in self.model_fields_set:
            _dict['references'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedFindingTemplateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'tags': obj.get('tags'),
                'vulnerability_ids': [
                    VulnerabilityIdTemplateRequest.from_dict(_item) for _item in obj['vulnerability_ids']
                ]
                if obj.get('vulnerability_ids') is not None
                else None,
                'title': obj.get('title'),
                'cwe': obj.get('cwe'),
                'cvssv3': obj.get('cvssv3'),
                'severity': obj.get('severity'),
                'description': obj.get('description'),
                'mitigation': obj.get('mitigation'),
                'impact': obj.get('impact'),
                'references': obj.get('references'),
                'template_match': obj.get('template_match'),
                'template_match_title': obj.get('template_match_title'),
            }
        )
        return _obj
