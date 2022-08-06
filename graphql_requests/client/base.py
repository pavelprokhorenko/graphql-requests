import json
from typing import Any, Dict, Union

from graphql_requests.typedefs import JSONEncoder


class GraphQLBaseClient:

    __slots__ = [
        "_base_url",
        "_headers",
        "_cookies",
        "_json_serialize",
        "_timeout",
    ]

    def __init__(
        self,
        base_url: str,
        *,
        headers: Union[Dict[str, Any], None] = None,
        cookies: Union[Dict[str, Any], None] = None,
        json_serialize: Union[JSONEncoder, None] = json.dumps,
        timeout: Union[float, None] = 15  # seconds
    ) -> None:
        if headers is None:
            headers = dict()
        headers["Content-Type"] = "application/json"

        self._base_url = base_url
        self._headers = headers
        self._cookies = cookies
        self._json_serialize = json_serialize
        self._timeout = timeout

    def _build_send_data(
        self, query: str, operation_name: str, variables: Union[str, Dict[str, Any]]
    ) -> str:
        """Serialize request payload to ``str``."""
        data = {
            "query": query,
            "operation_name": operation_name,
            "variables": variables,
        }
        return self._json_serialize(data, default=str)

    @property
    def headers(self) -> Dict[str, Any]:
        """The default headers of the client session."""
        return self._headers

    @property
    def cookies(self) -> Dict[str, Any]:
        """The session cookies."""
        return self._cookies

    @property
    def json_serialize(self) -> JSONEncoder:
        """Json serializer callable."""
        return self._json_serialize

    @property
    def timeout(self) -> float:
        """Timeout for the session."""
        return self._timeout
