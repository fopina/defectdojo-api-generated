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
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing_extensions import Annotated, Self


class PatchedMetaRequest(BaseModel):
    """
    PatchedMetaRequest
    """  # noqa: E501

    product: Optional[StrictInt] = None
    endpoint: Optional[StrictInt] = None
    finding: Optional[StrictInt] = None
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=120)]] = None
    value: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=300)]] = None
    __properties: ClassVar[List[str]] = ['product', 'endpoint', 'finding', 'name', 'value']

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
        """Create an instance of PatchedMetaRequest from a JSON string"""
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
        # set to None if product (nullable) is None
        # and model_fields_set contains the field
        if self.product is None and 'product' in self.model_fields_set:
            _dict['product'] = None

        # set to None if endpoint (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint is None and 'endpoint' in self.model_fields_set:
            _dict['endpoint'] = None

        # set to None if finding (nullable) is None
        # and model_fields_set contains the field
        if self.finding is None and 'finding' in self.model_fields_set:
            _dict['finding'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedMetaRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'product': obj.get('product'),
                'endpoint': obj.get('endpoint'),
                'finding': obj.get('finding'),
                'name': obj.get('name'),
                'value': obj.get('value'),
            }
        )
        return _obj
