import ssl
import threading
from typing import Dict, Union


class MyTestApiClient:
    """A class for keeping track of data related to the API

    Attributes:
        base_url: The base URL for the API, all requests are made to a relative path to this URL
        cookies: A dictionary of cookies to be sent with every request
        headers: A dictionary of headers to be sent with every request
        timeout: The maximum amount of a time in seconds a request can take. API functions will raise
            httpx.TimeoutException if this is exceeded.
        verify_ssl: Whether or not to verify the SSL certificate of the API server. This should be True in production,
            but can be set to False for testing purposes.
        raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
            status code that was not documented in the source OpenAPI document.
        follow_redirects: Whether or not to follow redirects. Default value is False.
    """

    __lock__ = threading.RLock()
    __instance__: Union["MyTestApiClient", None] = None

    @classmethod
    def configure(
        cls,
        base_url: str = "http://localhost:8080",
        cookies: Union[Dict[str, str], None] = None,
        headers: Union[Dict[str, str], None] = None,
        timeout: float = 5.0,
        verify_ssl: Union[str, bool, ssl.SSLContext] = True,
        raise_on_unexpected_status: bool = False,
        follow_redirects: bool = False,
        token: Union[str, None] = None,
        prefix: str = "Bearer",
        auth_header_name: str = "Authorization",
    ) -> "MyTestApiClient":
        cookies = cookies if cookies is not None else {}
        headers = headers if headers is not None else {}

        with cls.__lock__:
            cls.__instance__ = cls(
                base_url=base_url,
                cookies=cookies,
                headers=headers,
                timeout=timeout,
                verify_ssl=verify_ssl,
                raise_on_unexpected_status=raise_on_unexpected_status,
                follow_redirects=follow_redirects,
                token=token,
                prefix=prefix,
                auth_header_name=auth_header_name,
            )

        return cls.__instance__

    def __init__(
        self,
        base_url: str,
        cookies: Union[Dict[str, str], None] = None,
        headers: Union[Dict[str, str], None] = None,
        timeout: float = 5.0,
        verify_ssl: Union[str, bool, ssl.SSLContext] = True,
        raise_on_unexpected_status: bool = False,
        follow_redirects: bool = False,
        token: Union[str, None] = None,
        prefix: str = "Bearer",
        auth_header_name: str = "Authorization",
    ):
        cookies = cookies if cookies is not None else {}
        headers = headers if headers is not None else {}

        self.base_url = base_url
        self.cookies = cookies
        self.headers = headers
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self.raise_on_unexpected_status = raise_on_unexpected_status
        self.follow_redirects = follow_redirects
        self.token = token
        self.prefix = prefix
        self.auth_header_name = auth_header_name

    @classmethod
    def instance(cls) -> "MyTestApiClient":
        if cls.__instance__ is None:
            return cls.configure()
        else:
            return cls.__instance__

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints"""
        if not self.token:
            return {**self.headers}
        auth_header_value = f"{self.prefix} {self.token}" if self.prefix else self.token
        return {self.auth_header_name: auth_header_value, **self.headers}

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def get_timeout(self) -> float:
        return self.timeout
