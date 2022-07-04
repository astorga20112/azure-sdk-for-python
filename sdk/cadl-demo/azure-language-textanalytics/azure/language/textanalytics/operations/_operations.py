# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .._serialization import Serializer
from .._vendor import _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_analyze_analyzeText_request(
    *, api_version: str, show_stats: Optional[bool] = None, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/:analyze-text"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if show_stats is not None:
        _params["showStats"] = _SERIALIZER.query("show_stats", show_stats, "bool")

    return HttpRequest(method="post", url=_url, params=_params, **kwargs)


def build_analyze_submitJob_request(*, api_version: str, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/analyze-text/jobs"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    return HttpRequest(method="post", url=_url, params=_params, **kwargs)


def build_analyze_getJobStatus_request(
    job_id: str,
    *,
    api_version: str,
    top: Optional[int] = None,
    skip: Optional[int] = None,
    show_stats: Optional[bool] = None,
    **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/analyze-text/jobs/{jobId}"
    path_format_arguments = {
        "jobId": _SERIALIZER.url("job_id", job_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if top is not None:
        _params["top"] = _SERIALIZER.query("top", top, "int")
    if skip is not None:
        _params["skip"] = _SERIALIZER.query("skip", skip, "int")
    if show_stats is not None:
        _params["showStats"] = _SERIALIZER.query("show_stats", show_stats, "bool")

    return HttpRequest(method="get", url=_url, params=_params, **kwargs)


def build_analyze_cancelJob_request(job_id: str, *, api_version: str, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/analyze-text/jobs/{jobId}:cancel"
    path_format_arguments = {
        "jobId": _SERIALIZER.url("job_id", job_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    return HttpRequest(method="post", url=_url, params=_params, **kwargs)


class Analyze:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.language.textanalytics.MicrosoftCognitiveLanguageTextAnalytics`'s
        :attr:`analyze` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def analyzeText(  # pylint: disable=inconsistent-return-statements
        self, *, api_version: str, show_stats: Optional[bool] = None, **kwargs: Any
    ) -> None:
        """Submit a collection of text documents for analysis.  Specify a single unique task to be
        executed immediately.

        :keyword api_version: The API version to use for this operation. Required.
        :paramtype api_version: str
        :keyword show_stats: If set to true, response will contain request and document level
         statistics. Default value is None.
        :paramtype show_stats: bool
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            nan: HttpResponseError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_analyze_analyzeText_request(
            api_version=api_version,
            show_stats=show_stats,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def submitJob(self, *, api_version: str, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Submit a collection of text documents for analysis. Specify one or more unique tasks to be
        executed as a long-running operation.

        :keyword api_version: The API version to use for this operation. Required.
        :paramtype api_version: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            nan: HttpResponseError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_analyze_submitJob_request(
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["Operation-Location"] = self._deserialize("str", response.headers.get("Operation-Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    @distributed_trace
    def getJobStatus(  # pylint: disable=inconsistent-return-statements
        self,
        job_id: str,
        *,
        api_version: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        show_stats: Optional[bool] = None,
        **kwargs: Any
    ) -> None:
        """Get the status of an analysis job.  A job may consist of one or more tasks.  Once all tasks are
        succeeded, the job will transition to the succeeded state and results will be available for
        each task.

        :param job_id: Job ID. Required.
        :type job_id: str
        :keyword api_version: The API version to use for this operation. Required.
        :paramtype api_version: str
        :keyword top: The maximum number of resources to return from the collection. Default value is
         None.
        :paramtype top: int
        :keyword skip: An offset into the collection of the first resource to be returned. Default
         value is None.
        :paramtype skip: int
        :keyword show_stats: If set to true, response will contain request and document level
         statistics. Default value is None.
        :paramtype show_stats: bool
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            nan: HttpResponseError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_analyze_getJobStatus_request(
            job_id=job_id,
            api_version=api_version,
            top=top,
            skip=skip,
            show_stats=show_stats,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def cancelJob(  # pylint: disable=inconsistent-return-statements
        self, job_id: str, *, api_version: str, **kwargs: Any
    ) -> None:
        """Cancel a long-running Text Analysis job.

        :param job_id: Job ID. Required.
        :type job_id: str
        :keyword api_version: The API version to use for this operation. Required.
        :paramtype api_version: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            nan: HttpResponseError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_analyze_cancelJob_request(
            job_id=job_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["Operation-Location"] = self._deserialize("str", response.headers.get("Operation-Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)
