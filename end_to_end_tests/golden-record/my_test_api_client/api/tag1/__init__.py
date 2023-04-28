from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ...client import MyTestApiClient

from . import get_tag_with_number


class Tag1:
    def __init__(self, client: "MyTestApiClient"):
        self.__client = client

    def get_tag_with_number(
        self,
    ) -> Any:
        """
        Raises:
            errors.UnexpectedStatus: If the server returns a non 2xx status code.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return get_tag_with_number.sync(
            client=self.__client,
        )

    async def get_tag_with_number_async(
        self,
    ) -> Any:
        """
        Raises:
            errors.UnexpectedStatus: If the server returns a non 2xx status code.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return await get_tag_with_number.asyncio(
            client=self.__client,
        )
