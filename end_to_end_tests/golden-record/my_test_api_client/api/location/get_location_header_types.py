from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict, Union

import httpx

if TYPE_CHECKING:
    from ...client import MyTestApiClient

from typing import Union

from ... import errors
from ...models.get_location_header_types_int_enum_header import GetLocationHeaderTypesIntEnumHeader
from ...models.get_location_header_types_string_enum_header import GetLocationHeaderTypesStringEnumHeader
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    boolean_header: Union[Unset, bool] = UNSET,
    string_header: Union[Unset, str] = UNSET,
    number_header: Union[Unset, float] = UNSET,
    integer_header: Union[Unset, int] = UNSET,
    int_enum_header: Union[Unset, GetLocationHeaderTypesIntEnumHeader] = UNSET,
    string_enum_header: Union[Unset, GetLocationHeaderTypesStringEnumHeader] = UNSET,
    client: "MyTestApiClient",
) -> Dict[str, Any]:
    url = "{}/location/header/types".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(boolean_header, Unset):
        headers["Boolean-Header"] = "true" if boolean_header else "false"

    if not isinstance(string_header, Unset):
        headers["String-Header"] = string_header

    if not isinstance(number_header, Unset):
        headers["Number-Header"] = str(number_header)

    if not isinstance(integer_header, Unset):
        headers["Integer-Header"] = str(integer_header)

    if not isinstance(int_enum_header, Unset):
        headers["Int-Enum-Header"] = str(int_enum_header)

    if not isinstance(string_enum_header, Unset):
        headers["String-Enum-Header"] = str(string_enum_header)

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


def sync_detailed(
    *,
    boolean_header: Union[Unset, bool] = UNSET,
    string_header: Union[Unset, str] = UNSET,
    number_header: Union[Unset, float] = UNSET,
    integer_header: Union[Unset, int] = UNSET,
    int_enum_header: Union[Unset, GetLocationHeaderTypesIntEnumHeader] = UNSET,
    string_enum_header: Union[Unset, GetLocationHeaderTypesStringEnumHeader] = UNSET,
    client: "MyTestApiClient",
) -> Response[Any]:
    """
    Args:
        boolean_header (Union[Unset, bool]):
        string_header (Union[Unset, str]):
        number_header (Union[Unset, float]):
        integer_header (Union[Unset, int]):
        int_enum_header (Union[Unset, GetLocationHeaderTypesIntEnumHeader]):
        string_enum_header (Union[Unset, GetLocationHeaderTypesStringEnumHeader]):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        boolean_header=boolean_header,
        string_header=string_header,
        number_header=number_header,
        integer_header=integer_header,
        int_enum_header=int_enum_header,
        string_enum_header=string_enum_header,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    boolean_header: Union[Unset, bool] = UNSET,
    string_header: Union[Unset, str] = UNSET,
    number_header: Union[Unset, float] = UNSET,
    integer_header: Union[Unset, int] = UNSET,
    int_enum_header: Union[Unset, GetLocationHeaderTypesIntEnumHeader] = UNSET,
    string_enum_header: Union[Unset, GetLocationHeaderTypesStringEnumHeader] = UNSET,
    client: "MyTestApiClient",
) -> Any:
    """
    Args:
        boolean_header (Union[Unset, bool]):
        string_header (Union[Unset, str]):
        number_header (Union[Unset, float]):
        integer_header (Union[Unset, int]):
        int_enum_header (Union[Unset, GetLocationHeaderTypesIntEnumHeader]):
        string_enum_header (Union[Unset, GetLocationHeaderTypesStringEnumHeader]):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    return sync_detailed(
        client=client,
        boolean_header=boolean_header,
        string_header=string_header,
        number_header=number_header,
        integer_header=integer_header,
        int_enum_header=int_enum_header,
        string_enum_header=string_enum_header,
    ).parsed


async def asyncio_detailed(
    *,
    boolean_header: Union[Unset, bool] = UNSET,
    string_header: Union[Unset, str] = UNSET,
    number_header: Union[Unset, float] = UNSET,
    integer_header: Union[Unset, int] = UNSET,
    int_enum_header: Union[Unset, GetLocationHeaderTypesIntEnumHeader] = UNSET,
    string_enum_header: Union[Unset, GetLocationHeaderTypesStringEnumHeader] = UNSET,
    client: "MyTestApiClient",
) -> Response[Any]:
    """
    Args:
        boolean_header (Union[Unset, bool]):
        string_header (Union[Unset, str]):
        number_header (Union[Unset, float]):
        integer_header (Union[Unset, int]):
        int_enum_header (Union[Unset, GetLocationHeaderTypesIntEnumHeader]):
        string_enum_header (Union[Unset, GetLocationHeaderTypesStringEnumHeader]):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        boolean_header=boolean_header,
        string_header=string_header,
        number_header=number_header,
        integer_header=integer_header,
        int_enum_header=int_enum_header,
        string_enum_header=string_enum_header,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    boolean_header: Union[Unset, bool] = UNSET,
    string_header: Union[Unset, str] = UNSET,
    number_header: Union[Unset, float] = UNSET,
    integer_header: Union[Unset, int] = UNSET,
    int_enum_header: Union[Unset, GetLocationHeaderTypesIntEnumHeader] = UNSET,
    string_enum_header: Union[Unset, GetLocationHeaderTypesStringEnumHeader] = UNSET,
    client: "MyTestApiClient",
) -> Any:
    """
    Args:
        boolean_header (Union[Unset, bool]):
        string_header (Union[Unset, str]):
        number_header (Union[Unset, float]):
        integer_header (Union[Unset, int]):
        int_enum_header (Union[Unset, GetLocationHeaderTypesIntEnumHeader]):
        string_enum_header (Union[Unset, GetLocationHeaderTypesStringEnumHeader]):

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    return (
        await asyncio_detailed(
            client=client,
            boolean_header=boolean_header,
            string_header=string_header,
            number_header=number_header,
            integer_header=integer_header,
            int_enum_header=int_enum_header,
            string_enum_header=string_enum_header,
        )
    ).parsed
