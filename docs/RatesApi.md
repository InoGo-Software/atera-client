# atera_client.RatesApi

All URIs are relative to *https://app.atera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rates_delete_expense**](RatesApi.md#rates_delete_expense) | **DELETE** /api/v3/rates/expenses/{expenseId} | Delete specified expense
[**rates_delete_product**](RatesApi.md#rates_delete_product) | **DELETE** /api/v3/rates/products/{productId} | Delete specified product
[**rates_expense_query_dto**](RatesApi.md#rates_expense_query_dto) | **GET** /api/v3/rates/expenses/{expenseId} | Find specified expense
[**rates_get_expenses**](RatesApi.md#rates_get_expenses) | **GET** /api/v3/rates/expenses | Find expenses
[**rates_get_products**](RatesApi.md#rates_get_products) | **GET** /api/v3/rates/products | Find products
[**rates_post_expense**](RatesApi.md#rates_post_expense) | **POST** /api/v3/rates/expenses | Create expense
[**rates_post_product**](RatesApi.md#rates_post_product) | **POST** /api/v3/rates/products | Create product
[**rates_product_query_dto**](RatesApi.md#rates_product_query_dto) | **GET** /api/v3/rates/products/{productId} | Find specified product
[**rates_put_expense**](RatesApi.md#rates_put_expense) | **PUT** /api/v3/rates/expenses/{expenseId} | Update specified expense
[**rates_put_product**](RatesApi.md#rates_put_product) | **PUT** /api/v3/rates/products/{productId} | Update specified product


# **rates_delete_expense**
> Object rates_delete_expense(expense_id)

Delete specified expense

Deletes a specified expense. Requires the expense ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.RatesApi()
expense_id = 789 # int | Required - System Expense ID

try:
    # Delete specified expense
    api_response = api_instance.rates_delete_expense(expense_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->rates_delete_expense: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expense_id** | **int**| Required - System Expense ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rates_delete_product**
> Object rates_delete_product(product_id)

Delete specified product

Deletes a specified product. Requires the product ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.RatesApi()
product_id = 789 # int | Required - System Product ID

try:
    # Delete specified product
    api_response = api_instance.rates_delete_product(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->rates_delete_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| Required - System Product ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rates_expense_query_dto**
> RateQueryDTO rates_expense_query_dto(expense_id)

Find specified expense

Returns a specified expense. Requires the expense ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.RatesApi()
expense_id = 789 # int | Required - System expense ID

try:
    # Find specified expense
    api_response = api_instance.rates_expense_query_dto(expense_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->rates_expense_query_dto: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expense_id** | **int**| Required - System expense ID | 

### Return type

[**RateQueryDTO**](RateQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rates_get_expenses**
> APIResultWrapperRateQueryDTO rates_get_expenses(page=page, items_in_page=items_in_page)

Find expenses

Returns a list of expenses.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.RatesApi()
page = 56 # int | Optional - Page index, based on items per page (default is 1) (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)

try:
    # Find expenses
    api_response = api_instance.rates_get_expenses(page=page, items_in_page=items_in_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->rates_get_expenses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional - Page index, based on items per page (default is 1) | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 

### Return type

[**APIResultWrapperRateQueryDTO**](APIResultWrapperRateQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rates_get_products**
> APIResultWrapperRateQueryDTO rates_get_products(page=page, items_in_page=items_in_page)

Find products

Returns a list of products.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.RatesApi()
page = 56 # int | Optional - Page index, based on items per page (default is 1) (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)

try:
    # Find products
    api_response = api_instance.rates_get_products(page=page, items_in_page=items_in_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->rates_get_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional - Page index, based on items per page (default is 1) | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 

### Return type

[**APIResultWrapperRateQueryDTO**](APIResultWrapperRateQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rates_post_expense**
> Result rates_post_expense(expense)

Create expense

Creates a new expense. Requires an expense description.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.RatesApi()
expense = atera_client.CreateProductExpenseRateDTO() # CreateProductExpenseRateDTO | Required - System Expense object

try:
    # Create expense
    api_response = api_instance.rates_post_expense(expense)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->rates_post_expense: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expense** | [**CreateProductExpenseRateDTO**](CreateProductExpenseRateDTO.md)| Required - System Expense object | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rates_post_product**
> Result rates_post_product(product)

Create product

Creates a new product. Requires a product description.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.RatesApi()
product = atera_client.CreateProductExpenseRateDTO() # CreateProductExpenseRateDTO | Required - System Product object

try:
    # Create product
    api_response = api_instance.rates_post_product(product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->rates_post_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | [**CreateProductExpenseRateDTO**](CreateProductExpenseRateDTO.md)| Required - System Product object | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rates_product_query_dto**
> RateQueryDTO rates_product_query_dto(product_id)

Find specified product

Returns a specified product. Requires the product ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.RatesApi()
product_id = 789 # int | Required - System product ID

try:
    # Find specified product
    api_response = api_instance.rates_product_query_dto(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->rates_product_query_dto: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| Required - System product ID | 

### Return type

[**RateQueryDTO**](RateQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rates_put_expense**
> Result rates_put_expense(expense_id, expense)

Update specified expense

Updates a specified expense. Requires the expense ID.              <br /><br />               The following fields are editable:              <br /><br />               Description              <br />              Category              <br />               Amount              <br />              SKU              <br />              Archived

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.RatesApi()
expense_id = 789 # int | Required - System Expense ID
expense = atera_client.UpdateProductExpenseRateDTO() # UpdateProductExpenseRateDTO | Required - System Expense object

try:
    # Update specified expense
    api_response = api_instance.rates_put_expense(expense_id, expense)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->rates_put_expense: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expense_id** | **int**| Required - System Expense ID | 
 **expense** | [**UpdateProductExpenseRateDTO**](UpdateProductExpenseRateDTO.md)| Required - System Expense object | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rates_put_product**
> Result rates_put_product(product_id, product)

Update specified product

Updates a specified product. Requires the product ID.              <br /><br />               The following fields are editable:              <br /><br />               Description              <br />              Category              <br />               Amount              <br />              SKU              <br />              Archived

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.RatesApi()
product_id = 789 # int | Required - System Product ID
product = atera_client.UpdateProductExpenseRateDTO() # UpdateProductExpenseRateDTO | Required - System Product object

try:
    # Update specified product
    api_response = api_instance.rates_put_product(product_id, product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->rates_put_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| Required - System Product ID | 
 **product** | [**UpdateProductExpenseRateDTO**](UpdateProductExpenseRateDTO.md)| Required - System Product object | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

