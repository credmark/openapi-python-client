from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict, List, cast

import httpx

if TYPE_CHECKING:
    from ...client import MyTestApiClient

from typing import Dict, List, cast

from ... import errors
from ...models.http_validation_error import HTTPValidationError
from ...types import File, Response


def _get_kwargs(*, multipart_data: List[File], client: "MyTestApiClient") -> Dict[str, Any]:
    url = "{}/tests/upload/multiple".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = []
    for multipart_data_item_data in multipart_data:
        multipart_data_item = multipart_data_item_data.to_tuple()

        multipart_multipart_data.append(multipart_data_item)

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "files": multipart_multipart_data,
    }


def _parse_response(*, client: "MyTestApiClient", response: httpx.Response) -> Any:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, response.json())
        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        raise errors.UnexpectedStatus(response.status_code, response.content, response_422)
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: "MyTestApiClient", response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(*, multipart_data: List[File], client: "MyTestApiClient") -> Response[Any]:
    """Upload multiple files

     Upload several files in the same request

    Args:
        multipart_data (List[File]):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(*, multipart_data: List[File], client: "MyTestApiClient") -> Any:
    """Upload multiple files

     Upload several files in the same request

    Args:
        multipart_data (List[File]):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(*, multipart_data: List[File], client: "MyTestApiClient") -> Response[Any]:
    """Upload multiple files

     Upload several files in the same request

    Args:
        multipart_data (List[File]):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(*, multipart_data: List[File], client: "MyTestApiClient") -> Any:
    """Upload multiple files

     Upload several files in the same request

    Args:
        multipart_data (List[File]):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
