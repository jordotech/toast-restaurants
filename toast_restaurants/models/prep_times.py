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


class PrepTimes(object):
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
        'delivery_prep_time': 'int',
        'delivery_time_after_open': 'int',
        'delivery_time_before_close': 'int',
        'takeout_prep_time': 'int',
        'takeout_time_after_open': 'int',
        'takeout_time_before_close': 'int',
        'takeout_throttling_time': 'int',
        'delivery_throttling_time': 'int'
    }

    attribute_map = {
        'delivery_prep_time': 'deliveryPrepTime',
        'delivery_time_after_open': 'deliveryTimeAfterOpen',
        'delivery_time_before_close': 'deliveryTimeBeforeClose',
        'takeout_prep_time': 'takeoutPrepTime',
        'takeout_time_after_open': 'takeoutTimeAfterOpen',
        'takeout_time_before_close': 'takeoutTimeBeforeClose',
        'takeout_throttling_time': 'takeoutThrottlingTime',
        'delivery_throttling_time': 'deliveryThrottlingTime'
    }

    def __init__(self, delivery_prep_time=None, delivery_time_after_open=None, delivery_time_before_close=None, takeout_prep_time=None, takeout_time_after_open=None, takeout_time_before_close=None, takeout_throttling_time=None, delivery_throttling_time=None):
        """
        PrepTimes - a model defined in Swagger
        """

        self._delivery_prep_time = None
        self._delivery_time_after_open = None
        self._delivery_time_before_close = None
        self._takeout_prep_time = None
        self._takeout_time_after_open = None
        self._takeout_time_before_close = None
        self._takeout_throttling_time = None
        self._delivery_throttling_time = None

        if delivery_prep_time is not None:
          self.delivery_prep_time = delivery_prep_time
        if delivery_time_after_open is not None:
          self.delivery_time_after_open = delivery_time_after_open
        if delivery_time_before_close is not None:
          self.delivery_time_before_close = delivery_time_before_close
        if takeout_prep_time is not None:
          self.takeout_prep_time = takeout_prep_time
        if takeout_time_after_open is not None:
          self.takeout_time_after_open = takeout_time_after_open
        if takeout_time_before_close is not None:
          self.takeout_time_before_close = takeout_time_before_close
        if takeout_throttling_time is not None:
          self.takeout_throttling_time = takeout_throttling_time
        if delivery_throttling_time is not None:
          self.delivery_throttling_time = delivery_throttling_time

    @property
    def delivery_prep_time(self):
        """
        Gets the delivery_prep_time of this PrepTimes.
        The amount of time, in minutes, that it takes to prepare an online delivery order. 

        :return: The delivery_prep_time of this PrepTimes.
        :rtype: int
        """
        return self._delivery_prep_time

    @delivery_prep_time.setter
    def delivery_prep_time(self, delivery_prep_time):
        """
        Sets the delivery_prep_time of this PrepTimes.
        The amount of time, in minutes, that it takes to prepare an online delivery order. 

        :param delivery_prep_time: The delivery_prep_time of this PrepTimes.
        :type: int
        """

        self._delivery_prep_time = delivery_prep_time

    @property
    def delivery_time_after_open(self):
        """
        Gets the delivery_time_after_open of this PrepTimes.
        The amount of time, in minutes, that it takes for delivery service to become available after the restaurant opens. 

        :return: The delivery_time_after_open of this PrepTimes.
        :rtype: int
        """
        return self._delivery_time_after_open

    @delivery_time_after_open.setter
    def delivery_time_after_open(self, delivery_time_after_open):
        """
        Sets the delivery_time_after_open of this PrepTimes.
        The amount of time, in minutes, that it takes for delivery service to become available after the restaurant opens. 

        :param delivery_time_after_open: The delivery_time_after_open of this PrepTimes.
        :type: int
        """

        self._delivery_time_after_open = delivery_time_after_open

    @property
    def delivery_time_before_close(self):
        """
        Gets the delivery_time_before_close of this PrepTimes.
        The amount of time, in minutes, before the restaurant closing time that delivery service becomes unavailable. 

        :return: The delivery_time_before_close of this PrepTimes.
        :rtype: int
        """
        return self._delivery_time_before_close

    @delivery_time_before_close.setter
    def delivery_time_before_close(self, delivery_time_before_close):
        """
        Sets the delivery_time_before_close of this PrepTimes.
        The amount of time, in minutes, before the restaurant closing time that delivery service becomes unavailable. 

        :param delivery_time_before_close: The delivery_time_before_close of this PrepTimes.
        :type: int
        """

        self._delivery_time_before_close = delivery_time_before_close

    @property
    def takeout_prep_time(self):
        """
        Gets the takeout_prep_time of this PrepTimes.
        The amount of time, in minutes, that it takes to prepare an online takeout order. 

        :return: The takeout_prep_time of this PrepTimes.
        :rtype: int
        """
        return self._takeout_prep_time

    @takeout_prep_time.setter
    def takeout_prep_time(self, takeout_prep_time):
        """
        Sets the takeout_prep_time of this PrepTimes.
        The amount of time, in minutes, that it takes to prepare an online takeout order. 

        :param takeout_prep_time: The takeout_prep_time of this PrepTimes.
        :type: int
        """

        self._takeout_prep_time = takeout_prep_time

    @property
    def takeout_time_after_open(self):
        """
        Gets the takeout_time_after_open of this PrepTimes.
        The amount of time, in minutes, that it takes for takeout service to become available after the restaurant opens. 

        :return: The takeout_time_after_open of this PrepTimes.
        :rtype: int
        """
        return self._takeout_time_after_open

    @takeout_time_after_open.setter
    def takeout_time_after_open(self, takeout_time_after_open):
        """
        Sets the takeout_time_after_open of this PrepTimes.
        The amount of time, in minutes, that it takes for takeout service to become available after the restaurant opens. 

        :param takeout_time_after_open: The takeout_time_after_open of this PrepTimes.
        :type: int
        """

        self._takeout_time_after_open = takeout_time_after_open

    @property
    def takeout_time_before_close(self):
        """
        Gets the takeout_time_before_close of this PrepTimes.
        The amount of time, in minutes, before the restaurant closing time that takeout service becomes unavailable. 

        :return: The takeout_time_before_close of this PrepTimes.
        :rtype: int
        """
        return self._takeout_time_before_close

    @takeout_time_before_close.setter
    def takeout_time_before_close(self, takeout_time_before_close):
        """
        Sets the takeout_time_before_close of this PrepTimes.
        The amount of time, in minutes, before the restaurant closing time that takeout service becomes unavailable. 

        :param takeout_time_before_close: The takeout_time_before_close of this PrepTimes.
        :type: int
        """

        self._takeout_time_before_close = takeout_time_before_close

    @property
    def takeout_throttling_time(self):
        """
        Gets the takeout_throttling_time of this PrepTimes.
        The amount of time, in minutes, that an online takeout order is delayed before the Toast POS fires it in the kitchen. 

        :return: The takeout_throttling_time of this PrepTimes.
        :rtype: int
        """
        return self._takeout_throttling_time

    @takeout_throttling_time.setter
    def takeout_throttling_time(self, takeout_throttling_time):
        """
        Sets the takeout_throttling_time of this PrepTimes.
        The amount of time, in minutes, that an online takeout order is delayed before the Toast POS fires it in the kitchen. 

        :param takeout_throttling_time: The takeout_throttling_time of this PrepTimes.
        :type: int
        """

        self._takeout_throttling_time = takeout_throttling_time

    @property
    def delivery_throttling_time(self):
        """
        Gets the delivery_throttling_time of this PrepTimes.
        The amount of time, in minutes, that an online delivery order is delayed before the Toast POS fires it in the kitchen. 

        :return: The delivery_throttling_time of this PrepTimes.
        :rtype: int
        """
        return self._delivery_throttling_time

    @delivery_throttling_time.setter
    def delivery_throttling_time(self, delivery_throttling_time):
        """
        Sets the delivery_throttling_time of this PrepTimes.
        The amount of time, in minutes, that an online delivery order is delayed before the Toast POS fires it in the kitchen. 

        :param delivery_throttling_time: The delivery_throttling_time of this PrepTimes.
        :type: int
        """

        self._delivery_throttling_time = delivery_throttling_time

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
        if not isinstance(other, PrepTimes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
