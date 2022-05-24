# atera_client.BillingApi

All URIs are relative to *https://app.atera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_get**](BillingApi.md#billing_get) | **GET** /api/v3/billing/invoices | Find invoices
[**billing_invoice_query_dto**](BillingApi.md#billing_invoice_query_dto) | **GET** /api/v3/billing/invoice/{invoiceNumber} | Find specified invoice


# **billing_get**
> APIResultWrapperInvoiceQueryDTO billing_get(page=page, items_in_page=items_in_page)

Find invoices

Returns a list of invoices.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.BillingApi()
page = 56 # int | Optional - Page index, based on items per page (default is 1) (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)

try:
    # Find invoices
    api_response = api_instance.billing_get(page=page, items_in_page=items_in_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional - Page index, based on items per page (default is 1) | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 

### Return type

[**APIResultWrapperInvoiceQueryDTO**](APIResultWrapperInvoiceQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_invoice_query_dto**
> InvoiceQueryDTO billing_invoice_query_dto(invoice_number)

Find specified invoice

Returns a specified invoice. Requires the invoice number.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.BillingApi()
invoice_number = 789 # int | Required - System invoice number

try:
    # Find specified invoice
    api_response = api_instance.billing_invoice_query_dto(invoice_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_invoice_query_dto: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_number** | **int**| Required - System invoice number | 

### Return type

[**InvoiceQueryDTO**](InvoiceQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

