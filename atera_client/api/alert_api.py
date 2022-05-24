# coding: utf-8

"""
    Welcome to the Atera API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from atera_client.api_client import ApiClient


class AlertApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def alert_delete(self, alert_id, **kwargs):  # noqa: E501
        """Delete specified alert  # noqa: E501

        Deletes a specified alert. Requires the alert ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alert_delete(alert_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int alert_id: Required - System alert ID (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.alert_delete_with_http_info(alert_id, **kwargs)  # noqa: E501
        else:
            (data) = self.alert_delete_with_http_info(alert_id, **kwargs)  # noqa: E501
            return data

    def alert_delete_with_http_info(self, alert_id, **kwargs):  # noqa: E501
        """Delete specified alert  # noqa: E501

        Deletes a specified alert. Requires the alert ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alert_delete_with_http_info(alert_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int alert_id: Required - System alert ID (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["alert_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method alert_delete" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'alert_id' is set
        if self.api_client.client_side_validation and (
            "alert_id" not in params or params["alert_id"] is None
        ):  # noqa: E501
            raise ValueError("Missing the required parameter `alert_id` when calling `alert_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "alert_id" in params:
            path_params["alertId"] = params["alert_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "text/json", "application/xml", "text/xml"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/v3/alerts/{alertId}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Object",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def alert_get(self, **kwargs):  # noqa: E501
        """Find alerts  # noqa: E501

        Returns a list of alerts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alert_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Optional - Page index, based on items per page (default is 20)
        :param int items_in_page: Optional - Number of items per page (default is 20)
        :param str alert_status:
        :return: APIResultWrapperAlertQueryDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.alert_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.alert_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def alert_get_with_http_info(self, **kwargs):  # noqa: E501
        """Find alerts  # noqa: E501

        Returns a list of alerts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alert_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Optional - Page index, based on items per page (default is 20)
        :param int items_in_page: Optional - Number of items per page (default is 20)
        :param str alert_status:
        :return: APIResultWrapperAlertQueryDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["page", "items_in_page", "alert_status"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method alert_get" % key)
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "items_in_page" in params:
            query_params.append(("itemsInPage", params["items_in_page"]))  # noqa: E501
        if "alert_status" in params:
            query_params.append(("alertStatus", params["alert_status"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "text/json"])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/v3/alerts",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="APIResultWrapperAlertQueryDTO",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def alert_get_0(self, alert_id, **kwargs):  # noqa: E501
        """Find specified alert  # noqa: E501

        Returns an alert. Requires the alert ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alert_get_0(alert_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int alert_id: Required - System alert ID (required)
        :return: AlertQueryDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.alert_get_0_with_http_info(alert_id, **kwargs)  # noqa: E501
        else:
            (data) = self.alert_get_0_with_http_info(alert_id, **kwargs)  # noqa: E501
            return data

    def alert_get_0_with_http_info(self, alert_id, **kwargs):  # noqa: E501
        """Find specified alert  # noqa: E501

        Returns an alert. Requires the alert ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alert_get_0_with_http_info(alert_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int alert_id: Required - System alert ID (required)
        :return: AlertQueryDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["alert_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method alert_get_0" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'alert_id' is set
        if self.api_client.client_side_validation and (
            "alert_id" not in params or params["alert_id"] is None
        ):  # noqa: E501
            raise ValueError("Missing the required parameter `alert_id` when calling `alert_get_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "alert_id" in params:
            path_params["alertId"] = params["alert_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "text/json", "application/xml", "text/xml"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/v3/alerts/{alertId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="AlertQueryDTO",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def alert_post(self, alert, **kwargs):  # noqa: E501
        """Create alert  # noqa: E501

        Creates a new alert. Requires the device's global unique identifier (GUID).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alert_post(alert, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateAlertDTO alert: Required - System alert object (required)
        :return: Result
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.alert_post_with_http_info(alert, **kwargs)  # noqa: E501
        else:
            (data) = self.alert_post_with_http_info(alert, **kwargs)  # noqa: E501
            return data

    def alert_post_with_http_info(self, alert, **kwargs):  # noqa: E501
        """Create alert  # noqa: E501

        Creates a new alert. Requires the device's global unique identifier (GUID).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alert_post_with_http_info(alert, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateAlertDTO alert: Required - System alert object (required)
        :return: Result
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["alert"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method alert_post" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'alert' is set
        if self.api_client.client_side_validation and ("alert" not in params or params["alert"] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `alert` when calling `alert_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "alert" in params:
            body_params = params["alert"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "text/json"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json", "text/json", "application/xml", "text/xml", "application/x-www-form-urlencoded"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/v3/alerts",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Result",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
