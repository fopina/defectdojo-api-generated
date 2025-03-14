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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing_extensions import Annotated, Self


class Endpoint(BaseModel):
    """
    Endpoint
    """  # noqa: E501

    id: StrictInt
    tags: Optional[List[StrictStr]] = None
    protocol: Optional[Annotated[str, Field(strict=True, max_length=20)]] = Field(
        default=None, description="The communication protocol/scheme such as 'http', 'ftp', 'dns', etc."
    )
    userinfo: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(
        default=None, description="User info as 'alice', 'bob', etc."
    )
    host: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(
        default=None,
        description="The host name or IP address. It must not include the port number. For example '127.0.0.1', 'localhost', 'yourdomain.com'.",
    )
    port: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(
        default=None, description='The network port associated with the endpoint.'
    )
    path: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(
        default=None,
        description="The location of the resource, it must not start with a '/'. For example endpoint/420/edit",
    )
    query: Optional[Annotated[str, Field(strict=True, max_length=1000)]] = Field(
        default=None, description="The query string, the question mark should be omitted.For example 'group=4&team=8'"
    )
    fragment: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(
        default=None,
        description="The fragment identifier which follows the hash mark. The hash mark should be omitted. For example 'section-13', 'paragraph-2'.",
    )
    product: Optional[StrictInt] = None
    endpoint_params: List[StrictInt]
    findings: List[StrictInt]
    __properties: ClassVar[List[str]] = [
        'id',
        'tags',
        'protocol',
        'userinfo',
        'host',
        'port',
        'path',
        'query',
        'fragment',
        'product',
        'endpoint_params',
        'findings',
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
        """Create an instance of Endpoint from a JSON string"""
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
                'endpoint_params',
                'findings',
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if protocol (nullable) is None
        # and model_fields_set contains the field
        if self.protocol is None and 'protocol' in self.model_fields_set:
            _dict['protocol'] = None

        # set to None if userinfo (nullable) is None
        # and model_fields_set contains the field
        if self.userinfo is None and 'userinfo' in self.model_fields_set:
            _dict['userinfo'] = None

        # set to None if host (nullable) is None
        # and model_fields_set contains the field
        if self.host is None and 'host' in self.model_fields_set:
            _dict['host'] = None

        # set to None if port (nullable) is None
        # and model_fields_set contains the field
        if self.port is None and 'port' in self.model_fields_set:
            _dict['port'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and 'path' in self.model_fields_set:
            _dict['path'] = None

        # set to None if query (nullable) is None
        # and model_fields_set contains the field
        if self.query is None and 'query' in self.model_fields_set:
            _dict['query'] = None

        # set to None if fragment (nullable) is None
        # and model_fields_set contains the field
        if self.fragment is None and 'fragment' in self.model_fields_set:
            _dict['fragment'] = None

        # set to None if product (nullable) is None
        # and model_fields_set contains the field
        if self.product is None and 'product' in self.model_fields_set:
            _dict['product'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Endpoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'id': obj.get('id'),
                'tags': obj.get('tags'),
                'protocol': obj.get('protocol'),
                'userinfo': obj.get('userinfo'),
                'host': obj.get('host'),
                'port': obj.get('port'),
                'path': obj.get('path'),
                'query': obj.get('query'),
                'fragment': obj.get('fragment'),
                'product': obj.get('product'),
                'endpoint_params': obj.get('endpoint_params'),
                'findings': obj.get('findings'),
            }
        )
        return _obj
