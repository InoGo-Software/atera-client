# atera_client.DeviceApi

All URIs are relative to *https://app.atera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_create_generic_device**](DeviceApi.md#device_create_generic_device) | **POST** /api/v3/devices/genericdevice | Create Generic device
[**device_create_http_device**](DeviceApi.md#device_create_http_device) | **POST** /api/v3/devices/httpdevice | Create HTTP device
[**device_create_snmp_device_v1_v2**](DeviceApi.md#device_create_snmp_device_v1_v2) | **POST** /api/v3/devices/snmpdevice/v1v2 | Create SNMP device V1/V2
[**device_create_snmp_device_v3**](DeviceApi.md#device_create_snmp_device_v3) | **POST** /api/v3/devices/snmpdevice/v3 | Create SNMP device V3
[**device_create_tcp_device**](DeviceApi.md#device_create_tcp_device) | **POST** /api/v3/devices/tcpdevice | Create TCP device
[**device_delete**](DeviceApi.md#device_delete) | **DELETE** /api/v3/devices/genericdevice/{deviceId} | Delete specified Generic device
[**device_delete_http**](DeviceApi.md#device_delete_http) | **DELETE** /api/v3/devices/httpdevice/{deviceId} | Delete specified HTTP device
[**device_delete_snmp**](DeviceApi.md#device_delete_snmp) | **DELETE** /api/v3/devices/snmpdevice/{deviceId} | Delete specified SNMP device
[**device_delete_tcp**](DeviceApi.md#device_delete_tcp) | **DELETE** /api/v3/devices/tcpdevice/{deviceId} | Delete specified TCP device
[**device_get_generic_device**](DeviceApi.md#device_get_generic_device) | **GET** /api/v3/devices/genericdevice/{deviceId} | Find specified Generic device
[**device_get_generic_devices**](DeviceApi.md#device_get_generic_devices) | **GET** /api/v3/devices/genericdevices | Find Generic devices
[**device_get_http_device**](DeviceApi.md#device_get_http_device) | **GET** /api/v3/devices/httpdevice/{deviceId} | Find specified HTTP device
[**device_get_http_devices**](DeviceApi.md#device_get_http_devices) | **GET** /api/v3/devices/httpdevices | Find HTTP devices
[**device_get_snmp_device**](DeviceApi.md#device_get_snmp_device) | **GET** /api/v3/devices/snmpdevice/{deviceId} | Find specified SNMP device
[**device_get_snmp_devices**](DeviceApi.md#device_get_snmp_devices) | **GET** /api/v3/devices/snmpdevices | Find SNMP devices
[**device_get_tcp_device**](DeviceApi.md#device_get_tcp_device) | **GET** /api/v3/devices/tcpdevice/{deviceId} | Find specified TCP device
[**device_get_tcp_devices**](DeviceApi.md#device_get_tcp_devices) | **GET** /api/v3/devices/tcpdevices | Find TCP devices


# **device_create_generic_device**
> CreatedDeviceRes device_create_generic_device(request)

Create Generic device

Returns device ID and Device Guid.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
request = atera_client.CreateGenericDTO() # CreateGenericDTO | Required - new device params

try:
    # Create Generic device
    api_response = api_instance.device_create_generic_device(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_create_generic_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateGenericDTO**](CreateGenericDTO.md)| Required - new device params | 

### Return type

[**CreatedDeviceRes**](CreatedDeviceRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_create_http_device**
> CreatedDeviceRes device_create_http_device(request)

Create HTTP device

Returns device ID and Device Guid.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
request = atera_client.CreateHttpDTO() # CreateHttpDTO | Required - new device params

try:
    # Create HTTP device
    api_response = api_instance.device_create_http_device(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_create_http_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateHttpDTO**](CreateHttpDTO.md)| Required - new device params | 

### Return type

[**CreatedDeviceRes**](CreatedDeviceRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_create_snmp_device_v1_v2**
> CreatedDeviceRes device_create_snmp_device_v1_v2(request)

Create SNMP device V1/V2

Returns device ID and Device Guid.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
request = atera_client.CreateSNMPDTOV1V2() # CreateSNMPDTOV1V2 | Required - new device params

try:
    # Create SNMP device V1/V2
    api_response = api_instance.device_create_snmp_device_v1_v2(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_create_snmp_device_v1_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateSNMPDTOV1V2**](CreateSNMPDTOV1V2.md)| Required - new device params | 

### Return type

[**CreatedDeviceRes**](CreatedDeviceRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_create_snmp_device_v3**
> CreatedDeviceRes device_create_snmp_device_v3(request)

Create SNMP device V3

Returns device ID and Device Guid.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
request = atera_client.CreateSNMPDTOV3() # CreateSNMPDTOV3 | Required - new device params

try:
    # Create SNMP device V3
    api_response = api_instance.device_create_snmp_device_v3(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_create_snmp_device_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateSNMPDTOV3**](CreateSNMPDTOV3.md)| Required - new device params | 

### Return type

[**CreatedDeviceRes**](CreatedDeviceRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_create_tcp_device**
> CreatedDeviceRes device_create_tcp_device(request)

Create TCP device

Returns device ID and Device Guid.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
request = atera_client.CreateTCPDTO() # CreateTCPDTO | Required - new device params

try:
    # Create TCP device
    api_response = api_instance.device_create_tcp_device(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_create_tcp_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateTCPDTO**](CreateTCPDTO.md)| Required - new device params | 

### Return type

[**CreatedDeviceRes**](CreatedDeviceRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_delete**
> Object device_delete(device_id)

Delete specified Generic device

Deletes a Generic device. Requires the device ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
device_id = 789 # int | Required - System Device ID

try:
    # Delete specified Generic device
    api_response = api_instance.device_delete(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Required - System Device ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_delete_http**
> Object device_delete_http(device_id)

Delete specified HTTP device

Deletes an HTTP device. Requires the device ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
device_id = 789 # int | Required - System Device ID

try:
    # Delete specified HTTP device
    api_response = api_instance.device_delete_http(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_delete_http: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Required - System Device ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_delete_snmp**
> Object device_delete_snmp(device_id)

Delete specified SNMP device

Deletes an SNMP device. Requires the device ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
device_id = 789 # int | Required - System Device ID

try:
    # Delete specified SNMP device
    api_response = api_instance.device_delete_snmp(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_delete_snmp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Required - System Device ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_delete_tcp**
> Object device_delete_tcp(device_id)

Delete specified TCP device

Deletes a TCP device. Requires the device ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
device_id = 789 # int | Required - System Device ID

try:
    # Delete specified TCP device
    api_response = api_instance.device_delete_tcp(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_delete_tcp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Required - System Device ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_get_generic_device**
> GenericDeviceQueryDTO device_get_generic_device(device_id)

Find specified Generic device

Returns a Generic device. Requires the device ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
device_id = 789 # int | Required - System Device ID

try:
    # Find specified Generic device
    api_response = api_instance.device_get_generic_device(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_get_generic_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Required - System Device ID | 

### Return type

[**GenericDeviceQueryDTO**](GenericDeviceQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_get_generic_devices**
> APIResultWrapperGenericDeviceQueryDTO device_get_generic_devices(page=page, items_in_page=items_in_page, customer_id=customer_id, monitoring_agent_id=monitoring_agent_id)

Find Generic devices

Returns a list of Generic devices.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
page = 56 # int | Optional - Page index (default is 1), based on items per page (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)
customer_id = 789 # int | Optional - Customer ID (default is NULL) (optional)
monitoring_agent_id = 789 # int | Optional - Monitoring Agent ID (default is NULL) (optional)

try:
    # Find Generic devices
    api_response = api_instance.device_get_generic_devices(page=page, items_in_page=items_in_page, customer_id=customer_id, monitoring_agent_id=monitoring_agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_get_generic_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional - Page index (default is 1), based on items per page | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 
 **customer_id** | **int**| Optional - Customer ID (default is NULL) | [optional] 
 **monitoring_agent_id** | **int**| Optional - Monitoring Agent ID (default is NULL) | [optional] 

### Return type

[**APIResultWrapperGenericDeviceQueryDTO**](APIResultWrapperGenericDeviceQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_get_http_device**
> HttpDeviceQueryDTO device_get_http_device(device_id)

Find specified HTTP device

Returns an HTTP device. Requires the device ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
device_id = 789 # int | Required - System Device ID

try:
    # Find specified HTTP device
    api_response = api_instance.device_get_http_device(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_get_http_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Required - System Device ID | 

### Return type

[**HttpDeviceQueryDTO**](HttpDeviceQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_get_http_devices**
> APIResultWrapperHttpDeviceQueryDTO device_get_http_devices(page=page, items_in_page=items_in_page, customer_id=customer_id, monitoring_agent_id=monitoring_agent_id)

Find HTTP devices

Returns a list of HTTP devices.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
page = 56 # int | Optional - Page index (default is 1), based on items per page (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)
customer_id = 789 # int | Optional - Customer ID (default is NULL) (optional)
monitoring_agent_id = 789 # int | Optional - Monitoring Agent ID (default is NULL) (optional)

try:
    # Find HTTP devices
    api_response = api_instance.device_get_http_devices(page=page, items_in_page=items_in_page, customer_id=customer_id, monitoring_agent_id=monitoring_agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_get_http_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional - Page index (default is 1), based on items per page | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 
 **customer_id** | **int**| Optional - Customer ID (default is NULL) | [optional] 
 **monitoring_agent_id** | **int**| Optional - Monitoring Agent ID (default is NULL) | [optional] 

### Return type

[**APIResultWrapperHttpDeviceQueryDTO**](APIResultWrapperHttpDeviceQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_get_snmp_device**
> SNMPDeviceQueryDTO device_get_snmp_device(device_id)

Find specified SNMP device

Returns an SNMP device. Requires the device ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
device_id = 789 # int | Required - System Device ID

try:
    # Find specified SNMP device
    api_response = api_instance.device_get_snmp_device(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_get_snmp_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Required - System Device ID | 

### Return type

[**SNMPDeviceQueryDTO**](SNMPDeviceQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_get_snmp_devices**
> APIResultWrapperSNMPDeviceQueryDTO device_get_snmp_devices(page=page, items_in_page=items_in_page, customer_id=customer_id, monitoring_agent_id=monitoring_agent_id)

Find SNMP devices

Returns a list of SNMP devices.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
page = 56 # int | Optional - Page index (default is 1), based on items per page (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)
customer_id = 789 # int | Optional - Customer ID (default is NULL) (optional)
monitoring_agent_id = 789 # int | Optional - Monitoring Agent ID (default is NULL) (optional)

try:
    # Find SNMP devices
    api_response = api_instance.device_get_snmp_devices(page=page, items_in_page=items_in_page, customer_id=customer_id, monitoring_agent_id=monitoring_agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_get_snmp_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional - Page index (default is 1), based on items per page | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 
 **customer_id** | **int**| Optional - Customer ID (default is NULL) | [optional] 
 **monitoring_agent_id** | **int**| Optional - Monitoring Agent ID (default is NULL) | [optional] 

### Return type

[**APIResultWrapperSNMPDeviceQueryDTO**](APIResultWrapperSNMPDeviceQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_get_tcp_device**
> TcpDeviceQueryDTO device_get_tcp_device(device_id)

Find specified TCP device

Returns a TCP device. Requires the device ID.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
device_id = 789 # int | Required - System Device ID

try:
    # Find specified TCP device
    api_response = api_instance.device_get_tcp_device(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_get_tcp_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Required - System Device ID | 

### Return type

[**TcpDeviceQueryDTO**](TcpDeviceQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_get_tcp_devices**
> APIResultWrapperTcpDeviceQueryDTO device_get_tcp_devices(page=page, items_in_page=items_in_page, customer_id=customer_id, monitoring_agent_id=monitoring_agent_id)

Find TCP devices

Returns a list of TCP devices.

### Example
```python
from __future__ import print_function
import time
import atera_client
from atera_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = atera_client.DeviceApi()
page = 56 # int | Optional - Page index (default is 1), based on items per page (optional)
items_in_page = 56 # int | Optional - Number of items per page (default is 20, max is 50) (optional)
customer_id = 789 # int | Optional - Customer ID (default is NULL) (optional)
monitoring_agent_id = 789 # int | Optional - Monitoring Agent ID (default is NULL) (optional)

try:
    # Find TCP devices
    api_response = api_instance.device_get_tcp_devices(page=page, items_in_page=items_in_page, customer_id=customer_id, monitoring_agent_id=monitoring_agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_get_tcp_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional - Page index (default is 1), based on items per page | [optional] 
 **items_in_page** | **int**| Optional - Number of items per page (default is 20, max is 50) | [optional] 
 **customer_id** | **int**| Optional - Customer ID (default is NULL) | [optional] 
 **monitoring_agent_id** | **int**| Optional - Monitoring Agent ID (default is NULL) | [optional] 

### Return type

[**APIResultWrapperTcpDeviceQueryDTO**](APIResultWrapperTcpDeviceQueryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

