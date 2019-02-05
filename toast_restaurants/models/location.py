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


class Location(object):
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
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'state_code': 'str',
        'zip_code': 'str',
        'country': 'str',
        'phone': 'str',
        'latitude': 'float',
        'longitude': 'float'
    }

    attribute_map = {
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'state_code': 'stateCode',
        'zip_code': 'zipCode',
        'country': 'country',
        'phone': 'phone',
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, address1=None, address2=None, city=None, state_code=None, zip_code=None, country=None, phone=None, latitude=None, longitude=None):
        """
        Location - a model defined in Swagger
        """

        self._address1 = None
        self._address2 = None
        self._city = None
        self._state_code = None
        self._zip_code = None
        self._country = None
        self._phone = None
        self._latitude = None
        self._longitude = None

        if address1 is not None:
          self.address1 = address1
        if address2 is not None:
          self.address2 = address2
        if city is not None:
          self.city = city
        if state_code is not None:
          self.state_code = state_code
        if zip_code is not None:
          self.zip_code = zip_code
        if country is not None:
          self.country = country
        if phone is not None:
          self.phone = phone
        if latitude is not None:
          self.latitude = latitude
        if longitude is not None:
          self.longitude = longitude

    @property
    def address1(self):
        """
        Gets the address1 of this Location.
        The first line of the street address of the restaurant.

        :return: The address1 of this Location.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this Location.
        The first line of the street address of the restaurant.

        :param address1: The address1 of this Location.
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this Location.
        The second line of the street address of the restaurant.

        :return: The address2 of this Location.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this Location.
        The second line of the street address of the restaurant.

        :param address2: The address2 of this Location.
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """
        Gets the city of this Location.
        The city or town of the restaurant. restaurant.

        :return: The city of this Location.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Location.
        The city or town of the restaurant. restaurant.

        :param city: The city of this Location.
        :type: str
        """

        self._city = city

    @property
    def state_code(self):
        """
        Gets the state_code of this Location.
        The abbreviation of the state or province of the restaurant.

        :return: The state_code of this Location.
        :rtype: str
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code):
        """
        Sets the state_code of this Location.
        The abbreviation of the state or province of the restaurant.

        :param state_code: The state_code of this Location.
        :type: str
        """

        self._state_code = state_code

    @property
    def zip_code(self):
        """
        Gets the zip_code of this Location.
        The ZIP or postal code of the restaurant.

        :return: The zip_code of this Location.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """
        Sets the zip_code of this Location.
        The ZIP or postal code of the restaurant.

        :param zip_code: The zip_code of this Location.
        :type: str
        """

        self._zip_code = zip_code

    @property
    def country(self):
        """
        Gets the country of this Location.
        The nation of the restaurant.

        :return: The country of this Location.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Location.
        The nation of the restaurant.

        :param country: The country of this Location.
        :type: str
        """

        self._country = country

    @property
    def phone(self):
        """
        Gets the phone of this Location.

        :return: The phone of this Location.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this Location.

        :param phone: The phone of this Location.
        :type: str
        """

        self._phone = phone

    @property
    def latitude(self):
        """
        Gets the latitude of this Location.
        The north/south geographic coordinate of the restaurant, in decimal degrees.

        :return: The latitude of this Location.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this Location.
        The north/south geographic coordinate of the restaurant, in decimal degrees.

        :param latitude: The latitude of this Location.
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """
        Gets the longitude of this Location.
        The east/west geographic coordinate of the restaurant, in decimal degrees.

        :return: The longitude of this Location.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this Location.
        The east/west geographic coordinate of the restaurant, in decimal degrees.

        :param longitude: The longitude of this Location.
        :type: float
        """

        self._longitude = longitude

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
        if not isinstance(other, Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
