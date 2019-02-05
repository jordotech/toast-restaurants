# swagger_client.DefaultApi

All URIs are relative to *https://localhostrestaurants/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_management_group_guid_restaurants_get**](DefaultApi.md#groups_management_group_guid_restaurants_get) | **GET** /groups/{managementGroupGUID}/restaurants | Lists all restaurants in a management group.
[**restaurants_restaurant_guid_get**](DefaultApi.md#restaurants_restaurant_guid_get) | **GET** /restaurants/{restaurantGUID} | Returns information about the configuration of a restaurant.


# **groups_management_group_guid_restaurants_get**
> list[Restaurant] groups_management_group_guid_restaurants_get(management_group_guid)

Lists all restaurants in a management group.

Returns an array of <a href=\"#/definitions/Restaurant\">`Restaurant`</a> objects that are a part of the restaurant management group you specify in the `managementGroupGUID` path parameter. Each `Restaurant` object contains the unique Toast POS identifier for the restaurant in its `guid` value. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
management_group_guid = 'management_group_guid_example' # str | The GUID of the restaurant management group.

try: 
    # Lists all restaurants in a management group.
    api_response = api_instance.groups_management_group_guid_restaurants_get(management_group_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_management_group_guid_restaurants_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **management_group_guid** | **str**| The GUID of the restaurant management group. | 

### Return type

[**list[Restaurant]**](Restaurant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restaurants_restaurant_guid_get**
> RestaurantInfo restaurants_restaurant_guid_get(restaurant_guid)

Returns information about the configuration of a restaurant.

Returns a <a href=\"#/definitions/RestaurantInfo\">`RestaurantInfo`</a> object that contains detailed information about the configuration of a restaurant. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
restaurant_guid = 'restaurant_guid_example' # str | The GUID of the restaurant.

try: 
    # Returns information about the configuration of a restaurant.
    api_response = api_instance.restaurants_restaurant_guid_get(restaurant_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->restaurants_restaurant_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restaurant_guid** | **str**| The GUID of the restaurant. | 

### Return type

[**RestaurantInfo**](RestaurantInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

