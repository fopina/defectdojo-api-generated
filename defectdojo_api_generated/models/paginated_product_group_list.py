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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing_extensions import Self

from defectdojo_api_generated.models.paginated_product_group_list_prefetch import PaginatedProductGroupListPrefetch
from defectdojo_api_generated.models.product_group import ProductGroup


class PaginatedProductGroupList(BaseModel):
    """
    PaginatedProductGroupList
    """  # noqa: E501

    count: StrictInt
    next: Optional[StrictStr] = None
    previous: Optional[StrictStr] = None
    results: List[ProductGroup]
    prefetch: Optional[PaginatedProductGroupListPrefetch] = None
    __properties: ClassVar[List[str]] = ['count', 'next', 'previous', 'results', 'prefetch']

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
        """Create an instance of PaginatedProductGroupList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item_results in self.results:
                if _item_results:
                    _items.append(_item_results.to_dict())
            _dict['results'] = _items
        # override the default output from pydantic by calling `to_dict()` of prefetch
        if self.prefetch:
            _dict['prefetch'] = self.prefetch.to_dict()
        # set to None if next (nullable) is None
        # and model_fields_set contains the field
        if self.next is None and 'next' in self.model_fields_set:
            _dict['next'] = None

        # set to None if previous (nullable) is None
        # and model_fields_set contains the field
        if self.previous is None and 'previous' in self.model_fields_set:
            _dict['previous'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaginatedProductGroupList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'count': obj.get('count'),
                'next': obj.get('next'),
                'previous': obj.get('previous'),
                'results': [ProductGroup.from_dict(_item) for _item in obj['results']]
                if obj.get('results') is not None
                else None,
                'prefetch': PaginatedProductGroupListPrefetch.from_dict(obj['prefetch'])
                if obj.get('prefetch') is not None
                else None,
            }
        )
        return _obj
