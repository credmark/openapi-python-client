from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict

import httpx

if TYPE_CHECKING:
    from ...client import MyTestApiClient

from ... import errors
from ...types import UNSET, Response


def _get_kwargs(
    param_path: str, *, param_query: str = "overridden_in_GET", client: "MyTestApiClient"
) -> Dict[str, Any]:
    url = "{}/common_parameters_overriding/{param}".format(client.base_url, param=param_path)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["param"] = param_query

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
    param_path: str, *, param_query: str = "overridden_in_GET", client: "MyTestApiClient"
) -> Response[Any]:
    """Test that if you have an overriding property from `PathItem` in `Operation`, it produces valid code

    Args:
        param_path (str):
        param_query (str): A parameter with the same name as another. Default:
            'overridden_in_GET'. Example: an example string.

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        param_path=param_path,
        client=client,
        param_query=param_query,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(param_path: str, *, param_query: str = "overridden_in_GET", client: "MyTestApiClient") -> Any:
    """Test that if you have an overriding property from `PathItem` in `Operation`, it produces valid code

    Args:
        param_path (str):
        param_query (str): A parameter with the same name as another. Default:
            'overridden_in_GET'. Example: an example string.

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    return sync_detailed(
        param_path=param_path,
        client=client,
        param_query=param_query,
    ).parsed


async def asyncio_detailed(
    param_path: str, *, param_query: str = "overridden_in_GET", client: "MyTestApiClient"
) -> Response[Any]:
    """Test that if you have an overriding property from `PathItem` in `Operation`, it produces valid code

    Args:
        param_path (str):
        param_query (str): A parameter with the same name as another. Default:
            'overridden_in_GET'. Example: an example string.

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        param_path=param_path,
        client=client,
        param_query=param_query,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(param_path: str, *, param_query: str = "overridden_in_GET", client: "MyTestApiClient") -> Any:
    """Test that if you have an overriding property from `PathItem` in `Operation`, it produces valid code

    Args:
        param_path (str):
        param_query (str): A parameter with the same name as another. Default:
            'overridden_in_GET'. Example: an example string.

    Raises:
        errors.UnexpectedStatus: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    return (
        await asyncio_detailed(
            param_path=param_path,
            client=client,
            param_query=param_query,
        )
    ).parsed
