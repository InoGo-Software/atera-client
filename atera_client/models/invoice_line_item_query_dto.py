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


class InvoiceLineItemQueryDTO(object):
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
        'product': 'str',
        'description': 'str',
        'quantity': 'float',
        'rate': 'float',
        'tax_percentage': 'float',
        'discount_percentage': 'float',
        'total': 'float',
        'subtotal': 'float',
        'tax': 'float',
        'line_idx': 'int'
    }

    attribute_map = {
        'product': 'Product',
        'description': 'Description',
        'quantity': 'Quantity',
        'rate': 'Rate',
        'tax_percentage': 'TaxPercentage',
        'discount_percentage': 'DiscountPercentage',
        'total': 'Total',
        'subtotal': 'Subtotal',
        'tax': 'Tax',
        'line_idx': 'LineIdx'
    }

    def __init__(self, product=None, description=None, quantity=None, rate=None, tax_percentage=None, discount_percentage=None, total=None, subtotal=None, tax=None, line_idx=None, _configuration=None):  # noqa: E501
        """InvoiceLineItemQueryDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product = None
        self._description = None
        self._quantity = None
        self._rate = None
        self._tax_percentage = None
        self._discount_percentage = None
        self._total = None
        self._subtotal = None
        self._tax = None
        self._line_idx = None
        self.discriminator = None

        if product is not None:
            self.product = product
        if description is not None:
            self.description = description
        if quantity is not None:
            self.quantity = quantity
        if rate is not None:
            self.rate = rate
        if tax_percentage is not None:
            self.tax_percentage = tax_percentage
        if discount_percentage is not None:
            self.discount_percentage = discount_percentage
        if total is not None:
            self.total = total
        if subtotal is not None:
            self.subtotal = subtotal
        if tax is not None:
            self.tax = tax
        if line_idx is not None:
            self.line_idx = line_idx

    @property
    def product(self):
        """Gets the product of this InvoiceLineItemQueryDTO.  # noqa: E501


        :return: The product of this InvoiceLineItemQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this InvoiceLineItemQueryDTO.


        :param product: The product of this InvoiceLineItemQueryDTO.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def description(self):
        """Gets the description of this InvoiceLineItemQueryDTO.  # noqa: E501


        :return: The description of this InvoiceLineItemQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InvoiceLineItemQueryDTO.


        :param description: The description of this InvoiceLineItemQueryDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def quantity(self):
        """Gets the quantity of this InvoiceLineItemQueryDTO.  # noqa: E501


        :return: The quantity of this InvoiceLineItemQueryDTO.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this InvoiceLineItemQueryDTO.


        :param quantity: The quantity of this InvoiceLineItemQueryDTO.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def rate(self):
        """Gets the rate of this InvoiceLineItemQueryDTO.  # noqa: E501


        :return: The rate of this InvoiceLineItemQueryDTO.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this InvoiceLineItemQueryDTO.


        :param rate: The rate of this InvoiceLineItemQueryDTO.  # noqa: E501
        :type: float
        """

        self._rate = rate

    @property
    def tax_percentage(self):
        """Gets the tax_percentage of this InvoiceLineItemQueryDTO.  # noqa: E501


        :return: The tax_percentage of this InvoiceLineItemQueryDTO.  # noqa: E501
        :rtype: float
        """
        return self._tax_percentage

    @tax_percentage.setter
    def tax_percentage(self, tax_percentage):
        """Sets the tax_percentage of this InvoiceLineItemQueryDTO.


        :param tax_percentage: The tax_percentage of this InvoiceLineItemQueryDTO.  # noqa: E501
        :type: float
        """

        self._tax_percentage = tax_percentage

    @property
    def discount_percentage(self):
        """Gets the discount_percentage of this InvoiceLineItemQueryDTO.  # noqa: E501


        :return: The discount_percentage of this InvoiceLineItemQueryDTO.  # noqa: E501
        :rtype: float
        """
        return self._discount_percentage

    @discount_percentage.setter
    def discount_percentage(self, discount_percentage):
        """Sets the discount_percentage of this InvoiceLineItemQueryDTO.


        :param discount_percentage: The discount_percentage of this InvoiceLineItemQueryDTO.  # noqa: E501
        :type: float
        """

        self._discount_percentage = discount_percentage

    @property
    def total(self):
        """Gets the total of this InvoiceLineItemQueryDTO.  # noqa: E501


        :return: The total of this InvoiceLineItemQueryDTO.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InvoiceLineItemQueryDTO.


        :param total: The total of this InvoiceLineItemQueryDTO.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def subtotal(self):
        """Gets the subtotal of this InvoiceLineItemQueryDTO.  # noqa: E501


        :return: The subtotal of this InvoiceLineItemQueryDTO.  # noqa: E501
        :rtype: float
        """
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        """Sets the subtotal of this InvoiceLineItemQueryDTO.


        :param subtotal: The subtotal of this InvoiceLineItemQueryDTO.  # noqa: E501
        :type: float
        """

        self._subtotal = subtotal

    @property
    def tax(self):
        """Gets the tax of this InvoiceLineItemQueryDTO.  # noqa: E501


        :return: The tax of this InvoiceLineItemQueryDTO.  # noqa: E501
        :rtype: float
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this InvoiceLineItemQueryDTO.


        :param tax: The tax of this InvoiceLineItemQueryDTO.  # noqa: E501
        :type: float
        """

        self._tax = tax

    @property
    def line_idx(self):
        """Gets the line_idx of this InvoiceLineItemQueryDTO.  # noqa: E501


        :return: The line_idx of this InvoiceLineItemQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._line_idx

    @line_idx.setter
    def line_idx(self, line_idx):
        """Sets the line_idx of this InvoiceLineItemQueryDTO.


        :param line_idx: The line_idx of this InvoiceLineItemQueryDTO.  # noqa: E501
        :type: int
        """

        self._line_idx = line_idx

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
        if issubclass(InvoiceLineItemQueryDTO, dict):
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
        if not isinstance(other, InvoiceLineItemQueryDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvoiceLineItemQueryDTO):
            return True

        return self.to_dict() != other.to_dict()