from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ...client import MyTestApiClient

import datetime
from typing import Optional, Union, cast

from dateutil.parser import isoparse

from ...models.get_location_header_types_int_enum_header import GetLocationHeaderTypesIntEnumHeader
from ...models.get_location_header_types_string_enum_header import GetLocationHeaderTypesStringEnumHeader
from ...types import UNSET, Unset
from . import get_location_header_types, get_location_query_optionality


class Location:
    def __init__(self, client: "MyTestApiClient"):
        self.__client = client

    def get_location_query_optionality(
        self,
        *,
        not_null_required: datetime.datetime,
        null_required: Union[Unset, None, datetime.datetime] = UNSET,
        null_not_required: Union[Unset, None, datetime.datetime] = UNSET,
        not_null_not_required: Union[Unset, None, datetime.datetime] = UNSET,
    ) -> Any:
        """
        Args:
            not_null_required (datetime.datetime):
            null_required (Union[Unset, None, datetime.datetime]):
            null_not_required (Union[Unset, None, datetime.datetime]):
            not_null_not_required (Union[Unset, None, datetime.datetime]):

        Raises:
            errors.UnexpectedStatus: If the server returns a non 2xx status code.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return get_location_query_optionality.sync(
            client=self.__client,
            not_null_required=not_null_required,
            null_required=null_required,
            null_not_required=null_not_required,
            not_null_not_required=not_null_not_required,
        )

    async def get_location_query_optionality_async(
        self,
        *,
        not_null_required: datetime.datetime,
        null_required: Union[Unset, None, datetime.datetime] = UNSET,
        null_not_required: Union[Unset, None, datetime.datetime] = UNSET,
        not_null_not_required: Union[Unset, None, datetime.datetime] = UNSET,
    ) -> Any:
        """
        Args:
            not_null_required (datetime.datetime):
            null_required (Union[Unset, None, datetime.datetime]):
            null_not_required (Union[Unset, None, datetime.datetime]):
            not_null_not_required (Union[Unset, None, datetime.datetime]):

        Raises:
            errors.UnexpectedStatus: If the server returns a non 2xx status code.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return await get_location_query_optionality.asyncio(
            client=self.__client,
            not_null_required=not_null_required,
            null_required=null_required,
            null_not_required=null_not_required,
            not_null_not_required=not_null_not_required,
        )

    def get_location_header_types(
        self,
        *,
        boolean_header: Union[Unset, bool] = UNSET,
        string_header: Union[Unset, str] = UNSET,
        number_header: Union[Unset, float] = UNSET,
        integer_header: Union[Unset, int] = UNSET,
        int_enum_header: Union[Unset, GetLocationHeaderTypesIntEnumHeader] = UNSET,
        string_enum_header: Union[Unset, GetLocationHeaderTypesStringEnumHeader] = UNSET,
    ) -> Any:
        """
        Args:
            boolean_header (Union[Unset, bool]):
            string_header (Union[Unset, str]):
            number_header (Union[Unset, float]):
            integer_header (Union[Unset, int]):
            int_enum_header (Union[Unset, GetLocationHeaderTypesIntEnumHeader]):
            string_enum_header (Union[Unset, GetLocationHeaderTypesStringEnumHeader]):

        Raises:
            errors.UnexpectedStatus: If the server returns a non 2xx status code.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return get_location_header_types.sync(
            client=self.__client,
            boolean_header=boolean_header,
            string_header=string_header,
            number_header=number_header,
            integer_header=integer_header,
            int_enum_header=int_enum_header,
            string_enum_header=string_enum_header,
        )

    async def get_location_header_types_async(
        self,
        *,
        boolean_header: Union[Unset, bool] = UNSET,
        string_header: Union[Unset, str] = UNSET,
        number_header: Union[Unset, float] = UNSET,
        integer_header: Union[Unset, int] = UNSET,
        int_enum_header: Union[Unset, GetLocationHeaderTypesIntEnumHeader] = UNSET,
        string_enum_header: Union[Unset, GetLocationHeaderTypesStringEnumHeader] = UNSET,
    ) -> Any:
        """
        Args:
            boolean_header (Union[Unset, bool]):
            string_header (Union[Unset, str]):
            number_header (Union[Unset, float]):
            integer_header (Union[Unset, int]):
            int_enum_header (Union[Unset, GetLocationHeaderTypesIntEnumHeader]):
            string_enum_header (Union[Unset, GetLocationHeaderTypesStringEnumHeader]):

        Raises:
            errors.UnexpectedStatus: If the server returns a non 2xx status code.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return await get_location_header_types.asyncio(
            client=self.__client,
            boolean_header=boolean_header,
            string_header=string_header,
            number_header=number_header,
            integer_header=integer_header,
            int_enum_header=int_enum_header,
            string_enum_header=string_enum_header,
        )
