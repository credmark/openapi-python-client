from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict, cast

import httpx

if TYPE_CHECKING:
    from ...client import MyTestApiClient

from ... import errors
from ...types import Response


def _get_kwargs(*, my_token: str, client: "MyTestApiClient") -> Dict[str, Any]:
    url = "{}/auth/token_with_cookie".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    cookies["MyToken"] = my_token

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: "MyTestApiClient", response: httpx.Response) -> Any:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, response.json())
        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = None
        raise errors.UnexpectedStatus(response.status_code, response.content, response_401)
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: "MyTestApiClient", response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(*, my_token: str, client: "MyTestApiClient") -> Response[Any]:
    """TOKEN_WITH_COOKIE

     Test optional cookie parameters

    Args:
        my_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        my_token=my_token,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(*, my_token: str, client: "MyTestApiClient") -> Any:
    """TOKEN_WITH_COOKIE

     Test optional cookie parameters

    Args:
        my_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    return sync_detailed(
        client=client,
        my_token=my_token,
    ).parsed


async def asyncio_detailed(*, my_token: str, client: "MyTestApiClient") -> Response[Any]:
    """TOKEN_WITH_COOKIE

     Test optional cookie parameters

    Args:
        my_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        my_token=my_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(*, my_token: str, client: "MyTestApiClient") -> Any:
    """TOKEN_WITH_COOKIE

     Test optional cookie parameters

    Args:
        my_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    return (
        await asyncio_detailed(
            client=client,
            my_token=my_token,
        )
    ).parsed
