from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict, Union

import httpx

if TYPE_CHECKING:
    from ...client import MyTestApiClient

from typing import Union

from ... import errors
from ...types import UNSET, Response, Unset


def _get_kwargs(*, common: Union[Unset, None, str] = UNSET, client: "MyTestApiClient") -> Dict[str, Any]:
    url = "{}/common_parameters".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["common"] = common

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: "MyTestApiClient", response: httpx.Response) -> Any:
    if response.status_code == HTTPStatus.OK:
        response_200 = None
        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: "MyTestApiClient", response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(*, common: Union[Unset, None, str] = UNSET, client: "MyTestApiClient") -> Response[Any]:
    """
    Args:
        common (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        common=common,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(*, common: Union[Unset, None, str] = UNSET, client: "MyTestApiClient") -> Any:
    """
    Args:
        common (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    return sync_detailed(
        client=client,
        common=common,
    ).parsed


async def asyncio_detailed(*, common: Union[Unset, None, str] = UNSET, client: "MyTestApiClient") -> Response[Any]:
    """
    Args:
        common (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        common=common,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(*, common: Union[Unset, None, str] = UNSET, client: "MyTestApiClient") -> Any:
    """
    Args:
        common (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    return (
        await asyncio_detailed(
            client=client,
            common=common,
        )
    ).parsed
