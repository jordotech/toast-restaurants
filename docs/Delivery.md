# Delivery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates whether the restaurant provides delivery service and has enabled the delivery configuration in the Toast administration back-end.  | [optional] 
**minimum** | **float** | The minimum order price that is qualified for delivery. For example, a restaurant might not deliver orders that cost less than $25.00.  | [optional] 
**area** | **str** | The geographic area in which the restaurant provides delivery service. The delivery area is represented by an encoded set of latitude and longitude coordinates that describe a polygon area on a map. The coordinates are encoded using the Google maps encoded polyline algorithm format. For more information about the way that the encoded polyline algorithm format encodes location coordinates, see https://developers.google.com/maps/documentation/utilities/polylinealgorithm. You can decode the coordinates of the delivery area using any software that supports the encoded polyline algorithm format. For example, you can decode the coordinates using the Mapline Polyline decoding program (https://github.com/mapbox/polyline). The delivery area coordinates are a JSON array of decimal degree latitude and longitude pairs. For example, &#x60;[[42.36083,-71.14798],[42.34028,-71.15673],[42.3272,-71.14386]]&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


