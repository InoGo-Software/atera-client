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


class BlockHoursContractQueryDTO(object):
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
        "hours_included": "float",
        "price_per_hour": "RateQueryDTO",
        "overage_rate": "RateQueryDTO",
        "commit_rollover": "bool",
        "billing_period": "str",
    }

    attribute_map = {
        "hours_included": "HoursIncluded",
        "price_per_hour": "PricePerHour",
        "overage_rate": "OverageRate",
        "commit_rollover": "CommitRollover",
        "billing_period": "BillingPeriod",
    }

    def __init__(
        self,
        hours_included=None,
        price_per_hour=None,
        overage_rate=None,
        commit_rollover=None,
        billing_period=None,
        _configuration=None,
    ):  # noqa: E501
        """BlockHoursContractQueryDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._hours_included = None
        self._price_per_hour = None
        self._overage_rate = None
        self._commit_rollover = None
        self._billing_period = None
        self.discriminator = None

        if hours_included is not None:
            self.hours_included = hours_included
        if price_per_hour is not None:
            self.price_per_hour = price_per_hour
        if overage_rate is not None:
            self.overage_rate = overage_rate
        if commit_rollover is not None:
            self.commit_rollover = commit_rollover
        if billing_period is not None:
            self.billing_period = billing_period

    @property
    def hours_included(self):
        """Gets the hours_included of this BlockHoursContractQueryDTO.  # noqa: E501


        :return: The hours_included of this BlockHoursContractQueryDTO.  # noqa: E501
        :rtype: float
        """
        return self._hours_included

    @hours_included.setter
    def hours_included(self, hours_included):
        """Sets the hours_included of this BlockHoursContractQueryDTO.


        :param hours_included: The hours_included of this BlockHoursContractQueryDTO.  # noqa: E501
        :type: float
        """

        self._hours_included = hours_included

    @property
    def price_per_hour(self):
        """Gets the price_per_hour of this BlockHoursContractQueryDTO.  # noqa: E501


        :return: The price_per_hour of this BlockHoursContractQueryDTO.  # noqa: E501
        :rtype: RateQueryDTO
        """
        return self._price_per_hour

    @price_per_hour.setter
    def price_per_hour(self, price_per_hour):
        """Sets the price_per_hour of this BlockHoursContractQueryDTO.


        :param price_per_hour: The price_per_hour of this BlockHoursContractQueryDTO.  # noqa: E501
        :type: RateQueryDTO
        """

        self._price_per_hour = price_per_hour

    @property
    def overage_rate(self):
        """Gets the overage_rate of this BlockHoursContractQueryDTO.  # noqa: E501


        :return: The overage_rate of this BlockHoursContractQueryDTO.  # noqa: E501
        :rtype: RateQueryDTO
        """
        return self._overage_rate

    @overage_rate.setter
    def overage_rate(self, overage_rate):
        """Sets the overage_rate of this BlockHoursContractQueryDTO.


        :param overage_rate: The overage_rate of this BlockHoursContractQueryDTO.  # noqa: E501
        :type: RateQueryDTO
        """

        self._overage_rate = overage_rate

    @property
    def commit_rollover(self):
        """Gets the commit_rollover of this BlockHoursContractQueryDTO.  # noqa: E501


        :return: The commit_rollover of this BlockHoursContractQueryDTO.  # noqa: E501
        :rtype: bool
        """
        return self._commit_rollover

    @commit_rollover.setter
    def commit_rollover(self, commit_rollover):
        """Sets the commit_rollover of this BlockHoursContractQueryDTO.


        :param commit_rollover: The commit_rollover of this BlockHoursContractQueryDTO.  # noqa: E501
        :type: bool
        """

        self._commit_rollover = commit_rollover

    @property
    def billing_period(self):
        """Gets the billing_period of this BlockHoursContractQueryDTO.  # noqa: E501


        :return: The billing_period of this BlockHoursContractQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this BlockHoursContractQueryDTO.


        :param billing_period: The billing_period of this BlockHoursContractQueryDTO.  # noqa: E501
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
        if issubclass(BlockHoursContractQueryDTO, dict):
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
        if not isinstance(other, BlockHoursContractQueryDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlockHoursContractQueryDTO):
            return True

        return self.to_dict() != other.to_dict()
