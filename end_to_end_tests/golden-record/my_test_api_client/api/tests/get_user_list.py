from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

import httpx

if TYPE_CHECKING:
    from ...client import MyTestApiClient

import datetime
from typing import Dict, List, Optional, Union

from ... import errors
from ...models.a_model import AModel
from ...models.an_enum import AnEnum
from ...models.an_enum_with_null import AnEnumWithNull
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    an_enum_value: List[AnEnum],
    an_enum_value_with_null: List[Optional[AnEnumWithNull]],
    an_enum_value_with_only_null: List[None],
    some_date: Union[datetime.date, datetime.datetime],
    client: "MyTestApiClient",
) -> Dict[str, Any]:
    url = "{}/tests/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_an_enum_value = []
    for an_enum_value_item_data in an_enum_value:
        an_enum_value_item = an_enum_value_item_data.value

        json_an_enum_value.append(an_enum_value_item)

    params["an_enum_value"] = json_an_enum_value

    json_an_enum_value_with_null = []
    for an_enum_value_with_null_item_data in an_enum_value_with_null:
        an_enum_value_with_null_item = (
            an_enum_value_with_null_item_data.value if an_enum_value_with_null_item_data else None
        )

        json_an_enum_value_with_null.append(an_enum_value_with_null_item)

    params["an_enum_value_with_null"] = json_an_enum_value_with_null

    json_an_enum_value_with_only_null = an_enum_value_with_only_null

    params["an_enum_value_with_only_null"] = json_an_enum_value_with_only_null

    json_some_date: str

    if isinstance(some_date, datetime.date):
        json_some_date = some_date.isoformat()
    else:
        json_some_date = some_date.isoformat()

    params["some_date"] = json_some_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: "MyTestApiClient", response: httpx.Response
) -> Optional[Union[HTTPValidationError, List["AModel"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.LOCKED:
        response_423 = HTTPValidationError.from_dict(response.json())

        return response_423
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: "MyTestApiClient", response: httpx.Response
) -> Response[Union[HTTPValidationError, List["AModel"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    an_enum_value: List[AnEnum],
    an_enum_value_with_null: List[Optional[AnEnumWithNull]],
    an_enum_value_with_only_null: List[None],
    some_date: Union[datetime.date, datetime.datetime],
    client: "MyTestApiClient",
) -> Response[Union[HTTPValidationError, List["AModel"]]]:
    """Get List

     Get a list of things

    Args:
        an_enum_value (List[AnEnum]):
        an_enum_value_with_null (List[Optional[AnEnumWithNull]]):
        an_enum_value_with_only_null (List[None]):
        some_date (Union[datetime.date, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['AModel']]]
    """

    kwargs = _get_kwargs(
        client=client,
        an_enum_value=an_enum_value,
        an_enum_value_with_null=an_enum_value_with_null,
        an_enum_value_with_only_null=an_enum_value_with_only_null,
        some_date=some_date,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    an_enum_value: List[AnEnum],
    an_enum_value_with_null: List[Optional[AnEnumWithNull]],
    an_enum_value_with_only_null: List[None],
    some_date: Union[datetime.date, datetime.datetime],
    client: "MyTestApiClient",
) -> Optional[Union[HTTPValidationError, List["AModel"]]]:
    """Get List

     Get a list of things

    Args:
        an_enum_value (List[AnEnum]):
        an_enum_value_with_null (List[Optional[AnEnumWithNull]]):
        an_enum_value_with_only_null (List[None]):
        some_date (Union[datetime.date, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['AModel']]]
    """

    return sync_detailed(
        client=client,
        an_enum_value=an_enum_value,
        an_enum_value_with_null=an_enum_value_with_null,
        an_enum_value_with_only_null=an_enum_value_with_only_null,
        some_date=some_date,
    ).parsed


async def asyncio_detailed(
    *,
    an_enum_value: List[AnEnum],
    an_enum_value_with_null: List[Optional[AnEnumWithNull]],
    an_enum_value_with_only_null: List[None],
    some_date: Union[datetime.date, datetime.datetime],
    client: "MyTestApiClient",
) -> Response[Union[HTTPValidationError, List["AModel"]]]:
    """Get List

     Get a list of things

    Args:
        an_enum_value (List[AnEnum]):
        an_enum_value_with_null (List[Optional[AnEnumWithNull]]):
        an_enum_value_with_only_null (List[None]):
        some_date (Union[datetime.date, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['AModel']]]
    """

    kwargs = _get_kwargs(
        client=client,
        an_enum_value=an_enum_value,
        an_enum_value_with_null=an_enum_value_with_null,
        an_enum_value_with_only_null=an_enum_value_with_only_null,
        some_date=some_date,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    an_enum_value: List[AnEnum],
    an_enum_value_with_null: List[Optional[AnEnumWithNull]],
    an_enum_value_with_only_null: List[None],
    some_date: Union[datetime.date, datetime.datetime],
    client: "MyTestApiClient",
) -> Optional[Union[HTTPValidationError, List["AModel"]]]:
    """Get List

     Get a list of things

    Args:
        an_enum_value (List[AnEnum]):
        an_enum_value_with_null (List[Optional[AnEnumWithNull]]):
        an_enum_value_with_only_null (List[None]):
        some_date (Union[datetime.date, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['AModel']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            an_enum_value=an_enum_value,
            an_enum_value_with_null=an_enum_value_with_null,
            an_enum_value_with_only_null=an_enum_value_with_only_null,
            some_date=some_date,
        )
    ).parsed
