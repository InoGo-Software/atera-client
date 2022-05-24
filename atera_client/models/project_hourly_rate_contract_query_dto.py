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


class ProjectHourlyRateContractQueryDTO(object):
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
        'primary_rate': 'RateQueryDTO',
        'additional_rates': 'list[RateQueryDTO]'
    }

    attribute_map = {
        'primary_rate': 'PrimaryRate',
        'additional_rates': 'AdditionalRates'
    }

    def __init__(self, primary_rate=None, additional_rates=None, _configuration=None):  # noqa: E501
        """ProjectHourlyRateContractQueryDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._primary_rate = None
        self._additional_rates = None
        self.discriminator = None

        if primary_rate is not None:
            self.primary_rate = primary_rate
        if additional_rates is not None:
            self.additional_rates = additional_rates

    @property
    def primary_rate(self):
        """Gets the primary_rate of this ProjectHourlyRateContractQueryDTO.  # noqa: E501


        :return: The primary_rate of this ProjectHourlyRateContractQueryDTO.  # noqa: E501
        :rtype: RateQueryDTO
        """
        return self._primary_rate

    @primary_rate.setter
    def primary_rate(self, primary_rate):
        """Sets the primary_rate of this ProjectHourlyRateContractQueryDTO.


        :param primary_rate: The primary_rate of this ProjectHourlyRateContractQueryDTO.  # noqa: E501
        :type: RateQueryDTO
        """

        self._primary_rate = primary_rate

    @property
    def additional_rates(self):
        """Gets the additional_rates of this ProjectHourlyRateContractQueryDTO.  # noqa: E501


        :return: The additional_rates of this ProjectHourlyRateContractQueryDTO.  # noqa: E501
        :rtype: list[RateQueryDTO]
        """
        return self._additional_rates

    @additional_rates.setter
    def additional_rates(self, additional_rates):
        """Sets the additional_rates of this ProjectHourlyRateContractQueryDTO.


        :param additional_rates: The additional_rates of this ProjectHourlyRateContractQueryDTO.  # noqa: E501
        :type: list[RateQueryDTO]
        """

        self._additional_rates = additional_rates

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
        if issubclass(ProjectHourlyRateContractQueryDTO, dict):
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
        if not isinstance(other, ProjectHourlyRateContractQueryDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectHourlyRateContractQueryDTO):
            return True

        return self.to_dict() != other.to_dict()
