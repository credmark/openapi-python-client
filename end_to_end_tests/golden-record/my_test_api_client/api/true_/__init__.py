from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ...client import MyTestApiClient

from . import false_


class True_:
    def __init__(self, client: "MyTestApiClient"):
        self.__client = client

    def false_(
        self,
        *,
        import_: str,
    ) -> Optional[Any]:
        """
        Args:
            import_ (str):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return false_.sync(
            client=self.__client,
            import_=import_,
        )

    async def false__async(
        self,
        *,
        import_: str,
    ) -> Optional[Any]:
        """
        Args:
            import_ (str):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        return await false_.asyncio(
            client=self.__client,
            import_=import_,
        )
