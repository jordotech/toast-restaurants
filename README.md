# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://localhostrestaurants/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**groups_management_group_guid_restaurants_get**](docs/DefaultApi.md#groups_management_group_guid_restaurants_get) | **GET** /groups/{managementGroupGUID}/restaurants | Lists all restaurants in a management group.
*DefaultApi* | [**restaurants_restaurant_guid_get**](docs/DefaultApi.md#restaurants_restaurant_guid_get) | **GET** /restaurants/{restaurantGUID} | Returns information about the configuration of a restaurant.


## Documentation For Models

 - [DaySchedule](docs/DaySchedule.md)
 - [Delivery](docs/Delivery.md)
 - [DeliveryPaymentOptions](docs/DeliveryPaymentOptions.md)
 - [General](docs/General.md)
 - [Hours](docs/Hours.md)
 - [Image](docs/Image.md)
 - [Location](docs/Location.md)
 - [OnlineOrdering](docs/OnlineOrdering.md)
 - [PaymentOptions](docs/PaymentOptions.md)
 - [PrepTimes](docs/PrepTimes.md)
 - [Restaurant](docs/Restaurant.md)
 - [RestaurantInfo](docs/RestaurantInfo.md)
 - [Schedules](docs/Schedules.md)
 - [Service](docs/Service.md)
 - [TakeoutPaymentOptions](docs/TakeoutPaymentOptions.md)
 - [URLs](docs/URLs.md)
 - [WeekSchedule](docs/WeekSchedule.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

integrations@toasttab.com

