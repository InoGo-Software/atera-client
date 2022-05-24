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


class ContactApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def contact_delete(self, contact_id, **kwargs):  # noqa: E501
        """Delete specified contact  # noqa: E501

        Deletes the contact. Requires the contact ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_delete(contact_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contact_id: Required - System Contact ID (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.contact_delete_with_http_info(contact_id, **kwargs)  # noqa: E501
        else:
            (data) = self.contact_delete_with_http_info(contact_id, **kwargs)  # noqa: E501
            return data

    def contact_delete_with_http_info(self, contact_id, **kwargs):  # noqa: E501
        """Delete specified contact  # noqa: E501

        Deletes the contact. Requires the contact ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_delete_with_http_info(contact_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contact_id: Required - System Contact ID (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["contact_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method contact_delete" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'contact_id' is set
        if self.api_client.client_side_validation and (
            "contact_id" not in params or params["contact_id"] is None
        ):  # noqa: E501
            raise ValueError("Missing the required parameter `contact_id` when calling `contact_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "contact_id" in params:
            path_params["contactId"] = params["contact_id"]  # noqa: E501

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
            "/api/v3/contacts/{contactId}",
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

    def contact_get(self, **kwargs):  # noqa: E501
        """Find Contacts  # noqa: E501

        Accepts whole or partial emails / phone numbers. If partial, will return all contacts whose emails / phone numbers contain the input string.              <br />              Return Contact List  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Optional - Page index (default is 1), based on items per page
        :param int items_in_page: Optional - Number of items per page (default is 20, max is 50)
        :param str search_options_email:
        :param str search_options_phone:
        :return: APIResultWrapperContactQueryDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.contact_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.contact_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def contact_get_with_http_info(self, **kwargs):  # noqa: E501
        """Find Contacts  # noqa: E501

        Accepts whole or partial emails / phone numbers. If partial, will return all contacts whose emails / phone numbers contain the input string.              <br />              Return Contact List  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Optional - Page index (default is 1), based on items per page
        :param int items_in_page: Optional - Number of items per page (default is 20, max is 50)
        :param str search_options_email:
        :param str search_options_phone:
        :return: APIResultWrapperContactQueryDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["page", "items_in_page", "search_options_email", "search_options_phone"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method contact_get" % key)
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "items_in_page" in params:
            query_params.append(("itemsInPage", params["items_in_page"]))  # noqa: E501
        if "search_options_email" in params:
            query_params.append(("searchOptions.email", params["search_options_email"]))  # noqa: E501
        if "search_options_phone" in params:
            query_params.append(("searchOptions.phone", params["search_options_phone"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "text/json"])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/v3/contacts",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="APIResultWrapperContactQueryDTO",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def contact_get_0(self, contact_id, **kwargs):  # noqa: E501
        """Find specified contact  # noqa: E501

        Returns the specified contact. Requires the contact ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_get_0(contact_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contact_id: Required - System Contact ID (required)
        :return: ContactQueryDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.contact_get_0_with_http_info(contact_id, **kwargs)  # noqa: E501
        else:
            (data) = self.contact_get_0_with_http_info(contact_id, **kwargs)  # noqa: E501
            return data

    def contact_get_0_with_http_info(self, contact_id, **kwargs):  # noqa: E501
        """Find specified contact  # noqa: E501

        Returns the specified contact. Requires the contact ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_get_0_with_http_info(contact_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contact_id: Required - System Contact ID (required)
        :return: ContactQueryDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["contact_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method contact_get_0" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'contact_id' is set
        if self.api_client.client_side_validation and (
            "contact_id" not in params or params["contact_id"] is None
        ):  # noqa: E501
            raise ValueError("Missing the required parameter `contact_id` when calling `contact_get_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "contact_id" in params:
            path_params["contactId"] = params["contact_id"]  # noqa: E501

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
            "/api/v3/contacts/{contactId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ContactQueryDTO",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def contact_post(self, contact, **kwargs):  # noqa: E501
        """Create contact  # noqa: E501

        Creates a new contact for an existing customer. Requires the customer ID or the customer name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_post(contact, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateContactDTO contact: Required - System Contact Object (required)
        :return: Result
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.contact_post_with_http_info(contact, **kwargs)  # noqa: E501
        else:
            (data) = self.contact_post_with_http_info(contact, **kwargs)  # noqa: E501
            return data

    def contact_post_with_http_info(self, contact, **kwargs):  # noqa: E501
        """Create contact  # noqa: E501

        Creates a new contact for an existing customer. Requires the customer ID or the customer name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_post_with_http_info(contact, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateContactDTO contact: Required - System Contact Object (required)
        :return: Result
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["contact"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method contact_post" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'contact' is set
        if self.api_client.client_side_validation and (
            "contact" not in params or params["contact"] is None
        ):  # noqa: E501
            raise ValueError("Missing the required parameter `contact` when calling `contact_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "contact" in params:
            body_params = params["contact"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "text/json"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json", "text/json", "application/xml", "text/xml", "application/x-www-form-urlencoded"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/v3/contacts",
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

    def contact_put(self, contact_id, contact, **kwargs):  # noqa: E501
        """Update specified contact  # noqa: E501

        Updates an existing contact. Requires the contact ID.              <br /><br />               The following fields are editable:              <br /><br />               First Name (Firstname)              <br />              Last Name (Lastname)              <br />               Job Title (JobTitle)              <br />              Is Contact Person (IsContactPerson)              <br />              In Ignore Mode (InIgnoreMode)              <br />              Phone (Phone)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_put(contact_id, contact, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contact_id: Required - System Contact ID (required)
        :param UpdateContactDTO contact: Required - System Contact Object (required)
        :return: Result
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.contact_put_with_http_info(contact_id, contact, **kwargs)  # noqa: E501
        else:
            (data) = self.contact_put_with_http_info(contact_id, contact, **kwargs)  # noqa: E501
            return data

    def contact_put_with_http_info(self, contact_id, contact, **kwargs):  # noqa: E501
        """Update specified contact  # noqa: E501

        Updates an existing contact. Requires the contact ID.              <br /><br />               The following fields are editable:              <br /><br />               First Name (Firstname)              <br />              Last Name (Lastname)              <br />               Job Title (JobTitle)              <br />              Is Contact Person (IsContactPerson)              <br />              In Ignore Mode (InIgnoreMode)              <br />              Phone (Phone)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_put_with_http_info(contact_id, contact, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contact_id: Required - System Contact ID (required)
        :param UpdateContactDTO contact: Required - System Contact Object (required)
        :return: Result
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["contact_id", "contact"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method contact_put" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'contact_id' is set
        if self.api_client.client_side_validation and (
            "contact_id" not in params or params["contact_id"] is None
        ):  # noqa: E501
            raise ValueError("Missing the required parameter `contact_id` when calling `contact_put`")  # noqa: E501
        # verify the required parameter 'contact' is set
        if self.api_client.client_side_validation and (
            "contact" not in params or params["contact"] is None
        ):  # noqa: E501
            raise ValueError("Missing the required parameter `contact` when calling `contact_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "contact_id" in params:
            path_params["contactId"] = params["contact_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "contact" in params:
            body_params = params["contact"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "text/json"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json", "text/json", "application/xml", "text/xml", "application/x-www-form-urlencoded"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/v3/contacts/{contactId}",
            "PUT",
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

    def contact_put_0(self, contact_id, contact, **kwargs):  # noqa: E501
        """Update specified contact  # noqa: E501

        Updates an existing contact. Requires the contact ID.              <br /><br />               The following fields are editable:              <br /><br />               First Name (Firstname)              <br />              Last Name (Lastname)              <br />               Job Title (JobTitle)              <br />              Is Contact Person (IsContactPerson)              <br />              In Ignore Mode (InIgnoreMode)              <br />              Phone (Phone)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_put_0(contact_id, contact, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contact_id: Required - System Contact ID (required)
        :param UpdateContactDTO contact: Required - System Contact Object (required)
        :return: Result
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.contact_put_0_with_http_info(contact_id, contact, **kwargs)  # noqa: E501
        else:
            (data) = self.contact_put_0_with_http_info(contact_id, contact, **kwargs)  # noqa: E501
            return data

    def contact_put_0_with_http_info(self, contact_id, contact, **kwargs):  # noqa: E501
        """Update specified contact  # noqa: E501

        Updates an existing contact. Requires the contact ID.              <br /><br />               The following fields are editable:              <br /><br />               First Name (Firstname)              <br />              Last Name (Lastname)              <br />               Job Title (JobTitle)              <br />              Is Contact Person (IsContactPerson)              <br />              In Ignore Mode (InIgnoreMode)              <br />              Phone (Phone)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_put_0_with_http_info(contact_id, contact, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contact_id: Required - System Contact ID (required)
        :param UpdateContactDTO contact: Required - System Contact Object (required)
        :return: Result
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["contact_id", "contact"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method contact_put_0" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'contact_id' is set
        if self.api_client.client_side_validation and (
            "contact_id" not in params or params["contact_id"] is None
        ):  # noqa: E501
            raise ValueError("Missing the required parameter `contact_id` when calling `contact_put_0`")  # noqa: E501
        # verify the required parameter 'contact' is set
        if self.api_client.client_side_validation and (
            "contact" not in params or params["contact"] is None
        ):  # noqa: E501
            raise ValueError("Missing the required parameter `contact` when calling `contact_put_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "contact_id" in params:
            path_params["contactId"] = params["contact_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "contact" in params:
            body_params = params["contact"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "text/json"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json", "text/json", "application/xml", "text/xml", "application/x-www-form-urlencoded"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/v3/contacts/{contactId}",
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
