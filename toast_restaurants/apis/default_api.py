# coding: utf-8

"""
    Restaurant Info API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    Contact: integrations@toasttab.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DefaultApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def groups_management_group_guid_restaurants_get(self, management_group_guid, **kwargs):
        """
        Lists all restaurants in a management group.
        Returns an array of <a href=\"#/definitions/Restaurant\">`Restaurant`</a> objects that are a part of the restaurant management group you specify in the `managementGroupGUID` path parameter. Each `Restaurant` object contains the unique Toast POS identifier for the restaurant in its `guid` value. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.groups_management_group_guid_restaurants_get(management_group_guid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_group_guid: The GUID of the restaurant management group. (required)
        :return: list[Restaurant]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.groups_management_group_guid_restaurants_get_with_http_info(management_group_guid, **kwargs)
        else:
            (data) = self.groups_management_group_guid_restaurants_get_with_http_info(management_group_guid, **kwargs)
            return data

    def groups_management_group_guid_restaurants_get_with_http_info(self, management_group_guid, **kwargs):
        """
        Lists all restaurants in a management group.
        Returns an array of <a href=\"#/definitions/Restaurant\">`Restaurant`</a> objects that are a part of the restaurant management group you specify in the `managementGroupGUID` path parameter. Each `Restaurant` object contains the unique Toast POS identifier for the restaurant in its `guid` value. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.groups_management_group_guid_restaurants_get_with_http_info(management_group_guid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_group_guid: The GUID of the restaurant management group. (required)
        :return: list[Restaurant]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_group_guid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_management_group_guid_restaurants_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'management_group_guid' is set
        if ('management_group_guid' not in params) or (params['management_group_guid'] is None):
            raise ValueError("Missing the required parameter `management_group_guid` when calling `groups_management_group_guid_restaurants_get`")


        collection_formats = {}

        path_params = {}
        if 'management_group_guid' in params:
            path_params['managementGroupGUID'] = params['management_group_guid']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/groups/{managementGroupGUID}/restaurants', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[Restaurant]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def restaurants_restaurant_guid_get(self, restaurant_guid, **kwargs):
        """
        Returns information about the configuration of a restaurant.
        Returns a <a href=\"#/definitions/RestaurantInfo\">`RestaurantInfo`</a> object that contains detailed information about the configuration of a restaurant. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.restaurants_restaurant_guid_get(restaurant_guid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str restaurant_guid: The GUID of the restaurant. (required)
        :return: RestaurantInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.restaurants_restaurant_guid_get_with_http_info(restaurant_guid, **kwargs)
        else:
            (data) = self.restaurants_restaurant_guid_get_with_http_info(restaurant_guid, **kwargs)
            return data

    def restaurants_restaurant_guid_get_with_http_info(self, restaurant_guid, **kwargs):
        """
        Returns information about the configuration of a restaurant.
        Returns a <a href=\"#/definitions/RestaurantInfo\">`RestaurantInfo`</a> object that contains detailed information about the configuration of a restaurant. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.restaurants_restaurant_guid_get_with_http_info(restaurant_guid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str restaurant_guid: The GUID of the restaurant. (required)
        :return: RestaurantInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['restaurant_guid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method restaurants_restaurant_guid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'restaurant_guid' is set
        if ('restaurant_guid' not in params) or (params['restaurant_guid'] is None):
            raise ValueError("Missing the required parameter `restaurant_guid` when calling `restaurants_restaurant_guid_get`")


        collection_formats = {}

        path_params = {}
        if 'restaurant_guid' in params:
            path_params['restaurantGUID'] = params['restaurant_guid']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/restaurants/{restaurantGUID}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RestaurantInfo',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
