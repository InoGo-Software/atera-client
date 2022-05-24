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


class AlertQueryDTO(object):
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
        'alert_id': 'int',
        'code': 'int',
        'source': 'str',
        'title': 'str',
        'severity': 'str',
        'created': 'datetime',
        'snoozed_end_date': 'datetime',
        'device_guid': 'str',
        'additional_info': 'str',
        'archived': 'bool',
        'alert_category_id': 'str',
        'archived_date': 'datetime',
        'ticket_id': 'int',
        'alert_message': 'str',
        'device_name': 'str',
        'customer_id': 'int',
        'customer_name': 'str',
        'folder_id': 'int',
        'polling_cycles_count': 'int'
    }

    attribute_map = {
        'alert_id': 'AlertID',
        'code': 'Code',
        'source': 'Source',
        'title': 'Title',
        'severity': 'Severity',
        'created': 'Created',
        'snoozed_end_date': 'SnoozedEndDate',
        'device_guid': 'DeviceGuid',
        'additional_info': 'AdditionalInfo',
        'archived': 'Archived',
        'alert_category_id': 'AlertCategoryID',
        'archived_date': 'ArchivedDate',
        'ticket_id': 'TicketID',
        'alert_message': 'AlertMessage',
        'device_name': 'DeviceName',
        'customer_id': 'CustomerID',
        'customer_name': 'CustomerName',
        'folder_id': 'FolderID',
        'polling_cycles_count': 'PollingCyclesCount'
    }

    def __init__(self, alert_id=None, code=None, source=None, title=None, severity=None, created=None, snoozed_end_date=None, device_guid=None, additional_info=None, archived=None, alert_category_id=None, archived_date=None, ticket_id=None, alert_message=None, device_name=None, customer_id=None, customer_name=None, folder_id=None, polling_cycles_count=None, _configuration=None):  # noqa: E501
        """AlertQueryDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alert_id = None
        self._code = None
        self._source = None
        self._title = None
        self._severity = None
        self._created = None
        self._snoozed_end_date = None
        self._device_guid = None
        self._additional_info = None
        self._archived = None
        self._alert_category_id = None
        self._archived_date = None
        self._ticket_id = None
        self._alert_message = None
        self._device_name = None
        self._customer_id = None
        self._customer_name = None
        self._folder_id = None
        self._polling_cycles_count = None
        self.discriminator = None

        if alert_id is not None:
            self.alert_id = alert_id
        if code is not None:
            self.code = code
        if source is not None:
            self.source = source
        if title is not None:
            self.title = title
        if severity is not None:
            self.severity = severity
        if created is not None:
            self.created = created
        if snoozed_end_date is not None:
            self.snoozed_end_date = snoozed_end_date
        if device_guid is not None:
            self.device_guid = device_guid
        if additional_info is not None:
            self.additional_info = additional_info
        if archived is not None:
            self.archived = archived
        if alert_category_id is not None:
            self.alert_category_id = alert_category_id
        if archived_date is not None:
            self.archived_date = archived_date
        if ticket_id is not None:
            self.ticket_id = ticket_id
        if alert_message is not None:
            self.alert_message = alert_message
        if device_name is not None:
            self.device_name = device_name
        if customer_id is not None:
            self.customer_id = customer_id
        if customer_name is not None:
            self.customer_name = customer_name
        if folder_id is not None:
            self.folder_id = folder_id
        if polling_cycles_count is not None:
            self.polling_cycles_count = polling_cycles_count

    @property
    def alert_id(self):
        """Gets the alert_id of this AlertQueryDTO.  # noqa: E501


        :return: The alert_id of this AlertQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._alert_id

    @alert_id.setter
    def alert_id(self, alert_id):
        """Sets the alert_id of this AlertQueryDTO.


        :param alert_id: The alert_id of this AlertQueryDTO.  # noqa: E501
        :type: int
        """

        self._alert_id = alert_id

    @property
    def code(self):
        """Gets the code of this AlertQueryDTO.  # noqa: E501


        :return: The code of this AlertQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AlertQueryDTO.


        :param code: The code of this AlertQueryDTO.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def source(self):
        """Gets the source of this AlertQueryDTO.  # noqa: E501


        :return: The source of this AlertQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this AlertQueryDTO.


        :param source: The source of this AlertQueryDTO.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def title(self):
        """Gets the title of this AlertQueryDTO.  # noqa: E501


        :return: The title of this AlertQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AlertQueryDTO.


        :param title: The title of this AlertQueryDTO.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def severity(self):
        """Gets the severity of this AlertQueryDTO.  # noqa: E501


        :return: The severity of this AlertQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this AlertQueryDTO.


        :param severity: The severity of this AlertQueryDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["Information", "Warning", "Critical"]  # noqa: E501
        if (self._configuration.client_side_validation and
                severity not in allowed_values):
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def created(self):
        """Gets the created of this AlertQueryDTO.  # noqa: E501


        :return: The created of this AlertQueryDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AlertQueryDTO.


        :param created: The created of this AlertQueryDTO.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def snoozed_end_date(self):
        """Gets the snoozed_end_date of this AlertQueryDTO.  # noqa: E501


        :return: The snoozed_end_date of this AlertQueryDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._snoozed_end_date

    @snoozed_end_date.setter
    def snoozed_end_date(self, snoozed_end_date):
        """Sets the snoozed_end_date of this AlertQueryDTO.


        :param snoozed_end_date: The snoozed_end_date of this AlertQueryDTO.  # noqa: E501
        :type: datetime
        """

        self._snoozed_end_date = snoozed_end_date

    @property
    def device_guid(self):
        """Gets the device_guid of this AlertQueryDTO.  # noqa: E501


        :return: The device_guid of this AlertQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._device_guid

    @device_guid.setter
    def device_guid(self, device_guid):
        """Sets the device_guid of this AlertQueryDTO.


        :param device_guid: The device_guid of this AlertQueryDTO.  # noqa: E501
        :type: str
        """

        self._device_guid = device_guid

    @property
    def additional_info(self):
        """Gets the additional_info of this AlertQueryDTO.  # noqa: E501


        :return: The additional_info of this AlertQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this AlertQueryDTO.


        :param additional_info: The additional_info of this AlertQueryDTO.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def archived(self):
        """Gets the archived of this AlertQueryDTO.  # noqa: E501


        :return: The archived of this AlertQueryDTO.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this AlertQueryDTO.


        :param archived: The archived of this AlertQueryDTO.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def alert_category_id(self):
        """Gets the alert_category_id of this AlertQueryDTO.  # noqa: E501


        :return: The alert_category_id of this AlertQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._alert_category_id

    @alert_category_id.setter
    def alert_category_id(self, alert_category_id):
        """Sets the alert_category_id of this AlertQueryDTO.


        :param alert_category_id: The alert_category_id of this AlertQueryDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["Hardware", "Disk", "Availability", "Performance", "Exchange", "General"]  # noqa: E501
        if (self._configuration.client_side_validation and
                alert_category_id not in allowed_values):
            raise ValueError(
                "Invalid value for `alert_category_id` ({0}), must be one of {1}"  # noqa: E501
                .format(alert_category_id, allowed_values)
            )

        self._alert_category_id = alert_category_id

    @property
    def archived_date(self):
        """Gets the archived_date of this AlertQueryDTO.  # noqa: E501


        :return: The archived_date of this AlertQueryDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_date

    @archived_date.setter
    def archived_date(self, archived_date):
        """Sets the archived_date of this AlertQueryDTO.


        :param archived_date: The archived_date of this AlertQueryDTO.  # noqa: E501
        :type: datetime
        """

        self._archived_date = archived_date

    @property
    def ticket_id(self):
        """Gets the ticket_id of this AlertQueryDTO.  # noqa: E501


        :return: The ticket_id of this AlertQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        """Sets the ticket_id of this AlertQueryDTO.


        :param ticket_id: The ticket_id of this AlertQueryDTO.  # noqa: E501
        :type: int
        """

        self._ticket_id = ticket_id

    @property
    def alert_message(self):
        """Gets the alert_message of this AlertQueryDTO.  # noqa: E501


        :return: The alert_message of this AlertQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._alert_message

    @alert_message.setter
    def alert_message(self, alert_message):
        """Sets the alert_message of this AlertQueryDTO.


        :param alert_message: The alert_message of this AlertQueryDTO.  # noqa: E501
        :type: str
        """

        self._alert_message = alert_message

    @property
    def device_name(self):
        """Gets the device_name of this AlertQueryDTO.  # noqa: E501


        :return: The device_name of this AlertQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this AlertQueryDTO.


        :param device_name: The device_name of this AlertQueryDTO.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def customer_id(self):
        """Gets the customer_id of this AlertQueryDTO.  # noqa: E501


        :return: The customer_id of this AlertQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this AlertQueryDTO.


        :param customer_id: The customer_id of this AlertQueryDTO.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def customer_name(self):
        """Gets the customer_name of this AlertQueryDTO.  # noqa: E501


        :return: The customer_name of this AlertQueryDTO.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this AlertQueryDTO.


        :param customer_name: The customer_name of this AlertQueryDTO.  # noqa: E501
        :type: str
        """

        self._customer_name = customer_name

    @property
    def folder_id(self):
        """Gets the folder_id of this AlertQueryDTO.  # noqa: E501


        :return: The folder_id of this AlertQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this AlertQueryDTO.


        :param folder_id: The folder_id of this AlertQueryDTO.  # noqa: E501
        :type: int
        """

        self._folder_id = folder_id

    @property
    def polling_cycles_count(self):
        """Gets the polling_cycles_count of this AlertQueryDTO.  # noqa: E501


        :return: The polling_cycles_count of this AlertQueryDTO.  # noqa: E501
        :rtype: int
        """
        return self._polling_cycles_count

    @polling_cycles_count.setter
    def polling_cycles_count(self, polling_cycles_count):
        """Sets the polling_cycles_count of this AlertQueryDTO.


        :param polling_cycles_count: The polling_cycles_count of this AlertQueryDTO.  # noqa: E501
        :type: int
        """

        self._polling_cycles_count = polling_cycles_count

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
        if issubclass(AlertQueryDTO, dict):
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
        if not isinstance(other, AlertQueryDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertQueryDTO):
            return True

        return self.to_dict() != other.to_dict()