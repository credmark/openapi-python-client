# parameters


Method | HTTP Request | Description
------------- | ------------- | -------------
[**get_common_parameters_overriding_param**](#get_common_parameters_overriding_param) | GET /common_parameters_overriding/{param} | Test that if you have an overriding property from `PathItem` in `Operation`, it produces valid code
[**delete_common_parameters_overriding_param**](#delete_common_parameters_overriding_param) | DELETE /common_parameters_overriding/{param} | 
[**get_same_name_multiple_locations_param**](#get_same_name_multiple_locations_param) | GET /same-name-multiple-locations/{param} | 
[**multiple_path_parameters**](#multiple_path_parameters) | GET /multiple-path-parameters/{param4}/something/{param2}/{param1}/{param3} | 


# **get_common_parameters_overriding_param**

 Test that if you have an overriding property from `PathItem` in `Operation`, it produces valid code


### Parameters:
Name | Type | Description
------------ | ------------- | -------------
param_path | str | None
param_query | str | A parameter with the same name as another.


### Response Type
Any

# **delete_common_parameters_overriding_param**


### Parameters:
Name | Type | Description
------------ | ------------- | -------------
param_path | str | None
param_query | str | None


### Response Type
Any

# **get_same_name_multiple_locations_param**


### Parameters:
Name | Type | Description
------------ | ------------- | -------------
param_path | str | None
param_query | str | None
param_header | str | None
param_cookie | str | None


### Response Type
Any

# **multiple_path_parameters**


### Parameters:
Name | Type | Description
------------ | ------------- | -------------
param4 | str | None
param2 | int | None
param1 | str | None
param3 | int | None


### Response Type
Any

