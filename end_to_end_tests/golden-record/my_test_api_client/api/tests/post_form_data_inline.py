from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict, Optional

import httpx

if TYPE_CHECKING:
    from ...client import MyTestApiClient

from typing import Dict

from ... import errors
from ...models.post_form_data_inline_data import PostFormDataInlineData
from ...types import Response


def _get_kwargs(*, form_data: PostFormDataInlineData, client: "MyTestApiClient") -> Dict[str, Any]:
    url = "{}/tests/post_form_data_inline".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "data": form_data.to_dict(),
    }


def _parse_response(*, client: "MyTestApiClient", response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: "MyTestApiClient", response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(*, form_data: PostFormDataInlineData, client: "MyTestApiClient") -> Response[Any]:
    """Post form data (inline schema)

     Post form data (inline schema)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(*, form_data: PostFormDataInlineData, client: "MyTestApiClient") -> Optional[Any]:
    """Post form data (inline schema)

     Post form data (inline schema)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
    ).parsed


async def asyncio_detailed(*, form_data: PostFormDataInlineData, client: "MyTestApiClient") -> Response[Any]:
    """Post form data (inline schema)

     Post form data (inline schema)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(*, form_data: PostFormDataInlineData, client: "MyTestApiClient") -> Optional[Any]:
    """Post form data (inline schema)

     Post form data (inline schema)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
        )
    ).parsed
