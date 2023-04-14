from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ...client import MyTestApiClient

from typing import Optional, Union

from ...types import UNSET, Unset
from . import (
    delete_common_parameters_overriding_param,
    get_common_parameters_overriding_param,
    get_same_name_multiple_locations_param,
    multiple_path_parameters,
)


class Parameters:
    def __init__(self, client: "MyTestApiClient"):
        self.__client = client

    def get_common_parameters_overriding_param(
        self,
        param_path: str,
        *,
        param_query: str = "overridden_in_GET",
    ) -> Optional[Any]:
        """Test that if you have an overriding property from `PathItem` in `Operation`, it produces valid code

        Args:
            param_path (str):
            param_query (str): A parameter with the same name as another. Default:
                'overridden_in_GET'. Example: an example string.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return get_common_parameters_overriding_param.sync(
            client=self.__client,
            param_path=param_path,
            param_query=param_query,
        )

    async def get_common_parameters_overriding_param_async(
        self,
        param_path: str,
        *,
        param_query: str = "overridden_in_GET",
    ) -> Optional[Any]:
        """Test that if you have an overriding property from `PathItem` in `Operation`, it produces valid code

        Args:
            param_path (str):
            param_query (str): A parameter with the same name as another. Default:
                'overridden_in_GET'. Example: an example string.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return await get_common_parameters_overriding_param.asyncio(
            client=self.__client,
            param_path=param_path,
            param_query=param_query,
        )

    def delete_common_parameters_overriding_param(
        self,
        param_path: str,
        *,
        param_query: Union[Unset, None, str] = UNSET,
    ) -> Optional[Any]:
        """
        Args:
            param_path (str):
            param_query (Union[Unset, None, str]):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return delete_common_parameters_overriding_param.sync(
            client=self.__client,
            param_path=param_path,
            param_query=param_query,
        )

    async def delete_common_parameters_overriding_param_async(
        self,
        param_path: str,
        *,
        param_query: Union[Unset, None, str] = UNSET,
    ) -> Optional[Any]:
        """
        Args:
            param_path (str):
            param_query (Union[Unset, None, str]):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return await delete_common_parameters_overriding_param.asyncio(
            client=self.__client,
            param_path=param_path,
            param_query=param_query,
        )

    def get_same_name_multiple_locations_param(
        self,
        param_path: str,
        *,
        param_query: Union[Unset, None, str] = UNSET,
        param_header: Union[Unset, str] = UNSET,
        param_cookie: Union[Unset, str] = UNSET,
    ) -> Optional[Any]:
        """
        Args:
            param_path (str):
            param_query (Union[Unset, None, str]):
            param_header (Union[Unset, str]):
            param_cookie (Union[Unset, str]):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return get_same_name_multiple_locations_param.sync(
            client=self.__client,
            param_path=param_path,
            param_query=param_query,
            param_header=param_header,
            param_cookie=param_cookie,
        )

    async def get_same_name_multiple_locations_param_async(
        self,
        param_path: str,
        *,
        param_query: Union[Unset, None, str] = UNSET,
        param_header: Union[Unset, str] = UNSET,
        param_cookie: Union[Unset, str] = UNSET,
    ) -> Optional[Any]:
        """
        Args:
            param_path (str):
            param_query (Union[Unset, None, str]):
            param_header (Union[Unset, str]):
            param_cookie (Union[Unset, str]):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return await get_same_name_multiple_locations_param.asyncio(
            client=self.__client,
            param_path=param_path,
            param_query=param_query,
            param_header=param_header,
            param_cookie=param_cookie,
        )

    def multiple_path_parameters(
        self,
        param4: str,
        param2: int,
        param1: str,
        param3: int,
    ) -> Optional[Any]:
        """
        Args:
            param4 (str):
            param2 (int):
            param1 (str):
            param3 (int):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return multiple_path_parameters.sync(
            client=self.__client,
            param4=param4,
            param2=param2,
            param1=param1,
            param3=param3,
        )

    async def multiple_path_parameters_async(
        self,
        param4: str,
        param2: int,
        param1: str,
        param3: int,
    ) -> Optional[Any]:
        """
        Args:
            param4 (str):
            param2 (int):
            param1 (str):
            param3 (int):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return await multiple_path_parameters.asyncio(
            client=self.__client,
            param4=param4,
            param2=param2,
            param1=param1,
            param3=param3,
        )
