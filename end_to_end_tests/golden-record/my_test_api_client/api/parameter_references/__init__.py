from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ...client import MyTestApiClient

from typing import Optional, Union

from ...types import UNSET, Unset
from . import get_parameter_references_path_param


class ParameterReferences:
    def __init__(self, client: "MyTestApiClient"):
        self.__client = client

    def get_parameter_references_path_param(
        self,
        path_param: str,
        *,
        string_param: Union[Unset, None, str] = UNSET,
        integer_param: Union[Unset, None, int] = 0,
        header_param: Union[Unset, str] = UNSET,
        cookie_param: Union[Unset, str] = UNSET,
    ) -> Any:
        """Test different types of parameter references

        Args:
            path_param (str):
            string_param (Union[Unset, None, str]):
            integer_param (Union[Unset, None, int]):
            header_param (Union[Unset, str]):
            cookie_param (Union[Unset, str]):

        Raises:
            errors.UnexpectedStatus: If the server returns a non 2xx status code.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return get_parameter_references_path_param.sync(
            client=self.__client,
            path_param=path_param,
            string_param=string_param,
            integer_param=integer_param,
            header_param=header_param,
            cookie_param=cookie_param,
        )

    async def get_parameter_references_path_param_async(
        self,
        path_param: str,
        *,
        string_param: Union[Unset, None, str] = UNSET,
        integer_param: Union[Unset, None, int] = 0,
        header_param: Union[Unset, str] = UNSET,
        cookie_param: Union[Unset, str] = UNSET,
    ) -> Any:
        """Test different types of parameter references

        Args:
            path_param (str):
            string_param (Union[Unset, None, str]):
            integer_param (Union[Unset, None, int]):
            header_param (Union[Unset, str]):
            cookie_param (Union[Unset, str]):

        Raises:
            errors.UnexpectedStatus: If the server returns a non 2xx status code.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return await get_parameter_references_path_param.asyncio(
            client=self.__client,
            path_param=path_param,
            string_param=string_param,
            integer_param=integer_param,
            header_param=header_param,
            cookie_param=cookie_param,
        )
