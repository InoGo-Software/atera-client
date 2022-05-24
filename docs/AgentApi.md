# atera_client.AgentApi

All URIs are relative to *https://app.atera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_agent_query_dto**](AgentApi.md#agent_agent_query_dto) | **GET** /api/v3/agents/{agentId} | Get specified agent
[**agent_delete**](AgentApi.md#agent_delete) | **DELETE** /api/v3/agents/{agentId} | Delete specified agent
[**agent_get**](AgentApi.md#agent_get) | **GET** /api/v3/agents | Find agents
[**agent_get_agents_by_machine_name**](AgentApi.md#agent_get_agents_by_machine_name) | **GET** /api/v3/agents/machine/{machineName} | Get agents for specified machine.
[**agent_get_by_customer**](AgentApi.md#agent_get_by_customer) | **GET** /api/v3/agents/customer/{customerId} | Find agents for specified customer


# **agent_agent_query_dto**
> AgentQueryDTO agent_agent_query_dto(agent_id)

Get specified agent

Returns an agent. Requires the agent ID.              <br />               Please note that the property 'LastPatchManagementReceived' is no longer supported and will return a null reference.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.AgentApi()
agent_id = 789 # int | Required - System agent ID

try:
    # Get specified agent
    api_response = api_instance.agent_agent_query_dto(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->agent_agent_query_dto: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **int**| Required - System agent ID | 

### Return type

[**AgentQueryDTO**](AgentQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_delete**
> Object agent_delete(agent_id)

Delete specified agent

Deletes an agent. Requires the agent ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.AgentApi()
agent_id = 789 # int | Required - System agent ID

try:
    # Delete specified agent
    api_response = api_instance.agent_delete(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->agent_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **int**| Required - System agent ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_get**
> APIResultWrapperAgentQueryDTO agent_get(page=page, items_in_page=items_in_page)

Find agents

Returns a list of agents.              <br />               Please note that the property 'LastPatchManagementReceived' is no longer supported and will return a null reference.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.AgentApi()
page = 56 # int | Optional - Page index, based on items per page (default is 1) (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)

try:
    # Find agents
    api_response = api_instance.agent_get(page=page, items_in_page=items_in_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->agent_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional - Page index, based on items per page (default is 1) | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 

### Return type

[**APIResultWrapperAgentQueryDTO**](APIResultWrapperAgentQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_get_agents_by_machine_name**
> APIResultWrapperAgentQueryDTO agent_get_agents_by_machine_name(machine_name, page=page, items_in_page=items_in_page)

Get agents for specified machine.

Returns agents installed on a specified machine. Requires the machine name.              <br />               Please note that the property 'LastPatchManagementReceived' is no longer supported and will return a null reference.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.AgentApi()
machine_name = 'machine_name_example' # str | Required - System machine name
page = 56 # int | Optional - Page index (based on items per page) (optional)
items_in_page = 56 # int | Optional - Number of items per page. Default is 20 (optional)

try:
    # Get agents for specified machine.
    api_response = api_instance.agent_get_agents_by_machine_name(machine_name, page=page, items_in_page=items_in_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->agent_get_agents_by_machine_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **machine_name** | **str**| Required - System machine name | 
 **page** | **int**| Optional - Page index (based on items per page) | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page. Default is 20 | [optional] 

### Return type

[**APIResultWrapperAgentQueryDTO**](APIResultWrapperAgentQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_get_by_customer**
> APIResultWrapperAgentQueryDTO agent_get_by_customer(customer_id, page=page, items_in_page=items_in_page)

Find agents for specified customer

Returns agents for a specified customer. Requires the customer ID.              <br />               Please note that the property 'LastPatchManagementReceived' is no longer supported and will return a null reference.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.AgentApi()
customer_id = 789 # int | Required - Customer ID
page = 56 # int | Optional - Page index, based on items per page (default is 1) (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)

try:
    # Find agents for specified customer
    api_response = api_instance.agent_get_by_customer(customer_id, page=page, items_in_page=items_in_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->agent_get_by_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Required - Customer ID | 
 **page** | **int**| Optional - Page index, based on items per page (default is 1) | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 

### Return type

[**APIResultWrapperAgentQueryDTO**](APIResultWrapperAgentQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

