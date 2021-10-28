# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class FileSystemOperations:
    """FileSystemOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.storage.filedatalake.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def create(
        self,
        request_id_parameter: Optional[str] = None,
        timeout: Optional[int] = None,
        properties: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Create FileSystem.

        Create a FileSystem rooted at the specified location. If the FileSystem already exists, the
        operation fails.  This operation does not support conditional HTTP requests.

        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`.
        :type timeout: int
        :param properties: Optional. User-defined properties to be stored with the filesystem, in the
         format of a comma-separated list of name and value pairs "n1=v1, n2=v2, ...", where each value
         is a base64 encoded string. Note that the string may only contain ASCII characters in the
         ISO-8859-1 character set.  If the filesystem exists, any properties not included in the list
         will be removed.  All properties are removed if the header is omitted.  To merge new and
         existing properties, first get all existing properties and the current E-Tag, then make a
         conditional request with the E-Tag and include values for all properties.
        :type properties: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.create.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['resource'] = self._serialize.query("self._config.resource", self._config.resource, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if request_id_parameter is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if properties is not None:
            header_parameters['x-ms-properties'] = self._serialize.header("properties", properties, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))
        response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))
        response_headers['Last-Modified']=self._deserialize('rfc-1123', response.headers.get('Last-Modified'))
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
        response_headers['x-ms-namespace-enabled']=self._deserialize('str', response.headers.get('x-ms-namespace-enabled'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    create.metadata = {'url': '/{filesystem}'}  # type: ignore

    async def set_properties(
        self,
        request_id_parameter: Optional[str] = None,
        timeout: Optional[int] = None,
        properties: Optional[str] = None,
        modified_access_conditions: Optional["_models.ModifiedAccessConditions"] = None,
        **kwargs: Any
    ) -> None:
        """Set FileSystem Properties.

        Set properties for the FileSystem.  This operation supports conditional HTTP requests.  For
        more information, see `Specifying Conditional Headers for Blob Service Operations
        <https://docs.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations>`_.

        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`.
        :type timeout: int
        :param properties: Optional. User-defined properties to be stored with the filesystem, in the
         format of a comma-separated list of name and value pairs "n1=v1, n2=v2, ...", where each value
         is a base64 encoded string. Note that the string may only contain ASCII characters in the
         ISO-8859-1 character set.  If the filesystem exists, any properties not included in the list
         will be removed.  All properties are removed if the header is omitted.  To merge new and
         existing properties, first get all existing properties and the current E-Tag, then make a
         conditional request with the E-Tag and include values for all properties.
        :type properties: str
        :param modified_access_conditions: Parameter group.
        :type modified_access_conditions: ~azure.storage.filedatalake.models.ModifiedAccessConditions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        
        _if_modified_since = None
        _if_unmodified_since = None
        if modified_access_conditions is not None:
            _if_modified_since = modified_access_conditions.if_modified_since
            _if_unmodified_since = modified_access_conditions.if_unmodified_since
        accept = "application/json"

        # Construct URL
        url = self.set_properties.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['resource'] = self._serialize.query("self._config.resource", self._config.resource, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if request_id_parameter is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if properties is not None:
            header_parameters['x-ms-properties'] = self._serialize.header("properties", properties, 'str')
        if _if_modified_since is not None:
            header_parameters['If-Modified-Since'] = self._serialize.header("if_modified_since", _if_modified_since, 'rfc-1123')
        if _if_unmodified_since is not None:
            header_parameters['If-Unmodified-Since'] = self._serialize.header("if_unmodified_since", _if_unmodified_since, 'rfc-1123')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.patch(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))
        response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))
        response_headers['Last-Modified']=self._deserialize('rfc-1123', response.headers.get('Last-Modified'))
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    set_properties.metadata = {'url': '/{filesystem}'}  # type: ignore

    async def get_properties(
        self,
        request_id_parameter: Optional[str] = None,
        timeout: Optional[int] = None,
        **kwargs: Any
    ) -> None:
        """Get FileSystem Properties.

        All system and user-defined filesystem properties are specified in the response headers.

        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`.
        :type timeout: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_properties.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['resource'] = self._serialize.query("self._config.resource", self._config.resource, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if request_id_parameter is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))
        response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))
        response_headers['Last-Modified']=self._deserialize('rfc-1123', response.headers.get('Last-Modified'))
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
        response_headers['x-ms-properties']=self._deserialize('str', response.headers.get('x-ms-properties'))
        response_headers['x-ms-namespace-enabled']=self._deserialize('str', response.headers.get('x-ms-namespace-enabled'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    get_properties.metadata = {'url': '/{filesystem}'}  # type: ignore

    async def delete(
        self,
        request_id_parameter: Optional[str] = None,
        timeout: Optional[int] = None,
        modified_access_conditions: Optional["_models.ModifiedAccessConditions"] = None,
        **kwargs: Any
    ) -> None:
        """Delete FileSystem.

        Marks the FileSystem for deletion.  When a FileSystem is deleted, a FileSystem with the same
        identifier cannot be created for at least 30 seconds. While the filesystem is being deleted,
        attempts to create a filesystem with the same identifier will fail with status code 409
        (Conflict), with the service returning additional error information indicating that the
        filesystem is being deleted. All other operations, including operations on any files or
        directories within the filesystem, will fail with status code 404 (Not Found) while the
        filesystem is being deleted. This operation supports conditional HTTP requests.  For more
        information, see `Specifying Conditional Headers for Blob Service Operations
        <https://docs.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations>`_.

        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`.
        :type timeout: int
        :param modified_access_conditions: Parameter group.
        :type modified_access_conditions: ~azure.storage.filedatalake.models.ModifiedAccessConditions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        
        _if_modified_since = None
        _if_unmodified_since = None
        if modified_access_conditions is not None:
            _if_modified_since = modified_access_conditions.if_modified_since
            _if_unmodified_since = modified_access_conditions.if_unmodified_since
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['resource'] = self._serialize.query("self._config.resource", self._config.resource, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if request_id_parameter is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if _if_modified_since is not None:
            header_parameters['If-Modified-Since'] = self._serialize.header("if_modified_since", _if_modified_since, 'rfc-1123')
        if _if_unmodified_since is not None:
            header_parameters['If-Unmodified-Since'] = self._serialize.header("if_unmodified_since", _if_unmodified_since, 'rfc-1123')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
        response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    delete.metadata = {'url': '/{filesystem}'}  # type: ignore

    async def list_paths(
        self,
        recursive: bool,
        request_id_parameter: Optional[str] = None,
        timeout: Optional[int] = None,
        continuation: Optional[str] = None,
        path: Optional[str] = None,
        max_results: Optional[int] = None,
        upn: Optional[bool] = None,
        **kwargs: Any
    ) -> "_models.PathList":
        """List Paths.

        List FileSystem paths and their properties.

        :param recursive: Required.
        :type recursive: bool
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`.
        :type timeout: int
        :param continuation: Optional.  When deleting a directory, the number of paths that are deleted
         with each invocation is limited.  If the number of paths to be deleted exceeds this limit, a
         continuation token is returned in this response header.  When a continuation token is returned
         in the response, it must be specified in a subsequent invocation of the delete operation to
         continue deleting the directory.
        :type continuation: str
        :param path: Optional.  Filters results to paths within the specified directory. An error
         occurs if the directory does not exist.
        :type path: str
        :param max_results: An optional value that specifies the maximum number of items to return. If
         omitted or greater than 5,000, the response will include up to 5,000 items.
        :type max_results: int
        :param upn: Optional. Valid only when Hierarchical Namespace is enabled for the account. If
         "true", the user identity values returned in the x-ms-owner, x-ms-group, and x-ms-acl response
         headers will be transformed from Azure Active Directory Object IDs to User Principal Names.  If
         "false", the values will be returned as Azure Active Directory Object IDs. The default value is
         false. Note that group and application Object IDs are not translated because they do not have
         unique friendly names.
        :type upn: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PathList, or the result of cls(response)
        :rtype: ~azure.storage.filedatalake.models.PathList
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PathList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.list_paths.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['resource'] = self._serialize.query("self._config.resource", self._config.resource, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        if continuation is not None:
            query_parameters['continuation'] = self._serialize.query("continuation", continuation, 'str')
        if path is not None:
            query_parameters['directory'] = self._serialize.query("path", path, 'str')
        query_parameters['recursive'] = self._serialize.query("recursive", recursive, 'bool')
        if max_results is not None:
            query_parameters['maxResults'] = self._serialize.query("max_results", max_results, 'int', minimum=1)
        if upn is not None:
            query_parameters['upn'] = self._serialize.query("upn", upn, 'bool')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if request_id_parameter is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))
        response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))
        response_headers['Last-Modified']=self._deserialize('rfc-1123', response.headers.get('Last-Modified'))
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
        response_headers['x-ms-continuation']=self._deserialize('str', response.headers.get('x-ms-continuation'))
        deserialized = self._deserialize('PathList', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    list_paths.metadata = {'url': '/{filesystem}'}  # type: ignore

    async def list_blob_hierarchy_segment(
        self,
        prefix: Optional[str] = None,
        delimiter: Optional[str] = None,
        marker: Optional[str] = None,
        max_results: Optional[int] = None,
        include: Optional[List[Union[str, "_models.ListBlobsIncludeItem"]]] = None,
        showonly: Optional[str] = "deleted",
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.ListBlobsHierarchySegmentResponse":
        """The List Blobs operation returns a list of the blobs under the specified container.

        :param prefix: Filters results to filesystems within the specified prefix.
        :type prefix: str
        :param delimiter: When the request includes this parameter, the operation returns a BlobPrefix
         element in the response body that acts as a placeholder for all blobs whose names begin with
         the same substring up to the appearance of the delimiter character. The delimiter may be a
         single character or a string.
        :type delimiter: str
        :param marker: A string value that identifies the portion of the list of containers to be
         returned with the next listing operation. The operation returns the NextMarker value within the
         response body if the listing operation did not return all containers remaining to be listed
         with the current page. The NextMarker value can be used as the value for the marker parameter
         in a subsequent call to request the next page of list items. The marker value is opaque to the
         client.
        :type marker: str
        :param max_results: An optional value that specifies the maximum number of items to return. If
         omitted or greater than 5,000, the response will include up to 5,000 items.
        :type max_results: int
        :param include: Include this parameter to specify one or more datasets to include in the
         response.
        :type include: list[str or ~azure.storage.filedatalake.models.ListBlobsIncludeItem]
        :param showonly: Include this parameter to specify one or more datasets to include in the
         response.
        :type showonly: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled.
        :type request_id_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListBlobsHierarchySegmentResponse, or the result of cls(response)
        :rtype: ~azure.storage.filedatalake.models.ListBlobsHierarchySegmentResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ListBlobsHierarchySegmentResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        restype = "container"
        comp = "list"
        accept = "application/xml"

        # Construct URL
        url = self.list_blob_hierarchy_segment.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['restype'] = self._serialize.query("restype", restype, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')
        if prefix is not None:
            query_parameters['prefix'] = self._serialize.query("prefix", prefix, 'str')
        if delimiter is not None:
            query_parameters['delimiter'] = self._serialize.query("delimiter", delimiter, 'str')
        if marker is not None:
            query_parameters['marker'] = self._serialize.query("marker", marker, 'str')
        if max_results is not None:
            query_parameters['maxResults'] = self._serialize.query("max_results", max_results, 'int', minimum=1)
        if include is not None:
            query_parameters['include'] = self._serialize.query("include", include, '[str]', div=',')
        if showonly is not None:
            query_parameters['showonly'] = self._serialize.query("showonly", showonly, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id_parameter is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Content-Type']=self._deserialize('str', response.headers.get('Content-Type'))
        response_headers['x-ms-client-request-id']=self._deserialize('str', response.headers.get('x-ms-client-request-id'))
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
        response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))
        deserialized = self._deserialize('ListBlobsHierarchySegmentResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    list_blob_hierarchy_segment.metadata = {'url': '/{filesystem}'}  # type: ignore
