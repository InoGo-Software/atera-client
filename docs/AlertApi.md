# atera_client.AlertApi

All URIs are relative to *https://app.atera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alert_delete**](AlertApi.md#alert_delete) | **DELETE** /api/v3/alerts/{alertId} | Delete specified alert
[**alert_get**](AlertApi.md#alert_get) | **GET** /api/v3/alerts | Find alerts
[**alert_get_0**](AlertApi.md#alert_get_0) | **GET** /api/v3/alerts/{alertId} | Find specified alert
[**alert_post**](AlertApi.md#alert_post) | **POST** /api/v3/alerts | Create alert


# **alert_delete**
> Object alert_delete(alert_id)

Delete specified alert

Deletes a specified alert. Requires the alert ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.AlertApi()
alert_id = 789 # int | Required - System alert ID

try:
    # Delete specified alert
    api_response = api_instance.alert_delete(alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->alert_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| Required - System alert ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_get**
> APIResultWrapperAlertQueryDTO alert_get(page=page, items_in_page=items_in_page, alert_status=alert_status)

Find alerts

Returns a list of alerts.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.AlertApi()
page = 56 # int | Optional - Page index, based on items per page (default is 20) (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20) (optional)
alert_status = 'alert_status_example' # str |  (optional)

try:
    # Find alerts
    api_response = api_instance.alert_get(page=page, items_in_page=items_in_page, alert_status=alert_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->alert_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional - Page index, based on items per page (default is 20) | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20) | [optional] 
 **alert_status** | **str**|  | [optional] 

### Return type

[**APIResultWrapperAlertQueryDTO**](APIResultWrapperAlertQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_get_0**
> AlertQueryDTO alert_get_0(alert_id)

Find specified alert

Returns an alert. Requires the alert ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.AlertApi()
alert_id = 789 # int | Required - System alert ID

try:
    # Find specified alert
    api_response = api_instance.alert_get_0(alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->alert_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| Required - System alert ID | 

### Return type

[**AlertQueryDTO**](AlertQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_post**
> Result alert_post(alert)

Create alert

Creates a new alert. Requires the device's global unique identifier (GUID).

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.AlertApi()
alert = atera_client.CreateAlertDTO() # CreateAlertDTO | Required - System alert object

try:
    # Create alert
    api_response = api_instance.alert_post(alert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->alert_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert** | [**CreateAlertDTO**](CreateAlertDTO.md)| Required - System alert object | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

