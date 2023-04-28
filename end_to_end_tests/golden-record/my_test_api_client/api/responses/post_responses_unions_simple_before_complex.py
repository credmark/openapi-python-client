from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict

import httpx

if TYPE_CHECKING:
    from ...client import MyTestApiClient

from typing import Dict

from ... import errors
from ...models.post_responses_unions_simple_before_complex_response_200 import (
    PostResponsesUnionsSimpleBeforeComplexResponse200,
)
from ...types import Response


def _get_kwargs(client: "MyTestApiClient") -> Dict[str, Any]:
    url = "{}/responses/unions/simple_before_complex".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: "MyTestApiClient", response: httpx.Response
) -> PostResponsesUnionsSimpleBeforeComplexResponse200:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostResponsesUnionsSimpleBeforeComplexResponse200.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: "MyTestApiClient", response: httpx.Response
) -> Response[PostResponsesUnionsSimpleBeforeComplexResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(client: "MyTestApiClient") -> Response[PostResponsesUnionsSimpleBeforeComplexResponse200]:
    """Regression test for #603

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostResponsesUnionsSimpleBeforeComplexResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(client: "MyTestApiClient") -> PostResponsesUnionsSimpleBeforeComplexResponse200:
    """Regression test for #603

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostResponsesUnionsSimpleBeforeComplexResponse200]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(client: "MyTestApiClient") -> Response[PostResponsesUnionsSimpleBeforeComplexResponse200]:
    """Regression test for #603

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostResponsesUnionsSimpleBeforeComplexResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(client: "MyTestApiClient") -> PostResponsesUnionsSimpleBeforeComplexResponse200:
    """Regression test for #603

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostResponsesUnionsSimpleBeforeComplexResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
