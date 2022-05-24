# atera_client.ContractsApi

All URIs are relative to *https://app.atera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contracts_contract_query_dto**](ContractsApi.md#contracts_contract_query_dto) | **GET** /api/v3/contracts/{contractId} | Find specified contract
[**contracts_get**](ContractsApi.md#contracts_get) | **GET** /api/v3/contracts | Find contracts
[**contracts_get_by_customer**](ContractsApi.md#contracts_get_by_customer) | **GET** /api/v3/contracts/customer/{customerId} | Find contracts for specified customer


# **contracts_contract_query_dto**
> ContractQueryDTO contracts_contract_query_dto(contract_id)

Find specified contract

Returns a specified contract. Requires the contract ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.ContractsApi()
contract_id = 789 # int | Required. System contract ID

try:
    # Find specified contract
    api_response = api_instance.contracts_contract_query_dto(contract_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_contract_query_dto: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| Required. System contract ID | 

### Return type

[**ContractQueryDTO**](ContractQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get**
> APIResultWrapperContractQueryDTO contracts_get(page=page, items_in_page=items_in_page)

Find contracts

Returns a list of contracts.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.ContractsApi()
page = 56 # int | Optional - Page index, based on items per page (default is 1) (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)

try:
    # Find contracts
    api_response = api_instance.contracts_get(page=page, items_in_page=items_in_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional - Page index, based on items per page (default is 1) | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 

### Return type

[**APIResultWrapperContractQueryDTO**](APIResultWrapperContractQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_by_customer**
> APIResultWrapperContractQueryDTO contracts_get_by_customer(customer_id, page=page, items_in_page=items_in_page)

Find contracts for specified customer

Returns a list of contracts. Requires the customer ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.ContractsApi()
customer_id = 789 # int | Required - System customer ID
page = 56 # int | Optional - Page index, based on items per page (default is 1) (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)

try:
    # Find contracts for specified customer
    api_response = api_instance.contracts_get_by_customer(customer_id, page=page, items_in_page=items_in_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_by_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Required - System customer ID | 
 **page** | **int**| Optional - Page index, based on items per page (default is 1) | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 

### Return type

[**APIResultWrapperContractQueryDTO**](APIResultWrapperContractQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

