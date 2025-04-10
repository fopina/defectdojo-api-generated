# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic import Field, StrictFloat, StrictInt, StrictStr
from typing_extensions import Annotated

from defectdojo_api_generated.api_client import ApiClient, RequestSerialized
from defectdojo_api_generated.api_response import ApiResponse
from defectdojo_api_generated.models.paginated_questionnaire_answered_survey_list import (
    PaginatedQuestionnaireAnsweredSurveyList,
)
from defectdojo_api_generated.models.questionnaire_answered_survey import QuestionnaireAnsweredSurvey
from defectdojo_api_generated.rest import RESTResponseType


class QuestionnaireAnsweredQuestionnairesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    def questionnaire_answered_questionnaires_list(
        self,
        limit: Annotated[Optional[StrictInt], Field(description='Number of results to return per page.')] = None,
        offset: Annotated[
            Optional[StrictInt], Field(description='The initial index from which to return the results.')
        ] = None,
        prefetch: Annotated[
            Optional[List[StrictStr]],
            Field(description='List of fields for which to prefetch model instances and add those to the response'),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PaginatedQuestionnaireAnsweredSurveyList:
        """questionnaire_answered_questionnaires_list


        :param limit: Number of results to return per page.
        :type limit: int
        :param offset: The initial index from which to return the results.
        :type offset: int
        :param prefetch: List of fields for which to prefetch model instances and add those to the response
        :type prefetch: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._questionnaire_answered_questionnaires_list_serialize(
            limit=limit,
            offset=offset,
            prefetch=prefetch,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'PaginatedQuestionnaireAnsweredSurveyList',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def questionnaire_answered_questionnaires_list_with_http_info(
        self,
        limit: Annotated[Optional[StrictInt], Field(description='Number of results to return per page.')] = None,
        offset: Annotated[
            Optional[StrictInt], Field(description='The initial index from which to return the results.')
        ] = None,
        prefetch: Annotated[
            Optional[List[StrictStr]],
            Field(description='List of fields for which to prefetch model instances and add those to the response'),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PaginatedQuestionnaireAnsweredSurveyList]:
        """questionnaire_answered_questionnaires_list


        :param limit: Number of results to return per page.
        :type limit: int
        :param offset: The initial index from which to return the results.
        :type offset: int
        :param prefetch: List of fields for which to prefetch model instances and add those to the response
        :type prefetch: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._questionnaire_answered_questionnaires_list_serialize(
            limit=limit,
            offset=offset,
            prefetch=prefetch,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'PaginatedQuestionnaireAnsweredSurveyList',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    def questionnaire_answered_questionnaires_list_without_preload_content(
        self,
        limit: Annotated[Optional[StrictInt], Field(description='Number of results to return per page.')] = None,
        offset: Annotated[
            Optional[StrictInt], Field(description='The initial index from which to return the results.')
        ] = None,
        prefetch: Annotated[
            Optional[List[StrictStr]],
            Field(description='List of fields for which to prefetch model instances and add those to the response'),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """questionnaire_answered_questionnaires_list


        :param limit: Number of results to return per page.
        :type limit: int
        :param offset: The initial index from which to return the results.
        :type offset: int
        :param prefetch: List of fields for which to prefetch model instances and add those to the response
        :type prefetch: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._questionnaire_answered_questionnaires_list_serialize(
            limit=limit,
            offset=offset,
            prefetch=prefetch,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'PaginatedQuestionnaireAnsweredSurveyList',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        return response_data.response

    def _questionnaire_answered_questionnaires_list_serialize(
        self,
        limit,
        offset,
        prefetch,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {
            'prefetch': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if limit is not None:
            _query_params.append(('limit', limit))

        if offset is not None:
            _query_params.append(('offset', offset))

        if prefetch is not None:
            _query_params.append(('prefetch', prefetch))

        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # authentication setting
        _auth_settings: List[str] = ['basicAuth', 'cookieAuth', 'tokenAuth']

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v2/questionnaire_answered_questionnaires/',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    def questionnaire_answered_questionnaires_retrieve(
        self,
        id: Annotated[
            StrictInt, Field(description='A unique integer value identifying this Answered Engagement Survey.')
        ],
        prefetch: Annotated[
            Optional[List[StrictStr]],
            Field(description='List of fields for which to prefetch model instances and add those to the response'),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> QuestionnaireAnsweredSurvey:
        """questionnaire_answered_questionnaires_retrieve


        :param id: A unique integer value identifying this Answered Engagement Survey. (required)
        :type id: int
        :param prefetch: List of fields for which to prefetch model instances and add those to the response
        :type prefetch: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._questionnaire_answered_questionnaires_retrieve_serialize(
            id=id,
            prefetch=prefetch,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'QuestionnaireAnsweredSurvey',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def questionnaire_answered_questionnaires_retrieve_with_http_info(
        self,
        id: Annotated[
            StrictInt, Field(description='A unique integer value identifying this Answered Engagement Survey.')
        ],
        prefetch: Annotated[
            Optional[List[StrictStr]],
            Field(description='List of fields for which to prefetch model instances and add those to the response'),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[QuestionnaireAnsweredSurvey]:
        """questionnaire_answered_questionnaires_retrieve


        :param id: A unique integer value identifying this Answered Engagement Survey. (required)
        :type id: int
        :param prefetch: List of fields for which to prefetch model instances and add those to the response
        :type prefetch: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._questionnaire_answered_questionnaires_retrieve_serialize(
            id=id,
            prefetch=prefetch,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'QuestionnaireAnsweredSurvey',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    def questionnaire_answered_questionnaires_retrieve_without_preload_content(
        self,
        id: Annotated[
            StrictInt, Field(description='A unique integer value identifying this Answered Engagement Survey.')
        ],
        prefetch: Annotated[
            Optional[List[StrictStr]],
            Field(description='List of fields for which to prefetch model instances and add those to the response'),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """questionnaire_answered_questionnaires_retrieve


        :param id: A unique integer value identifying this Answered Engagement Survey. (required)
        :type id: int
        :param prefetch: List of fields for which to prefetch model instances and add those to the response
        :type prefetch: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._questionnaire_answered_questionnaires_retrieve_serialize(
            id=id,
            prefetch=prefetch,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'QuestionnaireAnsweredSurvey',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        return response_data.response

    def _questionnaire_answered_questionnaires_retrieve_serialize(
        self,
        id,
        prefetch,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {
            'prefetch': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if prefetch is not None:
            _query_params.append(('prefetch', prefetch))

        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # authentication setting
        _auth_settings: List[str] = ['basicAuth', 'cookieAuth', 'tokenAuth']

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v2/questionnaire_answered_questionnaires/{id}/',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )
