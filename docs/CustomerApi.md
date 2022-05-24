# atera_client.CustomerApi

All URIs are relative to *https://app.atera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_delete**](CustomerApi.md#customer_delete) | **DELETE** /api/v3/customers/{customerId} | Delete specified customer
[**customer_get**](CustomerApi.md#customer_get) | **GET** /api/v3/customers | Find Customers
[**customer_get_0**](CustomerApi.md#customer_get_0) | **GET** /api/v3/customers/{customerId} | Find specified customer
[**customer_post**](CustomerApi.md#customer_post) | **POST** /api/v3/customers | Create Customer
[**customer_post_0**](CustomerApi.md#customer_post_0) | **POST** /api/v3/customers/folders | Create Customer Folder
[**customer_post_1**](CustomerApi.md#customer_post_1) | **POST** /api/v3/customers/attachments | Create Customer Attachment
[**customer_put**](CustomerApi.md#customer_put) | **PUT** /api/v3/customers/{customerId} | Update specified customer
[**customer_put_0**](CustomerApi.md#customer_put_0) | **POST** /api/v3/customers/{customerId} | Update specified customer


# **customer_delete**
> Object customer_delete(customer_id)

Delete specified customer

Deletes a specified customer. Requires the customer ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomerApi()
customer_id = 789 # int | Required

try:
    # Delete specified customer
    api_response = api_instance.customer_delete(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Required | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_get**
> APIResultWrapperCustomerQueryDTO customer_get(page=page, items_in_page=items_in_page)

Find Customers

Returns a list of customers.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomerApi()
page = 56 # int | Optional - Page index, based on items per page (default is 1) (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)

try:
    # Find Customers
    api_response = api_instance.customer_get(page=page, items_in_page=items_in_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional - Page index, based on items per page (default is 1) | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 

### Return type

[**APIResultWrapperCustomerQueryDTO**](APIResultWrapperCustomerQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_get_0**
> CustomerQueryDTO customer_get_0(customer_id)

Find specified customer

Returns a specified customer. Requires the customer ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomerApi()
customer_id = 56 # int | Required

try:
    # Find specified customer
    api_response = api_instance.customer_get_0(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Required | 

### Return type

[**CustomerQueryDTO**](CustomerQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_post**
> Result customer_post(customer)

Create Customer

Creates a new customer. Requires the customer name.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomerApi()
customer = atera_client.CreateCustomerDTO() # CreateCustomerDTO | Required

try:
    # Create Customer
    api_response = api_instance.customer_post(customer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | [**CreateCustomerDTO**](CreateCustomerDTO.md)| Required | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_post_0**
> Result customer_post_0(folder)

Create Customer Folder

Requires the folder name and customer ID.              Threshold profile ID is optional; if not included, the folder will inherit the threshold profile applied to the customer, if applicable.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomerApi()
folder = atera_client.CreateCustomerFolderDTO() # CreateCustomerFolderDTO | Required

try:
    # Create Customer Folder
    api_response = api_instance.customer_post_0(folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | [**CreateCustomerFolderDTO**](CreateCustomerFolderDTO.md)| Required | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_post_1**
> Result customer_post_1(attachment)

Create Customer Attachment

Requires the customer ID and attachment name, including the file extension. Requires attachment to be represented in Base64 encoding.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomerApi()
attachment = atera_client.CreateCustomerAttachmentDTO() # CreateCustomerAttachmentDTO | Required

try:
    # Create Customer Attachment
    api_response = api_instance.customer_post_1(attachment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_post_1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment** | [**CreateCustomerAttachmentDTO**](CreateCustomerAttachmentDTO.md)| Required | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_put**
> Result customer_put(customer_id, customer)

Update specified customer

Updates an existing customer. Requires the customer ID.              <br /><br />               The following fields are editable:              <br /><br />               Customer Name (CustomerName)              <br />              Business Number (BusinessNumber)              <br />               Domain (Domain)              <br />              Address (Address)              <br />              City (City)              <br />              State (State)              <br />              Country (Country)              <br />              Phone (Phone)              <br />              Fax (Fax)              <br />              Notes (Notes)              <br />              Links (Links)              <br />              Longitude (Longitude)              <br />              Latitude (Latitude)              <br />              Zip Code (ZipCodeStr)

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomerApi()
customer_id = 789 # int | Required
customer = atera_client.UpdateCustomerDTO() # UpdateCustomerDTO | Required

try:
    # Update specified customer
    api_response = api_instance.customer_put(customer_id, customer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Required | 
 **customer** | [**UpdateCustomerDTO**](UpdateCustomerDTO.md)| Required | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_put_0**
> Result customer_put_0(customer_id, customer)

Update specified customer

Updates an existing customer. Requires the customer ID.              <br /><br />               The following fields are editable:              <br /><br />               Customer Name (CustomerName)              <br />              Business Number (BusinessNumber)              <br />               Domain (Domain)              <br />              Address (Address)              <br />              City (City)              <br />              State (State)              <br />              Country (Country)              <br />              Phone (Phone)              <br />              Fax (Fax)              <br />              Notes (Notes)              <br />              Links (Links)              <br />              Longitude (Longitude)              <br />              Latitude (Latitude)              <br />              Zip Code (ZipCodeStr)

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomerApi()
customer_id = 789 # int | Required
customer = atera_client.UpdateCustomerDTO() # UpdateCustomerDTO | Required

try:
    # Update specified customer
    api_response = api_instance.customer_put_0(customer_id, customer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_put_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Required | 
 **customer** | [**UpdateCustomerDTO**](UpdateCustomerDTO.md)| Required | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

