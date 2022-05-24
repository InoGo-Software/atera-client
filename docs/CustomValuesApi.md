# atera_client.CustomValuesApi

All URIs are relative to *https://app.atera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_values_get**](CustomValuesApi.md#custom_values_get) | **GET** /api/v3/customvalues/{rowId} | Find custom field value
[**custom_values_get_agent_field**](CustomValuesApi.md#custom_values_get_agent_field) | **GET** /api/v3/customvalues/agentfield/{agentId}/{fieldName} | Find custom field value for specified agent
[**custom_values_get_contact_field**](CustomValuesApi.md#custom_values_get_contact_field) | **GET** /api/v3/customvalues/contactfield/{contactId}/{fieldName} | Find custom field value for specified contact
[**custom_values_get_contract_field**](CustomValuesApi.md#custom_values_get_contract_field) | **GET** /api/v3/customvalues/contractfield/{contractId}/{fieldName} | Find custom field value for specified contract
[**custom_values_get_custom_fields**](CustomValuesApi.md#custom_values_get_custom_fields) | **GET** /api/v3/customvalues/customfields | Get list of custom field and value options
[**custom_values_get_customer_field**](CustomValuesApi.md#custom_values_get_customer_field) | **GET** /api/v3/customvalues/customerfield/{customerId}/{fieldName} | Find custom field value for specified customer
[**custom_values_get_generic_field**](CustomValuesApi.md#custom_values_get_generic_field) | **GET** /api/v3/customvalues/genericfield/{genericDeviceId}/{fieldName} | Find custom field value for specified generic
[**custom_values_get_http_field**](CustomValuesApi.md#custom_values_get_http_field) | **GET** /api/v3/customvalues/httpfield/{httpDeviceId}/{fieldName} | Find custom field value for specified HTTP
[**custom_values_get_sla_field**](CustomValuesApi.md#custom_values_get_sla_field) | **GET** /api/v3/customvalues/slafield/{slaId}/{fieldName} | Find custom field value for specified SLA
[**custom_values_get_snmp_field**](CustomValuesApi.md#custom_values_get_snmp_field) | **GET** /api/v3/customvalues/snmpfield/{snmpDeviceId}/{fieldName} | Find custom field value for specified SNMP
[**custom_values_get_tcp_field**](CustomValuesApi.md#custom_values_get_tcp_field) | **GET** /api/v3/customvalues/tcpfield/{tcpDeviceId}/{fieldName} | Find custom field value for specified TCP
[**custom_values_get_ticket_field**](CustomValuesApi.md#custom_values_get_ticket_field) | **GET** /api/v3/customvalues/ticketfield/{ticketId}/{fieldName} | Find custom field value for specified ticket
[**custom_values_set_agent_field**](CustomValuesApi.md#custom_values_set_agent_field) | **PUT** /api/v3/customvalues/agentfield/{agentId}/{fieldName} | Set value of custom field for specified Agent
[**custom_values_set_agent_field_0**](CustomValuesApi.md#custom_values_set_agent_field_0) | **PUT** /api/v3/customvalues/agentfield/{agentId}/{fieldName}/{value} | Set value of custom field for specified Agent
[**custom_values_set_contact_field**](CustomValuesApi.md#custom_values_set_contact_field) | **PUT** /api/v3/customvalues/contactfield/{contactId}/{fieldName} | Set value of custom field for specified Contact
[**custom_values_set_contact_field_0**](CustomValuesApi.md#custom_values_set_contact_field_0) | **PUT** /api/v3/customvalues/contactfield/{contactId}/{fieldName}/{value} | Set value of custom field for specified Contact
[**custom_values_set_contract_field**](CustomValuesApi.md#custom_values_set_contract_field) | **PUT** /api/v3/customvalues/contractfield/{contractId}/{fieldName} | Set value of custom field for specified Contract
[**custom_values_set_contract_field_0**](CustomValuesApi.md#custom_values_set_contract_field_0) | **PUT** /api/v3/customvalues/contractfield/{contractId}/{fieldName}/{value} | Set value of custom field for specified Contract
[**custom_values_set_customer_field**](CustomValuesApi.md#custom_values_set_customer_field) | **PUT** /api/v3/customvalues/customerfield/{customerId}/{fieldName} | Set value of custom field for specified Customer
[**custom_values_set_customer_field_0**](CustomValuesApi.md#custom_values_set_customer_field_0) | **PUT** /api/v3/customvalues/customerfield/{customerId}/{fieldName}/{value} | Set value of custom field for specified Customer
[**custom_values_set_generic_field**](CustomValuesApi.md#custom_values_set_generic_field) | **PUT** /api/v3/customvalues/genericfield/{genericDeviceId}/{fieldName} | Set value of custom field for specified Generic
[**custom_values_set_generic_field_0**](CustomValuesApi.md#custom_values_set_generic_field_0) | **PUT** /api/v3/customvalues/genericfield/{genericDeviceId}/{fieldName}/{value} | Set value of custom field for specified Generic
[**custom_values_set_http_field**](CustomValuesApi.md#custom_values_set_http_field) | **PUT** /api/v3/customvalues/httpfield/{httpDeviceId}/{fieldName} | Set value of custom field for specified HTTP
[**custom_values_set_http_field_0**](CustomValuesApi.md#custom_values_set_http_field_0) | **PUT** /api/v3/customvalues/httpfield/{httpDeviceId}/{fieldName}/{value} | Set value of custom field for specified HTTP
[**custom_values_set_sla_field**](CustomValuesApi.md#custom_values_set_sla_field) | **PUT** /api/v3/customvalues/slafield/{slaId}/{fieldName} | Set value of custom field for specified SLA
[**custom_values_set_sla_field_0**](CustomValuesApi.md#custom_values_set_sla_field_0) | **PUT** /api/v3/customvalues/slafield/{slaId}/{fieldName}/{value} | Set value of custom field for specified SLA
[**custom_values_set_snmp_field**](CustomValuesApi.md#custom_values_set_snmp_field) | **PUT** /api/v3/customvalues/snmpfield/{snmpDeviceId}/{fieldName} | Set value of custom field for specified SNMP
[**custom_values_set_snmp_field_0**](CustomValuesApi.md#custom_values_set_snmp_field_0) | **PUT** /api/v3/customvalues/snmpfield/{snmpDeviceId}/{fieldName}/{value} | Set value of custom field for specified SNMP
[**custom_values_set_tcp_field**](CustomValuesApi.md#custom_values_set_tcp_field) | **PUT** /api/v3/customvalues/tcpfield/{tcpDeviceId}/{fieldName} | Set value of custom field for specified TCP
[**custom_values_set_tcp_field_0**](CustomValuesApi.md#custom_values_set_tcp_field_0) | **PUT** /api/v3/customvalues/tcpfield/{tcpDeviceId}/{fieldName}/{value} | Set value of custom field for specified TCP
[**custom_values_set_ticket_field**](CustomValuesApi.md#custom_values_set_ticket_field) | **PUT** /api/v3/customvalues/ticketfield/{ticketId}/{fieldName} | Set custom field value for specified Ticket
[**custom_values_set_ticket_field_0**](CustomValuesApi.md#custom_values_set_ticket_field_0) | **PUT** /api/v3/customvalues/ticketfield/{ticketId}/{fieldName}/{value} | Set custom field value for specified Ticket


# **custom_values_get**
> list[CustomValueQueryDTO] custom_values_get(row_id)

Find custom field value

Returns a custom field value. Requires a custom value ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
row_id = 'row_id_example' # str | Required - Custom Value ID

try:
    # Find custom field value
    api_response = api_instance.custom_values_get(row_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **row_id** | **str**| Required - Custom Value ID | 

### Return type

[**list[CustomValueQueryDTO]**](CustomValueQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_get_agent_field**
> list[CustomValueQueryDTO] custom_values_get_agent_field(agent_id, field_name)

Find custom field value for specified agent

Returns a custom field value for a specified agent. Requires the agent ID and custom field name.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
agent_id = 789 # int | Required - System Agent ID
field_name = 'field_name_example' # str | Required - System Custom field name

try:
    # Find custom field value for specified agent
    api_response = api_instance.custom_values_get_agent_field(agent_id, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_get_agent_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **int**| Required - System Agent ID | 
 **field_name** | **str**| Required - System Custom field name | 

### Return type

[**list[CustomValueQueryDTO]**](CustomValueQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_get_contact_field**
> list[CustomValueQueryDTO] custom_values_get_contact_field(contact_id, field_name)

Find custom field value for specified contact

Returns a custom field value for a specified contact. Requires the contact ID and custom field name.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
contact_id = 789 # int | Required - System Contact ID
field_name = 'field_name_example' # str | Required - System custom field name

try:
    # Find custom field value for specified contact
    api_response = api_instance.custom_values_get_contact_field(contact_id, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_get_contact_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **int**| Required - System Contact ID | 
 **field_name** | **str**| Required - System custom field name | 

### Return type

[**list[CustomValueQueryDTO]**](CustomValueQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_get_contract_field**
> list[CustomValueQueryDTO] custom_values_get_contract_field(contract_id, field_name)

Find custom field value for specified contract

Returns a custom field value for a specified contract. Requires the contract ID and custom field name.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
contract_id = 789 # int | Required - System contract ID
field_name = 'field_name_example' # str | Required - System custom field name

try:
    # Find custom field value for specified contract
    api_response = api_instance.custom_values_get_contract_field(contract_id, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_get_contract_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| Required - System contract ID | 
 **field_name** | **str**| Required - System custom field name | 

### Return type

[**list[CustomValueQueryDTO]**](CustomValueQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_get_custom_fields**
> list[CustomFieldQueryDTO] custom_values_get_custom_fields()

Get list of custom field and value options

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()

try:
    # Get list of custom field and value options
    api_response = api_instance.custom_values_get_custom_fields()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_get_custom_fields: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CustomFieldQueryDTO]**](CustomFieldQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_get_customer_field**
> list[CustomValueQueryDTO] custom_values_get_customer_field(customer_id, field_name)

Find custom field value for specified customer

Returns a custom field value for a specified customer. Requires a customer ID and custom field name.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
customer_id = 789 # int | Required - System Customer ID
field_name = 'field_name_example' # str | Required - System custom field name

try:
    # Find custom field value for specified customer
    api_response = api_instance.custom_values_get_customer_field(customer_id, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_get_customer_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Required - System Customer ID | 
 **field_name** | **str**| Required - System custom field name | 

### Return type

[**list[CustomValueQueryDTO]**](CustomValueQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_get_generic_field**
> list[CustomValueQueryDTO] custom_values_get_generic_field(generic_device_id, field_name)

Find custom field value for specified generic

Returns a custom field value for a specified generic. Requires the generic ID and custom field name.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
generic_device_id = 789 # int | Required - System Generic ID
field_name = 'field_name_example' # str | Required - System Custom field name

try:
    # Find custom field value for specified generic
    api_response = api_instance.custom_values_get_generic_field(generic_device_id, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_get_generic_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_device_id** | **int**| Required - System Generic ID | 
 **field_name** | **str**| Required - System Custom field name | 

### Return type

[**list[CustomValueQueryDTO]**](CustomValueQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_get_http_field**
> list[CustomValueQueryDTO] custom_values_get_http_field(http_device_id, field_name)

Find custom field value for specified HTTP

Returns a custom field value for a specified HTTP. Requires the HTTP ID and custom field name.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
http_device_id = 789 # int | Required - System HTTP ID
field_name = 'field_name_example' # str | Required - System Custom field name

try:
    # Find custom field value for specified HTTP
    api_response = api_instance.custom_values_get_http_field(http_device_id, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_get_http_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **http_device_id** | **int**| Required - System HTTP ID | 
 **field_name** | **str**| Required - System Custom field name | 

### Return type

[**list[CustomValueQueryDTO]**](CustomValueQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_get_sla_field**
> list[CustomValueQueryDTO] custom_values_get_sla_field(sla_id, field_name)

Find custom field value for specified SLA

Returns a custom field value for a specified SLA. Requires the SLA ID and custom field name.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
sla_id = 789 # int | Required - System SLA ID
field_name = 'field_name_example' # str | Required - System Custom field name

try:
    # Find custom field value for specified SLA
    api_response = api_instance.custom_values_get_sla_field(sla_id, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_get_sla_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla_id** | **int**| Required - System SLA ID | 
 **field_name** | **str**| Required - System Custom field name | 

### Return type

[**list[CustomValueQueryDTO]**](CustomValueQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_get_snmp_field**
> list[CustomValueQueryDTO] custom_values_get_snmp_field(snmp_device_id, field_name)

Find custom field value for specified SNMP

Returns a custom field value for a specified SNMP. Requires the SNMP ID and custom field name.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
snmp_device_id = 789 # int | Required - System SNMP ID
field_name = 'field_name_example' # str | Required - System Custom field name

try:
    # Find custom field value for specified SNMP
    api_response = api_instance.custom_values_get_snmp_field(snmp_device_id, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_get_snmp_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snmp_device_id** | **int**| Required - System SNMP ID | 
 **field_name** | **str**| Required - System Custom field name | 

### Return type

[**list[CustomValueQueryDTO]**](CustomValueQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_get_tcp_field**
> list[CustomValueQueryDTO] custom_values_get_tcp_field(tcp_device_id, field_name)

Find custom field value for specified TCP

Returns a custom field value for a specified TCP. Requires the TCP ID and custom field name.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
tcp_device_id = 789 # int | Required - System TCP ID
field_name = 'field_name_example' # str | Required - System Custom field name

try:
    # Find custom field value for specified TCP
    api_response = api_instance.custom_values_get_tcp_field(tcp_device_id, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_get_tcp_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tcp_device_id** | **int**| Required - System TCP ID | 
 **field_name** | **str**| Required - System Custom field name | 

### Return type

[**list[CustomValueQueryDTO]**](CustomValueQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_get_ticket_field**
> list[CustomValueQueryDTO] custom_values_get_ticket_field(ticket_id, field_name)

Find custom field value for specified ticket

Returns a custom field value for a specified ticket. Requires a ticket ID and a custom field name.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
ticket_id = 789 # int | Required - System Ticket ID
field_name = 'field_name_example' # str | Required - System custom field name

try:
    # Find custom field value for specified ticket
    api_response = api_instance.custom_values_get_ticket_field(ticket_id, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_get_ticket_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **int**| Required - System Ticket ID | 
 **field_name** | **str**| Required - System custom field name | 

### Return type

[**list[CustomValueQueryDTO]**](CustomValueQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_agent_field**
> Object custom_values_set_agent_field(agent_id, field_name, value)

Set value of custom field for specified Agent

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
agent_id = 789 # int | Required - System Agent id
field_name = 'field_name_example' # str | Required - System Custom field name
value = atera_client.SetCustomValueDTO() # SetCustomValueDTO | Required - System custom value to set

try:
    # Set value of custom field for specified Agent
    api_response = api_instance.custom_values_set_agent_field(agent_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_agent_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **int**| Required - System Agent id | 
 **field_name** | **str**| Required - System Custom field name | 
 **value** | [**SetCustomValueDTO**](SetCustomValueDTO.md)| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_agent_field_0**
> Object custom_values_set_agent_field_0(agent_id, field_name, value)

Set value of custom field for specified Agent

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
agent_id = 789 # int | Required - System Agent id
field_name = 'field_name_example' # str | Required - System Custom field name
value = 'value_example' # str | Required - System custom value to set

try:
    # Set value of custom field for specified Agent
    api_response = api_instance.custom_values_set_agent_field_0(agent_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_agent_field_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **int**| Required - System Agent id | 
 **field_name** | **str**| Required - System Custom field name | 
 **value** | **str**| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_contact_field**
> Object custom_values_set_contact_field(contact_id, field_name, value)

Set value of custom field for specified Contact

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
contact_id = 789 # int | Required - System Contact id
field_name = 'field_name_example' # str | Required - System custom field name
value = atera_client.SetCustomValueDTO() # SetCustomValueDTO | Required - System custom value to set

try:
    # Set value of custom field for specified Contact
    api_response = api_instance.custom_values_set_contact_field(contact_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_contact_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **int**| Required - System Contact id | 
 **field_name** | **str**| Required - System custom field name | 
 **value** | [**SetCustomValueDTO**](SetCustomValueDTO.md)| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_contact_field_0**
> Object custom_values_set_contact_field_0(contact_id, field_name, value)

Set value of custom field for specified Contact

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
contact_id = 789 # int | Required - System Contact id
field_name = 'field_name_example' # str | Required - System custom field name
value = 'value_example' # str | Required - System custom value to set

try:
    # Set value of custom field for specified Contact
    api_response = api_instance.custom_values_set_contact_field_0(contact_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_contact_field_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **int**| Required - System Contact id | 
 **field_name** | **str**| Required - System custom field name | 
 **value** | **str**| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_contract_field**
> Object custom_values_set_contract_field(contract_id, field_name, value)

Set value of custom field for specified Contract

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
contract_id = 789 # int | Required - System contract id
field_name = 'field_name_example' # str | Required - System custom field name
value = atera_client.SetCustomValueDTO() # SetCustomValueDTO | Required - System custom value to set

try:
    # Set value of custom field for specified Contract
    api_response = api_instance.custom_values_set_contract_field(contract_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_contract_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| Required - System contract id | 
 **field_name** | **str**| Required - System custom field name | 
 **value** | [**SetCustomValueDTO**](SetCustomValueDTO.md)| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_contract_field_0**
> Object custom_values_set_contract_field_0(contract_id, field_name, value)

Set value of custom field for specified Contract

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
contract_id = 789 # int | Required - System contract id
field_name = 'field_name_example' # str | Required - System custom field name
value = 'value_example' # str | Required - System custom value to set

try:
    # Set value of custom field for specified Contract
    api_response = api_instance.custom_values_set_contract_field_0(contract_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_contract_field_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| Required - System contract id | 
 **field_name** | **str**| Required - System custom field name | 
 **value** | **str**| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_customer_field**
> Object custom_values_set_customer_field(customer_id, field_name, value)

Set value of custom field for specified Customer

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
customer_id = 789 # int | Required - System Customer id
field_name = 'field_name_example' # str | Required - System custom field name
value = atera_client.SetCustomValueDTO() # SetCustomValueDTO | Required - System custom value to set

try:
    # Set value of custom field for specified Customer
    api_response = api_instance.custom_values_set_customer_field(customer_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_customer_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Required - System Customer id | 
 **field_name** | **str**| Required - System custom field name | 
 **value** | [**SetCustomValueDTO**](SetCustomValueDTO.md)| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_customer_field_0**
> Object custom_values_set_customer_field_0(customer_id, field_name, value)

Set value of custom field for specified Customer

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
customer_id = 789 # int | Required - System Customer id
field_name = 'field_name_example' # str | Required - System custom field name
value = 'value_example' # str | Required - System custom value to set

try:
    # Set value of custom field for specified Customer
    api_response = api_instance.custom_values_set_customer_field_0(customer_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_customer_field_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Required - System Customer id | 
 **field_name** | **str**| Required - System custom field name | 
 **value** | **str**| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_generic_field**
> Object custom_values_set_generic_field(generic_device_id, field_name, value)

Set value of custom field for specified Generic

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
generic_device_id = 789 # int | Required - System Generic id
field_name = 'field_name_example' # str | Required - System Custom field name
value = atera_client.SetCustomValueDTO() # SetCustomValueDTO | Required - System custom value to set

try:
    # Set value of custom field for specified Generic
    api_response = api_instance.custom_values_set_generic_field(generic_device_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_generic_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_device_id** | **int**| Required - System Generic id | 
 **field_name** | **str**| Required - System Custom field name | 
 **value** | [**SetCustomValueDTO**](SetCustomValueDTO.md)| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_generic_field_0**
> Object custom_values_set_generic_field_0(generic_device_id, field_name, value)

Set value of custom field for specified Generic

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
generic_device_id = 789 # int | Required - System Generic id
field_name = 'field_name_example' # str | Required - System Custom field name
value = 'value_example' # str | Required - System custom value to set

try:
    # Set value of custom field for specified Generic
    api_response = api_instance.custom_values_set_generic_field_0(generic_device_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_generic_field_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_device_id** | **int**| Required - System Generic id | 
 **field_name** | **str**| Required - System Custom field name | 
 **value** | **str**| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_http_field**
> Object custom_values_set_http_field(http_device_id, field_name, value)

Set value of custom field for specified HTTP

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
http_device_id = 789 # int | Required - System HTTP id
field_name = 'field_name_example' # str | Required - System Custom field name
value = atera_client.SetCustomValueDTO() # SetCustomValueDTO | Required - System custom value to set

try:
    # Set value of custom field for specified HTTP
    api_response = api_instance.custom_values_set_http_field(http_device_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_http_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **http_device_id** | **int**| Required - System HTTP id | 
 **field_name** | **str**| Required - System Custom field name | 
 **value** | [**SetCustomValueDTO**](SetCustomValueDTO.md)| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_http_field_0**
> Object custom_values_set_http_field_0(http_device_id, field_name, value)

Set value of custom field for specified HTTP

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
http_device_id = 789 # int | Required - System HTTP id
field_name = 'field_name_example' # str | Required - System Custom field name
value = 'value_example' # str | Required - System custom value to set

try:
    # Set value of custom field for specified HTTP
    api_response = api_instance.custom_values_set_http_field_0(http_device_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_http_field_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **http_device_id** | **int**| Required - System HTTP id | 
 **field_name** | **str**| Required - System Custom field name | 
 **value** | **str**| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_sla_field**
> Object custom_values_set_sla_field(sla_id, field_name, value)

Set value of custom field for specified SLA

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
sla_id = 789 # int | Required - System SLA id
field_name = 'field_name_example' # str | Required - System Custom field name
value = atera_client.SetCustomValueDTO() # SetCustomValueDTO | Required - System custom value to set

try:
    # Set value of custom field for specified SLA
    api_response = api_instance.custom_values_set_sla_field(sla_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_sla_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla_id** | **int**| Required - System SLA id | 
 **field_name** | **str**| Required - System Custom field name | 
 **value** | [**SetCustomValueDTO**](SetCustomValueDTO.md)| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_sla_field_0**
> Object custom_values_set_sla_field_0(sla_id, field_name, value)

Set value of custom field for specified SLA

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
sla_id = 789 # int | Required - System SLA id
field_name = 'field_name_example' # str | Required - System Custom field name
value = 'value_example' # str | Required - System custom value to set

try:
    # Set value of custom field for specified SLA
    api_response = api_instance.custom_values_set_sla_field_0(sla_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_sla_field_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla_id** | **int**| Required - System SLA id | 
 **field_name** | **str**| Required - System Custom field name | 
 **value** | **str**| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_snmp_field**
> Object custom_values_set_snmp_field(snmp_device_id, field_name, value)

Set value of custom field for specified SNMP

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
snmp_device_id = 789 # int | Required - System SNMP id
field_name = 'field_name_example' # str | Required - System Custom field name
value = atera_client.SetCustomValueDTO() # SetCustomValueDTO | Required - System custom value to set

try:
    # Set value of custom field for specified SNMP
    api_response = api_instance.custom_values_set_snmp_field(snmp_device_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_snmp_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snmp_device_id** | **int**| Required - System SNMP id | 
 **field_name** | **str**| Required - System Custom field name | 
 **value** | [**SetCustomValueDTO**](SetCustomValueDTO.md)| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_snmp_field_0**
> Object custom_values_set_snmp_field_0(snmp_device_id, field_name, value)

Set value of custom field for specified SNMP

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
snmp_device_id = 789 # int | Required - System SNMP id
field_name = 'field_name_example' # str | Required - System Custom field name
value = 'value_example' # str | Required - System custom value to set

try:
    # Set value of custom field for specified SNMP
    api_response = api_instance.custom_values_set_snmp_field_0(snmp_device_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_snmp_field_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snmp_device_id** | **int**| Required - System SNMP id | 
 **field_name** | **str**| Required - System Custom field name | 
 **value** | **str**| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_tcp_field**
> Object custom_values_set_tcp_field(tcp_device_id, field_name, value)

Set value of custom field for specified TCP

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
tcp_device_id = 789 # int | Required - System TCP id
field_name = 'field_name_example' # str | Required - System Custom field name
value = atera_client.SetCustomValueDTO() # SetCustomValueDTO | Required - System custom value to set

try:
    # Set value of custom field for specified TCP
    api_response = api_instance.custom_values_set_tcp_field(tcp_device_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_tcp_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tcp_device_id** | **int**| Required - System TCP id | 
 **field_name** | **str**| Required - System Custom field name | 
 **value** | [**SetCustomValueDTO**](SetCustomValueDTO.md)| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_tcp_field_0**
> Object custom_values_set_tcp_field_0(tcp_device_id, field_name, value)

Set value of custom field for specified TCP

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
tcp_device_id = 789 # int | Required - System TCP id
field_name = 'field_name_example' # str | Required - System Custom field name
value = 'value_example' # str | Required - System custom value to set

try:
    # Set value of custom field for specified TCP
    api_response = api_instance.custom_values_set_tcp_field_0(tcp_device_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_tcp_field_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tcp_device_id** | **int**| Required - System TCP id | 
 **field_name** | **str**| Required - System Custom field name | 
 **value** | **str**| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_ticket_field**
> Object custom_values_set_ticket_field(ticket_id, field_name, value)

Set custom field value for specified Ticket

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
ticket_id = 789 # int | Required - System Ticket id
field_name = 'field_name_example' # str | Required - System custom field name
value = atera_client.SetCustomValueDTO() # SetCustomValueDTO | Required - System custom value to set

try:
    # Set custom field value for specified Ticket
    api_response = api_instance.custom_values_set_ticket_field(ticket_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_ticket_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **int**| Required - System Ticket id | 
 **field_name** | **str**| Required - System custom field name | 
 **value** | [**SetCustomValueDTO**](SetCustomValueDTO.md)| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_values_set_ticket_field_0**
> Object custom_values_set_ticket_field_0(ticket_id, field_name, value)

Set custom field value for specified Ticket

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.CustomValuesApi()
ticket_id = 789 # int | Required - System Ticket id
field_name = 'field_name_example' # str | Required - System custom field name
value = 'value_example' # str | Required - System custom value to set

try:
    # Set custom field value for specified Ticket
    api_response = api_instance.custom_values_set_ticket_field_0(ticket_id, field_name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomValuesApi->custom_values_set_ticket_field_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **int**| Required - System Ticket id | 
 **field_name** | **str**| Required - System custom field name | 
 **value** | **str**| Required - System custom value to set | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

