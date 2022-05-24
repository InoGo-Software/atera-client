# atera_client.ContactApi

All URIs are relative to *https://app.atera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contact_delete**](ContactApi.md#contact_delete) | **DELETE** /api/v3/contacts/{contactId} | Delete specified contact
[**contact_get**](ContactApi.md#contact_get) | **GET** /api/v3/contacts | Find Contacts
[**contact_get_0**](ContactApi.md#contact_get_0) | **GET** /api/v3/contacts/{contactId} | Find specified contact
[**contact_post**](ContactApi.md#contact_post) | **POST** /api/v3/contacts | Create contact
[**contact_put**](ContactApi.md#contact_put) | **PUT** /api/v3/contacts/{contactId} | Update specified contact
[**contact_put_0**](ContactApi.md#contact_put_0) | **POST** /api/v3/contacts/{contactId} | Update specified contact


# **contact_delete**
> Object contact_delete(contact_id)

Delete specified contact

Deletes the contact. Requires the contact ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.ContactApi()
contact_id = 789 # int | Required - System Contact ID

try:
    # Delete specified contact
    api_response = api_instance.contact_delete(contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->contact_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **int**| Required - System Contact ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_get**
> APIResultWrapperContactQueryDTO contact_get(page=page, items_in_page=items_in_page, search_options_email=search_options_email, search_options_phone=search_options_phone)

Find Contacts

Accepts whole or partial emails / phone numbers. If partial, will return all contacts whose emails / phone numbers contain the input string.              <br />              Return Contact List

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.ContactApi()
page = 56 # int | Optional - Page index (default is 1), based on items per page (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)
search_options_email = 'search_options_email_example' # str |  (optional)
search_options_phone = 'search_options_phone_example' # str |  (optional)

try:
    # Find Contacts
    api_response = api_instance.contact_get(page=page, items_in_page=items_in_page, search_options_email=search_options_email, search_options_phone=search_options_phone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->contact_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional - Page index (default is 1), based on items per page | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 
 **search_options_email** | **str**|  | [optional] 
 **search_options_phone** | **str**|  | [optional] 

### Return type

[**APIResultWrapperContactQueryDTO**](APIResultWrapperContactQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_get_0**
> ContactQueryDTO contact_get_0(contact_id)

Find specified contact

Returns the specified contact. Requires the contact ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.ContactApi()
contact_id = 789 # int | Required - System Contact ID

try:
    # Find specified contact
    api_response = api_instance.contact_get_0(contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->contact_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **int**| Required - System Contact ID | 

### Return type

[**ContactQueryDTO**](ContactQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_post**
> Result contact_post(contact)

Create contact

Creates a new contact for an existing customer. Requires the customer ID or the customer name.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.ContactApi()
contact = atera_client.CreateContactDTO() # CreateContactDTO | Required - System Contact Object

try:
    # Create contact
    api_response = api_instance.contact_post(contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->contact_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact** | [**CreateContactDTO**](CreateContactDTO.md)| Required - System Contact Object | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_put**
> Result contact_put(contact_id, contact)

Update specified contact

Updates an existing contact. Requires the contact ID.              <br /><br />               The following fields are editable:              <br /><br />               First Name (Firstname)              <br />              Last Name (Lastname)              <br />               Job Title (JobTitle)              <br />              Is Contact Person (IsContactPerson)              <br />              In Ignore Mode (InIgnoreMode)              <br />              Phone (Phone)

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.ContactApi()
contact_id = 789 # int | Required - System Contact ID
contact = atera_client.UpdateContactDTO() # UpdateContactDTO | Required - System Contact Object

try:
    # Update specified contact
    api_response = api_instance.contact_put(contact_id, contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->contact_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **int**| Required - System Contact ID | 
 **contact** | [**UpdateContactDTO**](UpdateContactDTO.md)| Required - System Contact Object | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_put_0**
> Result contact_put_0(contact_id, contact)

Update specified contact

Updates an existing contact. Requires the contact ID.              <br /><br />               The following fields are editable:              <br /><br />               First Name (Firstname)              <br />              Last Name (Lastname)              <br />               Job Title (JobTitle)              <br />              Is Contact Person (IsContactPerson)              <br />              In Ignore Mode (InIgnoreMode)              <br />              Phone (Phone)

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.ContactApi()
contact_id = 789 # int | Required - System Contact ID
contact = atera_client.UpdateContactDTO() # UpdateContactDTO | Required - System Contact Object

try:
    # Update specified contact
    api_response = api_instance.contact_put_0(contact_id, contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->contact_put_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **int**| Required - System Contact ID | 
 **contact** | [**UpdateContactDTO**](UpdateContactDTO.md)| Required - System Contact Object | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

