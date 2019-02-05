# OnlineOrdering

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates whether the restaurant allows online ordering and has enabled it in the Toast administration back-end.  | [optional] 
**scheduling** | **bool** | Indicates whether the online ordering function for the restaurant allows customers to place orders that will be fulfilled in the future. If this value is &#x60;false&#x60;, orders will be fulfilled as soon as possible.  | [optional] 
**special_requests** | **bool** | Indicates whether the online ordering function for the restaurant allows customers to include written notes with additional instructions for their orders.  | [optional] 
**special_requests_message** | **str** | A written message that is shown to customers when they include additional instructions with an order. For example, the message might be \&quot;no substitutions.\&quot;  | [optional] 
**payment_options** | [**PaymentOptions**](PaymentOptions.md) | Information about the forms of payment that the restaurant accepts for online orders.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


