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


class TcpDeviceQueryDTO(object):
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
        'name': 'str',
        'device_id': 'int',
        'device_guid': 'str',
        'hostname': 'str',
        'customer_id': 'int',
        'customer_name': 'str',
        'folder_id': 'int',
        'monitoring_agent_id': 'int',
        'monitored': 'bool',
        'ports': 'list[PortQueryDTO]'
    }

    attribute_map = {
        'name': 'Name',
        'device_id': 'DeviceID',
        'device_guid': 'DeviceGuid',
        'hostname': 'Hostname',
        'customer_id': 'CustomerID',
        'customer_name': 'CustomerName',
        'folder_id': 'FolderID',
        'monitoring_agent_id': 'MonitoringAgentID',
        'monitored': 'Monitored',
        'ports': 'Ports'
    }

    def __init__(self, name=None, device_id=None, device_guid=None, hostname=None, customer_id=None, customer_name=None, folder_id=None, monitoring_agent_id=None, monitored=None, ports=None, _configuration=None):  # noqa: E501
        """TcpDeviceQueryDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._device_id = None
        self._device_guid = None
        self._hostname = None
        self._customer_id = None
        self._customer_name = None
        self._folder_id = None
        self._monitoring_agent_id = None
        self._monitored = None
        self._ports = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if device_id is not None:
            self.device_id = device_id
        if device_guid is not None:
            self.device_guid = device_guid
        if hostname is not None:
            self.hostname = hostname
        if customer_id is not None:
            self.customer_id = customer_id
        if customer_name is not None:
            self.customer_name = customer_name
        if folder_id is not None:
            self.folder_id = folder_id
        if monitoring_agent_id is not None:
            self.monitoring_agent_id = monitoring_agent_id
        if monitored is not None:
            self.monitored = monitored
        if ports is not None:
            self.ports = ports

    @property
    def name(self):
        """Gets the name of this TcpDeviceQueryDTO.  # noqa: E501


        :return: The name of this TcpDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TcpDeviceQueryDTO.


        :param name: The name of this TcpDeviceQueryDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def device_id(self):
        """Gets the device_id of this TcpDeviceQueryDTO.  # noqa: E501


        :return: The device_id of this TcpDeviceQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this TcpDeviceQueryDTO.


        :param device_id: The device_id of this TcpDeviceQueryDTO.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def device_guid(self):
        """Gets the device_guid of this TcpDeviceQueryDTO.  # noqa: E501


        :return: The device_guid of this TcpDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._device_guid

    @device_guid.setter
    def device_guid(self, device_guid):
        """Sets the device_guid of this TcpDeviceQueryDTO.


        :param device_guid: The device_guid of this TcpDeviceQueryDTO.  # noqa: E501
        :type: str
        """

        self._device_guid = device_guid

    @property
    def hostname(self):
        """Gets the hostname of this TcpDeviceQueryDTO.  # noqa: E501


        :return: The hostname of this TcpDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this TcpDeviceQueryDTO.


        :param hostname: The hostname of this TcpDeviceQueryDTO.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def customer_id(self):
        """Gets the customer_id of this TcpDeviceQueryDTO.  # noqa: E501


        :return: The customer_id of this TcpDeviceQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this TcpDeviceQueryDTO.


        :param customer_id: The customer_id of this TcpDeviceQueryDTO.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def customer_name(self):
        """Gets the customer_name of this TcpDeviceQueryDTO.  # noqa: E501


        :return: The customer_name of this TcpDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this TcpDeviceQueryDTO.


        :param customer_name: The customer_name of this TcpDeviceQueryDTO.  # noqa: E501
        :type: str
        """

        self._customer_name = customer_name

    @property
    def folder_id(self):
        """Gets the folder_id of this TcpDeviceQueryDTO.  # noqa: E501


        :return: The folder_id of this TcpDeviceQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this TcpDeviceQueryDTO.


        :param folder_id: The folder_id of this TcpDeviceQueryDTO.  # noqa: E501
        :type: int
        """

        self._folder_id = folder_id

    @property
    def monitoring_agent_id(self):
        """Gets the monitoring_agent_id of this TcpDeviceQueryDTO.  # noqa: E501


        :return: The monitoring_agent_id of this TcpDeviceQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._monitoring_agent_id

    @monitoring_agent_id.setter
    def monitoring_agent_id(self, monitoring_agent_id):
        """Sets the monitoring_agent_id of this TcpDeviceQueryDTO.


        :param monitoring_agent_id: The monitoring_agent_id of this TcpDeviceQueryDTO.  # noqa: E501
        :type: int
        """

        self._monitoring_agent_id = monitoring_agent_id

    @property
    def monitored(self):
        """Gets the monitored of this TcpDeviceQueryDTO.  # noqa: E501


        :return: The monitored of this TcpDeviceQueryDTO.  # noqa: E501
        :rtype: bool
        """
        return self._monitored

    @monitored.setter
    def monitored(self, monitored):
        """Sets the monitored of this TcpDeviceQueryDTO.


        :param monitored: The monitored of this TcpDeviceQueryDTO.  # noqa: E501
        :type: bool
        """

        self._monitored = monitored

    @property
    def ports(self):
        """Gets the ports of this TcpDeviceQueryDTO.  # noqa: E501


        :return: The ports of this TcpDeviceQueryDTO.  # noqa: E501
        :rtype: list[PortQueryDTO]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this TcpDeviceQueryDTO.


        :param ports: The ports of this TcpDeviceQueryDTO.  # noqa: E501
        :type: list[PortQueryDTO]
        """

        self._ports = ports

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
        if issubclass(TcpDeviceQueryDTO, dict):
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
        if not isinstance(other, TcpDeviceQueryDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TcpDeviceQueryDTO):
            return True

        return self.to_dict() != other.to_dict()
