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


class BlockMoneyContractQueryDTO(object):
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
        'contract_amount': 'RateQueryDTO',
        'primary_rate': 'RateQueryDTO',
        'additional_rates': 'list[RateQueryDTO]',
        'commit_rollover': 'bool',
        'billing_period': 'str'
    }

    attribute_map = {
        'contract_amount': 'ContractAmount',
        'primary_rate': 'PrimaryRate',
        'additional_rates': 'AdditionalRates',
        'commit_rollover': 'CommitRollover',
        'billing_period': 'BillingPeriod'
    }

    def __init__(self, contract_amount=None, primary_rate=None, additional_rates=None, commit_rollover=None, billing_period=None, _configuration=None):  # noqa: E501
        """BlockMoneyContractQueryDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._contract_amount = None
        self._primary_rate = None
        self._additional_rates = None
        self._commit_rollover = None
        self._billing_period = None
        self.discriminator = None

        if contract_amount is not None:
            self.contract_amount = contract_amount
        if primary_rate is not None:
            self.primary_rate = primary_rate
        if additional_rates is not None:
            self.additional_rates = additional_rates
        if commit_rollover is not None:
            self.commit_rollover = commit_rollover
        if billing_period is not None:
            self.billing_period = billing_period

    @property
    def contract_amount(self):
        """Gets the contract_amount of this BlockMoneyContractQueryDTO.  # noqa: E501


        :return: The contract_amount of this BlockMoneyContractQueryDTO.  # noqa: E501
        :rtype: RateQueryDTO
        """
        return self._contract_amount

    @contract_amount.setter
    def contract_amount(self, contract_amount):
        """Sets the contract_amount of this BlockMoneyContractQueryDTO.


        :param contract_amount: The contract_amount of this BlockMoneyContractQueryDTO.  # noqa: E501
        :type: RateQueryDTO
        """

        self._contract_amount = contract_amount

    @property
    def primary_rate(self):
        """Gets the primary_rate of this BlockMoneyContractQueryDTO.  # noqa: E501


        :return: The primary_rate of this BlockMoneyContractQueryDTO.  # noqa: E501
        :rtype: RateQueryDTO
        """
        return self._primary_rate

    @primary_rate.setter
    def primary_rate(self, primary_rate):
        """Sets the primary_rate of this BlockMoneyContractQueryDTO.


        :param primary_rate: The primary_rate of this BlockMoneyContractQueryDTO.  # noqa: E501
        :type: RateQueryDTO
        """

        self._primary_rate = primary_rate

    @property
    def additional_rates(self):
        """Gets the additional_rates of this BlockMoneyContractQueryDTO.  # noqa: E501


        :return: The additional_rates of this BlockMoneyContractQueryDTO.  # noqa: E501
        :rtype: list[RateQueryDTO]
        """
        return self._additional_rates

    @additional_rates.setter
    def additional_rates(self, additional_rates):
        """Sets the additional_rates of this BlockMoneyContractQueryDTO.


        :param additional_rates: The additional_rates of this BlockMoneyContractQueryDTO.  # noqa: E501
        :type: list[RateQueryDTO]
        """

        self._additional_rates = additional_rates

    @property
    def commit_rollover(self):
        """Gets the commit_rollover of this BlockMoneyContractQueryDTO.  # noqa: E501


        :return: The commit_rollover of this BlockMoneyContractQueryDTO.  # noqa: E501
        :rtype: bool
        """
        return self._commit_rollover

    @commit_rollover.setter
    def commit_rollover(self, commit_rollover):
        """Sets the commit_rollover of this BlockMoneyContractQueryDTO.


        :param commit_rollover: The commit_rollover of this BlockMoneyContractQueryDTO.  # noqa: E501
        :type: bool
        """

        self._commit_rollover = commit_rollover

    @property
    def billing_period(self):
        """Gets the billing_period of this BlockMoneyContractQueryDTO.  # noqa: E501


        :return: The billing_period of this BlockMoneyContractQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this BlockMoneyContractQueryDTO.


        :param billing_period: The billing_period of this BlockMoneyContractQueryDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["EndOfContractDuration", "Weekly", "BiWeekly", "Monthly", "Quarterly", "TwiceAYear", "Yearly", "OnDemand"]  # noqa: E501
        if (self._configuration.client_side_validation and
                billing_period not in allowed_values):
            raise ValueError(
                "Invalid value for `billing_period` ({0}), must be one of {1}"  # noqa: E501
                .format(billing_period, allowed_values)
            )

        self._billing_period = billing_period

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
        if issubclass(BlockMoneyContractQueryDTO, dict):
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
        if not isinstance(other, BlockMoneyContractQueryDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlockMoneyContractQueryDTO):
            return True

        return self.to_dict() != other.to_dict()
