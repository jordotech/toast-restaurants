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


class PaymentOptions(object):
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
        'delivery': 'DeliveryPaymentOptions',
        'takeout': 'TakeoutPaymentOptions',
        'cc_tip': 'bool'
    }

    attribute_map = {
        'delivery': 'delivery',
        'takeout': 'takeout',
        'cc_tip': 'ccTip'
    }

    def __init__(self, delivery=None, takeout=None, cc_tip=None):
        """
        PaymentOptions - a model defined in Swagger
        """

        self._delivery = None
        self._takeout = None
        self._cc_tip = None

        if delivery is not None:
          self.delivery = delivery
        if takeout is not None:
          self.takeout = takeout
        if cc_tip is not None:
          self.cc_tip = cc_tip

    @property
    def delivery(self):
        """
        Gets the delivery of this PaymentOptions.

        :return: The delivery of this PaymentOptions.
        :rtype: DeliveryPaymentOptions
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """
        Sets the delivery of this PaymentOptions.

        :param delivery: The delivery of this PaymentOptions.
        :type: DeliveryPaymentOptions
        """

        self._delivery = delivery

    @property
    def takeout(self):
        """
        Gets the takeout of this PaymentOptions.

        :return: The takeout of this PaymentOptions.
        :rtype: TakeoutPaymentOptions
        """
        return self._takeout

    @takeout.setter
    def takeout(self, takeout):
        """
        Sets the takeout of this PaymentOptions.

        :param takeout: The takeout of this PaymentOptions.
        :type: TakeoutPaymentOptions
        """

        self._takeout = takeout

    @property
    def cc_tip(self):
        """
        Gets the cc_tip of this PaymentOptions.
        enables credit card tips

        :return: The cc_tip of this PaymentOptions.
        :rtype: bool
        """
        return self._cc_tip

    @cc_tip.setter
    def cc_tip(self, cc_tip):
        """
        Sets the cc_tip of this PaymentOptions.
        enables credit card tips

        :param cc_tip: The cc_tip of this PaymentOptions.
        :type: bool
        """

        self._cc_tip = cc_tip

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
        if not isinstance(other, PaymentOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
