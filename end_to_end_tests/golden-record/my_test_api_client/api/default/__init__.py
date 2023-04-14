from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ...client import MyTestApiClient

from typing import Optional, Union

from ...types import UNSET, Unset
from . import get_common_parameters, post_common_parameters


class Default:
    def __init__(self, client: "MyTestApiClient"):
        self.__client = client

    def get_common_parameters(
        self,
        *,
        common: Union[Unset, None, str] = UNSET,
    ) -> Optional[Any]:
        """
        Args:
            common (Union[Unset, None, str]):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return get_common_parameters.sync(
            client=self.__client,
            common=common,
        )

    async def get_common_parameters_async(
        self,
        *,
        common: Union[Unset, None, str] = UNSET,
    ) -> Optional[Any]:
        """
        Args:
            common (Union[Unset, None, str]):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return await get_common_parameters.asyncio(
            client=self.__client,
            common=common,
        )

    def post_common_parameters(
        self,
        *,
        common: Union[Unset, None, str] = UNSET,
    ) -> Optional[Any]:
        """
        Args:
            common (Union[Unset, None, str]):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return post_common_parameters.sync(
            client=self.__client,
            common=common,
        )

    async def post_common_parameters_async(
        self,
        *,
        common: Union[Unset, None, str] = UNSET,
    ) -> Optional[Any]:
        """
        Args:
            common (Union[Unset, None, str]):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return await post_common_parameters.asyncio(
            client=self.__client,
            common=common,
        )
