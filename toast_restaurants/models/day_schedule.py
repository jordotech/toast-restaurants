# coding: utf-8

"""
    Restaurant Info API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    Contact: integrations@toasttab.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DaySchedule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'schedule_name': 'str',
        'services': 'list[Service]',
        'open_time': 'str',
        'close_time': 'str'
    }

    attribute_map = {
        'schedule_name': 'scheduleName',
        'services': 'services',
        'open_time': 'openTime',
        'close_time': 'closeTime'
    }

    def __init__(self, schedule_name=None, services=None, open_time=None, close_time=None):
        """
        DaySchedule - a model defined in Swagger
        """

        self._schedule_name = None
        self._services = None
        self._open_time = None
        self._close_time = None

        if schedule_name is not None:
          self.schedule_name = schedule_name
        if services is not None:
          self.services = services
        if open_time is not None:
          self.open_time = open_time
        if close_time is not None:
          self.close_time = close_time

    @property
    def schedule_name(self):
        """
        Gets the schedule_name of this DaySchedule.
        The name of the type of day. For example, `weekday`.

        :return: The schedule_name of this DaySchedule.
        :rtype: str
        """
        return self._schedule_name

    @schedule_name.setter
    def schedule_name(self, schedule_name):
        """
        Sets the schedule_name of this DaySchedule.
        The name of the type of day. For example, `weekday`.

        :param schedule_name: The schedule_name of this DaySchedule.
        :type: str
        """

        self._schedule_name = schedule_name

    @property
    def services(self):
        """
        Gets the services of this DaySchedule.
        An array of `Service` objects that are available during the type of day. 

        :return: The services of this DaySchedule.
        :rtype: list[Service]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this DaySchedule.
        An array of `Service` objects that are available during the type of day. 

        :param services: The services of this DaySchedule.
        :type: list[Service]
        """

        self._services = services

    @property
    def open_time(self):
        """
        Gets the open_time of this DaySchedule.
        The time of day that the first service for the type of day begins. For example, the first service might begin at `06:00:00.000`. 

        :return: The open_time of this DaySchedule.
        :rtype: str
        """
        return self._open_time

    @open_time.setter
    def open_time(self, open_time):
        """
        Sets the open_time of this DaySchedule.
        The time of day that the first service for the type of day begins. For example, the first service might begin at `06:00:00.000`. 

        :param open_time: The open_time of this DaySchedule.
        :type: str
        """

        self._open_time = open_time

    @property
    def close_time(self):
        """
        Gets the close_time of this DaySchedule.
        The time of day that the last service for the type of day ends. For example, the last service might end at `02:00:00.000`. 

        :return: The close_time of this DaySchedule.
        :rtype: str
        """
        return self._close_time

    @close_time.setter
    def close_time(self, close_time):
        """
        Sets the close_time of this DaySchedule.
        The time of day that the last service for the type of day ends. For example, the last service might end at `02:00:00.000`. 

        :param close_time: The close_time of this DaySchedule.
        :type: str
        """

        self._close_time = close_time

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DaySchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
