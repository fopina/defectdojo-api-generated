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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from defectdojo_api_generated.models.product_meta import ProductMeta
from typing import Optional, Set
from typing_extensions import Self

class Product(BaseModel):
    """
    Product
    """ # noqa: E501
    id: StrictInt
    findings_count: StrictInt
    findings_list: List[StrictInt]
    tags: Optional[List[StrictStr]] = None
    product_meta: List[ProductMeta]
    name: Annotated[str, Field(strict=True, max_length=255)]
    description: Annotated[str, Field(strict=True, max_length=4000)]
    created: Optional[datetime]
    prod_numeric_grade: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    business_criticality: Optional[StrictStr] = Field(default=None, description="* `very high` - Very High * `high` - High * `medium` - Medium * `low` - Low * `very low` - Very Low * `none` - None")
    platform: Optional[StrictStr] = Field(default=None, description="* `web service` - API * `desktop` - Desktop * `iot` - Internet of Things * `mobile` - Mobile * `web` - Web")
    lifecycle: Optional[StrictStr] = Field(default=None, description="* `construction` - Construction * `production` - Production * `retirement` - Retirement")
    origin: Optional[StrictStr] = Field(default=None, description="* `third party library` - Third Party Library * `purchased` - Purchased * `contractor` - Contractor Developed * `internal` - Internally Developed * `open source` - Open Source * `outsourced` - Outsourced")
    user_records: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = Field(default=None, description="Estimate the number of user records within the application.")
    revenue: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Estimate the application's revenue.")
    external_audience: Optional[StrictBool] = Field(default=None, description="Specify if the application is used by people outside the organization.")
    internet_accessible: Optional[StrictBool] = Field(default=None, description="Specify if the application is accessible from the public internet.")
    enable_product_tag_inheritance: Optional[StrictBool] = Field(default=None, description="Enables product tag inheritance. Any tags added on a product will automatically be added to all Engagements, Tests, and Findings")
    enable_simple_risk_acceptance: Optional[StrictBool] = Field(default=None, description="Allows simple risk acceptance by checking/unchecking a checkbox.")
    enable_full_risk_acceptance: Optional[StrictBool] = Field(default=None, description="Allows full risk acceptance using a risk acceptance form, expiration date, uploaded proof, etc.")
    disable_sla_breach_notifications: Optional[StrictBool] = Field(default=None, description="Disable SLA breach notifications if configured in the global settings")
    product_manager: Optional[StrictInt] = None
    technical_contact: Optional[StrictInt] = None
    team_manager: Optional[StrictInt] = None
    prod_type: StrictInt
    sla_configuration: Optional[StrictInt] = None
    members: List[StrictInt]
    authorization_groups: List[StrictInt]
    regulations: Optional[List[StrictInt]] = None
    prefetch: Optional[PaginatedProductListPrefetch] = None
    __properties: ClassVar[List[str]] = ["id", "findings_count", "findings_list", "tags", "product_meta", "name", "description", "created", "prod_numeric_grade", "business_criticality", "platform", "lifecycle", "origin", "user_records", "revenue", "external_audience", "internet_accessible", "enable_product_tag_inheritance", "enable_simple_risk_acceptance", "enable_full_risk_acceptance", "disable_sla_breach_notifications", "product_manager", "technical_contact", "team_manager", "prod_type", "sla_configuration", "members", "authorization_groups", "regulations", "prefetch"]

    @field_validator('business_criticality')
    def business_criticality_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['very high', 'high', 'medium', 'low', 'very low', 'none', '']):
            raise ValueError("must be one of enum values ('very high', 'high', 'medium', 'low', 'very low', 'none', '')")
        return value

    @field_validator('platform')
    def platform_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['web service', 'desktop', 'iot', 'mobile', 'web', '']):
            raise ValueError("must be one of enum values ('web service', 'desktop', 'iot', 'mobile', 'web', '')")
        return value

    @field_validator('lifecycle')
    def lifecycle_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['construction', 'production', 'retirement', '']):
            raise ValueError("must be one of enum values ('construction', 'production', 'retirement', '')")
        return value

    @field_validator('origin')
    def origin_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['third party library', 'purchased', 'contractor', 'internal', 'open source', 'outsourced', '']):
            raise ValueError("must be one of enum values ('third party library', 'purchased', 'contractor', 'internal', 'open source', 'outsourced', '')")
        return value

    @field_validator('revenue')
    def revenue_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^-?\d{0,13}(?:\.\d{0,2})?$", value):
            raise ValueError(r"must validate the regular expression /^-?\d{0,13}(?:\.\d{0,2})?$/")
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
        """Create an instance of Product from a JSON string"""
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
        excluded_fields: Set[str] = set([
            "id",
            "findings_count",
            "findings_list",
            "product_meta",
            "created",
            "members",
            "authorization_groups",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in product_meta (list)
        _items = []
        if self.product_meta:
            for _item_product_meta in self.product_meta:
                if _item_product_meta:
                    _items.append(_item_product_meta.to_dict())
            _dict['product_meta'] = _items
        # override the default output from pydantic by calling `to_dict()` of prefetch
        if self.prefetch:
            _dict['prefetch'] = self.prefetch.to_dict()
        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and "created" in self.model_fields_set:
            _dict['created'] = None

        # set to None if prod_numeric_grade (nullable) is None
        # and model_fields_set contains the field
        if self.prod_numeric_grade is None and "prod_numeric_grade" in self.model_fields_set:
            _dict['prod_numeric_grade'] = None

        # set to None if business_criticality (nullable) is None
        # and model_fields_set contains the field
        if self.business_criticality is None and "business_criticality" in self.model_fields_set:
            _dict['business_criticality'] = None

        # set to None if platform (nullable) is None
        # and model_fields_set contains the field
        if self.platform is None and "platform" in self.model_fields_set:
            _dict['platform'] = None

        # set to None if lifecycle (nullable) is None
        # and model_fields_set contains the field
        if self.lifecycle is None and "lifecycle" in self.model_fields_set:
            _dict['lifecycle'] = None

        # set to None if origin (nullable) is None
        # and model_fields_set contains the field
        if self.origin is None and "origin" in self.model_fields_set:
            _dict['origin'] = None

        # set to None if user_records (nullable) is None
        # and model_fields_set contains the field
        if self.user_records is None and "user_records" in self.model_fields_set:
            _dict['user_records'] = None

        # set to None if revenue (nullable) is None
        # and model_fields_set contains the field
        if self.revenue is None and "revenue" in self.model_fields_set:
            _dict['revenue'] = None

        # set to None if product_manager (nullable) is None
        # and model_fields_set contains the field
        if self.product_manager is None and "product_manager" in self.model_fields_set:
            _dict['product_manager'] = None

        # set to None if technical_contact (nullable) is None
        # and model_fields_set contains the field
        if self.technical_contact is None and "technical_contact" in self.model_fields_set:
            _dict['technical_contact'] = None

        # set to None if team_manager (nullable) is None
        # and model_fields_set contains the field
        if self.team_manager is None and "team_manager" in self.model_fields_set:
            _dict['team_manager'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Product from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "findings_count": obj.get("findings_count"),
            "findings_list": obj.get("findings_list"),
            "tags": obj.get("tags"),
            "product_meta": [ProductMeta.from_dict(_item) for _item in obj["product_meta"]] if obj.get("product_meta") is not None else None,
            "name": obj.get("name"),
            "description": obj.get("description"),
            "created": obj.get("created"),
            "prod_numeric_grade": obj.get("prod_numeric_grade"),
            "business_criticality": obj.get("business_criticality"),
            "platform": obj.get("platform"),
            "lifecycle": obj.get("lifecycle"),
            "origin": obj.get("origin"),
            "user_records": obj.get("user_records"),
            "revenue": obj.get("revenue"),
            "external_audience": obj.get("external_audience"),
            "internet_accessible": obj.get("internet_accessible"),
            "enable_product_tag_inheritance": obj.get("enable_product_tag_inheritance"),
            "enable_simple_risk_acceptance": obj.get("enable_simple_risk_acceptance"),
            "enable_full_risk_acceptance": obj.get("enable_full_risk_acceptance"),
            "disable_sla_breach_notifications": obj.get("disable_sla_breach_notifications"),
            "product_manager": obj.get("product_manager"),
            "technical_contact": obj.get("technical_contact"),
            "team_manager": obj.get("team_manager"),
            "prod_type": obj.get("prod_type"),
            "sla_configuration": obj.get("sla_configuration"),
            "members": obj.get("members"),
            "authorization_groups": obj.get("authorization_groups"),
            "regulations": obj.get("regulations"),
            "prefetch": PaginatedProductListPrefetch.from_dict(obj["prefetch"]) if obj.get("prefetch") is not None else None
        })
        return _obj

from defectdojo_api_generated.models.paginated_product_list_prefetch import PaginatedProductListPrefetch
# TODO: Rewrite to not use raise_errors
Product.model_rebuild(raise_errors=False)

