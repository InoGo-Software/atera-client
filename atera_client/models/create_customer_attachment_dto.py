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


class CreateCustomerAttachmentDTO(object):
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
    swagger_types = {"customer_id": "int", "name": "str", "content_based64": "str"}

    attribute_map = {"customer_id": "CustomerId", "name": "Name", "content_based64": "ContentBased64"}

    def __init__(self, customer_id=None, name=None, content_based64=None, _configuration=None):  # noqa: E501
        """CreateCustomerAttachmentDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._customer_id = None
        self._name = None
        self._content_based64 = None
        self.discriminator = None

        self.customer_id = customer_id
        self.name = name
        self.content_based64 = content_based64

    @property
    def customer_id(self):
        """Gets the customer_id of this CreateCustomerAttachmentDTO.  # noqa: E501


        :return: The customer_id of this CreateCustomerAttachmentDTO.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CreateCustomerAttachmentDTO.


        :param customer_id: The customer_id of this CreateCustomerAttachmentDTO.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def name(self):
        """Gets the name of this CreateCustomerAttachmentDTO.  # noqa: E501


        :return: The name of this CreateCustomerAttachmentDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCustomerAttachmentDTO.


        :param name: The name of this CreateCustomerAttachmentDTO.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def content_based64(self):
        """Gets the content_based64 of this CreateCustomerAttachmentDTO.  # noqa: E501


        :return: The content_based64 of this CreateCustomerAttachmentDTO.  # noqa: E501
        :rtype: str
        """
        return self._content_based64

    @content_based64.setter
    def content_based64(self, content_based64):
        """Sets the content_based64 of this CreateCustomerAttachmentDTO.


        :param content_based64: The content_based64 of this CreateCustomerAttachmentDTO.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and content_based64 is None:
            raise ValueError("Invalid value for `content_based64`, must not be `None`")  # noqa: E501

        self._content_based64 = content_based64

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
        if issubclass(CreateCustomerAttachmentDTO, dict):
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
        if not isinstance(other, CreateCustomerAttachmentDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateCustomerAttachmentDTO):
            return True

        return self.to_dict() != other.to_dict()
