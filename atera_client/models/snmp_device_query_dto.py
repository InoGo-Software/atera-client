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


class SNMPDeviceQueryDTO(object):
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
        'customer_id': 'int',
        'customer_name': 'str',
        'folder_id': 'int',
        'hostname': 'str',
        'online': 'bool',
        'port': 'str',
        'community': 'str',
        'type': 'str',
        'version': 'str',
        'security_level': 'str',
        'authentication': 'str',
        'privacy': 'str',
        'monitored': 'bool',
        'monitoring_agent_id': 'int'
    }

    attribute_map = {
        'name': 'Name',
        'device_id': 'DeviceID',
        'device_guid': 'DeviceGuid',
        'customer_id': 'CustomerID',
        'customer_name': 'CustomerName',
        'folder_id': 'FolderID',
        'hostname': 'Hostname',
        'online': 'Online',
        'port': 'Port',
        'community': 'Community',
        'type': 'Type',
        'version': 'Version',
        'security_level': 'SecurityLevel',
        'authentication': 'Authentication',
        'privacy': 'Privacy',
        'monitored': 'Monitored',
        'monitoring_agent_id': 'MonitoringAgentID'
    }

    def __init__(self, name=None, device_id=None, device_guid=None, customer_id=None, customer_name=None, folder_id=None, hostname=None, online=None, port=None, community=None, type=None, version=None, security_level=None, authentication=None, privacy=None, monitored=None, monitoring_agent_id=None, _configuration=None):  # noqa: E501
        """SNMPDeviceQueryDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._device_id = None
        self._device_guid = None
        self._customer_id = None
        self._customer_name = None
        self._folder_id = None
        self._hostname = None
        self._online = None
        self._port = None
        self._community = None
        self._type = None
        self._version = None
        self._security_level = None
        self._authentication = None
        self._privacy = None
        self._monitored = None
        self._monitoring_agent_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if device_id is not None:
            self.device_id = device_id
        if device_guid is not None:
            self.device_guid = device_guid
        if customer_id is not None:
            self.customer_id = customer_id
        if customer_name is not None:
            self.customer_name = customer_name
        if folder_id is not None:
            self.folder_id = folder_id
        if hostname is not None:
            self.hostname = hostname
        if online is not None:
            self.online = online
        if port is not None:
            self.port = port
        if community is not None:
            self.community = community
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if security_level is not None:
            self.security_level = security_level
        if authentication is not None:
            self.authentication = authentication
        if privacy is not None:
            self.privacy = privacy
        if monitored is not None:
            self.monitored = monitored
        if monitoring_agent_id is not None:
            self.monitoring_agent_id = monitoring_agent_id

    @property
    def name(self):
        """Gets the name of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The name of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SNMPDeviceQueryDTO.


        :param name: The name of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def device_id(self):
        """Gets the device_id of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The device_id of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this SNMPDeviceQueryDTO.


        :param device_id: The device_id of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def device_guid(self):
        """Gets the device_guid of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The device_guid of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._device_guid

    @device_guid.setter
    def device_guid(self, device_guid):
        """Sets the device_guid of this SNMPDeviceQueryDTO.


        :param device_guid: The device_guid of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: str
        """

        self._device_guid = device_guid

    @property
    def customer_id(self):
        """Gets the customer_id of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The customer_id of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this SNMPDeviceQueryDTO.


        :param customer_id: The customer_id of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def customer_name(self):
        """Gets the customer_name of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The customer_name of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this SNMPDeviceQueryDTO.


        :param customer_name: The customer_name of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: str
        """

        self._customer_name = customer_name

    @property
    def folder_id(self):
        """Gets the folder_id of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The folder_id of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this SNMPDeviceQueryDTO.


        :param folder_id: The folder_id of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: int
        """

        self._folder_id = folder_id

    @property
    def hostname(self):
        """Gets the hostname of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The hostname of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this SNMPDeviceQueryDTO.


        :param hostname: The hostname of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def online(self):
        """Gets the online of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The online of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this SNMPDeviceQueryDTO.


        :param online: The online of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: bool
        """

        self._online = online

    @property
    def port(self):
        """Gets the port of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The port of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SNMPDeviceQueryDTO.


        :param port: The port of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def community(self):
        """Gets the community of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The community of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._community

    @community.setter
    def community(self, community):
        """Sets the community of this SNMPDeviceQueryDTO.


        :param community: The community of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: str
        """

        self._community = community

    @property
    def type(self):
        """Gets the type of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The type of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SNMPDeviceQueryDTO.


        :param type: The type of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The version of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SNMPDeviceQueryDTO.


        :param version: The version of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def security_level(self):
        """Gets the security_level of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The security_level of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        """Sets the security_level of this SNMPDeviceQueryDTO.


        :param security_level: The security_level of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["Undefined", "Authentication", "AuthenticationAndPrivacy"]  # noqa: E501
        if (self._configuration.client_side_validation and
                security_level not in allowed_values):
            raise ValueError(
                "Invalid value for `security_level` ({0}), must be one of {1}"  # noqa: E501
                .format(security_level, allowed_values)
            )

        self._security_level = security_level

    @property
    def authentication(self):
        """Gets the authentication of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The authentication of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this SNMPDeviceQueryDTO.


        :param authentication: The authentication of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: str
        """

        self._authentication = authentication

    @property
    def privacy(self):
        """Gets the privacy of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The privacy of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """Sets the privacy of this SNMPDeviceQueryDTO.


        :param privacy: The privacy of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: str
        """

        self._privacy = privacy

    @property
    def monitored(self):
        """Gets the monitored of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The monitored of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: bool
        """
        return self._monitored

    @monitored.setter
    def monitored(self, monitored):
        """Sets the monitored of this SNMPDeviceQueryDTO.


        :param monitored: The monitored of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: bool
        """

        self._monitored = monitored

    @property
    def monitoring_agent_id(self):
        """Gets the monitoring_agent_id of this SNMPDeviceQueryDTO.  # noqa: E501


        :return: The monitoring_agent_id of this SNMPDeviceQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._monitoring_agent_id

    @monitoring_agent_id.setter
    def monitoring_agent_id(self, monitoring_agent_id):
        """Sets the monitoring_agent_id of this SNMPDeviceQueryDTO.


        :param monitoring_agent_id: The monitoring_agent_id of this SNMPDeviceQueryDTO.  # noqa: E501
        :type: int
        """

        self._monitoring_agent_id = monitoring_agent_id

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
        if issubclass(SNMPDeviceQueryDTO, dict):
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
        if not isinstance(other, SNMPDeviceQueryDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SNMPDeviceQueryDTO):
            return True

        return self.to_dict() != other.to_dict()