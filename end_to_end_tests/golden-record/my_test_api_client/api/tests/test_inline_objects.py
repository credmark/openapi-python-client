from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict

import httpx

if TYPE_CHECKING:
    from ...client import MyTestApiClient

from typing import Dict

from ... import errors
from ...models.test_inline_objects_json_body import TestInlineObjectsJsonBody
from ...models.test_inline_objects_response_200 import TestInlineObjectsResponse200
from ...types import Response


def _get_kwargs(*, json_body: TestInlineObjectsJsonBody, client: "MyTestApiClient") -> Dict[str, Any]:
    url = "{}/tests/inline_objects".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: "MyTestApiClient", response: httpx.Response) -> TestInlineObjectsResponse200:
    if response.status_code == HTTPStatus.OK:
        response_200 = TestInlineObjectsResponse200.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: "MyTestApiClient", response: httpx.Response) -> Response[TestInlineObjectsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *, json_body: TestInlineObjectsJsonBody, client: "MyTestApiClient"
) -> Response[TestInlineObjectsResponse200]:
    """Test Inline Objects

    Args:
        json_body (TestInlineObjectsJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestInlineObjectsResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(*, json_body: TestInlineObjectsJsonBody, client: "MyTestApiClient") -> TestInlineObjectsResponse200:
    """Test Inline Objects

    Args:
        json_body (TestInlineObjectsJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestInlineObjectsResponse200]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *, json_body: TestInlineObjectsJsonBody, client: "MyTestApiClient"
) -> Response[TestInlineObjectsResponse200]:
    """Test Inline Objects

    Args:
        json_body (TestInlineObjectsJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestInlineObjectsResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(*, json_body: TestInlineObjectsJsonBody, client: "MyTestApiClient") -> TestInlineObjectsResponse200:
    """Test Inline Objects

    Args:
        json_body (TestInlineObjectsJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestInlineObjectsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
