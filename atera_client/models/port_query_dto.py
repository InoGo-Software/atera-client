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


class PortQueryDTO(object):
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
    swagger_types = {"port_number": "int", "monitored": "bool", "available": "bool"}

    attribute_map = {"port_number": "PortNumber", "monitored": "Monitored", "available": "Available"}

    def __init__(self, port_number=None, monitored=None, available=None, _configuration=None):  # noqa: E501
        """PortQueryDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._port_number = None
        self._monitored = None
        self._available = None
        self.discriminator = None

        if port_number is not None:
            self.port_number = port_number
        if monitored is not None:
            self.monitored = monitored
        if available is not None:
            self.available = available

    @property
    def port_number(self):
        """Gets the port_number of this PortQueryDTO.  # noqa: E501


        :return: The port_number of this PortQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._port_number

    @port_number.setter
    def port_number(self, port_number):
        """Sets the port_number of this PortQueryDTO.


        :param port_number: The port_number of this PortQueryDTO.  # noqa: E501
        :type: int
        """

        self._port_number = port_number

    @property
    def monitored(self):
        """Gets the monitored of this PortQueryDTO.  # noqa: E501


        :return: The monitored of this PortQueryDTO.  # noqa: E501
        :rtype: bool
        """
        return self._monitored

    @monitored.setter
    def monitored(self, monitored):
        """Sets the monitored of this PortQueryDTO.


        :param monitored: The monitored of this PortQueryDTO.  # noqa: E501
        :type: bool
        """

        self._monitored = monitored

    @property
    def available(self):
        """Gets the available of this PortQueryDTO.  # noqa: E501


        :return: The available of this PortQueryDTO.  # noqa: E501
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this PortQueryDTO.


        :param available: The available of this PortQueryDTO.  # noqa: E501
        :type: bool
        """

        self._available = available

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
        if issubclass(PortQueryDTO, dict):
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
        if not isinstance(other, PortQueryDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortQueryDTO):
            return True

        return self.to_dict() != other.to_dict()
