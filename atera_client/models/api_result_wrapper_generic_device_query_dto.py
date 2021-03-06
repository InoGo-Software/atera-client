# coding: utf-8

"""
    Welcome to the Atera API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from atera_client.configuration import Configuration


class APIResultWrapperGenericDeviceQueryDTO(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "items": "list[GenericDeviceQueryDTO]",
        "total_item_count": "int",
        "page": "int",
        "items_in_page": "int",
        "total_pages": "int",
        "prev_link": "str",
        "next_link": "str",
    }

    attribute_map = {
        "items": "items",
        "total_item_count": "totalItemCount",
        "page": "page",
        "items_in_page": "itemsInPage",
        "total_pages": "totalPages",
        "prev_link": "prevLink",
        "next_link": "nextLink",
    }

    def __init__(
        self,
        items=None,
        total_item_count=None,
        page=None,
        items_in_page=None,
        total_pages=None,
        prev_link=None,
        next_link=None,
        _configuration=None,
    ):  # noqa: E501
        """APIResultWrapperGenericDeviceQueryDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._items = None
        self._total_item_count = None
        self._page = None
        self._items_in_page = None
        self._total_pages = None
        self._prev_link = None
        self._next_link = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if total_item_count is not None:
            self.total_item_count = total_item_count
        if page is not None:
            self.page = page
        if items_in_page is not None:
            self.items_in_page = items_in_page
        if total_pages is not None:
            self.total_pages = total_pages
        if prev_link is not None:
            self.prev_link = prev_link
        if next_link is not None:
            self.next_link = next_link

    @property
    def items(self):
        """Gets the items of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501


        :return: The items of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501
        :rtype: list[GenericDeviceQueryDTO]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this APIResultWrapperGenericDeviceQueryDTO.


        :param items: The items of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501
        :type: list[GenericDeviceQueryDTO]
        """

        self._items = items

    @property
    def total_item_count(self):
        """Gets the total_item_count of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501


        :return: The total_item_count of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._total_item_count

    @total_item_count.setter
    def total_item_count(self, total_item_count):
        """Sets the total_item_count of this APIResultWrapperGenericDeviceQueryDTO.


        :param total_item_count: The total_item_count of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501
        :type: int
        """

        self._total_item_count = total_item_count

    @property
    def page(self):
        """Gets the page of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501

        The current page.  # noqa: E501

        :return: The page of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this APIResultWrapperGenericDeviceQueryDTO.

        The current page.  # noqa: E501

        :param page: The page of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def items_in_page(self):
        """Gets the items_in_page of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501

        The size of the page.  # noqa: E501

        :return: The items_in_page of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._items_in_page

    @items_in_page.setter
    def items_in_page(self, items_in_page):
        """Sets the items_in_page of this APIResultWrapperGenericDeviceQueryDTO.

        The size of the page.  # noqa: E501

        :param items_in_page: The items_in_page of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501
        :type: int
        """

        self._items_in_page = items_in_page

    @property
    def total_pages(self):
        """Gets the total_pages of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501

        Total count of pages in query  # noqa: E501

        :return: The total_pages of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this APIResultWrapperGenericDeviceQueryDTO.

        Total count of pages in query  # noqa: E501

        :param total_pages: The total_pages of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    @property
    def prev_link(self):
        """Gets the prev_link of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501

        Previous query url link (if exists)  # noqa: E501

        :return: The prev_link of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._prev_link

    @prev_link.setter
    def prev_link(self, prev_link):
        """Sets the prev_link of this APIResultWrapperGenericDeviceQueryDTO.

        Previous query url link (if exists)  # noqa: E501

        :param prev_link: The prev_link of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501
        :type: str
        """

        self._prev_link = prev_link

    @property
    def next_link(self):
        """Gets the next_link of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501

        Next query url link (if exists)  # noqa: E501

        :return: The next_link of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this APIResultWrapperGenericDeviceQueryDTO.

        Next query url link (if exists)  # noqa: E501

        :param next_link: The next_link of this APIResultWrapperGenericDeviceQueryDTO.  # noqa: E501
        :type: str
        """

        self._next_link = next_link

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(APIResultWrapperGenericDeviceQueryDTO, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, APIResultWrapperGenericDeviceQueryDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIResultWrapperGenericDeviceQueryDTO):
            return True

        return self.to_dict() != other.to_dict()
