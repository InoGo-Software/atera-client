# atera_client.TicketApi

All URIs are relative to *https://app.atera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ticket_delete**](TicketApi.md#ticket_delete) | **DELETE** /api/v3/tickets/{ticketId} | Delete specified ticket
[**ticket_get**](TicketApi.md#ticket_get) | **GET** /api/v3/tickets | Find tickets
[**ticket_get_0**](TicketApi.md#ticket_get_0) | **GET** /api/v3/tickets/{ticketId} | Find specified ticket
[**ticket_get_billable_duration**](TicketApi.md#ticket_get_billable_duration) | **GET** /api/v3/tickets/{ticketId}/billableduration | Find specified ticket (billable duration)
[**ticket_get_comments**](TicketApi.md#ticket_get_comments) | **GET** /api/v3/tickets/{ticketId}/comments | Find ticket comments list
[**ticket_get_non_billable_duration**](TicketApi.md#ticket_get_non_billable_duration) | **GET** /api/v3/tickets/{ticketId}/nonbillableduration | Find specified ticket (non-billable duration)
[**ticket_get_workhours**](TicketApi.md#ticket_get_workhours) | **GET** /api/v3/tickets/{ticketId}/workhours | Find specified ticket (workhours duration)
[**ticket_get_workhours_records**](TicketApi.md#ticket_get_workhours_records) | **GET** /api/v3/tickets/{ticketId}/workhoursrecords | Find tickets (workhour list)
[**ticket_post**](TicketApi.md#ticket_post) | **POST** /api/v3/tickets | Create ticket
[**ticket_put**](TicketApi.md#ticket_put) | **PUT** /api/v3/tickets/{ticketId} | Update specified ticket
[**ticket_put_0**](TicketApi.md#ticket_put_0) | **POST** /api/v3/tickets/{ticketId} | Update specified ticket
[**ticket_track_status_modified**](TicketApi.md#ticket_track_status_modified) | **GET** /api/v3/tickets/statusmodified | Find resolved and closed tickets


# **ticket_delete**
> Object ticket_delete(ticket_id)

Delete specified ticket

Deletes the specified ticket. Requires the ticket ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.TicketApi()
ticket_id = 789 # int | Required - System Ticket ID

try:
    # Delete specified ticket
    api_response = api_instance.ticket_delete(ticket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketApi->ticket_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **int**| Required - System Ticket ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_get**
> APIResultWrapperTicketQueryDTO ticket_get(page=page, items_in_page=items_in_page, customer_id=customer_id, ticket_status=ticket_status)

Find tickets

Returns a list of tickets.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.TicketApi()
page = 56 # int | Optional - Page index (default is 1), based on items per page (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)
customer_id = 789 # int |  (optional)
ticket_status = 'ticket_status_example' # str |  (optional)

try:
    # Find tickets
    api_response = api_instance.ticket_get(page=page, items_in_page=items_in_page, customer_id=customer_id, ticket_status=ticket_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketApi->ticket_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional - Page index (default is 1), based on items per page | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 
 **customer_id** | **int**|  | [optional] 
 **ticket_status** | **str**|  | [optional] 

### Return type

[**APIResultWrapperTicketQueryDTO**](APIResultWrapperTicketQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_get_0**
> TicketQueryDTO ticket_get_0(ticket_id)

Find specified ticket

Returns the specified ticket. Requires the ticket ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.TicketApi()
ticket_id = 789 # int | Required - System Ticket ID

try:
    # Find specified ticket
    api_response = api_instance.ticket_get_0(ticket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketApi->ticket_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **int**| Required - System Ticket ID | 

### Return type

[**TicketQueryDTO**](TicketQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_get_billable_duration**
> TicketDurationQueryDTO ticket_get_billable_duration(ticket_id)

Find specified ticket (billable duration)

Returns the specified ticket (billable duration). Requires the ticket ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.TicketApi()
ticket_id = 789 # int | Required - System Ticket ID

try:
    # Find specified ticket (billable duration)
    api_response = api_instance.ticket_get_billable_duration(ticket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketApi->ticket_get_billable_duration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **int**| Required - System Ticket ID | 

### Return type

[**TicketDurationQueryDTO**](TicketDurationQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_get_comments**
> APIResultWrapperTicketCommentQueryDTO ticket_get_comments(ticket_id, page=page, items_in_page=items_in_page)

Find ticket comments list

Returns the ticket comments. Requires the ticket ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.TicketApi()
ticket_id = 789 # int | Required - System Ticket ID
page = 56 # int | Optional - Page index (default is 1), based on items per page (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)

try:
    # Find ticket comments list
    api_response = api_instance.ticket_get_comments(ticket_id, page=page, items_in_page=items_in_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketApi->ticket_get_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **int**| Required - System Ticket ID | 
 **page** | **int**| Optional - Page index (default is 1), based on items per page | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 

### Return type

[**APIResultWrapperTicketCommentQueryDTO**](APIResultWrapperTicketCommentQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_get_non_billable_duration**
> TicketDurationQueryDTO ticket_get_non_billable_duration(ticket_id)

Find specified ticket (non-billable duration)

Returns the specified ticket (non-billable duration). Requires the ticket ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.TicketApi()
ticket_id = 789 # int | Required - System Ticket ID

try:
    # Find specified ticket (non-billable duration)
    api_response = api_instance.ticket_get_non_billable_duration(ticket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketApi->ticket_get_non_billable_duration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **int**| Required - System Ticket ID | 

### Return type

[**TicketDurationQueryDTO**](TicketDurationQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_get_workhours**
> TicketTimeEntriesSummaryQueryDTO ticket_get_workhours(ticket_id)

Find specified ticket (workhours duration)

Returns a record of the specified ticket's billable and non-billable workhours. Requires the ticket ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.TicketApi()
ticket_id = 789 # int | Required - System Ticket ID

try:
    # Find specified ticket (workhours duration)
    api_response = api_instance.ticket_get_workhours(ticket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketApi->ticket_get_workhours: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **int**| Required - System Ticket ID | 

### Return type

[**TicketTimeEntriesSummaryQueryDTO**](TicketTimeEntriesSummaryQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_get_workhours_records**
> APIResultWrapperTicketTimeEntriesQueryDTO ticket_get_workhours_records(ticket_id, page=page, items_in_page=items_in_page)

Find tickets (workhour list)

Returns the ticket's workhours. Requires the ticket ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.TicketApi()
ticket_id = 789 # int | Required - System Ticket ID
page = 56 # int | Optional - Page index (default is 1), based on items per page (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)

try:
    # Find tickets (workhour list)
    api_response = api_instance.ticket_get_workhours_records(ticket_id, page=page, items_in_page=items_in_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketApi->ticket_get_workhours_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **int**| Required - System Ticket ID | 
 **page** | **int**| Optional - Page index (default is 1), based on items per page | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 

### Return type

[**APIResultWrapperTicketTimeEntriesQueryDTO**](APIResultWrapperTicketTimeEntriesQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_post**
> Result ticket_post(ticket)

Create ticket

Creates a new ticket. Requires the enduser contact ID, title, and description.              <br /><br />               If you wish to create a new enduser for the ticket then you need to provide:              <br /><br />               Contact first name (EndUserFirstName)              <br />               Contact last name (EndUserLastName)              <br />               Email (EndUserEmail)

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.TicketApi()
ticket = atera_client.CreateTicketDTO() # CreateTicketDTO | Required - System Ticket object

try:
    # Create ticket
    api_response = api_instance.ticket_post(ticket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketApi->ticket_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket** | [**CreateTicketDTO**](CreateTicketDTO.md)| Required - System Ticket object | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_put**
> Result ticket_put(ticket_id, ticket)

Update specified ticket

Updates an existing ticket. Requires the ticket ID.              <br /><br />               The following fields are editable:              <br /><br />               Ticket Title (TicketTitle)              <br />              Ticket Status (TicketStatus)              <br />               Ticket Type (TicketType)              <br />              Ticket Priority (TicketPriority)              <br />              Ticket Impact (TicketImpact)              <br />              Assigned Technician ID (TechnicianContactID)

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.TicketApi()
ticket_id = 789 # int | Required - System Ticket ID
ticket = atera_client.UpdateTicketDTO() # UpdateTicketDTO | Required - System Ticket object

try:
    # Update specified ticket
    api_response = api_instance.ticket_put(ticket_id, ticket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketApi->ticket_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **int**| Required - System Ticket ID | 
 **ticket** | [**UpdateTicketDTO**](UpdateTicketDTO.md)| Required - System Ticket object | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_put_0**
> Result ticket_put_0(ticket_id, ticket)

Update specified ticket

Updates an existing ticket. Requires the ticket ID.              <br /><br />               The following fields are editable:              <br /><br />               Ticket Title (TicketTitle)              <br />              Ticket Status (TicketStatus)              <br />               Ticket Type (TicketType)              <br />              Ticket Priority (TicketPriority)              <br />              Ticket Impact (TicketImpact)              <br />              Assigned Technician ID (TechnicianContactID)

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.TicketApi()
ticket_id = 789 # int | Required - System Ticket ID
ticket = atera_client.UpdateTicketDTO() # UpdateTicketDTO | Required - System Ticket object

try:
    # Update specified ticket
    api_response = api_instance.ticket_put_0(ticket_id, ticket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketApi->ticket_put_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **int**| Required - System Ticket ID | 
 **ticket** | [**UpdateTicketDTO**](UpdateTicketDTO.md)| Required - System Ticket object | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_track_status_modified**
> APIResultWrapperTicketQueryDTO ticket_track_status_modified(page=page, items_in_page=items_in_page)

Find resolved and closed tickets

Returns a list of resolved and closed tickets.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.TicketApi()
page = 56 # int | Optional - Page index (default is 1), based on items per page (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)

try:
    # Find resolved and closed tickets
    api_response = api_instance.ticket_track_status_modified(page=page, items_in_page=items_in_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketApi->ticket_track_status_modified: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional - Page index (default is 1), based on items per page | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 

### Return type

[**APIResultWrapperTicketQueryDTO**](APIResultWrapperTicketQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

