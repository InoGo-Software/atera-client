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


class CustomFieldQueryDTO(object):
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
    swagger_types = {"name": "str", "data_type": "str", "target": "str", "possible_values": "list[OptionFieldValues]"}

    attribute_map = {"name": "Name", "data_type": "DataType", "target": "Target", "possible_values": "PossibleValues"}

    def __init__(self, name=None, data_type=None, target=None, possible_values=None, _configuration=None):  # noqa: E501
        """CustomFieldQueryDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._data_type = None
        self._target = None
        self._possible_values = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if data_type is not None:
            self.data_type = data_type
        if target is not None:
            self.target = target
        if possible_values is not None:
            self.possible_values = possible_values

    @property
    def name(self):
        """Gets the name of this CustomFieldQueryDTO.  # noqa: E501


        :return: The name of this CustomFieldQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomFieldQueryDTO.


        :param name: The name of this CustomFieldQueryDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def data_type(self):
        """Gets the data_type of this CustomFieldQueryDTO.  # noqa: E501


        :return: The data_type of this CustomFieldQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this CustomFieldQueryDTO.


        :param data_type: The data_type of this CustomFieldQueryDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["Text", "Boolean", "Numeric", "Date", "Options", "OptionsWithDependencies"]  # noqa: E501
        if self._configuration.client_side_validation and data_type not in allowed_values:
            raise ValueError(
                "Invalid value for `data_type` ({0}), must be one of {1}".format(  # noqa: E501
                    data_type, allowed_values
                )
            )

        self._data_type = data_type

    @property
    def target(self):
        """Gets the target of this CustomFieldQueryDTO.  # noqa: E501


        :return: The target of this CustomFieldQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this CustomFieldQueryDTO.


        :param target: The target of this CustomFieldQueryDTO.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Customer",
            "Ticket",
            "Contact",
            "Contract",
            "SLA",
            "Agent",
            "SNMPDevice",
            "TCPDevice",
            "HTTPDevice",
            "GenericDevice",
        ]  # noqa: E501
        if self._configuration.client_side_validation and target not in allowed_values:
            raise ValueError(
                "Invalid value for `target` ({0}), must be one of {1}".format(target, allowed_values)  # noqa: E501
            )

        self._target = target

    @property
    def possible_values(self):
        """Gets the possible_values of this CustomFieldQueryDTO.  # noqa: E501


        :return: The possible_values of this CustomFieldQueryDTO.  # noqa: E501
        :rtype: list[OptionFieldValues]
        """
        return self._possible_values

    @possible_values.setter
    def possible_values(self, possible_values):
        """Sets the possible_values of this CustomFieldQueryDTO.


        :param possible_values: The possible_values of this CustomFieldQueryDTO.  # noqa: E501
        :type: list[OptionFieldValues]
        """

        self._possible_values = possible_values

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
        if issubclass(CustomFieldQueryDTO, dict):
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
        if not isinstance(other, CustomFieldQueryDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomFieldQueryDTO):
            return True

        return self.to_dict() != other.to_dict()
