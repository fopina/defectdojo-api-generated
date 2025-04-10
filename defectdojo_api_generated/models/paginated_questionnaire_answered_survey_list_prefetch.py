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

from pydantic import BaseModel, ConfigDict
from typing_extensions import Self

from defectdojo_api_generated.models.finding_engagement import FindingEngagement
from defectdojo_api_generated.models.questionnaire_engagement_survey import QuestionnaireEngagementSurvey
from defectdojo_api_generated.models.user_stub import UserStub


class PaginatedQuestionnaireAnsweredSurveyListPrefetch(BaseModel):
    """
    PaginatedQuestionnaireAnsweredSurveyListPrefetch
    """  # noqa: E501

    assignee: Optional[Dict[str, UserStub]] = None
    engagement: Optional[Dict[str, FindingEngagement]] = None
    responder: Optional[Dict[str, UserStub]] = None
    survey: Optional[Dict[str, QuestionnaireEngagementSurvey]] = None
    __properties: ClassVar[List[str]] = ['assignee', 'engagement', 'responder', 'survey']

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
        """Create an instance of PaginatedQuestionnaireAnsweredSurveyListPrefetch from a JSON string"""
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
        """
        excluded_fields: Set[str] = set(
            [
                'assignee',
                'engagement',
                'responder',
                'survey',
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each value in assignee (dict)
        _field_dict = {}
        if self.assignee:
            for _key_assignee in self.assignee:
                if self.assignee[_key_assignee]:
                    _field_dict[_key_assignee] = self.assignee[_key_assignee].to_dict()
            _dict['assignee'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in engagement (dict)
        _field_dict = {}
        if self.engagement:
            for _key_engagement in self.engagement:
                if self.engagement[_key_engagement]:
                    _field_dict[_key_engagement] = self.engagement[_key_engagement].to_dict()
            _dict['engagement'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in responder (dict)
        _field_dict = {}
        if self.responder:
            for _key_responder in self.responder:
                if self.responder[_key_responder]:
                    _field_dict[_key_responder] = self.responder[_key_responder].to_dict()
            _dict['responder'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in survey (dict)
        _field_dict = {}
        if self.survey:
            for _key_survey in self.survey:
                if self.survey[_key_survey]:
                    _field_dict[_key_survey] = self.survey[_key_survey].to_dict()
            _dict['survey'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaginatedQuestionnaireAnsweredSurveyListPrefetch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                'assignee': dict((_k, UserStub.from_dict(_v)) for _k, _v in obj['assignee'].items())
                if obj.get('assignee') is not None
                else None,
                'engagement': dict((_k, FindingEngagement.from_dict(_v)) for _k, _v in obj['engagement'].items())
                if obj.get('engagement') is not None
                else None,
                'responder': dict((_k, UserStub.from_dict(_v)) for _k, _v in obj['responder'].items())
                if obj.get('responder') is not None
                else None,
                'survey': dict((_k, QuestionnaireEngagementSurvey.from_dict(_v)) for _k, _v in obj['survey'].items())
                if obj.get('survey') is not None
                else None,
            }
        )
        return _obj
