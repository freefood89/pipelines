# coding: utf-8

"""
    Kubeflow Pipelines API

    This file contains REST API specification for Kubeflow Pipelines. The file is autogenerated from the swagger definition.

    Contact: kubeflow-pipelines@google.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from kfp_server_api.api_client import ApiClient
from kfp_server_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RecurringRunServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_recurring_run(self, body, **kwargs):  # noqa: E501
        """Creates a new recurring run in an experiment, given the experiment ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_recurring_run(body, async_req=True)
        >>> result = thread.get()

        :param body: The recurring run to be created. (required)
        :type body: V2beta1RecurringRun
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: V2beta1RecurringRun
        """
        kwargs['_return_http_data_only'] = True
        return self.create_recurring_run_with_http_info(body, **kwargs)  # noqa: E501

    def create_recurring_run_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates a new recurring run in an experiment, given the experiment ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_recurring_run_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param body: The recurring run to be created. (required)
        :type body: V2beta1RecurringRun
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(V2beta1RecurringRun, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_recurring_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in local_var_params or  # noqa: E501
                                                        local_var_params['body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `body` when calling `create_recurring_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/apis/v2beta1/recurringruns', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V2beta1RecurringRun',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_recurring_run(self, recurring_run_id, **kwargs):  # noqa: E501
        """Deletes a recurring run.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_recurring_run(recurring_run_id, async_req=True)
        >>> result = thread.get()

        :param recurring_run_id: The ID of the recurring run to be deleted. (required)
        :type recurring_run_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_recurring_run_with_http_info(recurring_run_id, **kwargs)  # noqa: E501

    def delete_recurring_run_with_http_info(self, recurring_run_id, **kwargs):  # noqa: E501
        """Deletes a recurring run.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_recurring_run_with_http_info(recurring_run_id, async_req=True)
        >>> result = thread.get()

        :param recurring_run_id: The ID of the recurring run to be deleted. (required)
        :type recurring_run_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'recurring_run_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_recurring_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'recurring_run_id' is set
        if self.api_client.client_side_validation and ('recurring_run_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['recurring_run_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `recurring_run_id` when calling `delete_recurring_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'recurring_run_id' in local_var_params:
            path_params['recurring_run_id'] = local_var_params['recurring_run_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/apis/v2beta1/recurringruns/{recurring_run_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def disable_recurring_run(self, recurring_run_id, **kwargs):  # noqa: E501
        """Stops a recurring run and all its associated runs. The recurring run is not deleted.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.disable_recurring_run(recurring_run_id, async_req=True)
        >>> result = thread.get()

        :param recurring_run_id: The ID of the recurring runs to be disabled. (required)
        :type recurring_run_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.disable_recurring_run_with_http_info(recurring_run_id, **kwargs)  # noqa: E501

    def disable_recurring_run_with_http_info(self, recurring_run_id, **kwargs):  # noqa: E501
        """Stops a recurring run and all its associated runs. The recurring run is not deleted.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.disable_recurring_run_with_http_info(recurring_run_id, async_req=True)
        >>> result = thread.get()

        :param recurring_run_id: The ID of the recurring runs to be disabled. (required)
        :type recurring_run_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'recurring_run_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method disable_recurring_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'recurring_run_id' is set
        if self.api_client.client_side_validation and ('recurring_run_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['recurring_run_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `recurring_run_id` when calling `disable_recurring_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'recurring_run_id' in local_var_params:
            path_params['recurring_run_id'] = local_var_params['recurring_run_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/apis/v2beta1/recurringruns/{recurring_run_id}:disable', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def enable_recurring_run(self, recurring_run_id, **kwargs):  # noqa: E501
        """Restarts a recurring run that was previously stopped. All runs associated with the  recurring run will continue.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.enable_recurring_run(recurring_run_id, async_req=True)
        >>> result = thread.get()

        :param recurring_run_id: The ID of the recurring runs to be enabled. (required)
        :type recurring_run_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.enable_recurring_run_with_http_info(recurring_run_id, **kwargs)  # noqa: E501

    def enable_recurring_run_with_http_info(self, recurring_run_id, **kwargs):  # noqa: E501
        """Restarts a recurring run that was previously stopped. All runs associated with the  recurring run will continue.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.enable_recurring_run_with_http_info(recurring_run_id, async_req=True)
        >>> result = thread.get()

        :param recurring_run_id: The ID of the recurring runs to be enabled. (required)
        :type recurring_run_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'recurring_run_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enable_recurring_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'recurring_run_id' is set
        if self.api_client.client_side_validation and ('recurring_run_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['recurring_run_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `recurring_run_id` when calling `enable_recurring_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'recurring_run_id' in local_var_params:
            path_params['recurring_run_id'] = local_var_params['recurring_run_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/apis/v2beta1/recurringruns/{recurring_run_id}:enable', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_recurring_run(self, recurring_run_id, **kwargs):  # noqa: E501
        """Finds a specific recurring run by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_recurring_run(recurring_run_id, async_req=True)
        >>> result = thread.get()

        :param recurring_run_id: The ID of the recurring run to be retrieved. (required)
        :type recurring_run_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: V2beta1RecurringRun
        """
        kwargs['_return_http_data_only'] = True
        return self.get_recurring_run_with_http_info(recurring_run_id, **kwargs)  # noqa: E501

    def get_recurring_run_with_http_info(self, recurring_run_id, **kwargs):  # noqa: E501
        """Finds a specific recurring run by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_recurring_run_with_http_info(recurring_run_id, async_req=True)
        >>> result = thread.get()

        :param recurring_run_id: The ID of the recurring run to be retrieved. (required)
        :type recurring_run_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(V2beta1RecurringRun, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'recurring_run_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_recurring_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'recurring_run_id' is set
        if self.api_client.client_side_validation and ('recurring_run_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['recurring_run_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `recurring_run_id` when calling `get_recurring_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'recurring_run_id' in local_var_params:
            path_params['recurring_run_id'] = local_var_params['recurring_run_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/apis/v2beta1/recurringruns/{recurring_run_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V2beta1RecurringRun',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_recurring_runs(self, **kwargs):  # noqa: E501
        """Finds all recurring runs given experiment and namespace.  If experiment ID is not specified, find all recurring runs across all experiments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_recurring_runs(async_req=True)
        >>> result = thread.get()

        :param page_token: A page token to request the next page of results. The token is acquired from the nextPageToken field of the response from the previous ListRecurringRuns call or can be omitted when fetching the first page.
        :type page_token: str
        :param page_size: The number of recurring runs to be listed per page. If there are more recurring runs  than this number, the response message will contain a nextPageToken field you can use to fetch the next page.
        :type page_size: int
        :param sort_by: Can be formatted as \"field_name\", \"field_name asc\" or \"field_name desc\". Ascending by default.
        :type sort_by: str
        :param namespace: Optional input. The namespace the recurring runs belong to.
        :type namespace: str
        :param filter: A url-encoded, JSON-serialized Filter protocol buffer (see [filter.proto](https://github.com/kubeflow/pipelines/blob/master/backend/api/filter.proto)).
        :type filter: str
        :param experiment_id: The ID of the experiment to be retrieved. If empty, list recurring runs across all experiments.
        :type experiment_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: V2beta1ListRecurringRunsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.list_recurring_runs_with_http_info(**kwargs)  # noqa: E501

    def list_recurring_runs_with_http_info(self, **kwargs):  # noqa: E501
        """Finds all recurring runs given experiment and namespace.  If experiment ID is not specified, find all recurring runs across all experiments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_recurring_runs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param page_token: A page token to request the next page of results. The token is acquired from the nextPageToken field of the response from the previous ListRecurringRuns call or can be omitted when fetching the first page.
        :type page_token: str
        :param page_size: The number of recurring runs to be listed per page. If there are more recurring runs  than this number, the response message will contain a nextPageToken field you can use to fetch the next page.
        :type page_size: int
        :param sort_by: Can be formatted as \"field_name\", \"field_name asc\" or \"field_name desc\". Ascending by default.
        :type sort_by: str
        :param namespace: Optional input. The namespace the recurring runs belong to.
        :type namespace: str
        :param filter: A url-encoded, JSON-serialized Filter protocol buffer (see [filter.proto](https://github.com/kubeflow/pipelines/blob/master/backend/api/filter.proto)).
        :type filter: str
        :param experiment_id: The ID of the experiment to be retrieved. If empty, list recurring runs across all experiments.
        :type experiment_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(V2beta1ListRecurringRunsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'page_token',
            'page_size',
            'sort_by',
            'namespace',
            'filter',
            'experiment_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_recurring_runs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_token' in local_var_params and local_var_params['page_token'] is not None:  # noqa: E501
            query_params.append(('page_token', local_var_params['page_token']))  # noqa: E501
        if 'page_size' in local_var_params and local_var_params['page_size'] is not None:  # noqa: E501
            query_params.append(('page_size', local_var_params['page_size']))  # noqa: E501
        if 'sort_by' in local_var_params and local_var_params['sort_by'] is not None:  # noqa: E501
            query_params.append(('sort_by', local_var_params['sort_by']))  # noqa: E501
        if 'namespace' in local_var_params and local_var_params['namespace'] is not None:  # noqa: E501
            query_params.append(('namespace', local_var_params['namespace']))  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'experiment_id' in local_var_params and local_var_params['experiment_id'] is not None:  # noqa: E501
            query_params.append(('experiment_id', local_var_params['experiment_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/apis/v2beta1/recurringruns', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V2beta1ListRecurringRunsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)