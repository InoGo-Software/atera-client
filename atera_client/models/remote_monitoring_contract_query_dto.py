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


class RemoteMonitoringContractQueryDTO(object):
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
    swagger_types = {"rate_per_device": "RateQueryDTO", "count_by": "str", "billing_period": "str"}

    attribute_map = {"rate_per_device": "RatePerDevice", "count_by": "CountBy", "billing_period": "BillingPeriod"}

    def __init__(self, rate_per_device=None, count_by=None, billing_period=None, _configuration=None):  # noqa: E501
        """RemoteMonitoringContractQueryDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._rate_per_device = None
        self._count_by = None
        self._billing_period = None
        self.discriminator = None

        if rate_per_device is not None:
            self.rate_per_device = rate_per_device
        if count_by is not None:
            self.count_by = count_by
        if billing_period is not None:
            self.billing_period = billing_period

    @property
    def rate_per_device(self):
        """Gets the rate_per_device of this RemoteMonitoringContractQueryDTO.  # noqa: E501


        :return: The rate_per_device of this RemoteMonitoringContractQueryDTO.  # noqa: E501
        :rtype: RateQueryDTO
        """
        return self._rate_per_device

    @rate_per_device.setter
    def rate_per_device(self, rate_per_device):
        """Sets the rate_per_device of this RemoteMonitoringContractQueryDTO.


        :param rate_per_device: The rate_per_device of this RemoteMonitoringContractQueryDTO.  # noqa: E501
        :type: RateQueryDTO
        """

        self._rate_per_device = rate_per_device

    @property
    def count_by(self):
        """Gets the count_by of this RemoteMonitoringContractQueryDTO.  # noqa: E501


        :return: The count_by of this RemoteMonitoringContractQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._count_by

    @count_by.setter
    def count_by(self, count_by):
        """Sets the count_by of this RemoteMonitoringContractQueryDTO.


        :param count_by: The count_by of this RemoteMonitoringContractQueryDTO.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "PCAgents",
            "MacAgents",
            "ServerAgents",
            "OtherDevices",
            "AgentsOnly",
            "All",
            "PCsTotalGB",
            "ServersTotalGB",
            "TotalGB",
        ]  # noqa: E501
        if self._configuration.client_side_validation and count_by not in allowed_values:
            raise ValueError(
                "Invalid value for `count_by` ({0}), must be one of {1}".format(count_by, allowed_values)  # noqa: E501
            )

        self._count_by = count_by

    @property
    def billing_period(self):
        """Gets the billing_period of this RemoteMonitoringContractQueryDTO.  # noqa: E501


        :return: The billing_period of this RemoteMonitoringContractQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this RemoteMonitoringContractQueryDTO.


        :param billing_period: The billing_period of this RemoteMonitoringContractQueryDTO.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "EndOfContractDuration",
            "Weekly",
            "BiWeekly",
            "Monthly",
            "Quarterly",
            "TwiceAYear",
            "Yearly",
            "OnDemand",
        ]  # noqa: E501
        if self._configuration.client_side_validation and billing_period not in allowed_values:
            raise ValueError(
                "Invalid value for `billing_period` ({0}), must be one of {1}".format(  # noqa: E501
                    billing_period, allowed_values
                )
            )

        self._billing_period = billing_period

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
        if issubclass(RemoteMonitoringContractQueryDTO, dict):
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
        if not isinstance(other, RemoteMonitoringContractQueryDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoteMonitoringContractQueryDTO):
            return True

        return self.to_dict() != other.to_dict()
