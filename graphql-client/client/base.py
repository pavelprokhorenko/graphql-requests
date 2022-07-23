import json
from typing import Any, Optional

from ..typedefs import JSONEncoder


class GraphQLBaseClient:

    __slots__ = [
        "_url",
        "_headers",
        "_cookies",
        "_json_serialize",
        "_timeout",
    ]

    def __init__(
        self,
        url: str,
        *,
        headers: Optional[dict[str, Any]] = None,
        cookies: Optional[dict[str, Any]] = None,
        json_serialize: Optional[JSONEncoder] = json.dumps,
        timeout: Optional[float] = 60  # seconds
    ) -> None:
        if headers is None:
            headers = dict()
        headers["Content-Type"] = "application/json"

        self._url = url
        self._headers = headers
        self._cookies = cookies
        self._json_serialize = json_serialize
        self._timeout = timeout

    @property
    def headers(self) -> dict[str, Any]:
        """The default headers of the client session."""
        return self._headers

    @property
    def cookies(self) -> dict[str, Any]:
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
