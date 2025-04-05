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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing_extensions import Annotated, Self

from defectdojo_api_generated.models.paginated_tool_product_settings_list_prefetch import (
    PaginatedToolProductSettingsListPrefetch,
)


class ToolProductSettings(BaseModel):
    """
    ToolProductSettings
    """  # noqa: E501

    id: StrictInt
    setting_url: StrictStr
    product: StrictInt
    name: Annotated[str, Field(strict=True, max_length=200)]
    description: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = None
    url: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = None
    tool_project_id: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    tool_configuration: StrictInt
    notes: List[StrictInt]
    prefetch: Optional[PaginatedToolProductSettingsListPrefetch] = None
    __properties: ClassVar[List[str]] = [
        'id',
        'setting_url',
        'product',
        'name',
        'description',
        'url',
        'tool_project_id',
        'tool_configuration',
        'notes',
        'prefetch',
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
        """Create an instance of ToolProductSettings from a JSON string"""
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
        excluded_fields: Set[str] = set(
            [
                'id',
                'notes',
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
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and 'description' in self.model_fields_set:
            _dict['description'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and 'url' in self.model_fields_set:
            _dict['url'] = None

        # set to None if tool_project_id (nullable) is None
        # and model_fields_set contains the field
        if self.tool_project_id is None and 'tool_project_id' in self.model_fields_set:
            _dict['tool_project_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ToolProductSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'id': obj.get('id'),
                'setting_url': obj.get('setting_url'),
                'product': obj.get('product'),
                'name': obj.get('name'),
                'description': obj.get('description'),
                'url': obj.get('url'),
                'tool_project_id': obj.get('tool_project_id'),
                'tool_configuration': obj.get('tool_configuration'),
                'notes': obj.get('notes'),
                'prefetch': PaginatedToolProductSettingsListPrefetch.from_dict(obj['prefetch'])
                if obj.get('prefetch') is not None
                else None,
            }
        )
        return _obj
