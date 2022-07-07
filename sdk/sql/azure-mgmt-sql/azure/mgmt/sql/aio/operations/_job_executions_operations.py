# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar, Union, cast

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._job_executions_operations import build_cancel_request, build_create_or_update_request_initial, build_create_request_initial, build_get_request, build_list_by_agent_request, build_list_by_job_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class JobExecutionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.sql.aio.SqlManagementClient`'s
        :attr:`job_executions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def list_by_agent(
        self,
        resource_group_name: str,
        server_name: str,
        job_agent_name: str,
        create_time_min: Optional[datetime.datetime] = None,
        create_time_max: Optional[datetime.datetime] = None,
        end_time_min: Optional[datetime.datetime] = None,
        end_time_max: Optional[datetime.datetime] = None,
        is_active: Optional[bool] = None,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable[_models.JobExecutionListResult]:
        """Lists all executions in a job agent.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param server_name: The name of the server.
        :type server_name: str
        :param job_agent_name: The name of the job agent.
        :type job_agent_name: str
        :param create_time_min: If specified, only job executions created at or after the specified
         time are included. Default value is None.
        :type create_time_min: ~datetime.datetime
        :param create_time_max: If specified, only job executions created before the specified time are
         included. Default value is None.
        :type create_time_max: ~datetime.datetime
        :param end_time_min: If specified, only job executions completed at or after the specified time
         are included. Default value is None.
        :type end_time_min: ~datetime.datetime
        :param end_time_max: If specified, only job executions completed before the specified time are
         included. Default value is None.
        :type end_time_max: ~datetime.datetime
        :param is_active: If specified, only active or only completed job executions are included.
         Default value is None.
        :type is_active: bool
        :param skip: The number of elements in the collection to skip. Default value is None.
        :type skip: int
        :param top: The number of elements to return from the collection. Default value is None.
        :type top: int
        :keyword api_version: Api Version. Default value is "2020-11-01-preview". Note that overriding
         this default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either JobExecutionListResult or the result of
         cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.sql.models.JobExecutionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-11-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.JobExecutionListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_agent_request(
                    resource_group_name=resource_group_name,
                    server_name=server_name,
                    job_agent_name=job_agent_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    create_time_min=create_time_min,
                    create_time_max=create_time_max,
                    end_time_min=end_time_min,
                    end_time_max=end_time_max,
                    is_active=is_active,
                    skip=skip,
                    top=top,
                    template_url=self.list_by_agent.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_agent_request(
                    resource_group_name=resource_group_name,
                    server_name=server_name,
                    job_agent_name=job_agent_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    create_time_min=create_time_min,
                    create_time_max=create_time_max,
                    end_time_min=end_time_min,
                    end_time_max=end_time_max,
                    is_active=is_active,
                    skip=skip,
                    top=top,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("JobExecutionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_agent.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/executions"}  # type: ignore

    @distributed_trace_async
    async def cancel(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        server_name: str,
        job_agent_name: str,
        job_name: str,
        job_execution_id: str,
        **kwargs: Any
    ) -> None:
        """Requests cancellation of a job execution.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param server_name: The name of the server.
        :type server_name: str
        :param job_agent_name: The name of the job agent.
        :type job_agent_name: str
        :param job_name: The name of the job.
        :type job_name: str
        :param job_execution_id: The id of the job execution to cancel.
        :type job_execution_id: str
        :keyword api_version: Api Version. Default value is "2020-11-01-preview". Note that overriding
         this default value may result in unsupported behavior.
        :paramtype api_version: str
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

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-11-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_cancel_request(
            resource_group_name=resource_group_name,
            server_name=server_name,
            job_agent_name=job_agent_name,
            job_name=job_name,
            job_execution_id=job_execution_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.cancel.metadata['url'],
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    cancel.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}/cancel"}  # type: ignore


    async def _create_initial(
        self,
        resource_group_name: str,
        server_name: str,
        job_agent_name: str,
        job_name: str,
        **kwargs: Any
    ) -> Optional[_models.JobExecution]:
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-11-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional[_models.JobExecution]]

        
        request = build_create_request_initial(
            resource_group_name=resource_group_name,
            server_name=server_name,
            job_agent_name=job_agent_name,
            job_name=job_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._create_initial.metadata['url'],
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

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('JobExecution', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_initial.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/start"}  # type: ignore


    @distributed_trace_async
    async def begin_create(
        self,
        resource_group_name: str,
        server_name: str,
        job_agent_name: str,
        job_name: str,
        **kwargs: Any
    ) -> AsyncLROPoller[_models.JobExecution]:
        """Starts an elastic job execution.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param server_name: The name of the server.
        :type server_name: str
        :param job_agent_name: The name of the job agent.
        :type job_agent_name: str
        :param job_name: The name of the job to get.
        :type job_name: str
        :keyword api_version: Api Version. Default value is "2020-11-01-preview". Note that overriding
         this default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either JobExecution or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.sql.models.JobExecution]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-11-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.JobExecution]
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_initial(  # type: ignore
                resource_group_name=resource_group_name,
                server_name=server_name,
                job_agent_name=job_agent_name,
                job_name=job_name,
                api_version=api_version,
                cls=lambda x,y,z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('JobExecution', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(
                lro_delay,
                
                
                **kwargs
        ))  # type: AsyncPollingMethod
        elif polling is False: polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/start"}  # type: ignore

    @distributed_trace
    def list_by_job(
        self,
        resource_group_name: str,
        server_name: str,
        job_agent_name: str,
        job_name: str,
        create_time_min: Optional[datetime.datetime] = None,
        create_time_max: Optional[datetime.datetime] = None,
        end_time_min: Optional[datetime.datetime] = None,
        end_time_max: Optional[datetime.datetime] = None,
        is_active: Optional[bool] = None,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable[_models.JobExecutionListResult]:
        """Lists a job's executions.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param server_name: The name of the server.
        :type server_name: str
        :param job_agent_name: The name of the job agent.
        :type job_agent_name: str
        :param job_name: The name of the job to get.
        :type job_name: str
        :param create_time_min: If specified, only job executions created at or after the specified
         time are included. Default value is None.
        :type create_time_min: ~datetime.datetime
        :param create_time_max: If specified, only job executions created before the specified time are
         included. Default value is None.
        :type create_time_max: ~datetime.datetime
        :param end_time_min: If specified, only job executions completed at or after the specified time
         are included. Default value is None.
        :type end_time_min: ~datetime.datetime
        :param end_time_max: If specified, only job executions completed before the specified time are
         included. Default value is None.
        :type end_time_max: ~datetime.datetime
        :param is_active: If specified, only active or only completed job executions are included.
         Default value is None.
        :type is_active: bool
        :param skip: The number of elements in the collection to skip. Default value is None.
        :type skip: int
        :param top: The number of elements to return from the collection. Default value is None.
        :type top: int
        :keyword api_version: Api Version. Default value is "2020-11-01-preview". Note that overriding
         this default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either JobExecutionListResult or the result of
         cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.sql.models.JobExecutionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-11-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.JobExecutionListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_job_request(
                    resource_group_name=resource_group_name,
                    server_name=server_name,
                    job_agent_name=job_agent_name,
                    job_name=job_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    create_time_min=create_time_min,
                    create_time_max=create_time_max,
                    end_time_min=end_time_min,
                    end_time_max=end_time_max,
                    is_active=is_active,
                    skip=skip,
                    top=top,
                    template_url=self.list_by_job.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_job_request(
                    resource_group_name=resource_group_name,
                    server_name=server_name,
                    job_agent_name=job_agent_name,
                    job_name=job_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    create_time_min=create_time_min,
                    create_time_max=create_time_max,
                    end_time_min=end_time_min,
                    end_time_max=end_time_max,
                    is_active=is_active,
                    skip=skip,
                    top=top,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("JobExecutionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_job.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions"}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        server_name: str,
        job_agent_name: str,
        job_name: str,
        job_execution_id: str,
        **kwargs: Any
    ) -> _models.JobExecution:
        """Gets a job execution.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param server_name: The name of the server.
        :type server_name: str
        :param job_agent_name: The name of the job agent.
        :type job_agent_name: str
        :param job_name: The name of the job.
        :type job_name: str
        :param job_execution_id: The id of the job execution.
        :type job_execution_id: str
        :keyword api_version: Api Version. Default value is "2020-11-01-preview". Note that overriding
         this default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JobExecution, or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.JobExecution
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-11-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.JobExecution]

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            server_name=server_name,
            job_agent_name=job_agent_name,
            job_name=job_name,
            job_execution_id=job_execution_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata['url'],
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('JobExecution', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}"}  # type: ignore


    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        server_name: str,
        job_agent_name: str,
        job_name: str,
        job_execution_id: str,
        **kwargs: Any
    ) -> Optional[_models.JobExecution]:
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-11-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional[_models.JobExecution]]

        
        request = build_create_or_update_request_initial(
            resource_group_name=resource_group_name,
            server_name=server_name,
            job_agent_name=job_agent_name,
            job_name=job_name,
            job_execution_id=job_execution_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._create_or_update_initial.metadata['url'],
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

        if response.status_code not in [200, 201, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('JobExecution', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('JobExecution', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_initial.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}"}  # type: ignore


    @distributed_trace_async
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        server_name: str,
        job_agent_name: str,
        job_name: str,
        job_execution_id: str,
        **kwargs: Any
    ) -> AsyncLROPoller[_models.JobExecution]:
        """Creates or updates a job execution.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param server_name: The name of the server.
        :type server_name: str
        :param job_agent_name: The name of the job agent.
        :type job_agent_name: str
        :param job_name: The name of the job to get.
        :type job_name: str
        :param job_execution_id: The job execution id to create the job execution under.
        :type job_execution_id: str
        :keyword api_version: Api Version. Default value is "2020-11-01-preview". Note that overriding
         this default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either JobExecution or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.sql.models.JobExecution]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-11-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.JobExecution]
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_or_update_initial(  # type: ignore
                resource_group_name=resource_group_name,
                server_name=server_name,
                job_agent_name=job_agent_name,
                job_name=job_name,
                job_execution_id=job_execution_id,
                api_version=api_version,
                cls=lambda x,y,z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('JobExecution', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(
                lro_delay,
                
                
                **kwargs
        ))  # type: AsyncPollingMethod
        elif polling is False: polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create_or_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}"}  # type: ignore
