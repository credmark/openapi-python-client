from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ...client import MyTestApiClient

from typing import Dict, cast

from ...models.post_responses_unions_simple_before_complex_response_200 import (
    PostResponsesUnionsSimpleBeforeComplexResponse200,
)
from . import post_responses_unions_simple_before_complex


class Responses:
    def __init__(self, client: "MyTestApiClient"):
        self.__client = client

    def post_responses_unions_simple_before_complex(
        self,
    ) -> PostResponsesUnionsSimpleBeforeComplexResponse200:
        """Regression test for #603

        Raises:
            errors.UnexpectedStatus: If the server returns a non 2xx status code.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[PostResponsesUnionsSimpleBeforeComplexResponse200]
        """

        return post_responses_unions_simple_before_complex.sync(
            client=self.__client,
        )

    async def post_responses_unions_simple_before_complex_async(
        self,
    ) -> PostResponsesUnionsSimpleBeforeComplexResponse200:
        """Regression test for #603

        Raises:
            errors.UnexpectedStatus: If the server returns a non 2xx status code.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[PostResponsesUnionsSimpleBeforeComplexResponse200]
        """

        return await post_responses_unions_simple_before_complex.asyncio(
            client=self.__client,
        )
