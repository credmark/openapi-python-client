import ssl
from typing import Dict, Union

from .api.default import Default
from .api.location import Location
from .api.parameter_references import ParameterReferences
from .api.parameters import Parameters
from .api.responses import Responses
from .api.tag1 import Tag1
from .api.tests import Tests
from .api.true_ import True_


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
        follow_redirects: Whether or not to follow redirects. Default value is True.
    """

    def __init__(
        self,
        base_url: str,
        cookies: Union[Dict[str, str], None] = None,
        headers: Union[Dict[str, str], None] = None,
        timeout: float = 5.0,
        verify_ssl: Union[str, bool, ssl.SSLContext] = True,
        follow_redirects: bool = True,
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
        self.follow_redirects = follow_redirects
        self.token = token
        self.prefix = prefix
        self.auth_header_name = auth_header_name

        self.tests = Tests(client=self)
        self.responses = Responses(client=self)
        self.default = Default(client=self)
        self.parameters = Parameters(client=self)
        self.tag1 = Tag1(client=self)
        self.location = Location(client=self)
        self.true_ = True_(client=self)
        self.parameter_references = ParameterReferences(client=self)

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
