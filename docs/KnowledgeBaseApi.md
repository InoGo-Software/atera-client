# atera_client.KnowledgeBaseApi

All URIs are relative to *https://app.atera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**knowledge_base_get**](KnowledgeBaseApi.md#knowledge_base_get) | **GET** /api/v3/knowledgebases | Find articles


# **knowledge_base_get**
> APIResultWrapperKnowledgeBaseQueryDTO knowledge_base_get(page=page, items_in_page=items_in_page)

Find articles

Returns a list of articles.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.KnowledgeBaseApi()
page = 56 # int | Optional - Page index (default is 1), based on items per page (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)

try:
    # Find articles
    api_response = api_instance.knowledge_base_get(page=page, items_in_page=items_in_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeBaseApi->knowledge_base_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional - Page index (default is 1), based on items per page | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 

### Return type

[**APIResultWrapperKnowledgeBaseQueryDTO**](APIResultWrapperKnowledgeBaseQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

