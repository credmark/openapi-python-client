from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ...client import MyTestApiClient

import datetime
from io import BytesIO
from typing import Dict, List, Optional, Union, cast

from dateutil.parser import isoparse

from ...models.a_form_data import AFormData
from ...models.a_model import AModel
from ...models.an_enum import AnEnum
from ...models.an_enum_with_null import AnEnumWithNull
from ...models.an_int_enum import AnIntEnum
from ...models.body_upload_file_tests_upload_post import BodyUploadFileTestsUploadPost
from ...models.http_validation_error import HTTPValidationError
from ...models.model_with_union_property import ModelWithUnionProperty
from ...models.post_form_data_inline_data import PostFormDataInlineData
from ...models.test_inline_objects_json_body import TestInlineObjectsJsonBody
from ...models.test_inline_objects_response_200 import TestInlineObjectsResponse200
from ...types import UNSET, File, FileJsonType, Unset
from . import (
    callback_test,
    defaults_tests_defaults_post,
    description_with_backslash,
    get_basic_list_of_booleans,
    get_basic_list_of_floats,
    get_basic_list_of_integers,
    get_basic_list_of_strings,
    get_user_list,
    int_enum_tests_int_enum_post,
    json_body_tests_json_body_post,
    no_response_tests_no_response_get,
    octet_stream_tests_octet_stream_get,
    post_form_data,
    post_form_data_inline,
    post_tests_json_body_string,
    test_inline_objects,
    token_with_cookie_auth_token_with_cookie_get,
    unsupported_content_tests_unsupported_content_get,
    upload_file_tests_upload_post,
    upload_multiple_files_tests_upload_post,
)


