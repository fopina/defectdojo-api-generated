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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class EngagementCheckList(BaseModel):
    """
    EngagementCheckList
    """ # noqa: E501
    id: StrictInt
    session_management: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    encryption_crypto: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    configuration_management: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    authentication: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    authorization_and_access_control: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    data_input_sanitization_validation: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    sensitive_data: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    other: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    engagement: StrictInt
    session_issues: Optional[List[StrictInt]] = None
    crypto_issues: Optional[List[StrictInt]] = None
    config_issues: Optional[List[StrictInt]] = None
    auth_issues: Optional[List[StrictInt]] = None
    author_issues: Optional[List[StrictInt]] = None
    data_issues: Optional[List[StrictInt]] = None
    sensitive_issues: Optional[List[StrictInt]] = None
    other_issues: Optional[List[StrictInt]] = None
    __properties: ClassVar[List[str]] = ["id", "session_management", "encryption_crypto", "configuration_management", "authentication", "authorization_and_access_control", "data_input_sanitization_validation", "sensitive_data", "other", "engagement", "session_issues", "crypto_issues", "config_issues", "auth_issues", "author_issues", "data_issues", "sensitive_issues", "other_issues"]

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
        """Create an instance of EngagementCheckList from a JSON string"""
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
        excluded_fields: Set[str] = set([
            "id",
            "engagement",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EngagementCheckList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "session_management": obj.get("session_management"),
            "encryption_crypto": obj.get("encryption_crypto"),
            "configuration_management": obj.get("configuration_management"),
            "authentication": obj.get("authentication"),
            "authorization_and_access_control": obj.get("authorization_and_access_control"),
            "data_input_sanitization_validation": obj.get("data_input_sanitization_validation"),
            "sensitive_data": obj.get("sensitive_data"),
            "other": obj.get("other"),
            "engagement": obj.get("engagement"),
            "session_issues": obj.get("session_issues"),
            "crypto_issues": obj.get("crypto_issues"),
            "config_issues": obj.get("config_issues"),
            "auth_issues": obj.get("auth_issues"),
            "author_issues": obj.get("author_issues"),
            "data_issues": obj.get("data_issues"),
            "sensitive_issues": obj.get("sensitive_issues"),
            "other_issues": obj.get("other_issues")
        })
        return _obj


