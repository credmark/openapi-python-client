# location


Method | HTTP Request | Description
------------- | ------------- | -------------
[**get_location_query_optionality**](#get_location_query_optionality) | GET /location/query/optionality | 
[**get_location_header_types**](#get_location_header_types) | GET /location/header/types | 


# **get_location_query_optionality**


### Parameters:
Name | Type | Description
------------ | ------------- | -------------
not_null_required | datetime.datetime | None
null_required | datetime.datetime | None
null_not_required | datetime.datetime | None
not_null_not_required | datetime.datetime | None


### Response Type
Any

# **get_location_header_types**


### Parameters:
Name | Type | Description
------------ | ------------- | -------------
boolean_header | bool | None
string_header | str | None
number_header | float | None
integer_header | int | None
int_enum_header | GetLocationHeaderTypesIntEnumHeader | None
string_enum_header | GetLocationHeaderTypesStringEnumHeader | None


### Response Type
Any

