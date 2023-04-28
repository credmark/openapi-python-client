from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict, List, cast

import httpx

if TYPE_CHECKING:
    from ...client import MyTestApiClient

from typing import List, cast

from ... import errors
from ...types import Response


def _get_kwargs(client: "MyTestApiClient") -> Dict[str, Any]:
    url = "{}/tests/basic_lists/booleans".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: "MyTestApiClient", response: httpx.Response) -> List[bool]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(List[bool], response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: "MyTestApiClient", response: httpx.Response) -> Response[List[bool]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(client: "MyTestApiClient") -> Response[List[bool]]:
    """Get Basic List Of Booleans

     Get a list of booleans

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[bool]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(client: "MyTestApiClient") -> List[bool]:
    """Get Basic List Of Booleans

     Get a list of booleans

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[bool]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(client: "MyTestApiClient") -> Response[List[bool]]:
    """Get Basic List Of Booleans

     Get a list of booleans

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[bool]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(client: "MyTestApiClient") -> List[bool]:
    """Get Basic List Of Booleans

     Get a list of booleans

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[bool]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
