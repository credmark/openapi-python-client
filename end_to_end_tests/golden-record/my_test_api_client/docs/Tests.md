# tests


Method | HTTP Request | Description
------------- | ------------- | -------------
[**get_user_list**](#get_user_list) | GET /tests/ | Get a list of things 
[**get_basic_list_of_strings**](#get_basic_list_of_strings) | GET /tests/basic_lists/strings | Get a list of strings 
[**get_basic_list_of_integers**](#get_basic_list_of_integers) | GET /tests/basic_lists/integers | Get a list of integers 
[**get_basic_list_of_floats**](#get_basic_list_of_floats) | GET /tests/basic_lists/floats | Get a list of floats 
[**get_basic_list_of_booleans**](#get_basic_list_of_booleans) | GET /tests/basic_lists/booleans | Get a list of booleans 
[**post_form_data**](#post_form_data) | POST /tests/post_form_data | Post form data
[**post_form_data_inline**](#post_form_data_inline) | POST /tests/post_form_data_inline | Post form data (inline schema)
[**upload_file_tests_upload_post**](#upload_file_tests_upload_post) | POST /tests/upload | Upload a file 
[**upload_multiple_files_tests_upload_post**](#upload_multiple_files_tests_upload_post) | POST /tests/upload/multiple | Upload several files in the same request
[**json_body_tests_json_body_post**](#json_body_tests_json_body_post) | POST /tests/json_body | Try sending a JSON body 
[**post_tests_json_body_string**](#post_tests_json_body_string) | POST /tests/json_body/string | 
[**defaults_tests_defaults_post**](#defaults_tests_defaults_post) | POST /tests/defaults | 
[**octet_stream_tests_octet_stream_get**](#octet_stream_tests_octet_stream_get) | GET /tests/octet_stream | 
[**no_response_tests_no_response_get**](#no_response_tests_no_response_get) | GET /tests/no_response | 
[**unsupported_content_tests_unsupported_content_get**](#unsupported_content_tests_unsupported_content_get) | GET /tests/unsupported_content | 
[**int_enum_tests_int_enum_post**](#int_enum_tests_int_enum_post) | POST /tests/int_enum | 
[**test_inline_objects**](#test_inline_objects) | POST /tests/inline_objects | 
[**token_with_cookie_auth_token_with_cookie_get**](#token_with_cookie_auth_token_with_cookie_get) | GET /auth/token_with_cookie | Test optional cookie parameters
[**callback_test**](#callback_test) | POST /tests/callback | Try sending a request related to a callback
[**description_with_backslash**](#description_with_backslash) | GET /tests/description-with-backslash | Test description with \


# **get_user_list**

Get List

 Get a list of things


### Parameters:
Name | Type | Description
------------ | ------------- | -------------
an_enum_value | [List[AnEnum]](List[AnEnum]) | None
an_enum_value_with_null | [List[Optional[AnEnumWithNull]]](List[Optional[AnEnumWithNull]]) | None
an_enum_value_with_only_null | [List[None]](List[None]) | None
some_date | [Union[datetime.date, datetime.datetime]](Union[datetime.date, datetime.datetime]) | None


### Response Type
Union[HTTPValidationError, List['AModel']]

# **get_basic_list_of_strings**

Get Basic List Of Strings

 Get a list of strings



### Response Type
List[str]

# **get_basic_list_of_integers**

Get Basic List Of Integers

 Get a list of integers



### Response Type
List[int]

# **get_basic_list_of_floats**

Get Basic List Of Floats

 Get a list of floats



### Response Type
List[float]

# **get_basic_list_of_booleans**

Get Basic List Of Booleans

 Get a list of booleans



### Response Type
List[bool]

# **post_form_data**

Post form data

 Post form data



### Response Type
Any

# **post_form_data_inline**

Post form data (inline schema)

 Post form data (inline schema)



### Response Type
Any

# **upload_file_tests_upload_post**

Upload File

 Upload a file


### Parameters:
Name | Type | Description
------------ | ------------- | -------------
multipart_data | [BodyUploadFileTestsUploadPost](BodyUploadFileTestsUploadPost) | 


### Response Type
Union[Any, HTTPValidationError]

# **upload_multiple_files_tests_upload_post**

Upload multiple files

 Upload several files in the same request


### Parameters:
Name | Type | Description
------------ | ------------- | -------------
multipart_data | [List[File]](List[File]) | None


### Response Type
Union[Any, HTTPValidationError]

# **json_body_tests_json_body_post**

Json Body

 Try sending a JSON body


### Parameters:
Name | Type | Description
------------ | ------------- | -------------
json_body | [AModel](AModel) | A Model for testing all the ways custom objects can be used 


### Response Type
Union[Any, HTTPValidationError]

# **post_tests_json_body_string**

Json Body Which is String


### Parameters:
Name | Type | Description
------------ | ------------- | -------------
json_body | str | None


### Response Type
Union[HTTPValidationError, str]

# **defaults_tests_defaults_post**

Defaults


### Parameters:
Name | Type | Description
------------ | ------------- | -------------
string_prop | str | None
date_prop | datetime.date | None
float_prop | float | None
int_prop | int | None
boolean_prop | bool | None
list_prop | [List[AnEnum]](List[AnEnum]) | None
union_prop | [Union[float, str]](Union[float, str]) | None
union_prop_with_ref | [Union[AnEnum, float]](Union[AnEnum, float]) | None
enum_prop | AnEnum | For testing Enums in all the ways they can be used 
model_prop | [ModelWithUnionProperty](ModelWithUnionProperty) | 
required_model_prop | [ModelWithUnionProperty](ModelWithUnionProperty) | 


### Response Type
Union[Any, HTTPValidationError]

# **octet_stream_tests_octet_stream_get**

Octet Stream



### Response Type
File

# **no_response_tests_no_response_get**

No Response



### Response Type
Any

# **unsupported_content_tests_unsupported_content_get**

Unsupported Content



### Response Type
Any

# **int_enum_tests_int_enum_post**

Int Enum


### Parameters:
Name | Type | Description
------------ | ------------- | -------------
int_enum | AnIntEnum | An enumeration.


### Response Type
Union[Any, HTTPValidationError]

# **test_inline_objects**

Test Inline Objects


### Parameters:
Name | Type | Description
------------ | ------------- | -------------
json_body | [TestInlineObjectsJsonBody](TestInlineObjectsJsonBody) | 


### Response Type
TestInlineObjectsResponse200

# **token_with_cookie_auth_token_with_cookie_get**

TOKEN_WITH_COOKIE

 Test optional cookie parameters


### Parameters:
Name | Type | Description
------------ | ------------- | -------------
my_token | str | None


### Response Type
Any

# **callback_test**

Path with callback

 Try sending a request related to a callback


### Parameters:
Name | Type | Description
------------ | ------------- | -------------
json_body | [AModel](AModel) | A Model for testing all the ways custom objects can be used 


### Response Type
Union[Any, HTTPValidationError]

# **description_with_backslash**

Test description with \

 Test description with \



### Response Type
Any

