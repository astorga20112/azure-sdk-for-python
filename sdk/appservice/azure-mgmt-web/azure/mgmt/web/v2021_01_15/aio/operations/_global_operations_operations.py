# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, List, Optional, TypeVar

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._global_operations_operations import build_get_deleted_web_app_request, build_get_deleted_web_app_snapshots_request, build_get_subscription_operation_with_async_response_request
from .._vendor import MixinABC
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class GlobalOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.web.v2021_01_15.aio.WebSiteManagementClient`'s
        :attr:`global_operations` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace_async
    async def get_deleted_web_app(
        self,
        deleted_site_id: str,
        **kwargs: Any
    ) -> _models.DeletedSite:
        """Get deleted app for a subscription.

        Get deleted app for a subscription.

        :param deleted_site_id: The numeric ID of the deleted app, e.g. 12345.
        :type deleted_site_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DeletedSite, or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2021_01_15.models.DeletedSite
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-01-15"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.DeletedSite]

        
        request = build_get_deleted_web_app_request(
            deleted_site_id=deleted_site_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_deleted_web_app.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DeletedSite', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_deleted_web_app.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.Web/deletedSites/{deletedSiteId}"}  # type: ignore


    @distributed_trace_async
    async def get_deleted_web_app_snapshots(
        self,
        deleted_site_id: str,
        **kwargs: Any
    ) -> List[_models.Snapshot]:
        """Get all deleted apps for a subscription.

        Get all deleted apps for a subscription.

        :param deleted_site_id: The numeric ID of the deleted app, e.g. 12345.
        :type deleted_site_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of Snapshot, or the result of cls(response)
        :rtype: list[~azure.mgmt.web.v2021_01_15.models.Snapshot]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-01-15"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[List[_models.Snapshot]]

        
        request = build_get_deleted_web_app_snapshots_request(
            deleted_site_id=deleted_site_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_deleted_web_app_snapshots.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[Snapshot]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_deleted_web_app_snapshots.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.Web/deletedSites/{deletedSiteId}/snapshots"}  # type: ignore


    @distributed_trace_async
    async def get_subscription_operation_with_async_response(  # pylint: disable=inconsistent-return-statements
        self,
        location: str,
        operation_id: str,
        **kwargs: Any
    ) -> None:
        """Gets an operation in a subscription and given region.

        Gets an operation in a subscription and given region.

        :param location: Location name.
        :type location: str
        :param operation_id: Operation Id.
        :type operation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-01-15"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_get_subscription_operation_with_async_response_request(
            location=location,
            operation_id=operation_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_subscription_operation_with_async_response.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_subscription_operation_with_async_response.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/operations/{operationId}"}  # type: ignore

