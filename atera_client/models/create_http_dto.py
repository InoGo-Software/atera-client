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


class CreateHttpDTO(object):
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
        'url': 'str',
        'pattern': 'str',
        'name': 'str',
        'customer_id': 'int',
        'folder_id': 'int',
        'monitoring_agent_id': 'int',
        'monitored': 'bool'
    }

    attribute_map = {
        'url': 'URL',
        'pattern': 'Pattern',
        'name': 'Name',
        'customer_id': 'CustomerID',
        'folder_id': 'FolderID',
        'monitoring_agent_id': 'MonitoringAgentID',
        'monitored': 'Monitored'
    }

    def __init__(self, url=None, pattern=None, name=None, customer_id=None, folder_id=None, monitoring_agent_id=None, monitored=None, _configuration=None):  # noqa: E501
        """CreateHttpDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._url = None
        self._pattern = None
        self._name = None
        self._customer_id = None
        self._folder_id = None
        self._monitoring_agent_id = None
        self._monitored = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if pattern is not None:
            self.pattern = pattern
        if name is not None:
            self.name = name
        if customer_id is not None:
            self.customer_id = customer_id
        if folder_id is not None:
            self.folder_id = folder_id
        if monitoring_agent_id is not None:
            self.monitoring_agent_id = monitoring_agent_id
        if monitored is not None:
            self.monitored = monitored

    @property
    def url(self):
        """Gets the url of this CreateHttpDTO.  # noqa: E501


        :return: The url of this CreateHttpDTO.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateHttpDTO.


        :param url: The url of this CreateHttpDTO.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def pattern(self):
        """Gets the pattern of this CreateHttpDTO.  # noqa: E501


        :return: The pattern of this CreateHttpDTO.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this CreateHttpDTO.


        :param pattern: The pattern of this CreateHttpDTO.  # noqa: E501
        :type: str
        """

        self._pattern = pattern

    @property
    def name(self):
        """Gets the name of this CreateHttpDTO.  # noqa: E501


        :return: The name of this CreateHttpDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateHttpDTO.


        :param name: The name of this CreateHttpDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def customer_id(self):
        """Gets the customer_id of this CreateHttpDTO.  # noqa: E501


        :return: The customer_id of this CreateHttpDTO.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CreateHttpDTO.


        :param customer_id: The customer_id of this CreateHttpDTO.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def folder_id(self):
        """Gets the folder_id of this CreateHttpDTO.  # noqa: E501


        :return: The folder_id of this CreateHttpDTO.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this CreateHttpDTO.


        :param folder_id: The folder_id of this CreateHttpDTO.  # noqa: E501
        :type: int
        """

        self._folder_id = folder_id

    @property
    def monitoring_agent_id(self):
        """Gets the monitoring_agent_id of this CreateHttpDTO.  # noqa: E501


        :return: The monitoring_agent_id of this CreateHttpDTO.  # noqa: E501
        :rtype: int
        """
        return self._monitoring_agent_id

    @monitoring_agent_id.setter
    def monitoring_agent_id(self, monitoring_agent_id):
        """Sets the monitoring_agent_id of this CreateHttpDTO.


        :param monitoring_agent_id: The monitoring_agent_id of this CreateHttpDTO.  # noqa: E501
        :type: int
        """

        self._monitoring_agent_id = monitoring_agent_id

    @property
    def monitored(self):
        """Gets the monitored of this CreateHttpDTO.  # noqa: E501


        :return: The monitored of this CreateHttpDTO.  # noqa: E501
        :rtype: bool
        """
        return self._monitored

    @monitored.setter
    def monitored(self, monitored):
        """Sets the monitored of this CreateHttpDTO.


        :param monitored: The monitored of this CreateHttpDTO.  # noqa: E501
        :type: bool
        """

        self._monitored = monitored

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CreateHttpDTO, dict):
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
        if not isinstance(other, CreateHttpDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateHttpDTO):
            return True

        return self.to_dict() != other.to_dict()