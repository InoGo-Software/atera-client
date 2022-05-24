# InvoiceQueryDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_adhoc** | **bool** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**invoice_number** | **int** |  | [optional] 
**invoice_number_as_string** | **str** |  | [optional] 
**total** | **float** |  | [optional] 
**subtotal** | **float** |  | [optional] 
**tax** | **float** |  | [optional] 
**tax_percentage** | **float** |  | [optional] 
**invoice_date** | **datetime** |  | [optional] 
**contract_name** | **str** |  | [optional] 
**period_start_date** | **datetime** |  | [optional] 
**period_end_date** | **datetime** |  | [optional] 
**currency** | **str** |  | [optional] 
**line_items** | [**list[InvoiceLineItemQueryDTO]**](InvoiceLineItemQueryDTO.md) |  | [optional] 
**_from** | [**ContactDetails**](ContactDetails.md) |  | [optional] 
**to** | [**ContactDetails**](ContactDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


