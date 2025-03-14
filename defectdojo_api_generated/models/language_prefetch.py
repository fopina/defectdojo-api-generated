# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from defectdojo_api_generated.models.language_type import LanguageType
from defectdojo_api_generated.models.product import Product
from defectdojo_api_generated.models.user_stub import UserStub
from typing import Optional, Set
from typing_extensions import Self

class LanguagePrefetch(BaseModel):
    """
    LanguagePrefetch
    """ # noqa: E501
    language: Optional[Dict[str, LanguageType]] = None
    product: Optional[Dict[str, Product]] = None
    user: Optional[Dict[str, UserStub]] = None
    __properties: ClassVar[List[str]] = ["language", "product", "user"]

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
        """Create an instance of LanguagePrefetch from a JSON string"""
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
        excluded_fields: Set[str] = set([
            "language",
            "product",
            "user",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each value in language (dict)
        _field_dict = {}
        if self.language:
            for _key_language in self.language:
                if self.language[_key_language]:
                    _field_dict[_key_language] = self.language[_key_language].to_dict()
            _dict['language'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in product (dict)
        _field_dict = {}
        if self.product:
            for _key_product in self.product:
                if self.product[_key_product]:
                    _field_dict[_key_product] = self.product[_key_product].to_dict()
            _dict['product'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in user (dict)
        _field_dict = {}
        if self.user:
            for _key_user in self.user:
                if self.user[_key_user]:
                    _field_dict[_key_user] = self.user[_key_user].to_dict()
            _dict['user'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LanguagePrefetch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "language": dict(
                (_k, LanguageType.from_dict(_v))
                for _k, _v in obj["language"].items()
            )
            if obj.get("language") is not None
            else None,
            "product": dict(
                (_k, Product.from_dict(_v))
                for _k, _v in obj["product"].items()
            )
            if obj.get("product") is not None
            else None,
            "user": dict(
                (_k, UserStub.from_dict(_v))
                for _k, _v in obj["user"].items()
            )
            if obj.get("user") is not None
            else None
        })
        return _obj