class Tests:
    def __init__(self, client: "MyTestApiClient"):
        self.__client = client

    def get_user_list(
        self,
        *,
        an_enum_value: List[AnEnum],
        an_enum_value_with_null: List[Optional[AnEnumWithNull]],
        an_enum_value_with_only_null: List[None],
        some_date: Union[datetime.date, datetime.datetime],
    ) -> Optional[Union[HTTPValidationError, List["AModel"]]]:
        """Get List

         Get a list of things

        Args:
            an_enum_value (List[AnEnum]):
            an_enum_value_with_null (List[Optional[AnEnumWithNull]]):
            an_enum_value_with_only_null (List[None]):
            some_date (Union[datetime.date, datetime.datetime]):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[HTTPValidationError, List['AModel']]]
        """

        return get_user_list.sync(
            client=self.__client,
            an_enum_value=an_enum_value,
            an_enum_value_with_null=an_enum_value_with_null,
            an_enum_value_with_only_null=an_enum_value_with_only_null,
            some_date=some_date,
        )

    async def get_user_list_async(
        self,
        *,
        an_enum_value: List[AnEnum],
        an_enum_value_with_null: List[Optional[AnEnumWithNull]],
        an_enum_value_with_only_null: List[None],
        some_date: Union[datetime.date, datetime.datetime],
    ) -> Optional[Union[HTTPValidationError, List["AModel"]]]:
        """Get List

         Get a list of things

        Args:
            an_enum_value (List[AnEnum]):
            an_enum_value_with_null (List[Optional[AnEnumWithNull]]):
            an_enum_value_with_only_null (List[None]):
            some_date (Union[datetime.date, datetime.datetime]):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[HTTPValidationError, List['AModel']]]
        """

        return await get_user_list.asyncio(
            client=self.__client,
            an_enum_value=an_enum_value,
            an_enum_value_with_null=an_enum_value_with_null,
            an_enum_value_with_only_null=an_enum_value_with_only_null,
            some_date=some_date,
        )

    def get_basic_list_of_strings(
        self,
    ) -> Optional[List[str]]:
        """Get Basic List Of Strings

         Get a list of strings

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[List[str]]
        """

        return get_basic_list_of_strings.sync(
            client=self.__client,
        )

    async def get_basic_list_of_strings_async(
        self,
    ) -> Optional[List[str]]:
        """Get Basic List Of Strings

         Get a list of strings

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[List[str]]
        """

        return await get_basic_list_of_strings.asyncio(
            client=self.__client,
        )

    def get_basic_list_of_integers(
        self,
    ) -> Optional[List[int]]:
        """Get Basic List Of Integers

         Get a list of integers

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[List[int]]
        """

        return get_basic_list_of_integers.sync(
            client=self.__client,
        )

    async def get_basic_list_of_integers_async(
        self,
    ) -> Optional[List[int]]:
        """Get Basic List Of Integers

         Get a list of integers

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[List[int]]
        """

        return await get_basic_list_of_integers.asyncio(
            client=self.__client,
        )

    def get_basic_list_of_floats(
        self,
    ) -> Optional[List[float]]:
        """Get Basic List Of Floats

         Get a list of floats

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[List[float]]
        """

        return get_basic_list_of_floats.sync(
            client=self.__client,
        )

    async def get_basic_list_of_floats_async(
        self,
    ) -> Optional[List[float]]:
        """Get Basic List Of Floats

         Get a list of floats

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[List[float]]
        """

        return await get_basic_list_of_floats.asyncio(
            client=self.__client,
        )

    def get_basic_list_of_booleans(
        self,
    ) -> Optional[List[bool]]:
        """Get Basic List Of Booleans

         Get a list of booleans

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[List[bool]]
        """

        return get_basic_list_of_booleans.sync(
            client=self.__client,
        )

    async def get_basic_list_of_booleans_async(
        self,
    ) -> Optional[List[bool]]:
        """Get Basic List Of Booleans

         Get a list of booleans

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[List[bool]]
        """

        return await get_basic_list_of_booleans.asyncio(
            client=self.__client,
        )

    def post_form_data(
        self,
        *,
        form_data: AFormData,
    ) -> Optional[Any]:
        """Post form data

         Post form data

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return post_form_data.sync(
            client=self.__client,
            form_data=form_data,
        )

    async def post_form_data_async(
        self,
        *,
        form_data: AFormData,
    ) -> Optional[Any]:
        """Post form data

         Post form data

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return await post_form_data.asyncio(
            client=self.__client,
            form_data=form_data,
        )

    def post_form_data_inline(
        self,
        *,
        form_data: PostFormDataInlineData,
    ) -> Optional[Any]:
        """Post form data (inline schema)

         Post form data (inline schema)

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return post_form_data_inline.sync(
            client=self.__client,
            form_data=form_data,
        )

    async def post_form_data_inline_async(
        self,
        *,
        form_data: PostFormDataInlineData,
    ) -> Optional[Any]:
        """Post form data (inline schema)

         Post form data (inline schema)

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return await post_form_data_inline.asyncio(
            client=self.__client,
            form_data=form_data,
        )

    def upload_file_tests_upload_post(
        self,
        *,
        multipart_data: BodyUploadFileTestsUploadPost,
    ) -> Optional[Union[Any, HTTPValidationError]]:
        """Upload File

         Upload a file

        Args:
            multipart_data (BodyUploadFileTestsUploadPost):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Any, HTTPValidationError]]
        """

        return upload_file_tests_upload_post.sync(
            client=self.__client,
            multipart_data=multipart_data,
        )

    async def upload_file_tests_upload_post_async(
        self,
        *,
        multipart_data: BodyUploadFileTestsUploadPost,
    ) -> Optional[Union[Any, HTTPValidationError]]:
        """Upload File

         Upload a file

        Args:
            multipart_data (BodyUploadFileTestsUploadPost):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Any, HTTPValidationError]]
        """

        return await upload_file_tests_upload_post.asyncio(
            client=self.__client,
            multipart_data=multipart_data,
        )

    def upload_multiple_files_tests_upload_post(
        self,
        *,
        multipart_data: List[File],
    ) -> Optional[Union[Any, HTTPValidationError]]:
        """Upload multiple files

         Upload several files in the same request

        Args:
            multipart_data (List[File]):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Any, HTTPValidationError]]
        """

        return upload_multiple_files_tests_upload_post.sync(
            client=self.__client,
            multipart_data=multipart_data,
        )

    async def upload_multiple_files_tests_upload_post_async(
        self,
        *,
        multipart_data: List[File],
    ) -> Optional[Union[Any, HTTPValidationError]]:
        """Upload multiple files

         Upload several files in the same request

        Args:
            multipart_data (List[File]):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Any, HTTPValidationError]]
        """

        return await upload_multiple_files_tests_upload_post.asyncio(
            client=self.__client,
            multipart_data=multipart_data,
        )

    def json_body_tests_json_body_post(
        self,
        *,
        json_body: AModel,
    ) -> Optional[Union[Any, HTTPValidationError]]:
        """Json Body

         Try sending a JSON body

        Args:
            json_body (AModel): A Model for testing all the ways custom objects can be used

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Any, HTTPValidationError]]
        """

        return json_body_tests_json_body_post.sync(
            client=self.__client,
            json_body=json_body,
        )

    async def json_body_tests_json_body_post_async(
        self,
        *,
        json_body: AModel,
    ) -> Optional[Union[Any, HTTPValidationError]]:
        """Json Body

         Try sending a JSON body

        Args:
            json_body (AModel): A Model for testing all the ways custom objects can be used

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Any, HTTPValidationError]]
        """

        return await json_body_tests_json_body_post.asyncio(
            client=self.__client,
            json_body=json_body,
        )

    def post_tests_json_body_string(
        self,
        *,
        json_body: str,
    ) -> Optional[Union[HTTPValidationError, str]]:
        """Json Body Which is String

        Args:
            json_body (str):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[HTTPValidationError, str]]
        """

        return post_tests_json_body_string.sync(
            client=self.__client,
            json_body=json_body,
        )

    async def post_tests_json_body_string_async(
        self,
        *,
        json_body: str,
    ) -> Optional[Union[HTTPValidationError, str]]:
        """Json Body Which is String

        Args:
            json_body (str):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[HTTPValidationError, str]]
        """

        return await post_tests_json_body_string.asyncio(
            client=self.__client,
            json_body=json_body,
        )

    def defaults_tests_defaults_post(
        self,
        *,
        string_prop: str = "the default string",
        date_prop: datetime.date = isoparse("1010-10-10").date(),
        float_prop: float = 3.14,
        int_prop: int = 7,
        boolean_prop: bool = False,
        list_prop: List[AnEnum],
        union_prop: Union[float, str] = "not a float",
        union_prop_with_ref: Union[AnEnum, None, Unset, float] = 0.6,
        enum_prop: AnEnum,
        model_prop: "ModelWithUnionProperty",
        required_model_prop: "ModelWithUnionProperty",
    ) -> Optional[Union[Any, HTTPValidationError]]:
        """Defaults

        Args:
            string_prop (str):  Default: 'the default string'.
            date_prop (datetime.date):  Default: isoparse('1010-10-10').date().
            float_prop (float):  Default: 3.14.
            int_prop (int):  Default: 7.
            boolean_prop (bool):
            list_prop (List[AnEnum]):
            union_prop (Union[float, str]):  Default: 'not a float'.
            union_prop_with_ref (Union[AnEnum, None, Unset, float]):  Default: 0.6.
            enum_prop (AnEnum): For testing Enums in all the ways they can be used
            model_prop (ModelWithUnionProperty):
            required_model_prop (ModelWithUnionProperty):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Any, HTTPValidationError]]
        """

        return defaults_tests_defaults_post.sync(
            client=self.__client,
            string_prop=string_prop,
            date_prop=date_prop,
            float_prop=float_prop,
            int_prop=int_prop,
            boolean_prop=boolean_prop,
            list_prop=list_prop,
            union_prop=union_prop,
            union_prop_with_ref=union_prop_with_ref,
            enum_prop=enum_prop,
            model_prop=model_prop,
            required_model_prop=required_model_prop,
        )

    async def defaults_tests_defaults_post_async(
        self,
        *,
        string_prop: str = "the default string",
        date_prop: datetime.date = isoparse("1010-10-10").date(),
        float_prop: float = 3.14,
        int_prop: int = 7,
        boolean_prop: bool = False,
        list_prop: List[AnEnum],
        union_prop: Union[float, str] = "not a float",
        union_prop_with_ref: Union[AnEnum, None, Unset, float] = 0.6,
        enum_prop: AnEnum,
        model_prop: "ModelWithUnionProperty",
        required_model_prop: "ModelWithUnionProperty",
    ) -> Optional[Union[Any, HTTPValidationError]]:
        """Defaults

        Args:
            string_prop (str):  Default: 'the default string'.
            date_prop (datetime.date):  Default: isoparse('1010-10-10').date().
            float_prop (float):  Default: 3.14.
            int_prop (int):  Default: 7.
            boolean_prop (bool):
            list_prop (List[AnEnum]):
            union_prop (Union[float, str]):  Default: 'not a float'.
            union_prop_with_ref (Union[AnEnum, None, Unset, float]):  Default: 0.6.
            enum_prop (AnEnum): For testing Enums in all the ways they can be used
            model_prop (ModelWithUnionProperty):
            required_model_prop (ModelWithUnionProperty):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Any, HTTPValidationError]]
        """

        return await defaults_tests_defaults_post.asyncio(
            client=self.__client,
            string_prop=string_prop,
            date_prop=date_prop,
            float_prop=float_prop,
            int_prop=int_prop,
            boolean_prop=boolean_prop,
            list_prop=list_prop,
            union_prop=union_prop,
            union_prop_with_ref=union_prop_with_ref,
            enum_prop=enum_prop,
            model_prop=model_prop,
            required_model_prop=required_model_prop,
        )

    def octet_stream_tests_octet_stream_get(
        self,
    ) -> Optional[File]:
        """Octet Stream

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[File]
        """

        return octet_stream_tests_octet_stream_get.sync(
            client=self.__client,
        )

    async def octet_stream_tests_octet_stream_get_async(
        self,
    ) -> Optional[File]:
        """Octet Stream

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[File]
        """

        return await octet_stream_tests_octet_stream_get.asyncio(
            client=self.__client,
        )

    def no_response_tests_no_response_get(
        self,
    ) -> Optional[Any]:
        """No Response

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return no_response_tests_no_response_get.sync(
            client=self.__client,
        )

    async def no_response_tests_no_response_get_async(
        self,
    ) -> Optional[Any]:
        """No Response

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return await no_response_tests_no_response_get.asyncio(
            client=self.__client,
        )

    def unsupported_content_tests_unsupported_content_get(
        self,
    ) -> Optional[Any]:
        """Unsupported Content

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return unsupported_content_tests_unsupported_content_get.sync(
            client=self.__client,
        )

    async def unsupported_content_tests_unsupported_content_get_async(
        self,
    ) -> Optional[Any]:
        """Unsupported Content

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return await unsupported_content_tests_unsupported_content_get.asyncio(
            client=self.__client,
        )

    def int_enum_tests_int_enum_post(
        self,
        *,
        int_enum: AnIntEnum,
    ) -> Optional[Union[Any, HTTPValidationError]]:
        """Int Enum

        Args:
            int_enum (AnIntEnum): An enumeration.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Any, HTTPValidationError]]
        """

        return int_enum_tests_int_enum_post.sync(
            client=self.__client,
            int_enum=int_enum,
        )

    async def int_enum_tests_int_enum_post_async(
        self,
        *,
        int_enum: AnIntEnum,
    ) -> Optional[Union[Any, HTTPValidationError]]:
        """Int Enum

        Args:
            int_enum (AnIntEnum): An enumeration.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Any, HTTPValidationError]]
        """

        return await int_enum_tests_int_enum_post.asyncio(
            client=self.__client,
            int_enum=int_enum,
        )

    def test_inline_objects(
        self,
        *,
        json_body: TestInlineObjectsJsonBody,
    ) -> Optional[TestInlineObjectsResponse200]:
        """Test Inline Objects

        Args:
            json_body (TestInlineObjectsJsonBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[TestInlineObjectsResponse200]
        """

        return test_inline_objects.sync(
            client=self.__client,
            json_body=json_body,
        )

    async def test_inline_objects_async(
        self,
        *,
        json_body: TestInlineObjectsJsonBody,
    ) -> Optional[TestInlineObjectsResponse200]:
        """Test Inline Objects

        Args:
            json_body (TestInlineObjectsJsonBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[TestInlineObjectsResponse200]
        """

        return await test_inline_objects.asyncio(
            client=self.__client,
            json_body=json_body,
        )

    def token_with_cookie_auth_token_with_cookie_get(
        self,
        *,
        my_token: str,
    ) -> Optional[Any]:
        """TOKEN_WITH_COOKIE

         Test optional cookie parameters

        Args:
            my_token (str):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return token_with_cookie_auth_token_with_cookie_get.sync(
            client=self.__client,
            my_token=my_token,
        )

    async def token_with_cookie_auth_token_with_cookie_get_async(
        self,
        *,
        my_token: str,
    ) -> Optional[Any]:
        """TOKEN_WITH_COOKIE

         Test optional cookie parameters

        Args:
            my_token (str):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return await token_with_cookie_auth_token_with_cookie_get.asyncio(
            client=self.__client,
            my_token=my_token,
        )

    def callback_test(
        self,
        *,
        json_body: AModel,
    ) -> Optional[Union[Any, HTTPValidationError]]:
        """Path with callback

         Try sending a request related to a callback

        Args:
            json_body (AModel): A Model for testing all the ways custom objects can be used

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Any, HTTPValidationError]]
        """

        return callback_test.sync(
            client=self.__client,
            json_body=json_body,
        )

    async def callback_test_async(
        self,
        *,
        json_body: AModel,
    ) -> Optional[Union[Any, HTTPValidationError]]:
        """Path with callback

         Try sending a request related to a callback

        Args:
            json_body (AModel): A Model for testing all the ways custom objects can be used

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Any, HTTPValidationError]]
        """

        return await callback_test.asyncio(
            client=self.__client,
            json_body=json_body,
        )

    def description_with_backslash(
        self,
    ) -> Optional[Any]:
        r""" Test description with \

         Test description with \

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
         """

        return description_with_backslash.sync(
            client=self.__client,
        )

    async def description_with_backslash_async(
        self,
    ) -> Optional[Any]:
        r""" Test description with \

         Test description with \

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
         """

        return await description_with_backslash.asyncio(
            client=self.__client,
        )
